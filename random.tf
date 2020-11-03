resource "random_string" "application_insight" {
  length  = 16
  special = false
  upper   = false
}

resource "random_string" "storage_name" {
  length  = 16
  special = false
  upper   = false
}

resource "random_string" "storage_container" {
  length  = 16
  special = false
  upper   = false
}

resource "random_string" "app_service_plan_name" {
  length  = 16
  special = false
}

resource "random_string" "function_name" {
  length  = 16
  special = false
  upper   = false
}