import re

def replace_chars(string):
    pattern = r'[ ,.]'  
    replaced_string = re.sub(pattern, ':', string)
    return replaced_string

# Test the function
test_string = "This is a test, string. With spaces, commas, and dots."
result = replace_chars(test_string)
print("Original string:", test_string)
print("Replaced string:", result)

"""
Original string: This is a test, string. With spaces, commas, and dots.
Replaced string: This:is:a:test::string::With:spaces::commas::and:dots:
"""