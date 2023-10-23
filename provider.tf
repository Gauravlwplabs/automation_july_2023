terraform {
  required_version = ">=1.4"
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~>5.0.0"
    }
    null = {
      source  = "hashicorp/null"
      version = "3.2.1"
    }
  }

  backend "s3" {
    bucket         = "statestorebucket-lwplabs"
    key            = "terraformstatestore-batch-jul-2023"
    region         = "us-east-1"
    profile = "july"
    role_arn       = "arn:aws:iam::869510502397:role/batch_july_sts_assume_role"
    dynamodb_table = "statelocktable"
  }
}

provider "aws" {
  region  = "us-east-1"
  assume_role {
    role_arn     = "arn:aws:iam::869510502397:role/batch_july_sts_assume_role"
    session_name = "test"
  }
}
