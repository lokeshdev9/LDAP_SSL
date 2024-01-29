# LDAP SSL Certificate Notifier

This project consists of Python scripts to monitor changes in an LDAP server's SSL certificate and notify a team when changes occur.

## Table of Contents

- [Overview](#overview)
- [How to Use](#how-to-use)
- [Dependencies](#dependencies)
- [Configuration](#configuration)

## Overview

The project includes two main scripts:

- **ldap_ssl_checker.py**: Connects to an LDAP server, retrieves SSL certificate information, and detects changes.
- **notification_script.py**: Sends email notifications to the team when SSL certificate changes are detected.

## How to Use

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/lokeshdev9/LDAP_SSL.git
   cd LDAP_SSL

## Dependencies
Install Required Python Packages:

bash
Copy code
pip install -r requirements.txt

## Configuration:

Configure LDAP and Email settings in ldap_ssl_checker.py and notification_script.py

Run the Scripts:

python ldap_ssl_checker.py


Dependencies
Python3
ldap3
cryptography
smtplib



Configuration
Edit the following configuration parameters in ldap_ssl_checker.py and notification_script.py:

LDAP Configuration (ldap_ssl_checker.py)

ldap_server
ldap_user
ldap_password
ldap_search_base
Email Configuration (notification_script.py)

smtp_server
smtp_port
smtp_username
smtp_password
sender_email
recipient_email


