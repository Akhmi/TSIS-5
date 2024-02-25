import re

def insert_spaces(string):
    result = re.sub(r'(?<!^)(?=[A-Z])', ' ', string)
    return result

# Test the function
test_string = "InsertSpacesBetweenWordsStartingWithCapitalLetters"
result = insert_spaces(test_string)
print("Original string:", test_string)
print("Modified string:", result)

"""
Original string: InsertSpacesBetweenWordsStartingWithCapitalLetters
Modified string: Insert Spaces Between Words Starting With Capital Letters
"""