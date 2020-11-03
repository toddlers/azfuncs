variable "default_tags" {
  type = map
  default = {
    Environment = "TFG"
    Team        = "Cloud"
    CreatedBy   = "sureshp"
  }
}

variable "zipname"{
  type = string
}