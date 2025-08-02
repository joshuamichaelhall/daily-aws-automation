variable "aws_region" {
  description = "AWS region to deploy resources"
  type        = string
  default     = "us-east-1"
}

variable "aws_profile" {
  description = "AWS profile to use"
  type        = string
  default     = "iamadmin-general"
}

variable "project_name" {
  description = "Name of the project"
  type        = string
  default     = "daily-aws-automation"
}

variable "common_tags" {
  description = "Common tags to apply to all resources"
  type        = map(string)
  default = {
    ManagedBy = "terraform"
    Owner     = "joshua.hall"
    Purpose   = "AWS automation script testing"
    CostCenter = "development"
  }
}