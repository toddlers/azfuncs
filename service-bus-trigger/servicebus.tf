resource "azurerm_servicebus_namespace" "sb_namespace" {
  name                = var.sb_namespace_name
  location            = azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name
  sku                 = "Standard"

  tags = var.default_tags
}

resource "azurerm_servicebus_queue" "sb_queue" {
  name                = random_string.sb_queue.result
  resource_group_name = azurerm_resource_group.rg.name
  namespace_name      = azurerm_servicebus_namespace.sb_namespace.name

  enable_partitioning = true
}

resource "azurerm_servicebus_topic" "sb_topic_name" {
  name                = random_string.sb_topic.result
  resource_group_name = azurerm_resource_group.rg.name
  namespace_name      = azurerm_servicebus_namespace.sb_namespace.name

  enable_partitioning = true
}

resource "azurerm_servicebus_subscription" "example" {
  name                = "mysubscription"
  resource_group_name = azurerm_resource_group.rg.name
  namespace_name      = azurerm_servicebus_namespace.sb_namespace.name
  topic_name          = azurerm_servicebus_topic.sb_topic_name.name
  max_delivery_count  = 1
}