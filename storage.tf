resource "azurerm_storage_account" "spstorage" {
  name                     = random_string.storage_name.result
  resource_group_name      = azurerm_resource_group.rg.name
  location                 = azurerm_resource_group.rg.location
  account_tier             = "Standard"
  account_replication_type = "GRS"

  tags = var.default_tags
}

resource "azurerm_storage_container" "sptfstate" {
  name                  = random_string.storage_container.result
  storage_account_name  = azurerm_storage_account.spstorage.name
  container_access_type = "private"
}

resource "azurerm_storage_blob" "storage_blob" {
  name                   = "${var.zipname}.zip"
  storage_account_name   = azurerm_storage_account.spstorage.name
  storage_container_name = azurerm_storage_container.sptfstate.name
  type                   = "Block"
  # have to change this everytime to force update otherwise tf doesnt do anything.
  source                 = "./dist/${var.zipname}.zip"
}
data "azurerm_storage_account_sas" "storage_sas" {
  connection_string = azurerm_storage_account.spstorage.primary_connection_string
  https_only        = false
  resource_types {
    service   = false
    container = false
    object    = true
  }
  services {
    blob  = true
    queue = false
    table = false
    file  = false
  }
  start  = "2020-10-26"
  expiry = "2028-03-21"
  permissions {
    read    = true
    write   = false
    delete  = false
    list    = false
    add     = false
    create  = false
    update  = false
    process = false
  }
}