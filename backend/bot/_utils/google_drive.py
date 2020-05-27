# -*- coding:utf-8 -*-
"""
Brief: Set Of Google Drive(google spreadsheet) Module Functions

Structure:
  - Libraries
    - Basic Libraries
    - Installed(conda/pip) Libraries
    - User Libraries

  - Constants
    - External(.json/.py)
    - Internal

  - Functions
    - Basic Functions
    - Complex Functions

  - Main Function

Usage: import 
"""

##@@@@========================================================================
##@@@@ Libraries

##@@@-------------------------------------------------------------------------
##@@@ Basic Libraries
import os
import sys

##@@@-------------------------------------------------------------------------
##@@@ Installed(conda/pip) Libraries
import gspread
from oauth2client.service_account import ServiceAccountCredentials

##@@@-------------------------------------------------------------------------
##@@@ User Libraries



##@@@@========================================================================
##@@@@ Constants


##@@@-------------------------------------------------------------------------
##@@@ External(.json/.py)
sys.path.append(os.path.join(os.path.dirname(sys.path[0]), '_config'))
from _settings import _GOOGLE

##@@@-------------------------------------------------------------------------
##@@@ internal

credentials = ServiceAccountCredentials.from_json_keyfile_name(_GOOGLE['_JSON'], _GOOGLE['_SCOPE'])
gc = gspread.authorize(credentials)

# 스프레스시트 문서 가져오기 
_FILE = gc.open_by_url(_GOOGLE['_URLS']['TEST'])

# 시트 선택하기
# _SHEET = doc.worksheet('crop')
_SHEET = 'crop'
_SHEET = 'test'

##@@@@========================================================================
##@@@@ Functions
 
##@@@-------------------------------------------------------------------------
##@@@ Basic Functions

def open_google_sheet(name=''):
    if 'docs.google.com' in name: ## name에 'docs.google.com' 포함되어 있다면(url)
        ws = gc.open_by_url(name)
    else:
        ws = gc.open_by_url(_GOOGLE['_URLS'][name])
    return ws


## @@brief:: 다음에 입력할 행(row) 찾기
## @@note:: col = 1 (기준 열 번호 1 => A) / 기준열은 비어있는 값이 있으면 안됨!!!
def find_newRowNum(worksheet, col=1):
    str_list = list(filter(None, worksheet.col_values(1)))
    print(str_list)
    return len(str_list)+1
    #return str(len(str_list)+1)


# ## @@brief:: 첫번째 header 위치
# ## @@note:: 
# def find_newRowNum(worksheet, col=1):
#     str_list = list(filter(None, worksheet.col_values(1)))
#     print(str_list)
#     return len(str_list)+1
#     #return str(len(str_list)+1)


## @@brief:: 값으로 collum 번호 찾기
## @@note:: col = 1 (기준 열 번호 1 => A) / 기준열은 비어있는 값이 있으면 안됨!!!
def find_colbyValue(value, sheet=_SHEET, file=_FILE, row=None):
    worksheet = _FILE.worksheet(sheet)
    index = 0
    if row == None:
        cell = worksheet.find(value)
        index = cell.col
    else:
        vals = worksheet.row_values(row)
        for i, val in enumerate(vals):
          if val == value:
            index = i + 1
            break
    print(index)
    return index


## @@brief:: 첫번째 header 위치 찾기
## @@note:: value::None => 연속 3개 row에 값이 있는 위치(1~10 column을 확인), value::string => 첫번째 header 값, value::list => 첫번째 header 위치
def find_firstHeaderCell(value=None, sheet=_SHEET, file=_FILE):
    values = [None for j in range(0, 10)]
    worksheet = _FILE.worksheet(sheet)
    last = 0

    if value == None:
      for i in range(1, 5):
        for j in range(1, 8):
          val = worksheet.cell(j, i).value
          print(val)
          print(last)
          if val == None or val == '':
            print('empty:: i: {}, j: {}'.format(i, j))
            last = 0
          else:
            last += 1
            print('filled:: i: {}, j: {}'.format(i, j))
            print('val: {}'.format(val))
            if last > 2:
              return j


        #values[i] = [worksheet.cell(i, j).value for j in range(1, 5)]

    print(values)
    # worksheet = _FILE.worksheet(sheet)
    # cell = worksheet.find(value)
    # return [cell.col, cell.row]


##@@ brief:: sql insert(first: 첫번째 key(title/header), string => key, list => 첫번째 key 위치[i, j])
##@@ note:: dic(dictionary) {'key1': 'value1', ....}
def insert_cell(dic={}, first=[], header=0, sheet=_SHEET, file=_FILE):
    worksheet = _FILE.worksheet(sheet)
    row = find_newRowNum(worksheet)
    # if type(first) is 'str':
    #   col = find_firstHeaderCell(value, sheet=_SHEET, file=_FILE)[0]
    # else:
    #   col = first[0]
    
    for k, v in dic.items():
      col = find_firstHeaderCell(k, sheet=_SHEET, file=_FILE)[0]
      worksheet.update_cell(row, col, v)


##@@@@========================================================================
##@@@@ Functions

##@@@-------------------------------------------------------------------------
##@@@ Basic Functions


##@@@-------------------------------------------------------------------------
##@@@ Complex Functions



##@@@@========================================================================
##@@@@ Execute Test
if __name__ == "__main__":
  #find_firstHeaderCell(file=open_google_sheet('TEST'))
  find_firstHeaderCell(file=open_google_sheet('https://docs.google.com/spreadsheets/d/1zwHf6FEcqb_vyHC-3uSlzzE0ln8zoMsW5-YwNzTryLU/edit#gid=0'))