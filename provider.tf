terraform {
  required_version = ">=1.4"
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~>5.0.0"
    }
  }
}

provider "aws" {
  region  = "us-east-1"
  profile = "july"
  assume_role {
    role_arn     = "arn:aws:iam::520464532822:role/batch_july_sts_assume_role"
    session_name = "test"
  }
}
