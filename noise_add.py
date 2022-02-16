import cv2
import numpy as np
import random

def noise_add (image, noise_num, noise_file) : 
    """ 노이즈이미지를 뿌리는 함수
    Input/Output Image : numpy array, RGB 3 Channel. (H, W, C)
    noise_num : 한 이미지에 최대로 뿌릴 노이즈 개수
    noise_file : 노이즈 이미지 파일(3 Channel)의 경로 
    """
    img_bg = cv2.cvtColor(image , cv2.COLOR_RGB2BGR) # 노이즈를 뿌릴 대상 이미지
    img_fg = cv2.imread(filename=noise_file) # 노이즈
    h_bg, w_bg = img_bg.shape[0:2]

    h_bg_list = random.sample(range(0, h_bg-img_fg.shape[0]), noise_num)
    w_bg_list = random.sample(range(0, w_bg-img_fg.shape[1]), noise_num)
    
    for i in range(noise_num) :
        img_fg = cv2.imread(filename=noise_file) # 위에 입힐 이미지
        gray = cv2.cvtColor(img_fg, cv2.COLOR_BGR2GRAY) # (34, 36)
        mask = np.zeros_like(gray)
        mask[gray < 250] = 255
        mask_inv = cv2.bitwise_not(mask)
        
        h = h_bg_list[i]
        w = w_bg_list[i] 
        h_fg, w_fg = img_fg.shape[:2] # 로고 이미지의 높이와 너비를 저장
        roi = img_bg[h:h+h_fg, w:w+w_fg]

        masked_fg = cv2.bitwise_and(img_fg, img_fg, mask = mask)  # 둘이 같은 값일 때는 그 같은 값이 된다. 
        masked_bg = cv2.bitwise_and(roi, roi, mask = mask_inv) 

        added = masked_fg + masked_bg
        img_bg[h:h+h_fg, w:w+w_fg] = added
    
    result = cv2.cvtColor(img_bg , cv2.COLOR_BGR2RGB)
    return result