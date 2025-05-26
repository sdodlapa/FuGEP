#!/usr/bin/env python3
"""
Simple script to get the current version of FuGEP.
"""

import sys
from version_manager import FuGEPVersionManager

def main():
    """Get and print the current version."""
    try:
        manager = FuGEPVersionManager()
        version = manager.get_current_version()
        print(version)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        exit(1)

if __name__ == "__main__":
    main()