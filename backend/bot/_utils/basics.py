# -*- coding:utf-8 -*-
##@@@@========================================================================
##@@@@ Libraries

##@@@-------------------------------------------------------------------------
##@@@ Basic Libraries
import os
import sys
from pathlib import Path
import json
#from json import dumps
# from datetime import date, timedelta, datetime
# import time
# import re

##@@@-------------------------------------------------------------------------
##@@@ Installed(conda/pip) Libraries

##@@@-------------------------------------------------------------------------
##@@@ Data Management(File/Soup)

##@@ brief:: convert dictionary(json) to file
##@@ note:: [*****] 함수명 변경 필요(json_to_file)
def json_to_file(data, path):
  with open(path, 'w', encoding='UTF-8') as file:
    file.write(json.dumps(data, indent=2, ensure_ascii=False, default=str))


##@@ brief:: convert file to json
##@@ note:: 
def file_to_json(path):
  with open(path, encoding='UTF-8') as f:
    return json.load(f)


##@@ brief:: create a new file & write file
##@@ note::
def write_file(path, data):
  with open(path, 'w') as f:
    f.write(data)


##@@ brief:: open pen file and replace words
##@@ note:: [*****] 교정 필요 _traning/lecture/nomardcorders 참조
def modify_file(path, rpls={'org1':'rep1', 'org2':'rep2'}):
  # Read in the file
  with open(path, 'r') as file :
    data = file.read()

  # Replace the target string
  for key, val in rpls.items():
    #print(key + ':' + val)
    data = data.replace(key, val)

  # Write the file out again
  with open(path, 'w') as file:
    file.write(data)


##@@ brief:: add data onto an existing file
##@@ note::
def append_to_file(path, data):
  with open(path, 'a') as file:
    file.write(data + '\n')


##@@ brief:: delete the contents of a file
##@@ note::
def delete_file_contents(path):
  open(path, 'w').close()


##@@ brief:: read a file and convert each line to set items
##@@ note::
def file_to_set(file_name):
  results = set()
  with open(file_name, 'rt') as f:
    for line in f:
      results.add(line.replace('\n', ''))
  return results


##@@ brief:: iterate through a set, each item will be a line in a file
##@@ note::
def set_to_file(links, file_name):
  with open(file_name,"w") as f:
    for l in sorted(links):
      f.write(l+"\n")


##@@ brief:: convert soup to file
##@@ note:: 
def soup_to_file(soup, path):
  write_file(path, str(soup.prettify()))


# ##@@ brief:: generate & write excel file
# ##@@ note:: 
def write_excel(data=[], wb={}, callback=None):
  # create workbook open
  #load_wb = load_workbook()
  write_wb = Workbook()
  # worksheet open
  write_ws = write_wb.active
  write_ws.title = '성능평가'
  #write_ws = write_wb.create_sheet('충남')
  # write_ws = write_wb.active  # default sheet[Sheet1]

  # callback func: work with data
  if callback:
    callback(write_ws, data, wb)

    # write field name at cell
    # write field data at cell
  # save workbook
  write_wb.save('../_files/' + wb['name'])
  pass



# ##@@ brief:: generate excel file
# ##@@ note:: 
def update_excel(data=[], wb={}, callback=None):
  # create workbook open
  #load_wb = load_workbook()
  write_wb = Workbook()
  # worksheet open
  
    # write field name at cell
    # write field data at cell
  # close workbook
  pass


# ##@@ brief:: generate excel file
# ##@@ note:: 
def read_excel(data=[], wb={}, callback=None):
  # create workbook open
  #load_wb = load_workbook()
  write_wb = Workbook()
  # worksheet open
  
    # write field name at cell
    # write field data at cell
  # close workbook
  pass
##@@@-------------------------------------------------------------------------