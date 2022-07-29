import os
import re

def imgfname2label(imgdir, txtpath="./mylabel.txt", imgextension="png"):
    """
    이미지이름_레이블.png 형식의 이미지들이 있는 폴더를 입력받아
    이미지들의 텍스트 레이블 파일 생성 
    
    Args:
        imgdir (_type_): 이미지 파일이 들어있는 폴더 (이미지 이름 예시 : 이미지이름_레이블.png)
        txtpath (str, optional): 생성할 텍스트 레이블 파일 경로. Defaults to "./mylabel.txt".
        imgextension (str, optional): 이미지파일 확장자 지정. Defaults to "png".
    """
    filelist = [i for i in os.listdir(imgdir) if i.endswith(f".{imgextension}")] # 이미지파일 확장자 지정
    print("# image files : ", len(filelist)) # .png 이미지 파일만 모아서
    
    # mylabel.txt에 '<이미지파일이름>\t<레이블이름>' 쓰기
    with open (txtpath, 'w', encoding='utf8') as f: 
        for fname in filelist : 
            imgname_label = re.split("_", os.path.splitext(fname)[0])
            if len(imgname_label) == 2 :
                imgname = imgname_label[0]
                label = re.sub("\+", ":", imgname_label[1])
                f.write(f"{imgname}.{imgextension}\t{label}\n")