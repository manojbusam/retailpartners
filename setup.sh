#!/bin/bash

# Exit on error
set -e



# Create a new directory for the project
mkdir -p product_api
cd product_api

# Create a Python virtual environment
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Create requirements.txt (no need for sqlite3)
echo "" > requirements.txt  # Empty requirements.txt since sqlite3 is built-in

# Install dependencies (if any)
pip3 install -r ../requirements.txt  # This should succeed since it's empty

# Start MySQL server
mysql.server start

# Run the existing Python script using python3
python3 ../product_api.py

 

echo "Setup complete. The SQLite database has been created and populated with sample data."