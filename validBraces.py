class Stack:

    def __init__(self):
        self.stack = []

    def push(self, elem):
        self.stack.append(elem)

    def pop_last(self):
        return self.stack.pop()

    def reset(self):
        self.stack = []

    def is_empty(self):
        return not self.stack


class ValidBraces:
    lefts, rights = ('(', '{', '['), (')', '}', ']')

    def __init__(self, stack):
        self.stack = stack

    def __call__(self, string_input):
        self.string_input = string_input
        self.stack.reset()
        return self.is_valid()

    def is_valid(self):
        for elem in self.string_input:
            if elem in self.lefts:
                self.stack.push(elem)
            else:
                if self.stack.is_empty() or not self.rights.index(elem) == self.lefts.index(self.stack.pop_last()):
                    return False
        return self.stack.is_empty()


stack = Stack()
validBraces = ValidBraces(stack)
print(validBraces("{}()[]"), True)
