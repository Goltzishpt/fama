#!/bin/bash

set -e

PROJECT_ROOT=$(pwd)
TESTS_DIR="$PROJECT_ROOT/tests"
VENV_DIR="$PROJECT_ROOT/venv"
REQUIREMENTS_FILE="$PROJECT_ROOT/requirements.txt"

if [ -d "$VENV_DIR" ]; then
    source "$VENV_DIR/bin/activate"
else
    python3 -m venv "$VENV_DIR"
    source "$VENV_DIR/bin/activate"
fi

if [ -f "$REQUIREMENTS_FILE" ]; then
    pip install --upgrade pip
    pip install -r "$REQUIREMENTS_FILE"
else
    exit 1
fi

python3 run.py

python3 -m unittest discover "$TESTS_DIR"
