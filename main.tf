resource "azurerm_resource_group" "rg" {
  name     = "functiondeployment"
  location = "westeurope"
  tags     = var.default_tags
}

resource "azurerm_application_insights" "logging" {
  name                = random_string.application_insight.result
  location            = azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name
  application_type    = "other"
  tags                = var.default_tags
}