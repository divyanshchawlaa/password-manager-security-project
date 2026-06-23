#!/bin/bash

echo "======================================"
echo "Secure Password Manager Setup"
echo "======================================"

echo ""
echo "Creating virtual environment..."
python3 -m venv venv

echo ""
echo "Activating virtual environment..."
source venv/bin/activate

echo ""
echo "Installing dependencies..."
pip install -r requirements.txt

echo ""
echo "Generating encryption key..."
python generate_key.py

echo ""
echo "Creating database..."
python -c "from app import app, db; app.app_context().push(); db.create_all()"

echo ""
echo "======================================"
echo "Setup Complete"
echo "======================================"

echo ""
echo "Run the application using:"
echo ""
echo "python app.py"
