variable "cidr_for_vpc" {
  description = "CIDR range for vpc"
  type        = string
}

variable "tenancy" {
  description = "Tenancy of the resources created inside the VPC"
  type        = string
  default     = "default"
}

variable "enable_dns_support" {
  type    = bool
  default = true
}

variable "enable_dns_hostnames" {
  type    = bool
  default = true
}

variable "vpc_name" {
  description = "name of the vpc to be created"
  type        = string
}

variable "num_of_subnets" {
  type        = number
  description = "number of subnets required of public and private types"
}