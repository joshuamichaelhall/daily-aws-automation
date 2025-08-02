#!/usr/bin/env python3
"""
Setup Verification Script

Verifies that the development environment is properly configured
for running the daily AWS automation scripts.

Author: Joshua Michael Hall
Date: August 2025
"""

import sys
import os
import importlib
from pathlib import Path

from rich.console import Console
from rich.table import Table

console = Console()


def check_python_version():
    """Check if Python version meets requirements."""
    version = sys.version_info
    if version.major >= 3 and version.minor >= 9:
        return True, f"{version.major}.{version.minor}.{version.micro}"
    return False, f"{version.major}.{version.minor}.{version.micro}"


def check_required_packages():
    """Check if all required packages are installed."""
    required_packages = [
        'boto3',
        'click',
        'rich',
        'python-dotenv',
        'pandas',
        'tabulate',
        'pytest'
    ]
    
    results = []
    for package in required_packages:
        try:
            importlib.import_module(package.replace('-', '_'))
            results.append((package, True, "Installed"))
        except ImportError:
            results.append((package, False, "Not installed"))
    
    return results


def check_aws_credentials():
    """Check if AWS credentials are configured."""
    try:
        import boto3
        from botocore.exceptions import NoCredentialsError, ProfileNotFound
        
        # Check for environment variables or profiles
        session = boto3.Session()
        
        # Try to get credentials
        credentials = session.get_credentials()
        if credentials:
            return True, "AWS credentials found"
        else:
            return False, "No AWS credentials found"
            
    except Exception as e:
        return False, f"Error checking credentials: {str(e)}"


def check_environment_file():
    """Check if .env file exists."""
    env_path = Path(__file__).parent.parent.parent / '.env'
    if env_path.exists():
        return True, ".env file exists"
    return False, ".env file not found (copy from .env.example)"


def check_aws_connectivity():
    """Test basic AWS API connectivity."""
    try:
        import boto3
        
        sts = boto3.client('sts')
        identity = sts.get_caller_identity()
        return True, f"Connected as: {identity['Arn']}"
    except Exception as e:
        return False, f"Cannot connect to AWS: {str(e)}"


def main():
    """Run all setup verification checks."""
    console.print("\n[bold blue]Daily AWS Automation - Setup Verification[/bold blue]\n")
    
    # Create results table
    table = Table(title="Environment Check Results")
    table.add_column("Check", style="cyan")
    table.add_column("Status", style="bold")
    table.add_column("Details")
    
    # Python version check
    passed, version = check_python_version()
    table.add_row(
        "Python Version",
        "[green]✓ PASS[/green]" if passed else "[red]✗ FAIL[/red]",
        f"Python {version} (requires 3.9+)"
    )
    
    # Environment file check
    passed, details = check_environment_file()
    table.add_row(
        "Environment File",
        "[green]✓ PASS[/green]" if passed else "[yellow]⚠ WARNING[/yellow]",
        details
    )
    
    # Package checks
    package_results = check_required_packages()
    all_packages_installed = all(result[1] for result in package_results)
    
    failed_packages = [pkg[0] for pkg in package_results if not pkg[1]]
    if failed_packages:
        details = f"Missing: {', '.join(failed_packages)}"
    else:
        details = "All required packages installed"
    
    table.add_row(
        "Required Packages",
        "[green]✓ PASS[/green]" if all_packages_installed else "[red]✗ FAIL[/red]",
        details
    )
    
    # AWS credentials check
    passed, details = check_aws_credentials()
    table.add_row(
        "AWS Credentials",
        "[green]✓ PASS[/green]" if passed else "[red]✗ FAIL[/red]",
        details
    )
    
    # AWS connectivity check
    passed, details = check_aws_connectivity()
    table.add_row(
        "AWS Connectivity",
        "[green]✓ PASS[/green]" if passed else "[yellow]⚠ WARNING[/yellow]",
        details
    )
    
    # Display results
    console.print(table)
    
    # Package details if needed
    if not all_packages_installed:
        console.print("\n[yellow]To install missing packages:[/yellow]")
        console.print("pip install -r requirements.txt")
    
    # Overall status
    console.print("\n[bold]Overall Status:[/bold]")
    if all_packages_installed and check_python_version()[0]:
        console.print("[green]✓ Environment is ready for AWS automation scripts![/green]")
    else:
        console.print("[red]✗ Please fix the issues above before running scripts.[/red]")
        sys.exit(1)


if __name__ == "__main__":
    main()