'''
    An anagram is a word, a phrase, or a sentence formed from another by rearranging its letters. An example of this is
    "angel", which is an anagram of "glean".

    Write a function that receives an array of words, and returns the total number of distinct pairs of anagramic words
    inside it.

    Some examples:
        There are 2 anagrams in the array ["dell", "ledl", "abc", "cba"]
        There are 7 anagrams in the array ["dell", "ledl", "abc", "cba", "bca", "bac"]
'''
import itertools


def anagram_counter(words):
    anagram_dict = {}
    count = 0
    for word in words:
        key = tuple(sorted(list(word)))
        if key in anagram_dict:
            anagram_dict[key].append(word)
        else:
            anagram_dict[key] = [word]
    for el in anagram_dict.values():
        count += len([comb for comb in itertools.combinations(list(el), 2)])
    return count


print(anagram_counter(['dell', 'ledl', 'abc', 'cba', 'bca', 'bac', 'cab']))