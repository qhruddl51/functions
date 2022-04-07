import os
import shutil

# 파일 이름 리스트를 받아서 복사 or 이동시키는 함수
def move_copy_file (move_OR_copy, target, to_dir, from_dir) : 
    if move_OR_copy == "copy" : 
        for f in target : 
            if os.path.isfile(f"{from_dir}/{f}") :
                shutil.copy2(f"{from_dir}/{f}", f"{to_dir}/{f}")
            else : print(f'{f} -> This file is not in {from_dir}')
    elif move_OR_copy == "move" : 
        for f in target : 
            f_path = f"{from_dir}/{f}"
            if os.path.isfile(f_path) :
                shutil.move(f_path, f"{to_dir}")
            else : print(f'{f} -> This file is not in {from_dir}')
    else : 
        print('If you want to copy files, move_OR_copy = "copy"\nIf you want to move files, move_OR_copy = "move"')


if __name__ == "__main__" :
    run_num = "6_2"
    filelist = os.listdir(f"C:/project/기업은행/AIDA/labeled/run{run_num}")
    move_copy_file(move_OR_copy="copy", target=filelist, to_dir=f"C:/project/.../labeled2/run{run_num}", from_dir=f"C:/project/.../labeled/run{run_num}")
    