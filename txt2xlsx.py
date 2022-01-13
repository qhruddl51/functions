import openpyxl
import re
import random

# dbxlsx.xlsx의 첫번째 시트 이름은 Sheet1

def dbtxt2list (file="./a2ocorr/mydb.txt") : 
    """컬럼이 탭으로 구분된 txt 파일을 읽어서 한 행(리스트)씩 리스트에 담아 반환"""
    with open(file=file, mode='r', encoding='utf8') as txt : 
        lines = txt.readlines()
        lines = [re.sub('\n', "", l) for l in lines] # '\n' 제거
        new_lines = []
        
        for l in lines : 
            new_lines.append(re.split("\t", l))
            
    return new_lines


def list2xlsx(lines_list, xlsx_path="./a2ocorr/dbxlsx.xlsx") : 
    """dbtxt2list의 결과를 받아 엑셀파일에 작성"""
    wb = openpyxl.Workbook()
    sheet1 = wb['Sheet'] # 한 개 시트 지정
    sheet1.title = "Sheet1" # sheet 이름 변경
    # wb.create_sheet("Sheet2") # sheet 생성
    # wb.remove(wb['Sheet2']) # sheet 삭제
    
    for l in lines_list : 
        sheet1.append(l+[random.randint(1000, 10000)])
        
    # for i in sheet1.rows : 
    #     print(i)
    #     print(i[0].value, i[1].value, i[2].value)
    
    wb.save(xlsx_path) # sheet 저장
    pass # list2xlsx


dblist = dbtxt2list()
list2xlsx(dblist)