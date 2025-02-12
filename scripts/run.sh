#!/usr/bin/env bash
# run.sh — Activate the virtual environment and run Django using the module (-m) syntax

# Change to the project root (assumed to be the parent directory of the scripts folder)
cd "$(dirname "$0")/.." || { echo "Failed to change directory to project root"; exit 1; }

# Check if the virtual environment exists
if [ ! -d "venv" ]; then
    echo "Virtual environment 'venv' not found. Create it with:"
    python3 -m venv venv
    source venv/bin/activate
    pip3 install --upgrade pip
    pip3 install -r requirements.txt
    python3 manage.py migrate
    python3 manage.py runserver
    exit 1
fi

# Activate the virtual environment
echo "Activating virtual environment..."
source venv/bin/activate || { echo "Failed to activate venv"; exit 1; }
echo "Virtual environment activated."

# Ensure Django is installed in the virtual environment.
if ! python3 -c "import django" &>/dev/null; then
    echo "Django not found in the virtual environment. Installing Django..."
    pip3 install --break-system-packages django || { echo "Failed to install Django"; exit 1; }
    pip3 install --break-system-packages djangorestframework || { echo "Failed to install Django Rest Framework"; exit 1; }
fi # break system packages to bypass pip's protections against modifying system packages

# (Optional) You can print the current PYTHONPATH for debugging:
echo "Current PYTHONPATH: $PYTHONPATH"

# Start the Django development server using module syntax.
# This command runs the manage.py module as "API.manage" from the project root.
# (When using -m, sys.path[0] becomes the current working directory—in this case, baseAPI.)
echo "Starting Django development server..."
ls
cd API
ls
python3 manage.py runserver || { echo "Failed to start Django development server"; exit 1; }