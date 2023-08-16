locals {
  vpc_name = "${var.vpc_name}-lwplabs"
  newbits  = var.num_of_subnets == 1 ? 1 : var.num_of_subnets == 2 ? 2 : (var.num_of_subnets == 3 || var.num_of_subnets == 4) ? 3 : 4
}