variable "default_tags" {
  type = map
  default = {
    Environment = "TFG"
    Team        = "Cloud"
    CreatedBy   = "sureshp"
  }
}

variable "resource_group_name" {
  type = string
  default = "spzpl"
}

variable "location_name" {
  type = string
  default = "westeurope"
}

variable "storage_account_name" {
  type = string
  default = "spzpl"
}

variable "input_container_name"{
  type = string
  default = "inputitems"
}

variable "output_container_name"{
  type = string
  default = "outputitems"
}

variable "queue_name"{
  type = string
  default = "queuename"
}