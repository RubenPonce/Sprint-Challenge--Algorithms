'''
Your function should take in a signle parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
"""
takes in a word
counts the number of times that 'th' is in the word only lowercase
uses recursion

initialize counter at 0
split the string into an array
iterate over the array
    check for a "t"
    if there is a "t"
        check if the next elemen t is "h"
        then increment the counter by one
        return the counter

    return counter
"""
def count_th(word):
    counter = 0
    word_characters = list(word)
    print(word_characters)
    for i in range(len(word_characters) - 1):
        if word_characters[i] == "t" and i is not len(word_characters) - 1:
            if word_characters[i+1] == "h":
                counter +=1
    return counter


    # TBC
    
    pass

print(count_th("ththththththththth"))
print(count_th("ththththththththth"))