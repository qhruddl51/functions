import os
import re
import shutil



# root_dir/folder의 모든 파일들의 이름을 리스트로 반환
def filenames_list (root_dir, folder) : 
    filenames = os.listdir(f'{root_dir}/{folder}')
    print(f'Number of images (f"{root_dir}/{folder}") :: ', len(filenames))
    return filenames



# 클래스 별로 다른 폴더에 데이터(파일)가 분류되어 있을 때, 
# "파일의 경로 레이블" 의 형식으로 어노테이션 파일을 만들어준다. 
# 단, category_list의 클래스 이름과 폴더 이름은 동일해야 한다. 
def imgPath_class (root_dir, out_csv_path, category_list=None) :
    if category_list : pass
    else : 
        category_list = []
        for n in os.listdir(root_dir) : 
            if os.path.isdir(f"{root_dir}/{n}") :
                category_list.append(n)
        print("category list : ", category_list)
        
    total_data_size = 0
    with open(out_csv_path, mode='w') as f :
        for label, ca_name in enumerate(category_list) : 
            filenames = filenames_list(root_dir, ca_name)
            total_data_size += len(filenames)
            for filename in filenames :
                f.write(f'{root_dir}/{ca_name}/{filename} {label}\n')
        print("total data size : ", total_data_size)
        
    pass # imgPath_class



# root_dir = "C:/Users/qhrud/data/obj_data"
# img_dir = "img"
# annot_dir = "annot"
def imgPath_annotPath (root_dir, img_dir, annot_dir, out_csv_path) :
    with open(f'{out_csv_path}', mode='w') as f :
        img_names = filenames_list(root_dir, img_dir)

        for img_name in img_names :
            annot_path = f"{root_dir}/{annot_dir}/{img_name[:-4]}.txt"
            assert os.path.isfile(annot_path), f"File is not exists :: {annot_path}"
            f.write(f'{root_dir}/{img_dir}/{img_name} {root_dir}/{annot_dir}/{img_name[:-4]}.txt\n')

        



if __name__ == "__main__" : 
    # imgPath_class("C:/Users/qhrud/data/face_gender_img/Validation", "C:/Users/qhrud/data/face_gender_img/labels3.csv" )
    # imgPath_annotPath("C:/Users/qhrud/data/obj_data", "img", "annot", "C:/Users/qhrud/data/obj_data/labels2.csv" )