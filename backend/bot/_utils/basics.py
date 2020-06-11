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

