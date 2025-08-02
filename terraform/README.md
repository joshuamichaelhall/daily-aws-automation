# Terraform Infrastructure as Code

This directory contains Terraform configurations that complement the daily AWS automation scripts. These infrastructure definitions can be used to set up test environments for script development and demonstrate IaC best practices.

## Directory Structure

```
terraform/
├── modules/          # Reusable Terraform modules
│   ├── vpc/         # VPC and networking
│   ├── ec2/         # EC2 instances
│   ├── s3/          # S3 buckets
│   └── iam/         # IAM roles and policies
├── environments/    # Environment-specific configurations
│   ├── dev/        # Development environment
│   └── prod/       # Production environment
└── backend.tf      # State storage configuration
```

## Getting Started

### Prerequisites

- Terraform >= 1.5.0
- AWS CLI configured
- Appropriate AWS permissions

### Initialize Terraform

```bash
cd terraform/environments/dev
terraform init
terraform plan
terraform apply
```

### State Management

By default, state is stored locally. For team collaboration, configure remote state in `backend.tf`:

```hcl
terraform {
  backend "s3" {
    bucket = "your-terraform-state-bucket"
    key    = "daily-aws-automation/terraform.tfstate"
    region = "us-east-1"
  }
}
```

## Modules

### VPC Module
Creates a standard VPC with public/private subnets across multiple AZs.

### EC2 Module
Provisions EC2 instances with standard tagging and security groups.

### S3 Module
Creates S3 buckets with encryption and versioning enabled by default.

### IAM Module
Manages IAM roles and policies for script execution.

## Best Practices

1. **Always use modules** for reusability
2. **Tag everything** for cost tracking and organization
3. **Use variables** for environment-specific values
4. **Enable versioning** on state files
5. **Plan before apply** to review changes

## Integration with Scripts

The infrastructure created here provides:
- Test environments for script development
- Consistent resource naming for scripts to query
- Proper IAM roles for script execution
- Network isolation for security testing

## Cost Management

All resources are tagged with:
- `Project`: daily-aws-automation
- `Environment`: dev/prod
- `ManagedBy`: terraform
- `Owner`: joshua.hall

Use the cost calculator script to monitor spending!