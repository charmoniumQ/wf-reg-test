variable "os_disk_size_gb" {
  type    = string
  default = "30"
  # Usually can't be smaller than 30
}

variable "manager_vm_size" {
  type    = string
  default = "D8s_v5"
  #default = "Standard_DS1_v2"
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

data "azurerm_subscription" "default" {
}

data "azurerm_client_config" "default" {
}

resource "azurerm_resource_group" "default" {
  location = "eastus"
  name     = "terraform"
}

resource "azurerm_storage_account" "default" {
  name                     = "wfregtest2"
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
  name                = "default"
  location            = azurerm_resource_group.default.location
  resource_group_name = azurerm_resource_group.default.name

  ip_configuration {
    name                          = "default"
    subnet_id                     = azurerm_subnet.default.id
	private_ip_address_allocation = "Dynamic"
	public_ip_address_id          = azurerm_public_ip.manager_ip.id
  }
}

resource "azurerm_network_interface_security_group_association" "manager" {
  network_interface_id      = azurerm_network_interface.manager_nic.id
  network_security_group_id = azurerm_network_security_group.manager_nsg.id
}

resource "tls_private_key" "manager" {
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
	public_key = tls_private_key.manager.public_key_openssh
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

resource azurerm_role_assignment manager-deployment {
  scope              = azurerm_storage_container.deployment.resource_manager_id
  role_definition_name = "Storage Blob Data Contributor"
  principal_id       = azurerm_linux_virtual_machine.manager.identity[0].principal_id
}

resource azurerm_role_assignment manager-data {
  scope              = azurerm_storage_container.data.resource_manager_id
  role_definition_name = "Storage Blob Data Contributor"
  principal_id       = azurerm_linux_virtual_machine.manager.identity[0].principal_id
}

resource "null_resource" "manager_init" {
  depends_on = [azurerm_role_assignment.manager-deployment, azurerm_role_assignment.manager-data]
  connection {
    type        = "ssh"
    user        = var.username
	private_key = tls_private_key.manager.private_key_openssh
    host        = azurerm_linux_virtual_machine.manager.public_ip_address
  }
  provisioner "remote-exec" {
    inline = [
	  "echo hostname",
	  "nproc",
    ]
  }
}

output "manager_ip_address" {
  value = azurerm_linux_virtual_machine.manager.public_ip_address
}

output "manager_identity" {
  value = azurerm_linux_virtual_machine.manager.identity
}

output "manager_ssh_key" {
  value = tls_private_key.manager.private_key_openssh
  sensitive = true
}

# Create 1 spack builder machine
# Run spack build
# Delete it
# Create N worker machines
