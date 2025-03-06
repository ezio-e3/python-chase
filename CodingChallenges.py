# reversed strings
# complete the solution so it reverses the string passed into it
# 'world' => 'dlrow'

def reverse_string(str):
    word = list(str)
    word.reverse()
    empty_string = ''
    for i in word:
        empty_string += i
    return empty_string

print(reverse_string('Joe'))

# Complete the method that takes a boolean value and return a "Yes" string for true, or a "No" string for false.

def bool_to_word(value: bool):
    if value == True:
        return 'Yes'
    else:
        return 'No'

def bool_to_word_variartion(value: bool):
    return 'Yes' if value else 'No'

print(bool_to_word_variartion(False))