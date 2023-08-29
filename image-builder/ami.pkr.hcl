locals {
  image_name = "${var.app_name}-lwplabs-packer"
}

source "amazon-ebs" "this" {
  assume_role {
    role_arn     = "arn:aws:iam::869510502397:role/batch_july_sts_assume_role"
    session_name = "packer-test"
  }
  region        = var.region
  source_ami    = var.source_ami
  instance_type = var.instance_type
  ssh_username  = var.ssh_user_name
  ami_name      = local.image_name
  profile       = "july"
}

build {
  sources = [
    "source.amazon-ebs.this"
  ]

  provisioner "shell" {
    inline = [
      "sudo yum update -y",
      "sudo yum install httpd -y",
      "sudo systemctl enable httpd",
      "sudo systemctl start httpd",
      "sudo echo '<h1>Welcome to Automation course at LWPLabs pvt ltd</h1>'|sudo tee /var/www/html/index.html"
    ]
  }
}
