import re
import os


def myjoin(*paths) :
    pathstr = os.path.join(*paths)
    return re.sub(r"\\", "/", pathstr)


class LazyDecoder(json.JSONDecoder):
    def decode(self, s, **kwargs):
        """json 파일에서 파일 경로를 나타내는 string에 '\\'가 있더라도, 에러를 발생시키지 않고 '/'로 변환해 정상적으로 로드

        Usage:
            cfg_file="D:/.../generate_config.json"
            with open(cfg_file, 'r', encoding='utf-8') as json_file :
                params = json.load(json_file, cls=LazyDecoder)
        """
        regex_replacements = [
            (re.compile(r'([^\\])\\([^\\])'), r'\1\/\2'), # "//" -> "/"
            # (re.compile(r',(\s*])'), r'\1'), # ",  ]" -> "  ]"
        ]
        for regex, replacement in regex_replacements:
            s = regex.sub(replacement, s)
        return super().decode(s, **kwargs)


def path_parse(folder:str) : 
    folder_m = re.finditer(r'[/\\]+', folder)

    for m in folder_m  :
        root_dir_idx = m.start()
    # print(root_dir_idx)
    root_dir = folder[:root_dir_idx]
    return root_dir


# in_folder의 파일이름의 확장자만 ch_extension로 바꿔서 리스트로 반환
def ch_extension (in_folder, ch_extension="txt"): 
    filelist = os.listdir(in_folder)
    print("Number of files in in_folder : ", len(filelist))
    new_ext_filelist = []
    for filename in filelist : 
        filename_n = os.path.splitext(filename)[0] + f".{ch_extension}"
        new_ext_filelist.append(filename_n)
    return new_ext_filelist  # path2filename

