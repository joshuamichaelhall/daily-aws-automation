# Setup Guide

## Development Environment Setup

This guide walks you through setting up your local development environment for the Daily AWS Automation Scripts project.

### System Requirements

- **Operating System**: macOS, Linux, or Windows with WSL2
- **Python**: 3.9 or higher
- **AWS CLI**: Version 2.x configured with appropriate credentials
- **Git**: For version control

### Step-by-Step Setup

#### 1. AWS Configuration

Ensure you have AWS CLI configured with appropriate profiles:

```bash
aws configure list-profiles
```

You should see profiles like:
- `iamadmin-general` (for development/testing)
- `iamadmin-production` (for production operations)

If not configured, run:
```bash
aws configure --profile iamadmin-general
```

#### 2. Python Environment

Create and activate a virtual environment:

```bash
# Create virtual environment
python3 -m venv coffee-scripts-env

# Activate it
# On macOS/Linux:
source coffee-scripts-env/bin/activate

# On Windows:
coffee-scripts-env\Scripts\activate
```

#### 3. Install Dependencies

With the virtual environment activated:

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

#### 4. Environment Variables

Copy the example environment file and configure it:

```bash
cp .env.example .env
```

Edit `.env` with your preferred settings:
- `AWS_PROFILE`: Your default AWS profile
- `AWS_DEFAULT_REGION`: Your preferred AWS region
- `OUTPUT_FORMAT`: How you want results displayed (table/json/csv)
- `LOG_LEVEL`: Logging verbosity

#### 5. Pre-commit Hooks (Optional but Recommended)

Set up pre-commit hooks for code quality:

```bash
pre-commit install
```

This will automatically run:
- **black**: Code formatting
- **flake8**: Linting
- **mypy**: Type checking

### Testing Your Setup

Run the setup verification script:

```bash
python scripts/utils/verify_setup.py
```

This checks:
- ✅ Python version
- ✅ Required packages installed
- ✅ AWS credentials configured
- ✅ Environment variables set
- ✅ Basic AWS API connectivity

### IDE Configuration

#### VS Code (Recommended)

1. Install extensions:
   - Python
   - Pylance
   - AWS Toolkit

2. Configure settings.json:
```json
{
    "python.linting.enabled": true,
    "python.linting.flake8Enabled": true,
    "python.formatting.provider": "black",
    "python.testing.pytestEnabled": true,
    "editor.formatOnSave": true
}
```

#### PyCharm

1. Set Python interpreter to virtual environment
2. Enable black formatter
3. Configure AWS toolkit

### Common Issues and Solutions

#### Issue: boto3 cannot find credentials
**Solution**: Ensure AWS_PROFILE is set in .env or export it:
```bash
export AWS_PROFILE=iamadmin-general
```

#### Issue: Permission denied errors
**Solution**: Check IAM policies for your AWS profile. Minimum required:
- ec2:Describe*
- s3:List*, s3:GetBucketPolicy
- iam:List*, iam:Get*
- ce:GetCostAndUsage

#### Issue: Import errors
**Solution**: Ensure virtual environment is activated and dependencies installed:
```bash
which python  # Should show path within coffee-scripts-env
pip list      # Should show all required packages
```

### Daily Workflow

1. **Morning (5:15 AM)**:
   - Activate virtual environment
   - Pull latest changes: `git pull`
   - Create new day's script

2. **Development**:
   - Write script following template
   - Test with dry-run mode
   - Run against test AWS account

3. **Completion**:
   - Run tests: `pytest`
   - Commit with meaningful message
   - Push to GitHub

### Security Best Practices

1. **Never commit**:
   - AWS credentials
   - .env files (only .env.example)
   - Sensitive output data

2. **Always use**:
   - AWS profiles or IAM roles
   - Input validation
   - Try/catch blocks
   - Dry-run options for destructive operations

3. **Regular checks**:
   - Review IAM permissions
   - Audit script access patterns
   - Update dependencies monthly

### Getting Help

- **AWS Documentation**: [boto3 docs](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)
- **Project Issues**: [GitHub Issues](https://github.com/joshuamichaelhall/daily-aws-automation/issues)
- **AWS Support**: Through your AWS console

---

*Last updated: August 2025*