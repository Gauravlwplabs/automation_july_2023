# resource "aws_instance" "web" {
#   for_each = toset(["1","2"])
#   ami           = "ami-0f34c5ae932e6f0e4"
#   instance_type = "t2.micro"
# }

# # aws_instance.web= ["first", "second"]

# # splat expression
# output "public_ip" {
#   value = {for rahul, kiran in aws_instance.web: rahul => kiran.public_ip}
# }