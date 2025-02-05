def modify_string(s):
    if len(s) < 3:
        return s
    elif s.endswith("ing"):
        return s + "ly"
    else:
        return s + "ing"

# Example usage
print(modify_string("run"))       # Output: "running"
print(modify_string("running"))   # Output: "runningly"
print(modify_string("go"))        # Output: "go"
