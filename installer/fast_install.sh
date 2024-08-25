#!/bin/bash

ORIGINAL_DIR="$(pwd)"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

cd "$SCRIPT_DIR"

if command -v python &>/dev/null; then
    PYTHON_CMD="python"
elif command -v python3 &>/dev/null; then
    PYTHON_CMD="python3"
else
    echo "Unknown python alias." >&2
    exit 1
fi

$PYTHON_CMD install_tge.py -install_option 1 -install_minified n -skip_dependencies -clingy

cd "$ORIGINAL_DIR"