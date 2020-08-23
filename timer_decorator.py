"""
Write a timer() decorator that validates if a function it decorates is executed
within (less than) a given seconds interval and returns a boolean True or False accordingly.

Example:

from time import sleep

@timer(1)
def foo():
    sleep(0.1)

foo()
True

"""

from time import sleep
import time


def timer(argument):
    def decorator(func):
        def wrapper(*args, **kwargs):
            start_time = time.perf_counter()
            func(*args, **kwargs)
            stop = time.perf_counter()
            diff = stop - start_time
            if diff > argument:
                return False
            return True
        return wrapper
    return decorator


@timer(0.5)
def foo():
    sleep(2)


print(foo())
