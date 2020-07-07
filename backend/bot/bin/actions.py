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
sys.path.append(os.path.join(os.path.dirname(sys.path[0]), '_config'))
# sys.path.append(os.path.join(os.path.dirname(sys.path[0]), '_config'))
# from _settings import _ENV, _PATH, _MAP, _TESSERACT, _GOOGLE
from _settings import _ENV, _PATH
# from emulators import KEY_MAP as ui_key
# from emulators import OBJECTS as ui_obj
# from emulators import LOCATION_ROK_FULL as ui_xy
# from emulators import IMAGE_ROK_FULL as ui_img
sys.path.append(os.path.join(os.path.dirname(sys.path[0]), '_utils'))
from _basics import *


##@@@@========================================================================
##@@@@ Constants


##@@@-------------------------------------------------------------------------
##@@@ From:: External Files .py
_uis = file_to_json('../_config/uis.json', encoding='UTF-8')
_imgs = _PATH['_UIS']

#DATA_TYPES = file_to_json('../_files/res_data_type.json')

##@@@-------------------------------------------------------------------------
##@@@ From:: here itself
# 
# _OS = oss[_ENV['_OS']]
#_UI = emulators[_ENV['_EMULATOR']]

##@@@@========================================================================
##@@@@ Functions

def create_new_character():
    """
    """
    btns = [
        _uis['btn_Profile'],
        _uis['btn_Mod_Profile_Settings'],
        _uis['btn_Mod_Profile_Settings_CharacterManagement'],
    ]

    click_mouse_series(btns, interval=2, clicks=1)

    btn_create = _imgs + 'btn_Mod_CharacterMangement_CreateNewCharacter.png'
    print(btn_create)
    btn = match_image_box(template=btn_create, precision=0.99)

    for _ in range(0, 5):
        if btn is False:
            move_mouse_direction(direction=[0, -300])
            time.sleep(5)
            print('not Founded create(+) button')
            btn = match_image_box(template=btn_create, precision=0.99)
        else:
            print(btn)
            click_mouse(btn)
            time.sleep(10)
            return True
    
    return False


def do_scenario():
    """
    """
    kingdom = [600, 424] # 서버(왕국) 선택 버튼(last open)!!!
    # kingdom = [1280, 560] # 서버(왕국) 선택 버튼(4th last open)!!!
    btn_skip = [1770, 50] # SKIP 버튼
    skip = [10, 540]
    btn_tool = [94, 810]
    btn_map = [84, 994] # map, castle toggle button
    btn_build = [400, 800]
    btn_military = [88, 774]
    btn_quests = [72, 250]
    btn_go = [1510, 364] # go, claim toggle button

    btns0 = [
        kingdom, # 서버(왕국) 선택 버튼
        [1220, 768], # YES button
    ]
    click_mouse_series(btns0, interval=2, clicks=1)

    btn_china = _imgs + 'btn_civilization_china.png'
    pos_china = wait_match_image(template=btn_china, pause=3)
    print('pos_china: {}'.format(pos_china))

    if pos_china is not False:
        print('matched: {}'.format(pos_china))
        click_mouse(pos_china)
    else:
        return False

    btns1 = [
        pos_china, # 문명 선택 china
        [968, 768], # 약관 동의 accept btn
        pos_china, # 문명 선택 china
        [1624, 760], # confirm
        btn_skip,
    ]

    click_mouse_series(btns1, interval=2, clicks=1)
    time.sleep(3)

    btn_cityhall = _imgs + 'img_CityHall_01.png'
    pos_cityhall = wait_match_image(template=btn_cityhall, pause=3)
    
    if pos_cityhall is False:
        print('ROK is not loaded, YET.')
        return False
    else:
        print('ROK is loaded!!!')

    btns2 = [
        skip,
        skip,
        skip,
        skip,
        skip,
        btn_tool,
        btn_build,
        [1100, 550], # upgrage building button
        # skip,
        [988, 690], # collect button
        skip,
        skip,
        skip,
        btn_map,
        skip,
        skip,
    ]

    click_mouse_series(btns2, interval=2, clicks=1)
    time.sleep(30)

    btns2 = [
        skip,
        skip,
        btn_map,
        btn_map,
        skip,
        [780, 646], # barrack
        skip,
        [990, 860],
        skip,
        [1490, 890],
        skip,
        [778, 544], # train
        skip,
        [978, 480], # upgrade wall
        # skip,
        [960, 720],
        # skip,
        [1490, 830]
    ]

    click_mouse_series(btns2, interval=3, clicks=1)
    time.sleep(2)

    btns3 = [
        skip,
        skip,
        skip,
        btn_tool,
        btn_military,
        btn_build, # build tavern button
        [580, 333], # 
        skip,
        [670, 760], # recruit button
        skip,
        [1380, 910], # open button
        skip,
        skip,
        [292, 914], # confirm button
        skip,
        [600, 936], # confirm button2
        skip,
        [56, 60], # back button
    ]

    click_mouse_series(btns3, interval=3, clicks=1)
    time.sleep(5)

    btns4 = [
        skip,
        skip,
        skip,
        btn_map,
        btn_tool,
        [410, 740], # search button
        skip,
        skip,
        [956, 526], # barbarian
        [1382, 724], # attack
        [1516, 212], # new troops
        [298, 682], # select commandar
        [110, 282], # select commandar2
        [1390, 942], # march
    ]

    click_mouse_series(btns4, interval=3, clicks=1)
    time.sleep(40)

    btns5 = [
        skip,
        skip,
        skip,
        [868, 448], # barbarian target @@@@@
    ]
    click_mouse_series(btns5, interval=2, clicks=1)
    time.sleep(2)

    img_word =  _imgs + 'img_Scenario_SelectNewTarget.png'
    offset = [114, -128]  ## select new target (620, 540, 248, 32) / click center [858, 428]
    pos_word = wait_match_image(template=img_word, pause=3)
    if pos_word is False:
        return False
    else:
        pos_target = [pos_word[0] + offset[0], pos_word[1] + offset[1]]

    click_mouse(pos_target)
    time.sleep(2)

    btn_img =  _imgs + 'btn_Scenario_BarbarianAttack.png'
    #pos_btn = match_image_box(template=btn_img)
    click_mouse(match_image_box(template=btn_img))
    time.sleep(1)
    click_mouse([1514, 290])  # march
    time.sleep(30)

    btns6 = [
        skip,
        skip,
        skip,
        [294, 912], # confirm
        btn_map, # castle_map button
        skip,
        skip,
        btn_quests,
        btn_go,
        # skip,
        # skip,
        [1062, 766], # city hall
        [1490, 830], # upgrade city hall
        # skip,
        # skip,
        btn_quests,
        btn_go,
        # skip,
        btn_go,
    ]

    click_mouse_series(btns6, interval=3, clicks=1)
    time.sleep(5)

    btns7 = [
        skip,
        skip,
        btn_tool,
        btn_military,
        btn_build, # build scout camp
        [1280, 402], # build button
        skip,
        skip,
        [1380, 828], # scout button
        [1510, 480], # explore button
        [1210, 780], # explore2 button
        [1510, 250], # send button
        skip,
        skip,
        skip,
        btn_map,
        btn_quests,
        btn_go,
        btn_go,
        # skip,
        # skip,
        btn_tool,
        btn_military,
        btn_build, # build archery range
        [1624, 212], # build button
    ]

    click_mouse_series(btns7, interval=3, clicks=1)
    time.sleep(10)


def remove_trees():
    """
    """
    trees1 = [
        [160, 680],
        [410, 506],
        [255, 452],
        [315, 326],
        [528, 210],
        [732, 216],
        [949, 361],
        [903, 226],
        # [1057, 373],  ##
        [1070, 400],
        [1172, 468],
        [1194, 336],
        # [1324, 378],  ##
        [1332, 414],
        [1325, 383],
        [1448, 389],
        # [1688, 550], ##
        [1688, 578],
    ]

    trees2 = [
        [1718, 483],
        [1686, 419],
        [1562, 598],
        [1804, 430],
        [1444, 490],
    ]

    trees3 = [
        ([219, 927], [492, 949]),
        ([459, 840], [583, 945]),
        ([792, 879], [918, 947]),
        ([998, 724], [1126, 890]),
        ([947, 786], [1064, 950]),
    ]

    # trees2 = [
    #     [1804, 430],
    #     [1444, 490],
    #     [1562, 606],
    #     [210, 924],
    # ]

    # trees3 = [
    #     ([487, 939], [599, 947]),
    #     ([558, 822], [688, 948]),
    #     ([901, 874], [1016, 972]),
    #     ([1072, 768], [1218, 933]),
    #     ([1054, 784], [1178, 1003]),
    # ]

    for tree in trees1:
        remove_tree(tree)

    btn_map = [84, 994] # map, castle toggle button
    click_mouse(btn_map)
    time.sleep(3)
    click_mouse(btn_map)
    time.sleep(3)

    for tree in trees2:
        remove_tree(tree)

    for tree in trees3:
        remove_tree2(tree)


def remove_tree(pos=[204, 510]):
    """
    """
    #set_standard_view()
    click_mouse(pos)
    time.sleep(2)
    btn_shovel = _imgs + 'btn_RemoveBuilding_Shovel.png'
    print(btn_shovel)
    btn = match_image_box(btn_shovel)

    if btn is False:
        print('not founded!!')
        return False
    else:
        click_mouse(btn)

    click_mouse([712, 770]) # YES button
    time.sleep(3)


def remove_tree2(tree=([487, 939], [599, 947])):
    """
    """
    #set_standard_view()
    click_mouse(tree[0])
    time.sleep(2)
    click_mouse(tree[1])
    time.sleep(3)

    click_mouse([712, 770]) # YES button
    time.sleep(2)



# def do_verification_rewards():
#     if not wait_match_image(template, image):
#         return True
#     else:
#         return False


# def set_rok_ui():
#     pass

# ##@@@-------------------------------------------------------------------------
# ##@@@ Account / Character

# ## @@brief:: 
# ## @@note:: 
# def turnOnEmulator(emulator=_ENV['_EMULATOR']):
#     # 버튼
#     #_UI = emulators[emulator]['BUTTONS']

#     # For BLUESTACK
#     if emulator == 'BLUESTACK':
#         clickMouse(_UI['location']['icon_wallpaper'])
#         time.sleep(10)
#         clickMouse([1000, 500])

#     # For LDPLAYER
#     elif emulator == 'LDPLAYER':
#         # 바탕화면 더블 클릭
#         clickMouse2(_OS['ROK_WALLPAPER']['xy'])

#         ## popup 닫기 !!!!
#         ## 상단 메뉴바 아래 부분에서 '닫기' 버튼 있으면, 클릭!!!!
#         for btn in _UI['OUTER']['POPUP_CLOSES']:
#             time.sleep(1)
#             clickMouse(btn)

#         # ROK 아이콘 클릭
#         for _ in range(0, 15):
#             print('rok icon path: ' + _ENV['_IMAGES_FOLDER'] + _UI['OUTER']['WALLPAPER_ROK_MID']['fn'])
#             loaded = matchImageBox(_ENV['_IMAGES_FOLDER'] + _UI['OUTER']['WALLPAPER_ROK_MID']['fn'])
#             if loaded == False:
#                 time.sleep(10)
#             else:
#                 clickMouse(loaded)
#                 break

#         ## popup(avast) 닫기
#         clickMouse(_UI['OUTER']['POPUP_AVAST'])

#         # 최대화 버튼 클릭
#         time.sleep(2)
#         clickMouse(_UI['OUTER']['MENUBAR_MAX_MID']['xy'])

#         # 게임 화면 진입 여부 확인
#         for _ in range(0, 30):
#             loaded = matchImageBox(_ENV['_IMAGES_FOLDER'] + _UI['MAIN']['VIEWALLIANCE_MAX']['fn'])
#             if loaded == False:
#                 time.sleep(10)
#             else:
#                 print(loaded)
#                 break
        
#         ## 게임 화면 진입이 안된 경우 처리!!!
#         if loaded == False:
#             pass

#         time.sleep(2)
        
#         # 하단 메뉴 펼침
#         unfoldMenuBtn()
    
#     return 0


# ## @@brief:: 
# ## @@note:: 
# def turnOffEmulator(emulator=_ENV['_EMULATOR']):
#     clickMouse(_UI['MAIN']['MENUBAR_CLOSE_MAX']['xy'])
   
#     return 0


# ## @@brief:: 
# ## @@note:: 
# def checkEmulatorState():
#     pass


# ## @@brief:: viewMode 확인
# ## @@note:: 'CASTLE_VIEW' / 'ALLIANCE_VIEW' / 'KINGDOM_VIEW'
# def checkViewMode():
#     if matchImageBox(_ENV['_IMAGES_FOLDER'] + _UI['MAIN']['VIEWKINGDOM_MAX']['fn']):
#         return 'KINGDOM_VIEW'
#     elif matchImageBox(_ENV['_IMAGES_FOLDER'] + _UI['MAIN']['VIEWALLIANCE_MAX']['fn']):
#         return 'CASTLE_VIEW'
#     elif matchImageBox(_ENV['_IMAGES_FOLDER'] + _UI['MAIN']['VIEWCASTLE_MAX']['fn']):
#         return 'ALLIANCE_VIEW'


# ## @@brief:: viewMode 확인
# ## @@note:: 'CASTLE_VIEW' / 'ALLIANCE_VIEW' / 'KINGDOM_VIEW'
# def toggleViewMode():
#     clickMouse(_UI['MAIN']['VIEWCASTLE_MAX']['xy'])
#     return 0


# ## @@brief:: viewMode 확인@@@@@@@@@@@@@@@@@@@@@@
# ## @@note:: 'CASTLE_VIEW' / 'ALLIANCE_VIEW' / 'KINGDOM_VIEW'
# def setViewMode(viewMode='CASTLE_VIEW'):
#     if viewMode == 'KINGDOM_VIEW':
#         zoomKingdom()
    
#     if checkViewMode() == viewMode:
#         return 0

#     if checkViewMode() == 'KINGDOM_VIEW':
#         if viewMode == 'ALLIANCE_VIEW':
#             clickMouse(_UI['MAIN']['VIEWCASTLE_MAX']['xy'])
#             time.sleep(2)
#             clickMouse(_UI['MAIN']['VIEWCASTLE_MAX']['xy'])
#         elif viewMode == 'CASTLE_VIEW':
#             clickMouse(_UI['MAIN']['VIEWCASTLE_MAX']['xy'])
#     else:
#         toggleViewMode()
    
#     return 0


# ## @@brief:: 메뉴 버튼(campaign, items, alliance, commander) 펼치기
# ## @@note:: 
# def unfoldMenuBtn():
#     if not matchImageBox(_ENV['_IMAGES_FOLDER'] + _UI['MAIN']['CAMPAIGN_MAX']['fn']):
#         clickMouse(_UI['MAIN']['MENU_MAX']['xy'])



# ## @@brief:: 메뉴 버튼(campaign, items, alliance, commander) 펼치기
# ## @@note:: vector[0]: x방향, 1: _ENV(_MAX_X)//2
# def moveMapDirection(vector=[]):
#     _x = _ENV['_MAX_X']//2
#     _y = _ENV['_MAX_X']//2
#     # moveMouse(_x, _y)
#     dragInMap([vector[0]*_x, vector[1]*_y])
#     # moveMouse(vector[0]*_x, vector[1]*_y)

# ##@@@@========================================================================
# ##

# ## @@brief:: 지도를 최고로 축소시킴
# ## @@note:: 
# def zoomKingdom():
#     ## zoom mode 확인!!!
#     time.sleep(3)
#     pag.moveTo(_ENV['_MAX_X']//2, _ENV['_MAX_Y']//2, duration=0.0)
#     pag.rightClick()

#     shortcut = _UI['_SETTINGS']['_SHORTCUT']

#     for _ in range(0, shortcut['zoomth']):
#         time.sleep(0.1)
#         #설정에서 단축키(축소) 지정 확인 @@@@@@
#         pag.keyDown(shortcut['zoom_out'][0])
#         time.sleep(0.2)
#         pag.press(shortcut['zoom_out'][1])
#         #pag.hotkey(shortcut['zoom_out'][0], shortcut['zoom_out'][1])
#     pag.keyUp(shortcut['zoom_out'][0])



# def starter(delay=10):
#   print("I'm Starter, Now Start-----------------")
#   time.sleep(delay)
#   print("I'm Starter, Now End-------------------")


# def ender(delay=1):
#   print("I'm Ender, Now Start*****************")
#   time.sleep(delay)
#   print("I'm Ender, Now End*******************")


# def cb1(delay=8):
#   print("I'm cb1, Now Start+++++++++++++++")
#   time.sleep(delay)
#   print("I'm cb1, Now End+++++++++++++++++")


# def cb2(delay=6):
#   print("I'm cb2, Now Start##############")
#   time.sleep(delay)
#   print("I'm cb2, Now End################")


# def cb3(delay=4):
#   print("I'm cb3, Now Start^^^^^^^^^^^^^")
#   time.sleep(delay)
#   print("I'm cb3, Now End^^^^^^^^^^^^^^^")




# def doCallbackSeries(start, cbs, end):
#     print("I'm doCallbackSeries, Now Start===================")
#     start()
#     for cb in cbs:
#         cb()
#     end()
#     print("I'm doCallbackSeries, Now End===================")



# ##==============================
# from helpers import *

# _EMULATOR_ = 'ldplayer'
# _GIFT_MAX = 20
# _AVAST_POPUP = [1900, 900]
# _ZOOM_NO = 8
# _ZOOM_WHEEL = 100

# _SCREEN = [1920, 1080]
# _DELAY_CLICK = 2
# _CENTER = [_SCREEN[0]//2, _SCREEN[1]//2]
# _AREA_MARGIN = 50



# ## 에뮬레이터 켜기
# def turn_on(emulator=_EMULATOR_):
#     if emulator == 'bluestack':
#         double_click(emulators[emulator]['location']['icon_wallpaper'])
#         time.sleep(10)
#         click([1000, 500])
#         time.sleep(30)
#         ## full screen
#         pag.press('f11')
#         time.sleep(120)
#         pag.press('f11')
#     elif emulator == 'ldplayer':
#         double_click(emulators[emulator]['location']['icon_wallpaper'])
#         time.sleep(emulators[emulator]['delay']['loading'])
#         ## avast popup 닫기
#         click(_AVAST_POPUP)

#         click(emulators[emulator]['location']['icon_rok'])
#         time.sleep(emulators[emulator]['delay']['loading'])
#         time.sleep(emulators[emulator]['delay']['loading'])
#         click(emulators[emulator]['menubar']['max'])
#         # time.sleep(120)
#         # pag.press('f11')

#     ## 메뉴 버튼 펼치기!!! (로딩후 바로 디폴트값으로 변경!!!)
#     click(emulators[emulator]['rok_main_menu']['menus'])


# ## view mode가 map인가?
# def is_view_map():
#     pass


# ## view mode를 castle
# def toggle_view_castle():
#     if is_view_map():
#         click(emulators[emulator]['rok_main_menu']['zoom'])



# ## 도시 줌인
# def zoom_city(nth=_ZOOM_NO, emulator=_EMULATOR_):
#     ## zoom mode 확인!!!
#     time.sleep(3)
#     #toggle_view_castle()
#     ## 화면 중앙으로 마우스 포인터 이동
#     #pag.press('f11')
#     #time.sleep(1)

#     pag.moveTo(_CENTER[0], _CENTER[1], duration=0.0)
#     pag.rightClick()

#     #pag.moveTo(_CENTER[0], _CENTER[1], duration=0.0)
#     pag.keyDown('ctrl')
#     time.sleep(2)
#     # pag.mouseDown()
#     #pag.moveTo(_CENTER[0], _CENTER[1] + _ZOOM_WHEEL)
#     pag.scroll(_ZOOM_WHEEL)
#     # for s in range(100):
#     #     pag.scroll(-1)
#     #     time.sleep(0.5)
#     #pag.dragRel(0, _ZOOM_WHEEL)
#     # pag.mouseUp()
#     #pag.click()
#     #time.sleep(1)
    
#     #time.sleep(0.1)
#     #pag.scroll(_ZOOM_WHEEL)
#     time.sleep(0.1)
#     pag.keyUp('ctrl')

#     # pag.keyDown('shift')
#     # time.sleep(0.1)
#     # for _ in range(0, nth):
#     #     # 설정에서 단축키(축소) 지정 확인@@@@@@
#     #     #pag.hotkey('shift', '-')
#     #     pag.press('-')
#     #     time.sleep(3)
    
#     # pag.keyUp('shift')


# ## 도시 줌인
# def zoom_kingdom(nth=_ZOOM_NO, emulator=_EMULATOR_):
#     ## zoom mode 확인!!!
#     time.sleep(3)
#     pag.moveTo(_CENTER[0], _CENTER[1], duration=0.0)
#     pag.rightClick()

#     for _ in range(0, 300):
#         #time.sleep(2)
#         #설정에서 단축키(축소) 지정 확인@@@@@@
#         pag.hotkey('shift', '-')
#         #time.sleep(2)


# ## 좌표로 지도 이동
# def go_by_location(location=[0, 0], viewmode='kingdom'):
#     if viewmode == 'kingdom':
#         zoom_kingdom()
#         time.sleep(3)
#         input_coordinate(location)
#     elif viewmode == 'alliance':
#         zoom_kingdom()
#         time.sleep(3)
#         input_coordinate(location)
#     elif viewmode == 'castle':
#         zoom_kingdom()
#         time.sleep(3)
#         input_coordinate(location)

#     click([1284, 235])
#     click([1284, 235])
    

# ## 이동할 좌표 입력
# def input_coordinate(location=[0, 0]):
#     time.sleep(3)
#     click([662, 62], 0)
#     #확인!!! textArea 있는지
#     time.sleep(1)

#     click([902, 235], 0)
#     time.sleep(1)
#     click([100, 980], 0)
#     time.sleep(0.5)
#     #확인!!! textArea 있는지
#     pag.typewrite(str(location[0]))

#     time.sleep(2)
#     click([1116, 235], 0)
#     time.sleep(1)
#     click([1116, 235], 0)
#     time.sleep(1)

#     click([100, 980], 0)
#     time.sleep(0.5)
#     pag.typewrite(str(location[1]))
#     #pag.typewrite('345')
#     time.sleep(2)


# ## 캐릭터 로그인
# def login_character(nick, emulator=_EMULATOR_):
#   time.sleep(1)
#   click(emulators[emulator]['rok_main_menu']['profile'])
#   time.sleep(3)  
#   click(emulators[emulator]['rok_profiles']['settings'])
#   time.sleep(3) 
#   click(emulators[emulator]['rok_settings']['character_management'])
#   time.sleep(3)
#   click(emulators[emulator]['rok_character_management_icons'][get_character_index(nick)])
#   time.sleep(3)
#   click(emulators[emulator]['rok_character_login_icons']['yes'])
#   time.sleep(time.sleep(emulators[emulator]['delay']['loading']))

#   ## 메뉴 버튼 펼치기!!! (로딩후 바로 디폴트값으로 변경!!!)
#   click(emulators[emulator]['rok_main_menu']['menus'])

#   return 0


# ## 빌딩 클릭
# def click_building(nick='천년왕국', building='farm'):
#     zoom_city()
#     time.sleep(2)
#     #building_index = get_building_index(nick)
#     click(get_building_location(nick, building))
#     time.sleep(2)


# ## 도시 자원 채취
# def collect_city_resources(nick='천년왕국'):
#     click_building(nick, 'farm')

#     #buildings = ['farm', 'lumber_mill', 'quarry', 'goldmine']
#     buildings = ['lumber_mill', 'quarry', 'goldmine']
#     for building in buildings:
#         click(get_building_location(nick, building))
#         time.sleep(2)




# def send_troop(troop='new', location=''):
#     pass



# def gather_resource(resource='food', troop='new', levelup=0, emulator=_EMULATOR_):

#     if resource == 'food':
#         place = 'cropland'
#     elif resource == 'wood':
#         place = 'logging_camp'
#     elif resource == 'stone':
#         place = 'stone_deposit'
#     elif resource == 'gold':
#         place = 'gold_deposit'
#     else:
#         place = resource

#     time.sleep(1)
#     ## zoom mode 확인: default = castle  *map
#     click(emulators[emulator]['rok_main_menu']['zoom'])
#     time.sleep(3)
#     click(emulators[emulator]['rok_main_menu']['search'])
#     time.sleep(3)
#     click(emulators[emulator]['rok_search'][place]['icon'])
#     time.sleep(3)


#     ## 자원지가 존재하는지 확인!!! opencv ()

#     ## level up(plus)
#     for _ in range(0, levelup):
#         click(emulators[emulator]['rok_search'][place]['plus'])
#         time.sleep(1)

#     click(emulators[emulator]['rok_search'][place]['search'])


#     ## zoom mode : map mode -> castle mode
#     click(emulators[emulator]['rok_main_menu']['zoom'])
#     time.sleep(3)
#     click(_CENTER)
#     time.sleep(3)

#     click(emulators[emulator]['rok_search']['gather'])
#     time.sleep(3)

#     if troop == 'old':
#         click(emulators[emulator]['troop_queues'][0]['march'])
#     elif troop == 'new':  ## 부대 지정!!!!!
#         click(emulators[emulator]['new_troop']['icon'])
#         time.sleep(3)
#         #click(emulators[emulator]['new_troop']['1'])
#         click(emulators[emulator]['new_troop']['minus'])
#         time.sleep(3)
#         click(emulators[emulator]['new_troop']['march'])


# def defeat_barbarian_troops():
#     pass



# ## 연맹 선물 받기
# def receive_alliance_gifts(emulator=_EMULATOR_):
#     ## 메뉴 버튼 펼치기!!! (로딩후 바로 디폴트값으로 변경!!!)
#     # click(emulators[emulator]['rok_main_menu']['menus'])
#     click(emulators[emulator]['alliance']['icon'])
#     time.sleep(3)
#     click(emulators[emulator]['alliance']['gifts'])
#     time.sleep(3)

#     # 희귀 선물
#     click(emulators[emulator]['alliance_gifts']['tab_rare'])
#     time.sleep(2)

#     for _ in range(0, _GIFT_MAX):
#         click(emulators[emulator]['alliance_gifts']['bottom_claim'])
#         time.sleep(1)

#     loc = emulators[emulator]['alliance_gifts']['top_claim']
#     for i in range(0, 4):
#         click([loc[0], loc[1] + 140*i])
#         time.sleep(1)


#     # 일반 선물
#     click(emulators[emulator]['alliance_gifts']['tab_normal'])
#     time.sleep(2)
#     click(emulators[emulator]['alliance_gifts']['claim_all'])
#     time.sleep(2)
#     click(emulators[emulator]['alliance_gifts']['confirm'])
#     time.sleep(2)

#     click(emulators[emulator]['alliance_gifts']['close'])
#     time.sleep(2)
#     click(emulators[emulator]['alliance']['close'])


# ### 계정 생성
# def create_new_character(server=''):
#     pass


# ### 안개 걷어내기
# def recover_fog():
#     pass


# ### 신비의 동굴 탐색
# def explore_mysterious_cave(coord=[0,0]):
#     click(coord)
#     time.sleep(1)
#     click(_CENTER)
#     coord1 = compare_image_area('images/btn_mysteriousCave_investigate_1186_660_260_82.png')
#     if coord1:
#         click(coord1)
#         time.sleep(2)
#         coord2 = compare_image_area('images/btn_mysteriousCave_send_1326_224_252_82.png')
#         if coord2:
#             click(coord2)
#     time.sleep(2)



# ### 부족 선물 얻기
# def receive_tribal_village_gift(coord=[0,0]):
#     click(coord)
#     time.sleep(1)
#     click(_CENTER)
#     time.sleep(0.1)
#     pag.click(_CENTER[0], _CENTER[1] - 200)
#     time.sleep(1)



# ### 탐사 보고로 부터 성지, 관문 등 안개 해제, 부족 선물 얻기, 신비의 동굴 탐색(!!!)
# def recover_special_site_from_mail():
#     pass


# ## 자기 도시로 돌아가기
# def go_home():
#     click([140, 940], 1)
#     click([140, 940], 1)


# ### 작업 시간 지정!!!




# ###
# # verificatoin



# ### 동시 접속 감지 및 해결!!!



# ####################################
# if __name__ == "__main__":
#     #turn_on(_EMULATOR_)
#     #zoom_city()
#     #zoom_kingdom()
#     #go_by_location([160, 120])

#     # time.sleep(3)
#     # click([100, 980])
#     # time.sleep(2)
#     # #확인!!! textArea 있는지
#     # #pag.press(str(location[0]))
#     # # pag.press('backspace')
#     # # time.sleep(2)
#     # # pag.press('backspace')
#     # pag.typewrite('12')
#     # time.sleep(2)

#     #login_character('천년왕국', _EMULATOR_)
#     #gather_resource('wood', 'old')
#     #gather_resource('wood', 'new')
#     #receive_alliance_gifts()
#     #click_building('천년왕국', 'alliance_center')
#     #collect_city_resources('천년왕국')


#     for i in range(0, 2):
#         go_by_location([160*(i+1), 120])
#         for _ in range(0, 15):
#             #go_home()
#             # time.sleep(1)
#             zoom_kingdom()
#             time.sleep(3)
#             #coord = compare_image_area('images/_caveTest.png')
#             coord = compare_image_area('images/_villageTest1.png')
#             #coord = compare_image_area('images/_mask_mysteriousCaveUninvestigated_.png')
#             time.sleep(2)
#             if coord:
#                 receive_tribal_village_gift(coord)
#                 # explore_mysterious_cave(coord)
#                 # time.sleep(2)
#                 # #go_home()
#                 # time.sleep(1)



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
    time.sleep(5)
    # for _ in range(0, 20):
    #   pag.keyDown('down')
    #   time.sleep(0.1)
    

    #moveMapDirection([1, 0])

    #doCallbackSeries(starter, [cb1, cb2, cb3], ender)

    if create_new_character():
        time.sleep(10)
        do_scenario()

    # do_scenario()
    # remove_trees()
    #remove_tree2(([558, 822], [688, 948]))
    # move_mouse_direction(direction=[0, -100])