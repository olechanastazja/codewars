'''
    Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.
    Examples

    pig_it('Pig latin is cool') # igPay atinlay siay oolcay
    pig_it('Hello world !')     # elloHay orldway !
'''


def pig_it(text):
    return " ".join([e[1:] + e[0] + 'ay' if e.isalpha() else e for e in text.split()])


print(pig_it('Pig latin is a cool ?'))