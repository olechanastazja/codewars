'''
    Given an array, find the integer that appears an odd number of times.

    There will always be only one integer that appears an odd number of times.
'''


from collections import Counter


def find_it(seq):
    for k, v in Counter(seq).items():
        if v % 2 != 0:
            return k
