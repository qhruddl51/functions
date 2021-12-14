import os
import shutil

# 파일 이름 리스트를 받아서 복사 or 이동시키는 함수
def move_copy_file (move_OR_copy, target, to_dir, from_dir) : 
    if move_OR_copy == "copy" : 
        for f in target : 
            f_path = f"{from_dir}/{f}"
            if os.path.isfile(f_path) :
                shutil.copy2(f_path, f"{to_dir}")
            else : print(f'{f} -> This file is not in {from_dir}')
    elif move_OR_copy == "move" : 
        for f in target : 
            f_path = f"{from_dir}/{f}"
            if os.path.isfile(f_path) :
                shutil.move(f_path, f"{to_dir}")
            else : print(f'{f} -> This file is not in {from_dir}')
    else : 
        print('If you want to copy files, move_OR_copy = "copy"\nIf you want to move files, move_OR_copy = "move"')
