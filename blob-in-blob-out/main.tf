resource "azurerm_resource_group" "rg" {
  name     = "resource_group_name"
  location = "westeurope"
  tags     = var.default_tags
}
