# SAS SWAT Demo: CAS Analytics with OAuth2 and Python

A simple demonstration of connecting to SAS Cloud Analytics Services (CAS) using Python SWAT library with OAuth2 authentication.

## Overview

This project demonstrates how to:
- Authenticate with SAS Cloud using OAuth2
- Connect to CAS using the SWAT Python library
- Upload data and perform analytics
- Build and analyze a linear regression model

## Prerequisites

- Python 3.8+
- Access to SAS Cloud Analytics Services (CAS)
- SAS credentials for authentication

## Installation

1. Clone this repository:
```bash
git clone <repository-url>
cd sas-swat-demo
```

2. Create a virtual environment:
```bash
python -m venv venv
venv\Scripts\activate  # Windows
# or
source venv/bin/activate  # Linux/Mac
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
```bash
cp env.sample .env
```

Edit `.env` with your SAS credentials:
```
SAS_CLIENT_ID=your_client_id_here
SAS_CLIENT_SECRET=your_client_secret_here
SAS_BASE_URL=https://create.demo.sas.com
SAS_CERT_PATH=C:/sas/model-manager/demo-rootCA-Intermidiates_4CLI.pem
```

## Usage

Run the demo:
```bash
python cas.py
```

The script will:
1. Authenticate with SAS Cloud using OAuth2
2. Connect to CAS
3. Upload sample car data
4. Build a linear regression model predicting MPG from vehicle weight
5. Display model results and parameter estimates

## Project Structure

- `cas.py` - Main demo script with CAS analytics
- `auth_utils.py` - OAuth2 authentication utilities
- `requirements.txt` - Python dependencies
- `env.sample` - Environment variables template
- `.gitignore` - Git ignore rules for sensitive files

## Features

- **OAuth2 Authentication**: Secure token-based authentication with SAS Cloud
- **CAS Connection**: HTTPS connection to Cloud Analytics Services
- **Data Upload**: Upload pandas DataFrames to CAS
- **Analytics**: Perform regression analysis using CAS actions
- **Model Interpretation**: Extract and display model parameters


## Troubleshooting

- Ensure your SAS credentials are correct in the `.env` file
- Verify the certificate path is accessible
- Check that you have network access to the SAS Cloud instance

## Dependencies

- `swat` - SAS Cloud Analytics Services Python client
- `pandas` - Data manipulation
- `requests` - HTTP requests for OAuth2
- `python-dotenv` - Environment variable management
- `urllib3` - HTTP client library 