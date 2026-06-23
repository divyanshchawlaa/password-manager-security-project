#!/bin/bash

echo "Creating virtual environment..."

python3 -m venv venv

echo "Activating virtual environment..."

source venv/bin/activate

echo "Installing dependencies..."

pip install -r requirements.txt

echo "Generating encryption key..."

python generate_key.py

echo "Setup complete."

echo "Run the application using:"

echo "python app.py"
