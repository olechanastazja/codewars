"""
Write a function that takes in a string of one or more words, and returns the same string,
 but with all five or more letter words reversed.

spinWords( "This is another test" )=> returns "This is rehtona test"
"""


def spin_words(sentence):
    return " ".join([v[::-1] if len(v) >= 5 else v for i, v in enumerate(sentence.split())])


print(spin_words("hey kapitanie co słychać"))