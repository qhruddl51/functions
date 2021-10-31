import re

# 정규표현식을 이용해서 file path에서 파일 이름만 뽑아내고
# rm_extension에 파일 확장자를 지정해 확장자도 제거할 수 있다. 
def path2filename (path_list, rm_extension="jpg"): 
    for idx, path in enumerate(path_list) : 
        path = re.split("/", path)[-1]
        
        if rm_extension : 
            path = re.sub(pattern=f"[.]{rm_extension}", repl='', string=path)
        else : pass
        
        path_list[idx] = path
    
    return path_list  # path2filename
        
        
        
if __name__ == "__main__" :
    path_list = ['C:/Users/qhrud/data/obj_gun/labels/armas (1)_jpg.rf.c4150f819f9dc2a32.jpg', 'C:/Users/qhrud/data/obj_gun/images/armas (3)_jpg.rf.503b3196eb0954cd5e459e5bca4d139b.jpg']
    print(path2filename(path_list))