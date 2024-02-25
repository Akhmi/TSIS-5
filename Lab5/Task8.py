import re

def split_at_uppercase(string):
    parts = re.findall('[A-Z][^A-Z]*', string)
    return parts

# Test the function
test_string = "SplitThisStringAtUppercaseLetters"
result = split_at_uppercase(test_string)
print("Original string:", test_string)
print("Split parts:", result)

"""
Original string: SplitThisStringAtUppercaseLetters
Split parts: ['Split', 'This', 'String', 'At', 'Uppercase', 'Letters']
"""