def snake_to_camel(snake_str):
    components = snake_str.split('_')
    camel_case = components[0] + ''.join(x.title() for x in components[1:])
    return camel_case

# Test the function
snake_string = "hello_world_this_is_snake_case"
camel_string = snake_to_camel(snake_string)
print("Snake case:", snake_string)
print("Camel case:", camel_string)

"""
Snake case: hello_world_this_is_snake_case
Camel case: helloWorldThisIsSnakeCase
"""
