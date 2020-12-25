'''
    Given a hash of letters and the number of times they occur, recreate all of the possible anagram combinations that could be created using all of the letters, sorted alphabetically.

    The inputs will never include numbers, spaces or any special characters, only lowercase letters a-z.

    E.g. get_words({2=>["a"], 1=>["b", "c"]}) => ["aabc", "aacb", "abac", "abca", "acab", "acba", "baac", "baca", "bcaa", "caab", "caba", "cbaa"]

'''

from itertools import permutations


def get_words(hash_of_letters):
    letters_list = []
    for k, v in hash_of_letters.items():
        letters_list.extend(k*v)
    perm = permutations(letters_list)
    return sorted(["".join(i) for i in set(perm)])


print(get_words({2:["a"], 1:["b", "c"]}))
