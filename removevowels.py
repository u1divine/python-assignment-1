def remove_vowels(word):
    vowels = "aeiouAEIOU"
    result = "".join(char for char in word if char not in vowels)
    return result
text = input("Enter a text: ")
print ("Text without vowels:", remove_vowels(text))