variable app_name{
    description = "app name for the server"
    type = string
    default = "web-server"
}

variable source_ami{
    description = "AMI ID of source image"
    type = string
    default = "ami-08a52ddb321b32a8c"
}

variable instance_type{
    description = "Instance type of server"
    type = string
    default = "t2.micro"
}

variable ssh_user_name{
    description = "ssh user name of server"
    type = string
    default = "ec2-user"
}

variable region{
    type =string
}