// for linux based functions need to have separate service plan
resource "azurerm_app_service_plan" "fxnapp" {
  name                = "functiondeploy-lxfxn-plan"
  location            = azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name
  kind                = "FunctionApp"
  reserved            = true
#   is_xenon            = true

  sku {
    tier = "Dynamic"
    size = "Y1"
  }
  tags = var.default_tags

}
resource "azurerm_function_app" "function" {
  name                       = random_string.function_name.result
  location                   = azurerm_resource_group.rg.location
  resource_group_name        = azurerm_resource_group.rg.name
  app_service_plan_id        = azurerm_app_service_plan.fxnapp.id
  storage_account_name       = azurerm_storage_account.spstorage.name
  storage_account_access_key = azurerm_storage_account.spstorage.primary_access_key
  os_type                    = "linux"
  version                    = "~3"
  app_settings = {
    APPINSIGHTS_INSTRUMENTATIONKEY = azurerm_application_insights.logging.instrumentation_key
    # need to check how we can enforce a particular version of python
    FUNCTIONS_WORKER_RUNTIME       = "python"
    FUNCTION_APP_EDIT_MODE         = "readwrite"
    https_only                     = true
    # this didnt helped for updating the code in the function.
    # HASH                           = base64sha256(filesha256("./dist/${var.zipname}.zip"))
    WEBSITE_RUN_FROM_PACKAGE       = "https://${azurerm_storage_account.spstorage.name}.blob.core.windows.net/${azurerm_storage_container.sptfstate.name}/${azurerm_storage_blob.storage_blob.name}${data.azurerm_storage_account_sas.storage_sas.sas}"
  }
  #We ignore these because they're set/changed by Function deployment
  # below didnt worked not sure why.
  # lifecycle {
  #   ignore_changes = [
  #     app_settings["WEBSITE_RUN_FROM_PACKAGE"]
  #   ]
  # }
  tags = var.default_tags
}