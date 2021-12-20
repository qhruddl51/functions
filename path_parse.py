import re
import os

def path_parse(folder:str) : 
    folder_m = re.finditer(r'[/\\]+', folder)

    for m in folder_m  :
        root_dir_idx = m.start()
    # print(root_dir_idx)
    root_dir = folder[:root_dir_idx]
    return root_dir