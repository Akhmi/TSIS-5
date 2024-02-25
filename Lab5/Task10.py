def camel_to_snake(camel_str):
    snake_str = camel_str[0].lower()
    for char in camel_str[1:]:
        if char.isupper():
            snake_str += '_' + char.lower()  
        else:
            snake_str += char
    return snake_str

# Test the function
camel_string = "convertThisCamelCaseStringToSnakeCase"
snake_string = camel_to_snake(camel_string)
print("Camel case:", camel_string)
print("Snake case:", snake_string)

"""
Camel case: convertThisCamelCaseStringToSnakeCase
Snake case: convert_this_camel_case_string_to_snake_case
"""