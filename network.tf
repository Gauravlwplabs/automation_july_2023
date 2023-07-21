resource "aws_vpc" "this" {
  cidr_block         = "172.16.0.0/24"
  instance_tenancy   = "default"
  enable_dns_support = true
  tags = {
    Name = "three-tier-vpc-lwplabs"
  }
}


resource "aws_subnet" "private_subnet" {
  #count        = 2
  for_each = { "172.16.0.0/26" : "us-east-1a", "172.16.0.64/26" : "us-east-1b" } # map data
  #for_each = toset(["us-east-1a","us-east-1b"])
  vpc_id     = aws_vpc.this.id
  cidr_block = each.key
  # cidr_block        = element(["172.16.0.0/26", "172.16.0.64/26"], count.index)
  # availability_zone = element(["us-east-1a", "us-east-1b"], count.index)
  availability_zone = each.value
  tags = {
    Name = "private_subnet_${each.value}"
  }
}


resource "aws_subnet" "public_subnet" {
  for_each                = { "172.16.0.128/26" : "us-east-1a", "172.16.0.192/26" : "us-east-1b" }
  vpc_id                  = aws_vpc.this.id
  cidr_block              = each.key
  availability_zone       = each.value
  map_public_ip_on_launch = true
  tags = {
    Name = "public_subnet_${each.value}"
  }
}