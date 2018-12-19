"""Get project name from user input."""

import sys


def proj_name():
    """Get project name from user input."""
    if len(sys.argv) != 2:
        sys.exit("Project directory required.")
    return sys.argv[1]
