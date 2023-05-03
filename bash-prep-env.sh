#!/bin/bash

# Install virtualenv and development tools if not already installed
yum -y install python3-virtualenv python3-devel gcc

# Create a new virtual environment in the current directory
python3 -m venv myenv

# Activate the virtual environment
source myenv/bin/activate

# Install the required dependencies
pip install requests
