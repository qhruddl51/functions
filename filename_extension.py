import re

# 정규표현식을 이용해서 file path에서 파일 이름만 뽑아내 list로 반환
# ch_extension에 파일 확장자를 지정해 확장자를 삭제 또는 변환할 수 있다. 
def path2filename (path_list, ch_extension="txt"): 
    for idx, path in enumerate(path_list) : 
        if ch_extension : # 확장자 바꾸기
            # path = re.sub(pattern=f"[.]{rm_extension}", repl='', string=path)
            path = os.path.splitext(fileaname)[0] + ch_extension
            
        else : # 확장자 유지
            path = re.split("/", path)[-1]
        
        path_list[idx] = path
    
    return path_list  # path2filename
        
        
        
if __name__ == "__main__" :
    path_list = ['C:/Users/qhrud/data/obj_gun/labels/armas (1)_jpg.rf.c4150f819f9dc2a32.jpg', 'C:/Users/qhrud/data/obj_gun/images/armas (3)_jpg.rf.503b3196eb0954cd5e459e5bca4d139b.jpg']
    print(path2filename(path_list))