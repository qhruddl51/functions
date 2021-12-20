import os
import re
import shutil
import numpy as np
import random


# origin_folder_path 폴더에서 이미지 파일을 랜덤하게 percent만큼 뽑아서 
# new_folder_path 폴더로 복사하는 함수 
# 복사한 파일의 인덱스들을 반환
def sampling_in_folder(percent, origin_folder_path, new_folder_path, idxs=None) :
    filenames = os.listdir(f"{origin_folder_path}")
    filenames.sort()
    
    if idxs : # 인덱스 리스트를 주면,
        pass
    else : # 인덱스 리스트를 안주면, 인덱스 리스트를 새로 만든다. 
        n = int(len(filenames) * percent / 100)
        # random.sample() : 리스트에서 여러 가지를 랜덤으로 추출하기(중복 허용 X)
        idxs = random.sample(population=range(0, len(filenames)), k=n)
    
    for idx in idxs :
        shutil.copy2(f"{origin_folder_path}/{filenames[idx]}", f"{new_folder_path}/{filenames[idx]}")
        # shutil.move(f"{origin_folder_path}/{filename}", f"{new_folder_path}/{filename}")
    
    return idxs # img_copy_percent

