resource "random_integer" "ri" {
  min = 10000
  max = 99999
}

resource "azurerm_cosmosdb_account" "db" {
  name                = "tfex-cosmos-db-${random_integer.ri.result}"
  location            = azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name
  offer_type          = "Standard"
  kind                = "GlobalDocumentDB"

  enable_automatic_failover = false

  capabilities {
    name = "EnableAggregationPipeline"
  }

  capabilities {
    name = "mongoEnableDocLevelTTL"
  }

  capabilities {
    name = "MongoDBv3.4"
  }

  consistency_policy {
    consistency_level       = "BoundedStaleness"
    max_interval_in_seconds = 10
    max_staleness_prefix    = 200
  }

  # geo_location {
  #   location          = var.location_name
  #   failover_priority = 1
  # }

  geo_location {
    location          = azurerm_resource_group.rg.location
    failover_priority = 0
  }
}

# resource "azurerm_cosmosdb_mongo_database" "cdb-mongo" {
#   name                = "tfex-cosmos-mongo-db"
#   resource_group_name = azurerm_resource_group.rg.name
#   account_name        = azurerm_cosmosdb_account.db.name
#   throughput          = 400
# }

# resource "azurerm_cosmosdb_mongo_collection" "example" {
#   name                = "tfex-cosmos-mongo-db-collection"
#   resource_group_name = azurerm_resource_group.rg.name
#   account_name        = azurerm_cosmosdb_account.db.name
#   database_name       = azurerm_cosmosdb_mongo_database.cdb-mongo.name

#   default_ttl_seconds = "777"
#   shard_key           = "uniqueKey"
#   throughput          = 400
# }

resource "azurerm_cosmosdb_sql_database" "sql_db" {
  name                = "spzpl"
  resource_group_name = azurerm_cosmosdb_account.db.resource_group_name
  account_name        = azurerm_cosmosdb_account.db.name
  throughput          = 400
}

resource "azurerm_cosmosdb_sql_container" "feedcol_collection" {
  name                = "feedcol"
  resource_group_name = azurerm_cosmosdb_account.db.resource_group_name
  account_name        = azurerm_cosmosdb_account.db.name
  database_name       = azurerm_cosmosdb_sql_database.sql_db.name
  partition_key_path  = "/title"
  throughput          = 400
}

resource "azurerm_cosmosdb_sql_container" "leases_collection" {
  name                = "leases"
  resource_group_name = azurerm_cosmosdb_account.db.resource_group_name
  account_name        = azurerm_cosmosdb_account.db.name
  database_name       = azurerm_cosmosdb_sql_database.sql_db.name
  throughput          = 400
  partition_key_path  = "/title"
}