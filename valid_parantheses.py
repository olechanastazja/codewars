'''
    Write a function called that takes a string of parentheses, and determines if the order of the parentheses is valid. The function should return true if the string is valid, and false if it's invalid.
    Examples:
        "()"              =>  true
        ")(()))"          =>  false
        "("               =>  false
        "(())((()())())"  =>  true
'''


def valid_parentheses(string):
    stack = []
    for i in list(string):
        if i == ')' and not stack:
            return False
        if i == '(':
            stack.append(i)
        elif i == ')':
            stack.pop()

    return len(stack) == 0


print(valid_parentheses("((()))"))
