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

variable "jump_server_image" {
  type        = string
  description = "AMI ID for jump server"
  default     = "ami-08a52ddb321b32a8c"
}

variable "jump_server_instance_type" {
  type        = string
  description = "Instance type of jump server"
  default     = "t2.micro"
}

variable "web_server_instance_type" {
  type        = string
  description = "Instance type of jump server"
  default     = "t2.micro"
}

variable "inbound_rule_web" {
  description = "Inbound rules for web server"
  type = list(object({
    port        = number
    description = string
    protocol    = string
    }
  ))
  default = [{
    port        = 22
    description = "Allow ssh from jump server"
    protocol    = "tcp"
    },
    {
      port        = 80
      description = "Allow access on port 80 from ALB"
      protocol    = "tcp"
    }
  ]
}

variable "inbound_rule_app" {
  description = "Inbound rules for app server"
  type = list(object({
    port        = number
    description = string
    protocol    = string
    }
  ))
  default = [{
    port        = 22
    description = "Allow ssh from jump server"
    protocol    = "tcp"
    },
    {
      port        = 8080
      description = "Allow access on port 8080 from web server"
      protocol    = "tcp"
    }
  ]
}

variable "db_user_name" {
  description = "User Name for RDS"
  type = string
  default = "admin"
}

variable "db_password" {
  type = string
  description = "password for RDS"
  sensitive = true
}