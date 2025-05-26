#!/usr/bin/env python3
"""
Simple script to bump the version of FuGEP.
"""

import sys
import argparse
from version_manager import FuGEPVersionManager

def main():
    """Bump the version."""
    parser = argparse.ArgumentParser(description="Bump FuGEP version")
    parser.add_argument("type", choices=["major", "minor", "patch"],
                       default="patch", nargs='?',
                       help="Type of version bump (default: patch)")
    
    args = parser.parse_args()
    
    try:
        manager = FuGEPVersionManager()
        new_version = manager.bump_version(args.type)
        print(f"Version bumped to: {new_version}")
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()