terraform {
  required_version = ">= 1.5.0"
  
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region  = var.aws_region
  profile = var.aws_profile

  default_tags {
    tags = local.common_tags
  }
}

locals {
  environment = "dev"
  common_tags = merge(
    var.common_tags,
    {
      Project     = var.project_name
      Environment = local.environment
    }
  )
}

# VPC for development environment
module "vpc" {
  source = "../../modules/vpc"

  project_name       = var.project_name
  environment        = local.environment
  vpc_cidr          = "10.0.0.0/16"
  availability_zones = ["us-east-1a", "us-east-1b"]
  common_tags       = local.common_tags
}

# S3 bucket for script outputs
module "script_outputs" {
  source = "../../modules/s3"

  bucket_name       = "${var.project_name}-${local.environment}-outputs"
  environment       = local.environment
  enable_versioning = true
  common_tags      = local.common_tags

  lifecycle_rules = [
    {
      id               = "archive-old-outputs"
      enabled          = true
      transition_days  = 30
      storage_class    = "STANDARD_IA"
      expiration_days  = 90
    }
  ]
}