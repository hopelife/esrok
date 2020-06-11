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
import numpy as np

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


def fetch_sheet(file_, sheet_):
    return gc.open_by_url(_GOOGLE['_URLS'][file_]).worksheet(sheet_)


def list_to_dict(ls=[]):
    """
    Brief: convert list to dictionary
    Args: ls = [['h1', 'h2', 'h3', ...], ['c11', 'c12', 'c13', ....], ['c21', 'c22', 'c23', ....], ...]
    Returns: [{'h1':'c11', 'h2':'c12', ...}, {'h1':'c21', 'h2':'c22', ...}, ...]
    """
    return [dict(zip(ls[0], v)) for v in ls[1:]]


def flatten_list(ls):
    """
    Brief: flatten list
    Args: ls = [['c01', 'c02', 'c03', ...], ['c11', 'c12', 'c13', ....], ['c21', 'c22', 'c23', ....], ...]
    Returns: ['c01', 'c02', 'c03', ..., 'c11', 'c12', 'c13', ...., 'c21', 'c22', 'c23', ...., ...]
    """
    return np.array(ls).flatten()


def remove_empty_list(ls):
    """
    Brief: flatten list
    Args: ls = [['c01', 'c02', 'c03', ...], ['', '', '', ....], ['c21', 'c22', 'c23', ....], ...]
    Returns: [['c01', 'c02', 'c03', ...], ['c21', 'c22', 'c23', ....], ...]
    """
    return [l for l in ls if any(i != '' for i in l)]


def find_first_filled_row(data):
    """
    Brief: find first filled row
    Args: ls = ['', '', '', '', '', '', '', ''], ['', '', '', '', '', '', '', ''], ['', '', '', '', '', '', '', ''], ['', 'one', '', '', '', '', '', ''], ['', '03-01-1900', 'two', 'three', 'Buy', '', '', '']
    Returns: 4
    """
    for i, v in enumerate(flatten_list(data)):
        if v != '':
            return (i+1)//len(data[0]) + 1


def find_first_filled_col(data):
    """
    Brief: find first filled col
    Args: ls = ['', '', '', '', '', '', '', ''], ['', '', '', '', '', '', '', ''], ['', '', '', '', '', '', '', ''], ['', 'one', '', '', '', '', '', ''], ['', '03-01-1900', 'two', 'three', 'Buy', '', '', '']
    Returns: 2
    """
    for j in range(0, len(data)):
        for i, v in enumerate(flatten_list(data)[j::len(data[0])]):
            if v != '':
                return j + 1


def get_filled_dict(data, header=0):
    """
    Brief: find first filled col
    Args: 
        data = ['', '', '', '', '', '', '', ''], ['', '', '', '', '', '', '', ''], ['', '', '', '', '', '', '', ''], ['', 'one', '', '', '', '', '', ''], ['', '03-01-1900', 'two', 'three', 'Buy', '', '', '']
        header : 공백 열 제거 후 header 열의 상대 위치(ex: 1 -> 다음 행)
    Returns: 2
    """
    #return list_to_dict([v[find_first_filled_col(data)-1:] for v in data[find_first_filled_row(data)-1:]][header:])
    return list_to_dict([v[find_first_filled_col(data)-1:] for v in remove_empty_list(data)][header:])



##@@@-------------------------------------------------------------------------
##@@@ Complex Functions

def get_dict_from_sheet(ws, header=0):
    """
    Brief: find first filled col
    Args: 
        data = ['', '', '', '', '', '', '', ''], ['', '', '', '', '', '', '', ''], ['', '', '', '', '', '', '', ''], ['', 'one', '', '', '', '', '', ''], ['', '03-01-1900', 'two', 'three', 'Buy', '', '', '']
        header : 공백 열 제거 후 header 열의 상대 위치(ex: 1 -> 다음 행)
    Returns: 2
    """
    return get_filled_dict(ws.get_all_values(), header)


##@@@@========================================================================
##@@@@ Execute Test
if __name__ == '__main__':
    # data = [['', '', '', '', '', '', '', '', ''], ['', '', '', '', '', '', '', '', ''], ['', '', '', '', '', '', '', '', ''], ['', '', '', '', '', '', '', '', ''], ['', '', '1', '2', '3', '4', '5', '6', '7'], ['', '', '03-01-1900', 'two', 'three', 'Buy', '', '', ''], ['', '', 'timestamp', '', '6', 'Sell', '', '', ''], ['', '', '', 'value', 'one', 'two', '', 'three', ''], ['', '', '', '', '', '', '', '', ''], ['', '', '', '', '', '', '', '', ''], ['', '', '', '', '', '', '', '', ''], ['', '', '09-04-2019', '10', '', '2', '', '', '3'], ['', '', '09-03-2019', '2', '', 'Sell', '', '', ''], ['', '', '', '', '', '', '', '', ''], ['', '', '', '', '', '', '', '', ''], ['', '', '', '', 'something', '', '', '', '']]

    # # row = find_first_filled_row(data)
    # # col = find_first_filled_col(data)
    # dic = get_filled_dict(data, 0)
    # # print('f_data: {}, row: {}, col: {}, dic: {}'.format(flatten_list(data), row, col, dic))
    # print(dic)

    # d = [l for l in data if any(i != '' for i in l)]
    # print(d)

    sheetName = 'crop'
    spreadsheet = gc.open_by_url(_GOOGLE['_URLS']['TEST'])
    ws = spreadsheet.worksheet(sheetName)

    dic = get_dict_from_sheet(ws, header=0)
    print(dic)