resource "azurerm_storage_account" "spstorage" {
  name                     =  var.storage_account_name
  resource_group_name      = azurerm_resource_group.rg.name
  location                 = azurerm_resource_group.rg.location
  account_tier             = "Standard"
  account_replication_type = "GRS"

  tags = var.default_tags
}

resource "azurerm_storage_container" "inputitems" {
  name                  = var.input_container_name
  storage_account_name  = azurerm_storage_account.spstorage.name
  container_access_type = "private"
}

resource "azurerm_storage_container" "outputitems" {
  name                  = var.output_container_name
  storage_account_name  = azurerm_storage_account.spstorage.name
  container_access_type = "private"
}

resource "azurerm_storage_queue" "storage_queue" {
  name                 = var.queue_name
  storage_account_name = azurerm_storage_account.spstorage.name
}