import os
import re

# root_dir : 이미지와 레이블 디렉토리가 있는 루트 디렉토리
# 이미지 디렉토리 이름
# 레이블 디렉토리 이름
# 루트 디렉토리에 labels.csv 파일을 생성해준다. 
def prepare_datalist (root_dir:str , images_dir:str, labels_dir:str) : 
    images = os.listdir(f"{root_dir}/{images_dir}")
    labels = os.listdir(f"{root_dir}/{labels_dir}")
    
    with open(f"{root_dir}/labels.csv", "w", encoding='utf8') as f : 
        for i, l in zip(images, labels) :
            f.write(f"{root_dir}/{images_dir}/{i}\t{root_dir}/{labels_dir}/{l}\n")
    pass # prepare_datalist


if __name__ == "__main__" :
    prepare_datalist("C:/source/my_workspace/my_data/obj", "images", "labels")
