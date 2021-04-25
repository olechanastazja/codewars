from hashlib import md5


def coder(left=0, right=99999):
    for n in range(left, right + 1):
        n = str(n).encode('utf-8')
        if len(n) < 5:
            n = n.zfill(5)
        yield n


def crack(hash):
    num_gen = coder()
    for guess in num_gen:
        if md5(guess).hexdigest() == hash:
            return guess.decode('utf-8')

