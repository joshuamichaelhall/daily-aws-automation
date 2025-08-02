output "vpc_id" {
  description = "ID of the development VPC"
  value       = module.vpc.vpc_id
}

output "script_outputs_bucket" {
  description = "Name of the S3 bucket for script outputs"
  value       = module.script_outputs.bucket_id
}

output "public_subnet_ids" {
  description = "IDs of public subnets"
  value       = module.vpc.public_subnet_ids
}

output "private_subnet_ids" {
  description = "IDs of private subnets"
  value       = module.vpc.private_subnet_ids
}