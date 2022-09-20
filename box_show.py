import os
import cv2
import re
import numpy as np
import random


# imread와 동일한 기능
def hangulFilePathImageRead ( filePath ) :
    """Output Image : RGB 3 Channel. (W, H, C)"""
    try :
        stream = open(filePath.encode("utf-8") , "rb") 
        bytes = bytearray(stream.read()) 
        numpyArray = np.asarray(bytes, dtype=np.uint8) 
        result = cv2.imdecode(numpyArray , cv2.IMREAD_UNCHANGED) # BGR
        if result.shape[-1] == 3 : result = cv2.cvtColor(result, cv2.COLOR_BGR2RGB)
        elif result.shape[-1] == 4 : result = cv2.cvtColor(result, cv2.COLOR_BGRA2RGB)
        return result
    except FileNotFoundError as e :
        utils_logger.exception(f"FileNotFoundError: [Errno 2] No such file or directory: {filePath}")
        sys.exit(0)


def box_show (root_dir, img, annot, classes_txt="classes.txt", show_num=None, shuffle=True) : 
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

    classes = []
    with open(f"{root_dir}/{classes_txt}", 'r') as f:
        for line in f.readlines() : 
            classes.append(line.replace('\n', ""))
    num_classes = len(classes)
    print("num_classes : ", num_classes)
            
    # show_num을 지정하지 않으면, 이미지 전체를 모두 본다. 
    if show_num is None : show_num = len(images) 
    else : pass
    color_list = []
    for _ in range(num_classes) :
        color_list.append(tuple(np.random.randint(50, 250, size=(3, ), dtype=int)))
        
    font = cv2.FONT_HERSHEY_DUPLEX
    # for i, l in zip(images, labels) : 
    for idx in range(show_num) :
        if shuffle : idx = random.randint(0, len(images)-1)
        else : pass
        
        # imread
        image = hangulFilePathImageRead(f"{root_dir}/{img}/{images[idx]}")
        image = cv2.resize(src=image, dsize=(800, int(800*image.shape[0]/image.shape[1]))) ##
        height = image.shape[0]
        width = image.shape[1]
        label = images[idx].replace(".jpg", ".txt")
        label = label.replace(".png", ".txt")
            
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
                    color = color_list[int(label)]
                    color = (int(color[0]),int(color[1]),int(color[2]))
                    
                    cv2.putText(img=image, text=classes[int(label)], org=(int(width*bbox[0])-8, y0-10), fontFace=font, fontScale=1, color=color, thickness=1)
                    cv2.rectangle(img = image, pt1 = (x0, y0), pt2=(x1, y1), color=color, thickness=3)
                    
            cv2.namedWindow('image', cv2.WINDOW_AUTOSIZE)
            cv2.imshow('image', image)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        pass # for 
    
    print("Complete!")
    pass # box_show
        
        
if __name__ == "__main__" :
    # box_show("image_label", "image", "label", shuffle=False)
    box_show("C:/project/롯데캐피탈/data/신분증학습자료/202007/aug", "aug_image", "aug_label", classes_txt="classes.txt", shuffle=True, show_num=15)
    

