import os
import cv2
import re
import numpy as np
import random

# imread와 동일한 기능
def hangulFilePathImageRead ( filePath ) : 
    stream = open( filePath.encode("utf-8") , "rb") 
    bytes = bytearray(stream.read()) 
    numpyArray = np.asarray(bytes, dtype=np.uint8) 
    return cv2.imdecode(numpyArray , cv2.IMREAD_UNCHANGED)



def box_show (root_dir, img, annot, show_num=None, shuffle=True) : 
    """이미지에 box를 표시해주는 함수"""
    #    이미지 파일 이름과 box 좌표 파일 이름은 동일
    #    - root_dir : 이미지 폴더와 bbox 좌표 폴더가 있는 상위 디렉토리
    #    - img : 이미지가 있는 디렉토리
    #    - annot : bbox 좌표가 있는 디렉토리
    #    - show_num : 몇 개 이미지를 볼 것인지 지정
    
    images = os.listdir(f"{root_dir}/{img}")
    images.sort()
    labels = os.listdir(f"{root_dir}/{annot}")
    labels.sort()
    
    # show_num을 지정하지 않으면, 이미지 전체를 모두 본다. 
    if show_num is None : show_num = len(images) 
    else : pass
    
    font = cv2.FONT_HERSHEY_DUPLEX
    # for i, l in zip(images, labels) : 
    for idx in range(show_num) :
        if shuffle : idx = random.randint(0, len(images))
        else : pass
        print(idx)
        
        # imread
        image = hangulFilePathImageRead(f"{root_dir}/{img}/{images[idx]}")
        height = image.shape[0]
        width = image.shape[1]
        label = images[idx].replace(".jpg", ".txt")
        if os.path.isfile(f"{root_dir}/{annot}/{label}") :
            with open(f"{root_dir}/{annot}/{label}", 'r') as f :
                for line in f.readlines() :
                    line = line.splitlines()[0]
                    label_bbox = re.split(" ", line)
                    label = label_bbox[0]
                    bbox = list(map(float, label_bbox[1:]))
                    x0 = int(width*bbox[0]-width*bbox[2]/2)
                    y0 = int(height*bbox[1]-height*bbox[3]/2)
                    x1 = int(width*bbox[0]+width*bbox[2]/2)
                    y1 = int(height*bbox[1]+height*bbox[3]/2)
                    green = (0, 255, 0)
                    red = (0, 0, 255)
                    if label == "0" :
                        cv2.putText(img=image, text=label, org=(int(width*bbox[0])-8, y0-10), fontFace=font, fontScale=1, color=green, thickness=2)
                        cv2.rectangle(img = image, pt1 = (x0, y0), pt2=(x1, y1), color=green, thickness=3)
                    if label == "1" : 
                        cv2.putText(img=image, text=label, org=(int(width*bbox[0])-8, y0-10), fontFace=font, fontScale=1, color=red, thickness=2)
                        cv2.rectangle(img = image, pt1 = (x0, y0), pt2=(x1, y1), color=red, thickness=3)

            cv2.imshow('image', image)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        else : pass
    
        
        
if __name__ == "__main__" :
    # box_show("image_label", "image", "label", shuffle=False)
    box_show("C:/project/dgb/obj_detector/data/augmented", "images", "labels", show_num=50, shuffle=True)
    print("Complete!")

