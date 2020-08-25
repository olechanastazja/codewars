'''
    Implement a function that determines whether a string that contains only letters is an isogram. Ignore letter case.

    is_isogram("Dermatoglyphics" ) == true
    is_isogram("aba" ) == false
    is_isogram("moOse" ) == false # -- ignore letter case
'''


def is_isogram(string):
    return not any(string.lower().count(x) > 1 for x in string)
