# -*- coding:utf-8 -*-
"""
Brief: Set Of Image Recognition(opencv, tasseract) Module Functions

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
import time
import numpy as np

##@@@-------------------------------------------------------------------------
##@@@ Installed(conda/pip) Libraries
import pyautogui as pag
import cv2
import pytesseract

##@@@-------------------------------------------------------------------------
##@@@ User Libraries
import image_recognition as _ir
import _gspread as _gs
import gui as _gu


##@@@@========================================================================
##@@@@ Constants


##@@@-------------------------------------------------------------------------
##@@@ External(.json/.py)
sys.path.append(os.path.join(os.path.dirname(sys.path[0]), '_config'))
from _settings import _ENV, _PATH, _MAP
from emulators import KEY_MAP as ui_key
from emulators import LOCATION_ROK_FULL as ui_xy
from emulators import IMAGE_ROK_FULL as ui_img


##@@@@========================================================================
##@@@@ Functions

##@@@-------------------------------------------------------------------------
##@@@ Basic Functions

def setup_ui_images(file_='TEST', sheet_='crop'):
    dicts = _gs.get_dict_from_sheet(_gs.fetch_sheet(file_, sheet_), 0)
    for dic in dicts:
        for k, v in dic.items():
            if k == 'x_y_w_h' and v != '':
                # dicts.remove(dic)
                #_ir.save_screenshot(box=[1, 1, _ENV['_MAX_X'], _ENV['_MAX_Y']], path=None)
                #print('after len(dicts): {}'.format(len(dicts)))
                #dic = {'original': '스크린샷 2020-05-19 오전 12.02.47', 'x_y_w_h': '646, 726, 136, 82', 'prefix': 'btn_Mod_Profile_Settings_CharacterManagement_CharacterLogin_No'}
                shots = '/Volumes/data/dev/SynologyDrive/projects/_ROK/bot/_screenShots/'
                file = shots + dic['original'] + _ENV['_IMG_EXT']
                box = _gu.get_box_from_wh(list(map(int, dic['x_y_w_h'].replace(' ','').split(','))))
                path = '../images/_uis/' + dic['prefix'] + _ENV['_IMG_EXT']
                #print('file: {}, box: {}, path: {}'.format(file, box, path))
                #print('x_y_w_h: {}'.format(list(map(int, dic['x_y_w_h'].replace(' ','').split(',')))))
                #print('box: {}'.format(box))
                _ir.save_file_crop(file, box, path)
    # return dicts


##@@@@========================================================================
##@@@@ Execute Test
if __name__ == '__main__':
    dic = setup_ui_images('TEST', 'crop')
    #print(dic)