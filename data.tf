data "aws_availability_zones" "this" {
  all_availability_zones = true
  filter {
    name   = "opt-in-status"
    values = ["opt-in-not-required"]
  }
}

# output "map_az" {
#   value = {for index, az_name in slice(data.aws_availability_zones.this.names,0,var.num_of_subnets): index => az_name} 
# }
