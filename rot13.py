'''
    How can you tell an extrovert from an introvert at NSA? Va gur ryringbef, gur rkgebireg ybbxf ng gur BGURE thl'f fubrf.

    I found this joke on USENET, but the punchline is scrambled. Maybe you can decipher it? According to Wikipedia, ROT13 (http://en.wikipedia.org/wiki/ROT13) is frequently used to obfuscate jokes on USENET.

    Hint: For this task you're only supposed to substitue characters. Not spaces, punctuation, numbers etc. Test examples:

    rot13("EBG13 rknzcyr.") == "ROT13 example.";
    rot13("This is my first ROT13 excercise!" == "Guvf vf zl svefg EBG13 rkprepvfr!"
'''


import string

ALP_L = list(string.ascii_lowercase)
ALP_U = list(string.ascii_uppercase)


def rot13(txt):
    result = ""
    for l in txt:
        if not l.isalpha():
            result += l
        else:
            alp_lst = ALP_L if l.islower() else ALP_U
            index = alp_lst.index(l)
            result += alp_lst[index + 13] if index < 13 else alp_lst[(13 + index) - 26]
    return result


print(rot13('Aga naanan skdjf'))
