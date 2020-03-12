'''
    Assume "#" is like a backspace in string. This means that string "a#bc#d" actually is "bd"

    Your task is to process a string with "#" symbols.
    Examples

    "abc#d##c"      ==>  "ac"
    "abc##d######"  ==>  ""
    "#######"       ==>  ""
    ""              ==>  ""
'''


def clean_string(s):
    stack = []

    for c in s:
        if c == '#' and len(stack) > 0:
            stack.pop()
        elif c != '#':
            stack.append(c)

    return "".join(stack)

