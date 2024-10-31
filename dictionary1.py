def strings(word):
    return {string: len(string)for string in word}
strings_list = ["book", "pen", "pencil"]
print (strings(strings_list))