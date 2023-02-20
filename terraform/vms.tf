resource "azurerm_subnet" "default" {
  name                 = "default"
  resource_group_name  = azurerm_resource_group.default.name
  virtual_network_name = azurerm_virtual_network.default.name
  address_prefixes     = ["10.0.2.0/24"]
}

resource "azurerm_network_security_group" "sshable_nsg" {
  name                = "sshable-nsg"
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

#############################################
# Manager
#############################################

resource "azurerm_public_ip" "manager_ip" {
  name                = "manager"
  resource_group_name = azurerm_resource_group.default.name
  location            = azurerm_resource_group.default.location
  allocation_method   = "Dynamic"
}

resource "azurerm_network_interface" "manager_nic" {
  name                = "manager-nic"
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
  network_security_group_id = azurerm_network_security_group.sshable_nsg.id
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
    disk_size_gb         = var.manager_disk_size_gb
  }
  identity {
    type = "SystemAssigned"
  }
  connection {
    type        = "ssh"
      user        = var.username
      host        = azurerm_linux_virtual_machine.manager.public_ip_address
      private_key = tls_private_key.developer.private_key_openssh
  }
  provisioner "file" {
      content = tls_private_key.manager.private_key_openssh
      destination = "/home/${var.username}/.ssh/id_rsa"
  }
  provisioner "remote-exec" {
      inline = [
        "chmod 0600 ~/.ssh/id_rsa",
      ]
  }
  provisioner "file" {
	content = "export PARSL_WORKERS=$(python -c 'print(\",\".join(f\"worker-{i}\" for i in range(${var.workers}))))\nexport PARSL_CONFIG=~/wf-reg-test/parsl_configs/ssh_config.py\n"
      destination = "/home/${var.username}/parsl-config.sh"
  }
  # provisioner "remote-exec" {
  #     script = "../spack/setup_env.sh"
  # }
}

resource azurerm_role_assignment manager-storage {
  scope              = azurerm_storage_account.default.id
  role_definition_name = "Storage Blob Data Contributor"
  principal_id       = azurerm_linux_virtual_machine.manager.identity[0].principal_id
}

output "manager_ip" {
  value = azurerm_linux_virtual_machine.manager.public_ip_address
}

#############################################
# Worker
#############################################

resource "azurerm_network_interface" "worker_nic" {
  count               = var.workers
  name                = "worker-nic-${count.index}"
  location            = azurerm_resource_group.default.location
  resource_group_name = azurerm_resource_group.default.name

  ip_configuration {
    name                          = "worker-${count.index}"
    subnet_id                     = azurerm_subnet.default.id
    private_ip_address_allocation = "Dynamic"
  }
}

resource "azurerm_linux_virtual_machine" "worker" {
  count                 = var.workers
  name                  = "worker-${count.index}"
  location              = azurerm_resource_group.default.location
  resource_group_name   = azurerm_resource_group.default.name
  size                  = var.worker_vm_size
  admin_username        = var.username
  network_interface_ids = [azurerm_network_interface.worker_nic[count.index].id]
  disable_password_authentication = true
  admin_ssh_key {
    username   = var.username
    public_key = tls_private_key.manager.public_key_openssh
  }
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
    disk_size_gb         = var.worker_disk_size_gb
  }
  identity {
    type = "SystemAssigned"
  }
  # connection {
  #   type              = "ssh"
  #   user              = var.username
  #     host              = azurerm_linux_virtual_machine.worker[count.index].private_ip_address
  #     private_key       = tls_private_key.manager.private_key_openssh
  #     bastion_user      = var.username
  #     bastion_host      = azurerm_linux_virtual_machine.manager.public_ip_address
  #     bastion_host_key  = tls_private_key.manager.private_key_openssh
  # }
  # provisioner "remote-exec" {
  #     script = "../spack/setup_env.sh"
  # }
}

resource azurerm_role_assignment worker-data {
  count                = var.workers
  scope                = azurerm_storage_account.default.id
  role_definition_name = "Storage Blob Data Contributor"
  principal_id         = azurerm_linux_virtual_machine.worker[count.index].identity[0].principal_id
}

#############################################
# Builder
#############################################

# resource "azurerm_public_ip" "builder_ip" {
#   name                = "builder"
#   resource_group_name = azurerm_resource_group.default.name
#   location            = azurerm_resource_group.default.location
#   allocation_method   = "Dynamic"
# }


# resource "azurerm_network_interface" "builder_nic" {
#   name                = "builder-nic"
#   location            = azurerm_resource_group.default.location
#   resource_group_name = azurerm_resource_group.default.name

#   ip_configuration {
#     name                          = "builder"
#     subnet_id                     = azurerm_subnet.default.id
#     private_ip_address_allocation = "Dynamic"
#     public_ip_address_id          = azurerm_public_ip.builder_ip.id
#   }
# }

# resource "azurerm_network_interface_security_group_association" "builder" {
#   network_interface_id      = azurerm_network_interface.builder_nic.id
#   network_security_group_id = azurerm_network_security_group.sshable_nsg.id
# }

# resource "azurerm_linux_virtual_machine" "builder" {
#   name                  = "builder"
#   location              = azurerm_resource_group.default.location
#   resource_group_name   = azurerm_resource_group.default.name
#   size                  = var.builder_vm_size
#   admin_username        = var.username
#   network_interface_ids = [azurerm_network_interface.builder_nic.id]
#   disable_password_authentication = true
#   admin_ssh_key {
#     username   = var.username
#     public_key = tls_private_key.developer.public_key_openssh
#   }
#   source_image_reference {
#     publisher = var.vm_image.publisher
#     offer     = var.vm_image.offer
#     sku       = var.vm_image.sku
#     version   = var.vm_image.version
#   }
#   os_disk {
#     caching              = "ReadWrite"
#     storage_account_type = "StandardSSD_LRS"
#     disk_size_gb         = var.manager_disk_size_gb
#   }
#   identity {
#     type = "SystemAssigned"
#   }
#   # connection {
#   #   type        = "ssh"
#   #     user        = var.username
#   #     host        = azurerm_linux_virtual_machine.builder.public_ip_address
#   #     private_key = tls_private_key.developer.private_key_openssh
#   # }
#   # provisioner "remote-exec" {
#   #     script = "../spack/setup_env.sh"
#   # }
# }

# output "builder_ip" {
#   value = azurerm_linux_virtual_machine.builder.public_ip_address
# }
