# Daily AWS Automation Scripts 🚀

> Daily AWS automation scripts built during morning coffee. Practical boto3 solutions for real-world cloud engineering tasks.

## Overview

This repository contains a growing collection of AWS automation scripts developed during daily morning coffee sessions (5:15-5:30 AM). Each script solves a real-world cloud engineering problem, demonstrating practical applications of boto3 and AWS services.

### Why This Project Matters

As a cloud engineer transitioning from MSP ownership, I understand the importance of automation in managing cloud infrastructure efficiently. These scripts showcase:

- **Practical Problem Solving**: Each script addresses actual challenges faced in cloud operations
- **Cost Optimization**: Tools that help identify and reduce unnecessary AWS spending
- **Security Best Practices**: Automated security audits and compliance checks
- **Operational Excellence**: Streamlined workflows for common AWS tasks

## 🎯 Business Value

Every script in this collection provides tangible business benefits:

- **Time Savings**: Automate repetitive tasks that typically consume hours
- **Cost Reduction**: Identify unused resources and optimization opportunities
- **Risk Mitigation**: Proactive security scanning and compliance checking
- **Operational Insights**: Clear visibility into AWS resource utilization

## 📁 Repository Structure

```
daily-aws-automation/
├── scripts/
│   ├── week01/         # Week 1: Foundation scripts
│   ├── week02/         # Week 2: Security focus
│   └── utils/          # Shared utilities
├── docs/               # Documentation
├── tests/              # Unit tests
└── requirements.txt    # Python dependencies
```

## 🚀 Getting Started

### Prerequisites

- Python 3.9 or higher
- AWS CLI configured with appropriate credentials
- Basic understanding of AWS services

### Installation

1. Clone the repository:
```bash
git clone https://github.com/joshuamichaelhall/daily-aws-automation.git
cd daily-aws-automation
```

2. Create a virtual environment:
```bash
python -m venv coffee-scripts-env
source coffee-scripts-env/bin/activate  # On Windows: coffee-scripts-env\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Configure environment:
```bash
cp .env.example .env
# Edit .env with your AWS profile and preferences
```

## 📅 Week 1 Scripts

| Day | Script | Business Value |
|-----|--------|----------------|
| Mon | EC2 Instance Inventory | Asset management and cost tracking |
| Tue | S3 Bucket Security Audit | Security compliance reporting |
| Wed | Security Group Scanner | Security posture assessment |
| Thu | IAM User Access Report | Access review and compliance |
| Fri | Monthly Cost Calculator | Budget tracking and optimization |
| Sat | EBS Snapshot Automation | Backup automation and DR |

## 🔧 Usage Examples

### EC2 Instance Inventory
```bash
python scripts/week01/day01_ec2_inventory.py --profile production --output csv
```

### S3 Security Audit
```bash
python scripts/week01/day02_s3_security_audit.py --check-encryption --check-public
```

### Cost Calculator
```bash
python scripts/week01/day05_cost_calculator.py --month current --breakdown-by-service
```

## 🏗️ Technical Stack

- **Language**: Python 3.9+
- **AWS SDK**: boto3
- **CLI Framework**: Click
- **Output Formatting**: Rich
- **Testing**: pytest with moto for AWS mocking
- **Code Quality**: black, flake8, mypy

## 🔒 Security Considerations

- No credentials are hardcoded - all scripts use AWS profiles or IAM roles
- Input validation on all user-provided parameters
- Read-only operations by default with explicit flags for modifications
- Comprehensive error handling and logging

## 📈 Future Enhancements

- [ ] Week 2: Advanced security automation scripts
- [ ] Week 3: Cost optimization deep dives
- [ ] Week 4: Infrastructure as Code helpers
- [ ] Integration with AWS Organizations
- [ ] Slack/email notifications for critical findings
- [ ] Web dashboard for script results

## 🤝 Contributing

While this is primarily a personal learning project, suggestions and feedback are welcome! Feel free to:

- Open an issue for bug reports or feature suggestions
- Submit pull requests for improvements
- Share your own AWS automation ideas

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👤 Author

**Joshua Michael Hall**
- Former MSP Founder transitioning to Cloud Engineering
- Currently pursuing AWS Solutions Architect Associate certification
- Focus on cost optimization and security automation

Connect with me on [LinkedIn](https://linkedin.com/in/joshuamichaelhall) to discuss cloud automation and AWS best practices!

---

*Built with ☕ during morning coffee sessions | Pursuing excellence in cloud engineering*