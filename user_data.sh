#! /bin/bash

sudo yum update -y
sudo yum install httpd -y
sudo systemctl enable httpd
sudo systemctl start httpd
sudo echo "<h1>Welcome to Terraform course at LWPLabs</h1>"|sudo tee /var/www/html/index.html

