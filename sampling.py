import os
import re
import shutil
import numpy as np

# 폴더에 있는 파일 중 일부분을 무작위로 뽑아 원하는 폴더에 복사하거나 옮긺


# origin_folder_path 폴더에서 이미지 파일을 랜덤하게 percent만큼 뽑아서 new_folder_path 폴더로 복사하는 함수 
def img_move_n (percent, origin_folder_path, new_folder_path) :
    filenames = np.array(os.listdir(f"{origin_folder_path}"))
    filenames = np.random.permutation(filenames)
    n = int(len(filenames) * percent / 100)

    for filename in filenames[:n] :
        shutil.copy2(f"{origin_folder_path}/{filename}", f"{new_folder_path}/{filename}")
        # shutil.move(f"{origin_folder_path}/{filename}", f"{new_folder_path}/{filename}")
    pass # img_move_n



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



# origin_root_path : 상위 폴더의 경로(해당 폴더에 옮길 파일들을 담고 있는 여러 하위 폴더가 있다.)
# new_root_path : 새로운 상위 폴더의 경로
if __name__ == "__main__" :
    origin_root_path = "D:/test" ########################## 지정!
    origin_folder_names = os.listdir(origin_root_path)
    new_root_path = "D:/test_out" ######################### 지정!
    extract_percent = 10 ####################### 지정!

    createFolder(new_root_path)

    for o in origin_folder_names :
        origin_folder_path = os.path.join(origin_root_path, o)
        new_folder_path = os.path.join(new_root_path, o)
        createFolder(new_folder_path)
        img_move_n(percent=extract_percent, origin_folder_path=origin_folder_path, new_folder_path=new_folder_path)

