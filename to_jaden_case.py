'''
    Example:

    Not Jaden-Cased: "How can mirrors be real if our eyes aren't real"
    Jaden-Cased:     "How Can Mirrors Be Real If Our Eyes Aren't Real"
'''


def to_jaden_case(string):
   return " ".join([x.capitalize() for x in string.split()])

