'''
    How many times we create a python class and in the init method we just write:

    self.name1 = name1
    self.name2 = name2
    .....

    for all arguments.....

    How boring!!!!

    Your task here is to implement a metaclass that let this instantiation be done automatically. But let's see an example:

    class Person(metaclass=LazyInit):
      def __init__(self, name, age): pass

    When we create a Person object like:

    a_person = Person('John', 25)

    The expected behavior will be:

    print(a_person.name) # this will print John
    print(a_person.age)  # this will print 25

    Obviously the number of arguments might be different from class to class.

    Don't worry about **kwargs you will never be given keyword arguments in this kata!!!

    A little hint: a decorator could help you out doing the job!!!
'''
from inspect import getargspec


class LazyInit(type):

    def __new__(meta, classname, supers, classdict):
        classdict['__init__'] = lazy_init_decorator(classdict['__init__'])
        return type.__new__(meta, classname, supers, classdict)


def lazy_init_decorator(init):
    def wrapper_function(*args):
        args = getargspec(init)[0]
        argsvalues = [x for x in args[1:]]
        objref = args[0]
        print(objref)
        for x in args[1:]:
            objref.__setattr__(x, argsvalues.pop(0))

    return wrapper_function


class SuperClass(metaclass=LazyInit):
    def __init__(self, name, age):
        pass


a_super_class = SuperClass('Test', 100)
print(a_super_class.__dict__)