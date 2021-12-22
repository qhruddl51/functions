import jellyfish

# 문자열간 유사도 계산
def match(a, b):
    d = jellyfish.levenshtein_distance(a, b)
    f = 1 - d / len(a)
    return f