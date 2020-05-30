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

# Getting All Values From a Row or a Column
# # Get all values from the first row
# values_list = worksheet.row_values(1)

# # Get all values from the first column
# values_list = worksheet.col_values(1)
# Getting All Values From a Worksheet as a List of Lists
# list_of_lists = worksheet.get_all_values()
# Finding a Cell
# # Find a cell with exact string value
# cell = worksheet.find("Dough")

# print("Found something at R%sC%s" % (cell.row, cell.col))

# # Find a cell matching a regular expression
# amount_re = re.compile(r'(Big|Enormous) dough')
# cell = worksheet.find(amount_re)

##@@@-------------------------------------------------------------------------
##@@@ Complex Functions


def fill_google_rows(worksheet='', sheet_data={}, header_to_key={}, NUM_HEADER_ROW=1):
    headers = worksheet.row_values(NUM_HEADER_ROW)
    print(headers)
    put_values = []
    for v in sheet_data:
        temp = []
        for h in headers:
            temp.append(v[header_to_key[h]])
        put_values.append(temp)
    print(put_values)
    spreadsheet.values_append(sheetName, {'valueInputOption': 'USER_ENTERED'}, {'values': put_values})


def create_google_rows2(worksheet='', sheet_data={}, START_CELL=[1,1]):
    headers = [key for key, val in sheet_data[0].items()]

    # put_values = headers.copy()
    put_values = []
    put_values.append(headers)
    for v in sheet_data:
        temp = []
        for h in headers:
            temp.append(v[h])
        put_values.append(temp)
    print(put_values)
    spreadsheet.values_append(sheetName, {'valueInputOption': 'USER_ENTERED'}, {'values': put_values})


def update_sheet(ws, rows, left=1, top=1):
    """
    updates the google spreadsheet with given table
    - ws is gspread.models.Worksheet object
    - rows is a table (list of lists)
    - left is the number of the first column in the target document (beginning with 1)
    - top is the number of first row in the target document (beginning with 1)
    """

    # number of rows and columns
    num_lines, num_columns = len(rows), len(rows[0])

    cell_list = ws.range(
        gspread.utils.rowcol_to_a1(left,top)+':'+colrow_to_A1(left+num_columns-1, top+num_lines-1)
    )

    # modifying the values in the range

    for cell in cell_list:
        val = rows[cell.row-top][cell.col-left]
        cell.value = val

    # update in batch
    ws.update_cells(cell_list)

##@@@@========================================================================
##@@@@ Execute Test
if __name__ == "__main__":
    #find_firstHeaderCell(file=open_google_sheet('TEST'))
    #find_firstHeaderCell(file=open_google_sheet('https://docs.google.com/spreadsheets/d/1zwHf6FEcqb_vyHC-3uSlzzE0ln8zoMsW5-YwNzTryLU/edit#gid=0'))
    #spreadsheetId = "###"  # Please set the Spreadsheet ID.
    #sheetName = "Sheet1"  # Please set the sheet name.

    # 스프레스시트 문서 가져오기 
    #spreadsheet = gc.open_by_url(_GOOGLE['_URLS']['TEST'])

    # 시트 선택하기
    # _SHEET = doc.worksheet('crop')
    #_SHEET = 'crop'
    sheetName = 'test'

    spreadsheet = gc.open_by_url(_GOOGLE['_URLS']['TEST'])
    worksheet = spreadsheet.worksheet(sheetName)

    sheet_data = [{
        "timestamp": "09-04-2019",
        "value": "10.0",
        "company_name": "Xbox",
        "product": "Buy"
    }, {
        "timestamp": "09-03-2019",
        "value": "2.0",
        "company_name": "something",
        "product": "Sell"
    }]

    header_to_key = {
        'Date': 'timestamp',
        'Company_Name': 'company_name',
        'Traffic': 'value',
        'Product': 'product'
    }

  # client = gspread.authorize(credentials)
  # spreadsheet = client.open_by_key(spreadsheetId)
  # worksheet = spreadsheet.worksheet(sheetName)

#   headers = worksheet.row_values(1)
#   print(headers)
#   put_values = []
#   for v in sheet_data:
#       temp = []
#       for h in headers:
#           temp.append(v[header_to_key[h]])
#       put_values.append(temp)
#   print(put_values)
#   spreadsheet.values_append(sheetName, {'valueInputOption': 'USER_ENTERED'}, {'values': put_values})





    # create_google_rows2(worksheet, sheet_data)







    table = [['one', 'two', 'three'], [1, 2, 3]]

    # you may need to resize your worksheet so it have the neccessary cells
    # ws.resize(len(table),len(table[0]))

    update_sheet(worksheet, table, 3, 3)


def complete_quest():
	pass


def do_event():
	pass


def record_event_schedule(unit='DAY, WEEK'):
	pass





def write_villages_caves()
	pass

def find_villages_caves(center='', viewMode='', type=''):
	pass


def record_alliance_members(alliance='name/ranking', grade):
	pass
	
	
def record_alliance_members_by_ranking(ranking, grade):
	go_alliance_record()
	go_members_grade()
	count_members()
	get_members_info()
	fill_sheet_cells()
	pass		

def record_alliance_members_by_name(name, grade):
	pass





Date	Company_Name      Traffic      Product