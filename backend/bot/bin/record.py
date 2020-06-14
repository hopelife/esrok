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
import pyautogui as pag

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

def record_moreinfo_unit(level='R4', row=0, col=0):
    moreinfo = {'nick':''}

    prefix = 'val_Mod_Governor_Info_MoreInfo_'
    vals = ['Power', 'Kills', 'HighestPower', 'Victory', 'Defeat', 'Dead', 'ScoutTimes', 'ResourcesGathered', 'ResourceAssistance', 'AllianceHelpTimes']
    print('vals: {}'.format(vals))

    for val in vals:
        print('_vals[prefix + val]: {}'.format(_vals[prefix + val]))
        moreinfo[val] = _bs.do_ocr(_vals[prefix + val], color='WHITE', lang='digits', path='../images/test/' + val + '.png')

    ## More Info 내에 있는 Kill 상세 버튼
    _bs.click_mouse(position=[1290, 186])

    prefix = 'val_Pop_Governor_Info_MoreInfo_'
    tiers = ['Kills_1', 'Kills_2', 'Kills_3', 'Kills_4', 'Kills_5']
    #print('tiers: {}'.format(tiers))

    for tier in tiers:
        print('_tiers[prefix + tier]: {}'.format(_vals[prefix + tier]))
        moreinfo[tier] = _bs.do_ocr(_vals[prefix + tier], color='WHITE', lang='digits', path='../images/test/' + tier + '.png', reverse=False, gauss=7)

    #### btn_Mod_Governor_Info_MoreInfo_CopyNick
    position = _bs.compute_center_from_box(_bs.compute_box_from_wh([437, 171, 30, 30]))
    nick = _bs.click_copy(position=position)
    moreinfo['nick'] = nick


    for i in range(0, 3):
        pag.keyDown('esc')
        time.sleep(0.1)
        pag.keyUp('esc')
        time.sleep(3)

    return moreinfo  ## 


def record_moreinfo_level(level='R4'):
    ## 자기 등급 멤버 목록만 unfold
    ## 등급 멤버 인원 수 확인(행수 = ceil(우측 인원 수 / 열 수))
    ## - 마우스 드래그가 필요한 지 확인
    ## 행, 열 반복 루프(R4: 4열, 이외: 2열)
    ## 마우스 드래그가 필요한 지 확인

    #unfold_members_level(level)

    infos = []

    for i in range(0, rows):
        for j in range(0, cols):
            info = record_moreinfo_unit(level, i, j)
            infos.append(info)

    return infos


def ocr_test():
    positions = [
        [1540, 1000],  ## btn_  Alliance
        [124, 420],  ## tab_ Members
    ]

    click_coords = {
        'chief': [
            [660, 216],  ## 맹주 Profile
            [870, 164],  ## btn_   Info
            [464, 800]  ## btn_ MoreInfo
        ],
        'R4': {
            'title': [976, 390],
            'matrix': [4, 2],
            'interval': [360, 184],
            'start': [460, 516]
        }
    }

    btn_info = '../images/uis/btn_Mod_Alliance_AllianceMembers_Info.png'

    for position in positions:
        _bs.click_mouse(position=position)
        time.sleep(1.5)


def change_test():
    positions = [
        [74, 60],  ## btn_  Profile
        [1470, 800],  ## btn_ Settings
        [430, 572],  ## btn_ CharacterManagement
    ]

    for position in positions:
        _bs.click_mouse(position=position)
        time.sleep(1.5)

    btn_m004 = '../images/uis/btn_Character_m004.png'

    center = _bs.match_image_box(btn_m004)

    _bs.click_mouse(center)


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
    #print(ocr_test())
    change_test()