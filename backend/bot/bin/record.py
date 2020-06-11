# -*- coding:utf-8 -*-
"""
Brief: Record Module Functions

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
import sys
import os
import time
import random
import math
import re
# import json

##@@@-------------------------------------------------------------------------
##@@@ Installed(conda/pip) Libraries


##@@@-------------------------------------------------------------------------
##@@@ User Libraries



##@@@@========================================================================
##@@@@ Constants


##@@@-------------------------------------------------------------------------
##@@@ External(.json/.py)
sys.path.append(os.path.join(os.path.dirname(sys.path[0]), '_utils'))
import _basics as _bs
#sys.path.append(os.path.join(os.path.dirname(sys.path[0]), '_config'))
_uis = _bs.file_to_json('../_config/uis.json', encoding='UTF-8')
_vals = _bs.file_to_json('../_config/ui_boxes.json', encoding='UTF-8')
##@@@-------------------------------------------------------------------------
##@@@ internal



##@@@@========================================================================
##@@@@ Functions

##@@@-------------------------------------------------------------------------
##@@@ Basic Functions
def record_test():
    return _bs.click_copy(position=[1002, 346])

def click_test():
    _bs.click_mouse(position=_uis['btn_Mod_Alliance_Members_Rank4_1'])  ## btn_Mod_Alliance_Members_Rank4_1 / btn_QuickloanchOsxROK -> btn_WallpaperEmulROKMax

# def ocr_test():
#     return _bs.do_ocr([1420, 308, 1564, 356])  ## 


def ocr_test():
    prefix = 'val_Mod_Governor_Info_MoreInfo_'
    vals = ['Power', 'Kills', 'HighestPower', 'Victory', 'Defeat', 'Dead', 'ScoutTimes']
    moreinfo = {}
    print('vals: {}'.format(vals))
    for val in vals:
        print('_vals[prefix + val]: {}'.format(_vals[prefix + val]))
        moreinfo[val] = _bs.do_ocr(_vals[prefix + val], lang='digits')
    return moreinfo  ## 

##@@@-------------------------------------------------------------------------
##@@@ Complex Functions


##@@@@========================================================================
##@@@@ Execute Test
if __name__ == "__main__":
    #_bs.delay_secs(5)
    time.sleep(5)
    # nick = record_test()
    # print(nick)
    # click_test()
    print(ocr_test())