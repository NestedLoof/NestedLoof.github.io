"""Shared paths for the build scripts. Run scripts from anywhere; paths are relative to the repo."""
import os, sys
TOOLS = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(TOOLS)                      # the repository root (the site itself)
ASSETS = os.path.join(REPO, 'assets')
IMG = os.path.join(ASSETS, 'img')
FONTSRC = os.path.join(TOOLS, 'fontsrc')           # downloaded font sources (git-ignored)
# Optional: a local folder with fontTools installed via `pip install --target tools/pylib fonttools brotli`
PYLIB = os.path.join(TOOLS, 'pylib')
if os.path.isdir(PYLIB):
    sys.path.insert(0, PYLIB)
