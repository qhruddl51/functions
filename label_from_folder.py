import os

def filenames_list (root_dir, folder) : 
    filenames = os.listdir(f'{root_dir}/{folder}')
    print(f'{folder} data size : ', len(filenames))
    return filenames


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

