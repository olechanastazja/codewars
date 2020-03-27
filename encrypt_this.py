'''
    You want to create secret messages which can be deciphered by the Decipher this! kata. Here are the conditions:

        Your message is a string containing space separated words.
        You need to encrypt each word in the message using the following rules:
            The first letter needs to be converted to its ASCII code.
            The second letter needs to be switched with the last letter
        Keepin' it simple: There are no special characters in input.

    Examples:

    encrypt_this("Hello") == "72olle"
    encrypt_this("good") == "103doo"
    encrypt_this("hello world") == "104olle 119drlo"
'''


def encrypt_this(text):
    result = []
    for word in text.split():
        # strings are immutable
        word = list(word)
        word[0] = str(ord(word[0]))
        if len(word) > 2:
            word[1], word[-1] = word[-1], word[1]
        result.append(''.join(word))
    return ' '.join(result)


print(encrypt_this('A wise old owl lived in an oak'))