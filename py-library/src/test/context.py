import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

"""
import stuff from the local source here to test against it with the tests in testDir.
you can then run these tests from <projectName>/py-library/ with "pytest ." (no quotes).
if you want to test against a pip install, just import from the package name instead of 
.context in your test files

for testing against local source:
    (in context.py (this file)):
        from main.<package> import <thing>
    (in test_*.py):
        from .context import <thing>
        
for testing against pip install:
    (in test_*.py)
        from <package> import <thing>
"""
