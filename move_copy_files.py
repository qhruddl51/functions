import os
import shutil
import re

# 파일 이름 리스트를 받아서 복사 or 이동시키는 함수
def move_copy_file (move_OR_copy, target, to_dir, from_dir) : 
    if move_OR_copy == "copy" : 
        for f in target : 
            if os.path.isfile(f"{from_dir}/{f}") and f.endswith(".png") :
                new_f = re.split("_", os.path.splitext(f)[0])[0]+".png" ### 파일 저장 이름/형식 지정!
                shutil.copy2(f"{from_dir}/{f}", f"{to_dir}/{new_f}")
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
    # run_num = "6_2"
    # filelist = os.listdir(f"C:/project/신한카드/labeling/재학습데이터_김보경/1_tot")
    filelist = []
    with open("C:/project/신한카드/labeling/재학습_완료/2/mylabel2.txt", 'r', encoding='utf8') as f :
        linelist = f.readlines()
        for line in linelist :
            filelist.append(re.split('\t', line)[0])
    print(len(filelist))
    
    # move_copy_file(move_OR_copy="copy", target=filelist, to_dir=f"C:/project/신한카드/labeling/재학습_완료/2", from_dir=f"C:/project/신한카드/labeling/재학습데이터_김보경/2_tot_new")