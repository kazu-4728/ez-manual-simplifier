#!/bin/bash
set -euo pipefail

if [ "${CLAUDE_CODE_REMOTE:-}" != "true" ]; then
  exit 0
fi

cd "$CLAUDE_PROJECT_DIR"

pip install -r requirements.txt

# The base image ships a Debian-managed `cryptography` package that is
# missing its `_cffi_backend` extension, which crashes pdfminer (a
# markitdown dependency) at import time. Install a self-contained wheel
# to shadow it; --ignore-installed avoids pip trying (and failing) to
# uninstall the apt-managed package.
pip install --ignore-installed cryptography cffi
