resource "random_string" "sb_namespace" {
  length  = 10
  special = false
  upper   = false
}

resource "random_string" "sb_queue" {
  length  = 10
  special = false
  upper   = false
}
resource "random_string" "sb_topic" {
  length  = 10
  special = false
  upper   = false
}