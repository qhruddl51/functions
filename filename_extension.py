import re
import os

# in_folder의 파일이름의 확장자만 ch_extension로 바꿔서 리스트로 반환
def ch_extension (in_folder, ch_extension="txt"): 
    filelist = os.listdir(in_folder)
    print("Number of files in in_folder : ", len(filelist))
    new_ext_filelist = []
    for filename in filelist : 
        filename_n = os.path.splitext(filename)[0] + f".{ch_extension}"
        new_ext_filelist.append(filename_n)
    return new_ext_filelist  # path2filename
        
        
