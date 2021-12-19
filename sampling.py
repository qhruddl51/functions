import os
import re
import shutil
import numpy as np
import random


# origin_folder_path 폴더에서 이미지 파일을 랜덤하게 percent만큼 뽑아서 
# new_folder_path 폴더로 복사하는 함수 
def file_copy_move(percent, origin_folder_path, new_folder_path) :
    filenames = os.listdir(f"{origin_folder_path}")
    
    n = int(len(filenames) * percent / 100)
    idxs = random.sample(population=range(0, len(filenames)), k=n)
    
    for idx in idxs :
        shutil.copy2(f"{origin_folder_path}/{filenames[idx]}", f"{new_folder_path}/{filenames[idx]}")
        # shutil.move(f"{origin_folder_path}/{filename}", f"{new_folder_path}/{filename}")
    
    return idxs # img_copy_percent

