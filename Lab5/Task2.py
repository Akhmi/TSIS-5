import re

def match_pattern(string):
    pattern = 'ab{2,3}' 
    if re.fullmatch(pattern, string):
        return True
    else:
        return False

# Test the function
test_strings = ['ab', 'abb', 'abbb', 'ac', 'abc', 'abbc', 'abbbc']
for test_string in test_strings:
    print(f"String: {test_string}, Match: {match_pattern(test_string)}")

"""
String: ab, Match: False
String: abb, Match: True   
String: abbb, Match: True  
String: ac, Match: False   
String: abc, Match: False  
String: abbc, Match: False 
String: abbbc, Match: False
"""
