# Week 3: First Coffee Scripts (Simple & Safe)

## Overview
Your first week writing actual AWS automation! Focus on simple, read-only operations that build confidence.

## Coffee Script Rules
- **15 minutes maximum** per script
- **Read-only operations** only (no modifications)
- **5-15 lines of code** maximum
- **Business context** required
- **Daily commit** to build portfolio

## Scripts

| Day | Script | Purpose | Business Value |
|-----|--------|---------|----------------|
| Day 1 | hello_aws.py | Verify AWS connection | Troubleshooting & validation |
| Day 2 | list_regions.py | List all AWS regions | Architecture planning |
| Day 3 | count_buckets.py | Count S3 buckets | Asset inventory |
| Day 4 | ec2_summary.py | EC2 instance summary | Capacity planning |
| Day 5 | cost_preview.py | Today's AWS spend | Budget monitoring |

## Day 1: Hello AWS
```python
#!/usr/bin/env python3
"""Verify AWS connection and credentials"""
import boto3

sts = boto3.client('sts')
caller = sts.get_caller_identity()

print(f"Connected to AWS!")
print(f"Account: {caller['Account']}")
print(f"User: {caller['Arn'].split('/')[-1]}")
```

**Business Value**: Quick connectivity test for troubleshooting
**MSP Insight**: First step in any client environment audit

## Day 2: Region Explorer
```python
#!/usr/bin/env python3
"""List all available AWS regions"""
import boto3

ec2 = boto3.client('ec2')
regions = ec2.describe_regions()['Regions']

print(f"Found {len(regions)} AWS regions:")
for region in sorted(regions, key=lambda x: x['RegionName']):
    print(f"  - {region['RegionName']}")
```

**Business Value**: Architecture and disaster recovery planning
**MSP Insight**: Helps clients understand global infrastructure options

## Day 3: S3 Bucket Counter
```python
#!/usr/bin/env python3
"""Count total S3 buckets"""
import boto3

s3 = boto3.client('s3')
buckets = s3.list_buckets()['Buckets']

print(f"Total S3 buckets: {len(buckets)}")
if buckets:
    oldest = min(buckets, key=lambda x: x['CreationDate'])
    print(f"Oldest bucket: {oldest['Name']} ({oldest['CreationDate'].date()})")
```

**Business Value**: Asset inventory and compliance tracking
**MSP Insight**: First step in data governance assessment

## Day 4: EC2 Summary
```python
#!/usr/bin/env python3
"""Summarize EC2 instances by state"""
import boto3

ec2 = boto3.client('ec2')
instances = ec2.describe_instances()

total = 0
running = 0
for reservation in instances['Reservations']:
    for instance in reservation['Instances']:
        total += 1
        if instance['State']['Name'] == 'running':
            running += 1

print(f"EC2 Summary: {running} running, {total} total instances")
```

**Business Value**: Capacity planning and cost optimization
**MSP Insight**: Quick health check of compute resources

## Day 5: Cost Preview
```python
#!/usr/bin/env python3
"""Check today's AWS spending"""
import boto3
from datetime import datetime

ce = boto3.client('ce')
today = datetime.now().strftime('%Y-%m-%d')

result = ce.get_cost_and_usage(
    TimePeriod={'Start': today, 'End': today},
    Granularity='DAILY',
    Metrics=['UnblendedCost']
)

cost = float(result['ResultsByTime'][0]['Total']['UnblendedCost']['Amount'])
print(f"Today's spend so far: ${cost:.2f}")
```

**Business Value**: Real-time budget monitoring
**MSP Insight**: Daily cost awareness prevents bill shock

## Key Learnings This Week
- [ ] Basic boto3 client usage
- [ ] Simple error handling patterns
- [ ] AWS response parsing
- [ ] Git commit workflows
- [ ] Business value articulation

## Common Patterns
```python
# 1. Client creation
client = boto3.client('service-name')

# 2. Simple API call
response = client.operation_name()

# 3. Safe data extraction
data = response.get('Key', [])

# 4. Basic output
print(f"Found {len(data)} items")
```

## Success Metrics
- [ ] All 5 scripts work without errors
- [ ] Daily commits to GitHub
- [ ] Can explain business value of each script
- [ ] Comfortable with basic boto3 patterns
- [ ] Ready for Week 4 complexity

## Weekend Review
- Review all scripts and commit messages
- Create a personal cheat sheet
- Plan Week 4 improvements

## Notes
*Keep it simple! The goal is building confidence and daily habits, not complex automation.*

---
**Week 4 Preview**: Add basic business logic like finding stopped instances and missing tags.