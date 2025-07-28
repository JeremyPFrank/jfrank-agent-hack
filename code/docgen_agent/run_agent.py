#!/usr/bin/env python3
"""
Interactive Document Generation Agent Runner

This script provides an easy way to run the document generation agent
with command line input for the research topic.
"""

import os
import sys

# Add the code directory to the path so we can import the agent
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'code'))

from docgen_agent.__main__ import main

if __name__ == "__main__":
    main()
