#############################################
# Variables
#############################################

variable "os_disk_size_gb" {
  type    = string
  default = "30"
  # Usually can't be smaller than 30
}

variable "manager_vm_size" {
  type    = string
  default = "Standard_D2as_v5"
}

variable "builder_vm_size" {
  type    = string
  default = "Standard_D8as_v5"
}

variable "workers" {
  type    = int
  default = 4
}

variable "worker_vm_size" {
  type    = string
  default = "Standard_D2as_v5"
}

variable "vm_image" {
  type = object({
    publisher = string
    offer     = string
    sku       = string
    version   = string
  })
  default = {
    publisher = "Canonical"
    offer     = "0001-com-ubuntu-minimal-jammy"
    sku       = "minimal-22_04-lts-gen2"
    version   = "22.04.202211160"
  }
}

variable "username" {
  type = string
  default = "azureuser"
}

#############################################
# Terraform providers
#############################################

terraform {
  required_version = ">= 1.1.0"
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~>3"
    }
  }
}

provider "azurerm" {
  features {}
}

resource "azurerm_resource_group" "default" {
  location = "eastus"
  name     = "terraform"
}

#############################################
# Storage resources
#############################################

resource "azurerm_storage_account" "default" {
  name                     = "wfregtest"
  resource_group_name      = azurerm_resource_group.default.name
  location                 = azurerm_resource_group.default.location
  account_tier             = "Standard"
  account_replication_type = "LRS"
}

resource "azurerm_storage_container" "data" {
  name                  = "data"
  storage_account_name  = azurerm_storage_account.default.name
  container_access_type = "blob" # blobs are publicly accessible
}

resource "azurerm_storage_container" "deployment" {
  name                  = "deployment"
  storage_account_name  = azurerm_storage_account.default.name
  container_access_type = "blob" # blobs are publicly accessible
}

#############################################
# Manager resources
#############################################

resource "azurerm_virtual_network" "default" {
  name                = "default"
  address_space       = ["10.0.0.0/16"]
  location            = azurerm_resource_group.default.location
  resource_group_name = azurerm_resource_group.default.name
}

resource "azurerm_subnet" "default" {
  name                 = "default"
  resource_group_name  = azurerm_resource_group.default.name
  virtual_network_name = azurerm_virtual_network.default.name
  address_prefixes     = ["10.0.2.0/24"]
}

resource "azurerm_public_ip" "manager_ip" {
  name                = "manager"
  resource_group_name = azurerm_resource_group.default.name
  location            = azurerm_resource_group.default.location
  allocation_method   = "Dynamic"
}

resource "azurerm_network_security_group" "manager_nsg" {
  name                = "manager-nsg"
  location            = azurerm_resource_group.default.location
  resource_group_name = azurerm_resource_group.default.name

  security_rule {
    name                       = "SSH"
    priority                   = 1001
    direction                  = "Inbound"
    access                     = "Allow"
    protocol                   = "Tcp"
    source_port_range          = "*"
    destination_port_range     = "22"
    source_address_prefix      = "*"
    destination_address_prefix = "*"
  }
}

resource "azurerm_network_interface" "manager_nic" {
  name                = "manager_nic"
  location            = azurerm_resource_group.default.location
  resource_group_name = azurerm_resource_group.default.name

  ip_configuration {
    name                          = "manager"
    subnet_id                     = azurerm_subnet.default.id
	private_ip_address_allocation = "Dynamic"
	public_ip_address_id          = azurerm_public_ip.manager_ip.id
  }
}

resource "azurerm_network_interface_security_group_association" "manager" {
  network_interface_id      = azurerm_network_interface.manager_nic.id
  network_security_group_id = azurerm_network_security_group.manager_nsg.id
}

# Note, the TLS keys are named after the identity they represent.
# This represents actions taken by the dev.
resource "tls_private_key" "developer" {
  algorithm = "RSA"
  rsa_bits  = 4096
}

# This represents actions taken by the manager_vm
resource "tls_private_key" "manager_vm" {
  algorithm = "RSA"
  rsa_bits  = 4096
}

resource "azurerm_linux_virtual_machine" "manager" {
  name                  = "manager"
  location              = azurerm_resource_group.default.location
  resource_group_name   = azurerm_resource_group.default.name
  size                  = var.manager_vm_size
  admin_username        = var.username
  network_interface_ids = [azurerm_network_interface.manager_nic.id]
  disable_password_authentication = true
  admin_ssh_key {
	username   = var.username
	public_key = tls_private_key.developer.public_key_openssh
  }
  source_image_reference {
    publisher = var.vm_image.publisher
    offer     = var.vm_image.offer
    sku       = var.vm_image.sku
    version   = var.vm_image.version
  }
  os_disk {
    caching              = "ReadWrite"
    storage_account_type = "StandardSSD_LRS"
    disk_size_gb         = var.os_disk_size_gb
  }
  identity {
	type = "SystemAssigned"
  }
}

resource azurerm_role_assignment manager-data {
  scope              = azurerm_storage_container.data.resource_manager_id
  role_definition_name = "Storage Blob Data Contributor"
  principal_id       = azurerm_linux_virtual_machine.manager.identity[0].principal_id
}

resource "null_resource" "manager_init" {
  depends_on = [azurerm_role_assignment.manager-data]
  connection {
    type        = "ssh"
    user        = var.username
	private_key = tls_private_key.developer.private_key_openssh
    host        = azurerm_linux_virtual_machine.manager.public_ip_address
  }
  provisioner "remote-exec" {
	script = "setup_env.sh"
  }
  provisioner "file" {
	content = tls_private_key.manager_vm.private_key_openssh
	destination = "/home/${var.user}/.ssh/id_rsa"
  }
}

#############################################
# Worker resources
#############################################

resource "azurerm_network_interface" "worker_nic" {
  count               = var.workers
  name                = "worker_nic"
  location            = azurerm_resource_group.default.location
  resource_group_name = azurerm_resource_group.default.name

  ip_configuration {
	name                          = "worker-${count.index}"
    subnet_id                     = azurerm_subnet.default.id
	private_ip_address_allocation = "Dynamic"
  }
}

resource "azurerm_linux_virtual_machine" "worker" {
  name                  = "worker-${count.index}"
  location              = azurerm_resource_group.default.location
  resource_group_name   = azurerm_resource_group.default.name
  size                  = var.worker_vm_size
  admin_username        = var.username
  network_interface_ids = [azurerm_network_interface.worker_nic[count.index].id]
  disable_password_authentication = true
  admin_ssh_key {
	username   = var.username
	public_key = tls_private_key.manager_vm.public_key_openssh
  }
  source_image_reference {
    publisher = var.vm_image.publisher
    offer     = var.vm_image.offer
    sku       = var.vm_image.sku
    version   = var.vm_image.version
  }
  os_disk {
    caching              = "ReadWrite"
    storage_account_type = "StandardSSD_LRS"
    disk_size_gb         = var.os_disk_size_gb
  }
  identity {
	type = "SystemAssigned"
  }
}

resource azurerm_role_assignment worker-data {
  scope              = azurerm_storage_container.data.resource_manager_id
  role_definition_name = "Storage Blob Data Contributor"
  principal_id       = azurerm_linux_virtual_machine.worker.identity[0].principal_id
}

resource "null_resource" "worker_init" {
  depends_on = [azurerm_role_assignment.worker-data]
  connection {
    type        = "ssh"
    user        = var.username
	private_key = tls_private_key.developer.private_key_openssh
    host        = azurerm_linux_virtual_machine.manager.public_ip_address
  }
  provisioner "remote-exec" {
	script = "setup_env.sh"
  }
}

#############################################
# Outputs
#############################################

output "manager_ip_address" {
  value = azurerm_linux_virtual_machine.manager.public_ip_address
}

output "developer_ssh_key" {
  value = tls_private_key.developer.private_key_openssh
  sensitive = true
}
