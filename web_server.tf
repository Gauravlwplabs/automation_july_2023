resource "aws_instance" "web_server" {
  ami           = var.web_server_image
  instance_type = var.web_server_instance_type
  key_name      = "test"
  subnet_id     = element([for each_subnet in aws_subnet.private_subnet : each_subnet.id], 0)
  tags = {
    Name = "web-server-${local.vpc_name}"
  }
  user_data              = file("./user_data.sh")
  vpc_security_group_ids = [aws_security_group.allow_web_server.id]
}