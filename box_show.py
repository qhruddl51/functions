import os
import cv2
import re
import numpy as np

# imread와 동일한 기능
def hangulFilePathImageRead ( filePath ) : 
    stream = open( filePath.encode("utf-8") , "rb") 
    bytes = bytearray(stream.read()) 
    numpyArray = np.asarray(bytes, dtype=np.uint8) 
    return cv2.imdecode(numpyArray , cv2.IMREAD_UNCHANGED)



def box_show (root_dir, img, annot, show_num) : 
    """이미지에 box를 표시해주는 함수"""
    #    이미지 파일 이름과 box 좌표 파일 이름은 동일
    #    - root_dir : 이미지 폴더와 bbox 좌표 폴더가 있는 상위 디렉토리
    #    - img : 이미지가 있는 디렉토리
    #    - annot : bbox 좌표가 있는 디렉토리

    images = os.listdir(f"{root_dir}/{img}")
    labels = os.listdir(f"{root_dir}/{annot}")
    show = 0
    for i, l in zip(images, labels) : 
        show += 1
        # imread
        image = hangulFilePathImageRead(f"{root_dir}/{img}/{i}")
        height = image.shape[0]
        width = image.shape[1]
        
        with open(f"{root_dir}/{annot}/{l}", 'r') as f :
            for line in f.readlines() :
                line = line.splitlines()[0]
                label_bbox = re.split(" ", line)
                label = label_bbox[0]
                bbox = list(map(float, label_bbox[1:]))
                
                x0 = int(width*bbox[0]-width*bbox[2]/2)
                y0 = int(height*bbox[1]-height*bbox[3]/2)
                x1 = int(width*bbox[0]+width*bbox[2]/2)
                y1 = int(height*bbox[1]+height*bbox[3]/2)
                red = (0, 0, 255)
                cv2.rectangle(img = image, pt1 = (x0, y0), pt2=(x1, y1), color=red, thickness=3)

        cv2.imshow('image', image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        
        if show == show_num : break
        else : pass
        
        
if __name__ == "__main__" :
    box_show("C:/project/한국거래소/learning/train_data/augmented/positive", "img", "annot", show_num=50)

