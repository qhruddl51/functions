# txt, csv에서 특정 컬럼에 있는 파일이름들을 뽑아 리스트로 반환
# separtor에 구분기호 전달 
def col_extract(col:int, file:str, separtor=",") : 
    with open(file, "r") as f :
        lines = f.readlines()
        lines = [re.split(separtor, line) for line in lines]
        file_list = [line[col-1] for line in lines]
        if (len(lines[0]) == col) :
            if not file_list[-1].endswith("\n") : file_list[-1] = file_list[-1]+"\n"
            else : pass
            file_list = [line[:-1] for line in file_list]
        else : file_list = [line for line in file_list]
    return file_list