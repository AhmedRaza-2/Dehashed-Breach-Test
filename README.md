Breached Data Lookup Tool

This Python program allows users to check if their email or username has been compromised in known data breaches by searching through a provided CSV file.

Features

Search for email addresses or usernames in a local CSV file.

Display details of any breaches found.

Prerequisites

Python 3.x installed on your system.

The required dependencies (if any).

Installation

Clone or download the repository.

Ensure Python is installed by running:

python --version

Place the breached_data.csv file in the same directory as the script.

CSV File Format

The CSV file should have the following structure:

email,username,password,breach
john.doe@example.com,johndoe,password123,LinkedIn
jane.smith@example.com,janesmith,qwerty,Adobe
test.user@example.com,testuser,123456,Facebook
admin@example.com,admin,admin123,Yahoo

Usage

Run the script using the command:

python breach_lookup.py

Enter an email or username when prompted.

The script will check the CSV file and display breach details if found.

Example

Enter email or username: johndoe
Breached account found:
Email: john.doe@example.com
Username: johndoe
Breach: LinkedIn

Notes

The data in the CSV file is sample data; replace it with real breach data as needed.

No API access is required; everything runs locally.

License

This project is licensed under the MIT License.
