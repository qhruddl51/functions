import jellyfish


def match(a, b):
    d = jellyfish.levenshtein_distance(a, b)
    f = 1 - d / len(a)
    return f