import jellyfish

def decompose(s):
    # print(s)
    MMASK = 28 
    FMASK = 21 * MMASK # 588
    FOFF = 0xe000 # 0xe000 = 57344
    MOFF = FOFF + 32 # 57376
    LOFF = MOFF + 32 # 57408
    r = []
    for c in s: # 단어 s에서 한개 글자씩 뽑아서 
        c_ = ord(c) # 문자의 유니코드로 바꾼다.
        if 0xac00 <= c_ <= 0xd7a3: # 한글 글자만 뽑아서 (가-힣)
            # print(f"{chr(0xac00)} : ",0xac00)
            # print(f"{chr(0xd7a3)} : ",0xd7a3)
            # print(f"{chr(c_ )} : ",c_ )
            t = c_ - 0xac00
            f = t // FMASK # 초성 인덱스
            u = t % FMASK
            m = u // MMASK  # 중성 인덱스
            l = u % MMASK # 종성 인덱스
            r.append(chr(f + FOFF)) # 초성 append
            r.append(chr(m + MOFF)) # 중성 append
            r.append(chr(l + LOFF)) # 종성 append
        else:
            r.append(c) # 한글이 아니면 글자그대로 append
        # print(r) # ['\ue000', '\ue021', '\ue040']
    return "".join(r) # 리스트안의 요소를 쭉 이어붙여 하나의 문자열로 만듦


def hangul_decompose(s:str): # -> return : list
    r = []
    for c in s : 
        r.append(c)
        unic = ord(c)
        # 0x1100 : 4352
        if 0xac00 <= unic <= 0xd7a3 :
            first = int((unic - 0xac00 ) /21/28) # 초성인덱스
            middle = int((unic - 0xac00 - first*588)/28) # 중성인덱스
            last = int((unic - 0xac00 - first*588-middle*28)) # 종성인덱스
            # print(f"초성: {chr(0x1100+first)}   {0x1100+first} {first}")
            # print(f"중성: {chr(0x1161+middle)}  {0x1161+middle}    {middle}")
            # print(f"종성: {chr(0x11A7+last)}    {0x11A7+last}   {last}")
            first_c = chr(0x1100+first)
            middle_c = chr(0x1161+middle)
            last_c = chr(0x11A7+last)
            r += [first_c, middle_c, last_c]
        print(r) # ['ᄒ', 'ᅵ', 'ᇂ']
    return "".join(r) # 힣
    return r # hangul_decompose_fml


def jaccard_similarity(list1, list2): 
    diff_num = 0
    for a, b in zip(list1, list2):
        if a == b : pass
        else : diff_num += 1
    
    return diff_num # 다른 글자 수 평균
    # return float(len(s1.intersection(s2)) / len(s1.union(s2)))


def match(a, b):
    d = jellyfish.levenshtein_distance(a, b)
    f = 1 - d / len(a) 
    print("levenshtein : ", f)
    return f

if __name__ == "__main__" :
    a = hangul_decompose("자산총계")
    b = hangul_decompose("자산용계")
    wrong_str_num1 = jaccard_similarity(a, b)
    print(wrong_str_num1)
    
    a = hangul_decompose("개나리노란꽃그늘")
    b = hangul_decompose("개나리노란상상상")
    wrong_str_num2 = jaccard_similarity(a, b)

    print(wrong_str_num2)
    a = decompose("영업외익")
    b = decompose("영업외이익")
    print("my : ",match(a, b))
    # print("my : ",match(a, b)/(wrong_str_num1**0.01+1))
    