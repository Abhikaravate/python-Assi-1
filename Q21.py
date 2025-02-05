
import re

def isstring(s):
    pattern = re.compile("^[A-Za-z0-9]+$")
    return bool(pattern.match(s))


test_string = "Hello123"
if isstring(test_string):
    print("Valid string")
else:
    print("Invalid string")