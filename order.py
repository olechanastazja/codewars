'''
    "is2 Thi1s T4est 3a"  -->  "Thi1s is2 3a T4est"
    "4of Fo1r pe6ople g3ood th5e the2"  -->  "Fo1r the2 g3ood 4of th5e pe6ople"
    ""  -->  ""
'''

def order(sentence):
    words_dict = {}
    for word in sentence.split():
        for l in word:
            try:
                words_dict[int(l)] = word
            except ValueError:
                pass
    return " ".join([v for k, v in sorted(words_dict.items(), key=lambda item: item[0])])

print(order("is2 Thi1s T4est 3a"))