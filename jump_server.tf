resource "aws_instance" "jump_server" {
  ami           = var.jump_server_image
  instance_type = var.jump_server_instance_type
  key_name      = "test"
  subnet_id     = element([for each_subnet in aws_subnet.public_subnet : each_subnet.id], 0)
  tags = {
    Name = "jump-server-${local.vpc_name}"
  }
  vpc_security_group_ids = [aws_security_group.allow_ssh_jump_server.id]
  provisioner "local-exec" {
    command = "scp -i ~/Downloads/test.pem ~/Downloads/test.pem ec2-user@${self.public_ip}:~"
  }
}