import re

def match_pattern(string):
    pattern = r'^a.*b$'  
    if re.match(pattern, string):
        return True
    else:
        return False

# Test the function
test_strings = ['a', 'ab', 'axb', 'acb', 'abc', 'axbc', 'abcb', 'axbcb']
for test_string in test_strings:
    print(f"String: {test_string}, Match: {match_pattern(test_string)}")

"""
String: a, Match: False
String: ab, Match: True   
String: axb, Match: True  
String: acb, Match: True  
String: abc, Match: False 
String: axbc, Match: False
String: abcb, Match: True 
String: axbcb, Match: True
"""