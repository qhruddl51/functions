import os


# root_dir/folder의 모든 파일들의 이름을 리스트로 반환
def filenames_list (root_dir, folder) : 
    filenames = os.listdir(f'{root_dir}/{folder}')
    print(f'{folder} data size : ', len(filenames))
    return filenames



# 클래스 별로 다른 폴더에 데이터(파일)가 분류되어 있을 때, 
# "파일의 경로 레이블" 의 형식으로 어노테이션 파일을 만들어준다. 
# 단, category_list의 클래스 이름과 폴더 이름은 동일해야 한다. 
if __name__ == "__main__" : 
    root_dir = "C:/Users/qhrud/data/face_gender_img/Validation"
    category_list = ["female", "male"]
    total_data_size = 0 

    with open(f'{root_dir}/labels222.csv', mode='w') as f :
        for label, ca_name in enumerate(category_list) : 
            filenames = filenames_list(root_dir, ca_name)
            total_data_size += len(filenames)
            for filename in filenames :
                f.write(f'{root_dir}/{ca_name}/{filename} {label}\n')
        print("total data size : ", total_data_size)

