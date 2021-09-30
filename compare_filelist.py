#  하나의 폴더 안의 파일을 2-3개 카테고리로 분류할 때
# 중복 분류된 파일과 어느 카테고리에도 속하지 않는 파일 이름 뽑아내기 
# 파일 리스트를 가져오는 방식은 실제 파일들이 담겨있는 폴더에 접근하거나 
# .csv 파일의 특정 열을 읽는 방식 중 한 가지이다. 

import os
import random
import re

root_dir = "C:/Users/qhrud/workspace/functions/temp"

# 폴더 안의 파일들의 이름이 쓰인 csv 파일 만들기 
def filenames_csv (root_dir, folder) : 
    """폴더이름.csv 파일이 생성됨"""
    
    lines = os.listdir(f"{root_dir}/{folder}")
    csv_file_path = f"{root_dir}/{folder}.csv"
    
    with open(csv_file_path, 'w') as f :
        # lines = ["name,age", "John,28", "love,31"]
        for line in lines[:-1] : 
            f.write(line)
            # f.write(f",{random.randint(1,10)}")
            f.write("\n")
            pass # for
        f.write(lines[-1])
        # f.write(f",{random.randint(1,10)}")
        
    pass # filenames_csv



# 두 폴더에 중복 분류된 파일 이름 찾기 -> 목록을 리스트로 반환
def csv_col_extract(col:int, csvfile:str) : 
    with open(csvfile, "r") as f :
        lines = f.readlines()
        file_list = [re.split(",", line)[col-1] for line in lines]
    return file_list
    
    

    
if __name__ == "__main__" :
    root_dir = "C:/Users/qhrud/workspace/functions/temp"
    input_mode = "csv"
    category_names = ["female", "male", "total"]
    
    if input_mode == "csv" :
        filelist_1 = csv_col_extract(col=1, csvfile=f"{root_dir}/{category_names[0]}.csv")
        filelist_2 = csv_col_extract(col=1, csvfile=f"{root_dir}/{category_names[1]}.csv")
        total_filelist = csv_col_extract(col=1, csvfile=f"{root_dir}/{category_names[2]}.csv")
    elif input_mode == "folder" :
        female_filelist = os.listdir(f"{root_dir}/{category_names[0]}")
        male_filelist = os.listdir(f"{root_dir}/{category_names[1]}")
        total_filelist = os.listdir(f"{root_dir}/{category_names[2]}")
    else : print("input_mode should be 'csv' or 'folder'")
    
    
    intersaction_category = list(set(filelist_1) & set(filelist_2))
    print("intersaction_category : ", intersaction_category)
    
    union_category = set(filelist_1) | set(filelist_2)
    print("no_category : ", list(set(total_filelist) - union_category))
    
    