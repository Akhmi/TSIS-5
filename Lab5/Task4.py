import re

def find_sequences(string):
    pattern = r'[A-Z][a-z]+'  
    matches = re.findall(pattern, string)
    return matches

# Test the function
test_string = "This is a Test String with Some Uppercase Letters followed by lowercase letters."
result = find_sequences(test_string)
print("Found sequences:", result)

"""
Found sequences: ['This', 'Test', 'String', 'Some', 'Uppercase', 'Letters']
"""