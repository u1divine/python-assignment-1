# In camel case, the first letter of the first word is lowercase but the first letter of each subsequent word is uppercase
# In snake case, words are separated by underscores with all letters in lowercase
def camel_to_snake(camel_case):
    snake = ""
    for char in camel_case:
        if char.isupper():
            snake += "_" + char.lower()
        else:
            snake += char
    if snake [0] == "_":
        snake = snake[1:]
    return snake
camel = input("Enter a variable name in camel case: ")
print("Snake case:", camel_to_snake(camel))