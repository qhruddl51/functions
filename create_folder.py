import re
import shutil

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