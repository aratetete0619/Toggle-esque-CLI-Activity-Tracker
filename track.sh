#!/bin/bash

if [ -z "$TRACKER_PROJECT_DIR" ]; then
    echo "Error: TRACKER_PROJECT_DIR environment variable is not set. Please run the install.sh script first."
    exit 1
fi

cd "$TRACKER_PROJECT_DIR" && docker compose run app
