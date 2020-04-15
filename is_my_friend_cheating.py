'''
    A friend of mine takes a sequence of numbers from 1 to n (where n > 0).
    Within that sequence, he chooses two numbers, a and b.
    He says that the product of a and b should be equal to the sum of all numbers in the sequence, excluding a and b.
    Given a number n, could you tell me the numbers he excluded from the sequence?
'''


import itertools


def removNb(n):
    res = []
    lst = list(range(1, n+1))
    sm = sum(lst) + 1
    divisors = []
    for i in range(1, n):
        if sm % i == 0:
            divisors.append(i)
    for values in itertools.permutations(divisors, 2):
        if values[0] * values[1] == sm:
            res.append((values[0]-1, values[1]-1))
    return res


print(removNb(26))
