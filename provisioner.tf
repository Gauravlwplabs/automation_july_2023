# resource "null_resource" "this" {
#   # Changes to any instance of the cluster requires re-provisioning
#   triggers = {
#     always_run = timestamp()
#   }
#   provisioner "local-exec" {
#     command    = "scp  -o StrictHostKeyChecking=no -i ~/Downloads/test.pem ~/Downloads/test.pem ec2-user@${aws_instance.jump_server.public_ip}:~"
#     on_failure = continue
#   }
#   connection {
#     host        = aws_instance.jump_server.public_ip
#     type        = "ssh"
#     user        = "ec2-user"
#     private_key = file("~/Downloads/test.pem")
#   }
#   provisioner "remote-exec" {
#     inline = [
#       "chmod 400 test.pem"
#     ]
#     on_failure = continue
#   }

#   provisioner "file" {
#     source      = "user_data.sh"
#     destination = "/home/ec2-user/script"
#     on_failure  = continue
#   }


#   depends_on = [aws_instance.jump_server]
# }