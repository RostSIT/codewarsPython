def spin_words(sentence):
    new_sentence = ""
    for i in sentence.split(" "):
        if len(i) >= 5:
            new_sentence += (i[::-1]) + ' '
        else:
            new_sentence += i + ' '
    return new_sentence[:-1]


def spin_words1(sentence):
    # Your code goes here
    return " ".join([x[::-1] if len(x) >= 5 else x for x in sentence.split(" ")])


x = spin_words("Hey fellow warriors")
j = spin_words("This is a test")
print(x, j)
"""Write a function that takes in a string of one or more words, and returns the same string, but with all five or
more letter words reversed (Just like the name of this Kata). Strings passed in will consist of only letters and
spaces. Spaces will be included only when more than one word is present.

Examples: spinWords( "Hey fellow warriors" ) => returns "Hey wollef sroirraw" spinWords( "This is a test") => returns
"This is a test" spinWords( "This is another test" )=> returns "This is rehtona test" """

# def sprin_w(sentence):
#     new_s = ""
#     return [len(i) >= 5 if ]
