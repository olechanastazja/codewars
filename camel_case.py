'''
    Examples

    to_camel_case("the-stealth-warrior") # returns "theStealthWarrior"

    to_camel_case("The_Stealth_Warrior") # returns "TheStealthWarrior"
'''


import re


def to_camel_case(text):
    return "".join([x.capitalize() if i > 0 else x for i, x in enumerate(re.split('_|-',text))])