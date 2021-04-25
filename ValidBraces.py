
class ValidBracesStack:
    OPENING = ['(', '{', '[']
    CLOSING = [')', '}', ']']

    def __init__(self, string):
        self.string = string
        self.stack = []

    def __call__(self, input_string):
        for i, elem in enumerate(input_string):
            if elem in self.OPENING:
                self.push(elem)
            else:
                if not self.stack or self.matches(elem, input_string[i-1]):
                    return False
                self.stack.pop()
        return not self.stack

    # check with is out of curiosity
    def matches(self, elem, previous):
        return self.CLOSING.index(elem) == self.CLOSING.index(previous)

    def pop(self):
        return self.stack.pop()

    def push(self, elem):
        return self.stack.append(elem)

    def is_valid(self):
        return len(self.stack) == 0

x = ValidBracesStack("{(})")
x("{(})")
print(ValidBracesStack("{(})"))

