# -*- coding:utf-8 -*-
##@@@@========================================================================
##@@@@ Libraries

##@@@-------------------------------------------------------------------------
##@@@ Basic Libraries
import os
import sys
# from pathlib import Path
import time
# from datetime import date, timedelta, datetime
# #from bson.json_util import dumps
# import json
# import re
# import numpy as np
# import random

##@@@-------------------------------------------------------------------------
##@@@ User Libraries
# sys.path.append(os.path.join(os.path.dirname(sys.path[0]), '_utils'))
from _config import _ENV, oss, emulators
from _basics import *


##@@@@========================================================================
##@@@@ Constants


##@@@-------------------------------------------------------------------------
##@@@ From:: External Files .py

#DATA_TYPES = file_to_json('../_files/res_data_type.json')

##@@@-------------------------------------------------------------------------
##@@@ From:: here itself
# 
_OS = oss[_ENV['_OS']]
_UI = emulators[_ENV['_EMULATOR']]

##@@@@========================================================================
##@@@@ Functions

##@@@-------------------------------------------------------------------------
##@@@ Account / Character

## @@brief:: 
## @@note:: 
def turnOnEmulator(emulator=_ENV['_EMULATOR']):
    # 버튼
    #_UI = emulators[emulator]['BUTTONS']

    # For BLUESTACK
    if emulator == 'BLUESTACK':
        clickMouse(_UI['location']['icon_wallpaper'])
        time.sleep(10)
        clickMouse([1000, 500])

    # For LDPLAYER
    elif emulator == 'LDPLAYER':
        # 바탕화면 더블 클릭
        clickMouse2(_OS['ROK_WALLPAPER']['xy'])

        ## popup 닫기 !!!!
        ## 상단 메뉴바 아래 부분에서 '닫기' 버튼 있으면, 클릭!!!!
        for btn in _UI['OUTER']['POPUP_CLOSES']:
            time.sleep(1)
            clickMouse(btn)

        # ROK 아이콘 클릭
        for _ in range(0, 15):
            print('rok icon path: ' + _ENV['_IMAGES_FOLDER'] + _UI['OUTER']['WALLPAPER_ROK_MID']['fn'])
            loaded = matchImageBox(_ENV['_IMAGES_FOLDER'] + _UI['OUTER']['WALLPAPER_ROK_MID']['fn'])
            if loaded == False:
                time.sleep(10)
            else:
                clickMouse(loaded)
                break

        ## popup(avast) 닫기
        clickMouse(_UI['OUTER']['POPUP_AVAST'])

        # 최대화 버튼 클릭
        time.sleep(2)
        clickMouse(_UI['OUTER']['MENUBAR_MAX_MID']['xy'])

        # 게임 화면 진입 여부 확인
        for _ in range(0, 30):
            loaded = matchImageBox(_ENV['_IMAGES_FOLDER'] + _UI['MAIN']['VIEWALLIANCE_MAX']['fn'])
            if loaded == False:
                time.sleep(10)
            else:
                print(loaded)
                break
        
        ## 게임 화면 진입이 안된 경우 처리!!!
        if loaded == False:
            pass

        time.sleep(2)
        
        # 하단 메뉴 펼침
        unfoldMenuBtn()
    
    return 0


## @@brief:: 
## @@note:: 
def turnOffEmulator(emulator=_ENV['_EMULATOR']):
    clickMouse(_UI['MAIN']['MENUBAR_CLOSE_MAX']['xy'])
   
    return 0


## @@brief:: 
## @@note:: 
def checkEmulatorState():
    pass


## @@brief:: viewMode 확인
## @@note:: 'CASTLE_VIEW' / 'ALLIANCE_VIEW' / 'KINGDOM_VIEW'
def checkViewMode():
    if matchImageBox(_ENV['_IMAGES_FOLDER'] + _UI['MAIN']['VIEWKINGDOM_MAX']['fn']):
        return 'KINGDOM_VIEW'
    elif matchImageBox(_ENV['_IMAGES_FOLDER'] + _UI['MAIN']['VIEWALLIANCE_MAX']['fn']):
        return 'CASTLE_VIEW'
    elif matchImageBox(_ENV['_IMAGES_FOLDER'] + _UI['MAIN']['VIEWCASTLE_MAX']['fn']):
        return 'ALLIANCE_VIEW'


## @@brief:: viewMode 확인
## @@note:: 'CASTLE_VIEW' / 'ALLIANCE_VIEW' / 'KINGDOM_VIEW'
def toggleViewMode():
    clickMouse(_UI['MAIN']['VIEWCASTLE_MAX']['xy'])
    return 0


## @@brief:: viewMode 확인@@@@@@@@@@@@@@@@@@@@@@
## @@note:: 'CASTLE_VIEW' / 'ALLIANCE_VIEW' / 'KINGDOM_VIEW'
def setViewMode(viewMode='CASTLE_VIEW'):
    if viewMode == 'KINGDOM_VIEW':
        zoomKingdom()
    
    if checkViewMode() == viewMode:
        return 0

    if checkViewMode() == 'KINGDOM_VIEW':
        if viewMode == 'ALLIANCE_VIEW':
            clickMouse(_UI['MAIN']['VIEWCASTLE_MAX']['xy'])
            time.sleep(2)
            clickMouse(_UI['MAIN']['VIEWCASTLE_MAX']['xy'])
        elif viewMode == 'CASTLE_VIEW':
            clickMouse(_UI['MAIN']['VIEWCASTLE_MAX']['xy'])
    else:
        toggleViewMode()
    
    return 0


## @@brief:: 메뉴 버튼(campaign, items, alliance, commander) 펼치기
## @@note:: 
def unfoldMenuBtn():
    if not matchImageBox(_ENV['_IMAGES_FOLDER'] + _UI['MAIN']['CAMPAIGN_MAX']['fn']):
        clickMouse(_UI['MAIN']['MENU_MAX']['xy'])



## @@brief:: 메뉴 버튼(campaign, items, alliance, commander) 펼치기
## @@note:: vector[0]: x방향, 1: _ENV(_MAX_X)//2
def moveMapDirection(vector=[]):
    _x = _ENV['_MAX_X']//2
    _y = _ENV['_MAX_X']//2
    # moveMouse(_x, _y)
    dragInMap([vector[0]*_x, vector[1]*_y])
    # moveMouse(vector[0]*_x, vector[1]*_y)

##@@@@========================================================================
##

## @@brief:: 지도를 최고로 축소시킴
## @@note:: 
def zoomKingdom():
    ## zoom mode 확인!!!
    time.sleep(3)
    pag.moveTo(_ENV['_MAX_X']//2, _ENV['_MAX_Y']//2, duration=0.0)
    pag.rightClick()

    shortcut = _UI['_SETTINGS']['_SHORTCUT']

    for _ in range(0, shortcut['zoomth']):
        time.sleep(0.1)
        #설정에서 단축키(축소) 지정 확인 @@@@@@
        pag.keyDown(shortcut['zoom_out'][0])
        time.sleep(0.2)
        pag.press(shortcut['zoom_out'][1])
        #pag.hotkey(shortcut['zoom_out'][0], shortcut['zoom_out'][1])
    pag.keyUp(shortcut['zoom_out'][0])



def starter(delay=10):
  print("I'm Starter, Now Start-----------------")
  time.sleep(delay)
  print("I'm Starter, Now End-------------------")


def ender(delay=1):
  print("I'm Ender, Now Start*****************")
  time.sleep(delay)
  print("I'm Ender, Now End*******************")


def cb1(delay=8):
  print("I'm cb1, Now Start+++++++++++++++")
  time.sleep(delay)
  print("I'm cb1, Now End+++++++++++++++++")


def cb2(delay=6):
  print("I'm cb2, Now Start##############")
  time.sleep(delay)
  print("I'm cb2, Now End################")


def cb3(delay=4):
  print("I'm cb3, Now Start^^^^^^^^^^^^^")
  time.sleep(delay)
  print("I'm cb3, Now End^^^^^^^^^^^^^^^")




def doCallbackSeries(start, cbs, end):
    print("I'm doCallbackSeries, Now Start===================")
    start()
    for cb in cbs:
        cb()
    end()
    print("I'm doCallbackSeries, Now End===================")


##@@@@========================================================================
##@@@@ Execute Test
if __name__ == "__main__":
    #turnOnEmulator()
    print('====')
    #print(checkViewMode())
    #unfoldMenuBtn()
    # setViewMode('CASTLE_VIEW')
    # time.sleep(3)
    # setViewMode('ALLIANCE_VIEW')
    # time.sleep(3)
    # setViewMode('KINGDOM_VIEW')
    # time.sleep(3)
    # setViewMode('CASTLE_VIEW')
    time.sleep(3)
    # for _ in range(0, 20):
    #   pag.keyDown('down')
    #   time.sleep(0.1)
    

    moveMapDirection([1, 0])



    #doCallbackSeries(starter, [cb1, cb2, cb3], ender)
