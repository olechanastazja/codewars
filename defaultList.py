class DefaultList:

    def __init__(self, list_values, default_value):
        self.list_values = list_values
        self.default_value = default_value

    def __getitem__(self, key):
        try:
            self.list_values[key]
        except IndexError:
            return self.default_value

    def append(self, elem):
        self.list_values.append(elem)

    def extend(self, items):
        self.list_values.extend(items)

    def insert(self, pos, elem):
        self.list_values.insert(pos, elem)

    def remove(self, elem):
        self.list_values.remove(elem)

    def pop(self, pos):
        self.list_values.pop(pos)

