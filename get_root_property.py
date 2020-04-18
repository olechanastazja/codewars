'''
    Given an object of likely nested objects, where the final element is an array containing positive integers, write a function that returns the name of the root property that a particular integer lives in.
    E.g

    Heres what the object looks like:

    object = {
        "one": {
            "nest1": {
                "val1": [9, 34, 92, 100]
             }
        },
        "2f7": {
            "n1": [10, 92, 53, 71],
            "n2": [82, 34, 6, 19]
        }
    }
    getRootProperty(object, 9); //=> "one"
'''


def get_root_property(dict_, value):
    for k, v in dict_.items():
        if isinstance(v, list):
            if value in v:
                return k
        elif get_root_property(v, value):
            return k


dictionary = {
    "one": {
        "nest1": {
            "val1": [9, 34, 92, 100]
        }
    },
    "2f7": {
        "n1": [10, 92, 53, 71],
        "n2": [82, 34, 6, 19]
    }
}

print(get_root_property(dictionary, 6))