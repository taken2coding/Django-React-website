#!/bin/bash

# Exit on any error
set -e

# Define project paths
PROJECT_ROOT=$(pwd)
FRONTEND_DIR="$PROJECT_ROOT/frontend"
BACKEND_DIR="$PROJECT_ROOT/backend"
STATICFILES_DIR="$PROJECT_ROOT/staticfiles"
FRONTEND_STATIC_DIR="$STATICFILES_DIR/frontend"
STATIC_ROOT="$STATICFILES_DIR/backend"

# Step 1: Clean up previous static files to avoid conflicts
echo "Cleaning up previous static files..."
rm -rf "$FRONTEND_STATIC_DIR"/* "$STATIC_ROOT"/*

# Step 2: Build the frontend
echo "Building frontend..."
cd "$FRONTEND_DIR"
npm install  # Ensure dependencies are installed
npm run build

# Step 3: Move frontend build output to staticfiles/frontend/
#echo "Moving frontend build to $FRONTEND_STATIC_DIR..."
# Adjust this based on your frontend framework's output directory
# For React (Create React App), the default output is 'build/'
#mv build/* "$FRONTEND_STATIC_DIR" || {
#    echo "Error: Failed to move frontend build output"
#    exit 1
#}

# Clean up the temporary build directory
rm -rf build

# Step 4: Run Django collectstatic
echo "Running Django collectstatic..."
cd "$BACKEND_DIR"
pip install -r requirements.txt
python manage.py collectstatic --noinput || {
    echo "Error: collectstatic failed"
    exit 1
}
python manage.py migrate

echo "Build completed successfully!"
echo "Static files are in $STATIC_ROOT"
echo "front end Static files are in $FRONTEND_STATIC_DIR"