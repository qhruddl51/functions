'''
Usage: emptylabel.py <path>


Options:
    <path>              input image dir  [ex : "C:/workspace/images"] 

'''

import os
import shutil
from docopt import docopt

# negative 이미지 샘플에 대해 빈 레이블 텍스트 파일을 생성해줌
def make_emptylabel (img_dir) : 
    """object가 없는 negative 이미지 샘플에 대해 빈 레이블 텍스트 파일을 생성해줌

    Args:
        img_dir (str): negative 이미지 샘플만 들어 있는 폴더의 경로
    """
    # 이미지 파일만 이름 저장
    target = [i for i in os.listdir(img_dir) if (i.endswith(".jpg") or i.endswith(".JPG") or i.endswith(".png") or i.endswith(".PNG"))]
    
    # img_dir에 이미지가 아닌 파일이 있는지 알려준다.
    if len(os.listdir(img_dir))-len(target) != 0 :
        print("!! Warning : Non image file in image directory.")
    
    # img_dir안에 labels 디렉토리 만들기
    save_label_dir = f"{img_dir}/labels"
    createFolder(save_label_dir)
    
    for f in target : 
        new_f = f"{os.path.splitext(f)[0]}.txt" # 생성할 빈 레이블 텍스트 파일의 이름
        shutil.copy2(f"{img_dir}/{f}", f"{save_label_dir}/{new_f}")
    print()
    print(f"{len(target)} label files are generated! ")
    

# 폴더를 생성하는 함수
# 폴더가 존재할 경우는 폴더가 비어있지 않으면, 해당 폴더를 삭제 후 다시 생성
def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
            print(f"make directory : {directory}")
        else : 
            if not os.listdir(directory) : 
                print(f'"{directory}" directory already exists and is empty.') 
            else : 
                shutil.rmtree(directory)
                os.makedirs(directory)
                print(f'"{directory}" directory is not empty -> Clear directory!')
                
    except Exception: # OSError
        raise Exception(f"Error: Creating directory. {directory}")


    
if __name__ == "__main__" :
    path = os.path.join(os.path.dirname(__file__), './icon.ico')
    print(path)
    if os.path.isfile(path):
        self.root.iconbitmap(path)
        
    args = docopt(__doc__, version='DEMO 1.0')
    img_dir = args['<path>']
    make_emptylabel(img_dir)
    # make_emptylabel("images")