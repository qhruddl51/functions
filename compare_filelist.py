# 하나의 폴더 안의 파일을 2개 카테고리로 분류할 때
# 중복 분류된 파일과 어느 카테고리에도 속하지 않는 파일 이름 뽑아내기 

# 파일 리스트를 가져오는 방식은 실제 파일들이 담겨있는 폴더에 접근하거나 
# .csv 파일의 특정 열을 읽는 방식 중 한 가지이다. 

# 중복 파일 또는 어느 카테고리에도 속하지 않는 파일을 다른 디렉토리로 이동 or 복사

import os
import random
import re
import shutil


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



# csv에서 특정 컬럼에 있는 파일이름들을 뽑아 리스트로 반환
def csv_col_extract(col:int, csvfile:str) : 
    with open(csvfile, "r") as f :
        lines = f.readlines()
        file_list = [re.split(",", line)[col-1] for line in lines]
    return file_list
    
    
# 파일 이름 리스트를 받아서 복사 or 이동시키는 함수
def move_copy_file (move_OR_copy, target, to_dir, from_dir) : 
    if move_OR_copy == "copy" : 
        for f in target : 
            shutil.copy2(f"{from_dir}/{f}", f"{to_dir}")
    elif move_OR_copy == "move" : 
        for f in target : 
            shutil.move(f"{from_dir}/{f}", f"{to_dir}")
    else : 
        print('If you want to copy files, move_OR_copy = "copy"\nIf you want to move files, move_OR_copy = "move"')


# 폴더를 생성하는 함수
# 폴더가 존재할 경우는 폴더가 비어있지 않으면, 해당 폴더를 삭제 후 다시 생성
def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
            print(f"make directory : {directory}")
        else : 
            if not os.listdir(directory) : 
                print(f'"{directory}" directory is empty') 
            else : 
                shutil.rmtree(directory)
                os.makedirs(directory)
                print(f'"{directory}" directory is not empty -> clear directory')
                
    except OSError:
        print ('Error: Creating directory. ' +  directory)



if __name__ == "__main__" :
    input_mode = "folder"
    root_dir = "C:/Users/qhrud/workspace/functions/temp"
    category_names = ["female_13", "male_13", "total_30"] # category1, category2, 분류전 total

    move_OR_copy = "copy" # "move", "copy", None
    move_copy_target = "category2_only" # "else", "intersection", "category1_only", "category2_only"
    from_dir = "male_13" # 복사하거나 이동할 파일이 있는 원폴더의 경로 (category_names의 요소 중 하나)
    to_dir = "C:/Users/qhrud/workspace/functions/temp/male_only" # 복사하거나 이동할 디렉토리 경로
    
    #==================================================#
    if input_mode == "csv" :
        filelist_1 = csv_col_extract(col=1, csvfile=f"{root_dir}/{category_names[0]}.csv")
        filelist_2 = csv_col_extract(col=1, csvfile=f"{root_dir}/{category_names[1]}.csv")
        total_filelist = csv_col_extract(col=1, csvfile=f"{root_dir}/{category_names[2]}.csv")
        
        print("category1 : ", f"{root_dir}/{category_names[0]}.csv :: {len(filelist_1)}")
        print("category2 : ", f"{root_dir}/{category_names[1]}.csv :: {len(filelist_2)}")
        print("total : ", f"{root_dir}/{category_names[2]}.csv :: {len(total_filelist)}")
        
    elif input_mode == "folder" :
        filelist_1 = os.listdir(f"{root_dir}/{category_names[0]}")
        filelist_2 = os.listdir(f"{root_dir}/{category_names[1]}")
        total_filelist = os.listdir(f"{root_dir}/{category_names[2]}")
        
        print("- category1 : ", f"{root_dir}/{category_names[0]} :: {len(filelist_1)}")
        print("- category2 : ", f"{root_dir}/{category_names[1]} :: {len(filelist_2)}")
        print("- total : ", f"{root_dir}/{category_names[2]} :: {len(total_filelist)}")
        
    else : print("input_mode should be 'csv' or 'folder'")
    print("="*50)
    
    
    #==================================================#
    intersection_category = list(set(filelist_1) & set(filelist_2))
    print("intersection_category : ", len(intersection_category))
    print(intersection_category)
    
    union_category = set(filelist_1) | set(filelist_2)
    no_category = list(set(total_filelist) - union_category)
    print("no_category : ", len(no_category))
    print(no_category)
    print("="*50)
    
    
    #==================================================#
    # 파일을 복사 or 이동
    if (not move_OR_copy) or (move_OR_copy not in ["move", "copy"]) : pass 
    else : 
        print(f'{move_OR_copy} start!')
        createFolder(to_dir)
        
        if move_copy_target == "else"  :
            move_copy_file(move_OR_copy=move_OR_copy, target=no_category, to_dir=to_dir, from_dir=f"{root_dir}/{from_dir}")
        elif move_copy_target == "intersection" :
            move_copy_file(move_OR_copy=move_OR_copy, target=intersection_category, to_dir=to_dir, from_dir=f"{root_dir}/{from_dir}")
        elif move_copy_target == "category1_only" :
            category1_only = list(set(filelist_1) - set(filelist_2))
            move_copy_file(move_OR_copy=move_OR_copy, target=category1_only, to_dir=to_dir, from_dir=f"{root_dir}/{from_dir}")
        elif move_copy_target == "category2_only" :
            category2_only = list(set(filelist_2) - set(filelist_1))
            move_copy_file(move_OR_copy=move_OR_copy, target=category2_only, to_dir=to_dir, from_dir=f"{root_dir}/{from_dir}")
    
        print(f'{move_OR_copy} complete!')