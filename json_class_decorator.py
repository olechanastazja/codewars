'''
    Your task is to write a decorator that loads a given JSON file object and makes each key-value pair an attribute of the given class.

    Given the following data is written in the /tmp/myClass.json file:

    {
      "foo": "bar",
      "an_int": 5,
      "this_kata_is_awesome": true
    }

    Here's how you would use the decorator:

    @jsonattr("/tmp/myClass.json")
    class MyClass:
        pass


    MyClass.foo == "bar"
    MyClass.an_int == 5
    MyClass.this_kata_is_awesome == True
'''
import json


def jsonattr(filepath):
    with open(filepath) as f:
        data = json.load(f)

    def wrapper_func(cls):
        for k, v in data.items():
            setattr(cls, k, v)
        return cls
    return wrapper_func


@jsonattr("myClass.json")
class MyClass:
    def __init__(self, foo, an_int, this_kata_is_awesome):
        self.foo = foo
        self.an_int = an_int
        self.this_kata_is_awesome = this_kata_is_awesome


print(MyClass.foo)
