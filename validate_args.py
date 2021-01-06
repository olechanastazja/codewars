'''
    Implement the validate_args decorator, which raises an error (InvalidArgument) when the decorated function is called
    with arguments of the wrong type.
    Validate_args takes in a sequence of argument types as a variable number of arguments.

    Your decorator must be well-behaved, i.e. the returned function must have the same name and docstring as the original,
    and must be able to handle the same arguments.

    Example :

    @validate_args(str)
    def say_hello(name):
      return "Hello, " + name

    say_hello(1) # Raises InvalidArgument
    say_hello("Python") # Returns "Hello, Python"

    InvalidArgument is preloaded for you. You may use it as if you had defined it in your own code.
'''

import functools


def validate_args(*args):
    def decorator_validate(func):
        @functools.wraps(func)
        def wrapper_validate(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except TypeError:
                raise InvalidArgument()
        return wrapper_validate
    return decorator_validate
