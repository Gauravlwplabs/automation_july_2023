output "public_subnet_id" {
  value = [ for each in aws_subnet.public_subnet: each.id ]
}

output "vpc_id" {
  value = aws_vpc.this.id
}