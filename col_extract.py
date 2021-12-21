import csv
import re


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


# csv에서 컬럼단위로 리스트로 묶어 반환
def cols_extract(file:str, separtor=",", cols=None) : 
    with open(file, "r", encoding="utf8") as f :
        lines = list(csv.reader(f, delimiter=separtor)) # 한 라인씩 나온다. 
        cols_list = []
        
        if not cols : cols = range(1,len(lines[0])+1)
        else : pass
        
        for col in cols : 
            col_list = [line[col-1] for line in lines]
            if (len(lines[0]) == col) :
                if not col_list[-1].endswith("\n") : col_list[-1] = col_list[-1]+"\n"
                else : pass
                col_list = [line[:-1] for line in col_list]
            else : col_list = [line for line in col_list]
            
            cols_list.append([line[col-1] for line in lines])
            pass # 하나의 컬럼
        
    return cols_list # col_extract