import re

def match_pattern(string):
    pattern = 'ab*' 
    if re.fullmatch(pattern, string):
        return True
    else:
        return False

# Test the function
test_strings = ['a', 'ab', 'abb', 'abbb', 'ac', 'abc', 'abbc']
for test_string in test_strings:
    print(f"String: {test_string}, Match: {match_pattern(test_string)}")


"""
String: a, Match: True 
String: ab, Match: True
String: abb, Match: True  
String: abbb, Match: True 
String: ac, Match: False  
String: abc, Match: False 
String: abbc, Match: False
"""