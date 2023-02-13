#############################################
# Variables
#############################################

variable "os_disk_size_gb" {
  type    = string
  default = "64"
  # Usually can't be smaller than 30
}

# See https://azureprice.net/
variable "manager_vm_size" {
  type    = string
  default = "Standard_D2as_v5"
}

variable "builder_vm_size" {
  type    = string
  default = "Standard_D16as_v5"
}

variable "workers" {
  type    = number
  default = 5
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

resource "azurerm_virtual_network" "default" {
  name                = "default"
  address_space       = ["10.0.0.0/16"]
  location            = azurerm_resource_group.default.location
  resource_group_name = azurerm_resource_group.default.name
}

#############################################
# Storage resources
#############################################

resource "azurerm_storage_account" "default-premium" {
  name                     = "wfregtestfiles"
  resource_group_name      = azurerm_resource_group.default.name
  location                 = azurerm_resource_group.default.location
  account_tier             = "Premium"
  account_replication_type = "LRS"
  account_kind             = "FileStorage"
}

resource "azurerm_storage_share" "default" {
  name                 = "default"
  storage_account_name = azurerm_storage_account.default-premium.name
  quota                = 100
  enabled_protocol     = "NFS"
}

# resource "azurerm_private_endpoint" "nfs" {
#   name                = "nfs"
#   resource_group_name = azurerm_resource_group.default.name
#   location            = azurerm_resource_group.default.location
#   subnet_id           = azurerm_subnet.default.id
#   private_service_connection = {
# 	name                           = "nfs"
# 	is_manual_connection           = false
# 	private_connection_resource_id = 
#   }
# }

resource "azurerm_storage_account" "default" {
  name                     = "wfregtest"
  resource_group_name      = azurerm_resource_group.default.name
  location                 = azurerm_resource_group.default.location
  account_tier             = "Standard"
  account_replication_type = "LRS"
}

resource "azurerm_storage_container" "index" {
  name                  = "index"
  storage_account_name  = azurerm_storage_account.default.name
  container_access_type = "blob" # blobs are publicly accessible
}

resource "azurerm_storage_container" "web" {
  name                  = "$web"
  storage_account_name  = azurerm_storage_account.default.name
  container_access_type = "blob" # blobs are publicly accessible
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
# VM stuff
#############################################

# Note, the TLS keys are named after the identity they represent.
# This represents actions taken by the dev.
resource "tls_private_key" "developer" {
  algorithm = "RSA"
  rsa_bits  = 4096
}

# This represents actions taken by the manager
resource "tls_private_key" "manager" {
  algorithm = "RSA"
  rsa_bits  = 4096
}

output "developer_ssh_key" {
  value = tls_private_key.developer.private_key_openssh
  sensitive = true
}

output "worker_count" {
  value = var.workers
}
