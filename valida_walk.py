def is_valid_walk(walk):
    return len(walk) == 10 and walk.count("s") == walk.count("n") and \
           walk.count("w") == walk.count("e")