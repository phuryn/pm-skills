#!/bin/bash
set -euo pipefail

# Only run in Claude Code on the web
if [ "${CLAUDE_CODE_REMOTE:-}" != "true" ]; then
  exit 0
fi

# Python 3 is pre-installed and validate_plugins.py uses only stdlib.
# Ensure python3 is available on PATH.
command -v python3 >/dev/null 2>&1 || { echo "python3 not found"; exit 1; }
