# -*- coding:utf-8 -*-
"""
Brief: Set Of Game Bot Basic Module Functions

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
        - GUI Functions

    - Main Function

Usage: import _basics
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

##@@@-------------------------------------------------------------------------
##@@@ Installed(conda/pip) Libraries
import pyautogui as pag
import pyperclip

##@@@-------------------------------------------------------------------------
##@@@ User Libraries
import image_recognition as _ir


##@@@@========================================================================
##@@@@ Constants


##@@@-------------------------------------------------------------------------
##@@@ External(.json/.py)
sys.path.append(os.path.join(os.path.dirname(sys.path[0]), '_config'))
from _settings import _ENV, _PATH, _MAP
from emulators import KEY_MAP as ui_key
from emulators import LOCATION_ROK_FULL as ui_xy
from emulators import IMAGE_ROK_FULL as ui_img

##@@@-------------------------------------------------------------------------
##@@@ internal


##@@@@========================================================================
##@@@@ Functions

##@@@-------------------------------------------------------------------------
##@@@ Basic Functions

## @@@@@@
# def do_infinite_loop(callback, hotkey=''):
#     while True:
#         callback()
#         print("All done!")

#     if cv2.waitKey(0)
#         sys.exit()


def get_clipboard(position=[1002, 346]):
    click_mouse(position)
    print(pyperclip.paste())


def delay(interval=_ENV['_CLICK_INTERVAL'], rand=False):
    """
    Brief: delay intervals(sec)
    Args:
        interval (int): delay interval[sec].
        rand (boolean): generate random time
    Returns:
    Note:
        import time
    """
    if rand == True:
        time.sleep(random.uniform(interval + 0.0101, interval+ 0.0299))
    else:
        time.sleep(interval)
    return 0


def get_screen_max():
    pass


def get_screen_center():
    pass


def get_window_max():
    pass


def get_window_center():
    pass


def set_perspective_matrix():
    pass


def compute_pixel_coord_ratio():
    pass


def compute_coord_unit_size():
    pass


def track_mouse():
    """
    Brief: Mouse Tracker for Unit Test@@@@
    Args:

    """
    pass


def drag_by_coord():
    """
    Brief: possible to move out of screen
    Args:

    """
    pass


def drag_by_object():
    pass


def move_by_object():
    pass


def move_direction(start=[0,0], callback=None, direction=[1,0]):
    pass


def move_rotation(start=[0,0], step=1, count=1, callback=None, rotation='clockwise', angle=1):
    """
    Brief: 
    Args:
        step (int): size of coordinate when troops rotates
        count (int): 
        angle (int): 1 -> rotate 90 degree, 2 -> rotate 180 degree, 4 -> rotate 360 degree
    """
    pass

# def get_screen_center():
#     """
#     Brief: get screen center
#     """
#     return [_ENV['_MAX_X']//2,_ENV['_MAX_Y']//2]


def get_box_from_wh(wh):
    """
    Brief: get box from wh
        - box coordinate([x1:left, y1:top, x2:right, y2:bottom])
        - wh coordinate([x1, y1, w, h])
    Args:
        box (list): box coordinate
    Returns:
        wh (list): wh coordinate([x1, y1, w, h])
    """
    return [wh[0], wh[1], wh[0] + wh[2], wh[1] + wh[3]]


def get_wh_from_box(box):
    """
    Brief: get wh coordinate([x1, y1, w, h]) from box coordinate([x1:left, y1:top, x2:right, y2:bottom])
    Args:
        wh (list): wh coordinate([x1, y1, w, h])
    Returns:
        box (list): box coordinate
    """
    return [box[0], box[1], box[2] - box[0], box[3] - box[1]]



def get_center_from_box(box):
    """
    Brief: get box from wh
        - box coordinate([x1:left, y1:top, x2:right, y2:bottom])
        - wh coordinate([x1, y1, w, h])
    Args:
        box (list): box coordinate
    Returns:
        wh (list): wh coordinate([x1, y1, w, h])
    """
    return [(box[0] + box[2])//2, (box[1] + box[3])//2]

##@@@-------------------------------------------------------------------------
##@@@ simple GUI Functions(pyautogui:: mouse/keyboard) 

def click_mouse_series(positions, interval=_ENV['_CLICK_INTERVAL'], clicks=1):
    """
    Brief: click Mouse Series(마우스 연속 클릭)
    Args:
        positions (list): click positions
        interval (int): interval time[sec] for mouse click
        clicks (int): number of clicks
    """
    for position in positions:
        for _ in range(0, clicks):
            click_mouse(position)
            time.sleep(interval)


def click_mouse(position=[0, 0], button='LEFT', duration=_ENV['_MOUSE_DURATION']):
    """
    Brief: click Mouse(마우스 클릭)
    Args:
        position (list): click position
        button (str): mouse button of click
        duration (int):
    """
    pag.moveTo(position[0], position[1], duration)
    time.sleep(random.uniform(0.0101, 0.0299))
    pag.mouseDown()
    time.sleep(random.uniform(0.0101, 0.0299))
    pag.mouseUp()


def click_mouse2(position=[0, 0], button='LEFT', duration=_ENV['_MOUSE_DURATION']):
    """
    Brief: double click Mouse(마우스 더블 클릭)
    Args:
        position (list): click position
        button (str): mouse button of click
        duration (int):
    """
    pag.moveTo(position[0], position[1], duration)
    pag.mouseDown()
    time.sleep(random.uniform(0.0101, 0.0299))
    pag.mouseUp()
    pag.click(clicks=2)


def scrollMouse():
    """
    Brief: scrollMouse(마우스 스크롤)
    Args:
    """
    pass


def press_keys():
    """
    Brief: pressKeys
    Args:
    """
    pass


def press_hotkey():
    """
    Brief: pressHotKey
    Args:
    """
    pass

def down_mouse(callback, position=[0, 0], duration=1):
    """
    Brief: down Mouse(마우스 다운 - 액션 - 업)
    Args:
        callback (func): callback function
        button (str): mouse button of click
        duration (int):
    """
    pag.moveTo(position[0], position[1])
    pag.mouseDown()
    time.sleep(duration)
    callback()
    pag.mouseUp()

##@@@-------------------------------------------------------------------------
##@@@ complex GUI Functions(pyautogui:: mouse/keyboard)

def get_image_path(name, category='_UIS'):
    return _PATH[category] + ui_img[name] + _ENV['_IMG_EXT']


def get_viewmode():
    cityview = _ir.get_center_match_image(get_image_path('btn_GoWorldView'), precision=0.9)
    if cityview:
        return 'CITY_VIEW'
    else:
        return 'WORLD_VIEW'


def set_viewmode(mode='CITY_VIEW'):
    if get_viewmode() != mode:
        click_mouse(ui_xy['btn_GoWorldView'])


def zoom_out(nth=_ENV['_ZOOM_MAX']):
    pag.moveTo(_ENV['_MAX_X']//2, _ENV['_MAX_Y']//2)
    keys = ui_key[_ENV['_OS']]['ZOOM_OUT']
    for _ in range(0, nth):
        for key in keys:
            pag.keyDown(key)
            time.sleep(0.2)
        for key in keys:
            pag.keyUp(key)
            time.sleep(0.01)


def drag_in_map(relPoint=[0, 0], zeroPoint=[_ENV['_MAX_X']//2, _ENV['_MAX_Y']//2], viewMode='_CASTLE', duration=_ENV['_MOUSE_DURATION']):
    """
    Brief: dragInMap(게임 내에서 마우스 드래그)
    Args:
        relPoint (list): target point(relative)
        zeroPoint (list): starting point(relative)
        viewMode (str): _CASTLE / _ALLIANCE / _KINGDOM
        duration (int):
    """
    pag.moveTo(zeroPoint[0], zeroPoint[1], duration=0.0)
    pag.dragRel(relPoint[0], relPoint[1], duration=0.2, button='left')



def get_coordinate():
    """
    Brief: 지도에서 x, y 좌표를 입력하여 이동
    Args:
        location (list): 좌표
        viewmode (str): CITY_VIEW / WORLD_VIEW(min -> GLOBE)
    """
    if get_viewmode() is 'CITY_VIEW':
        set_viewmode('WORLD_VIEW')

    t = _ir.do_ocr([400, 16, 642, 46], 'eng', reverse=True)  # 전체
    s = _ir.do_ocr([418, 16, 484, 46], 'digits', reverse=True)  # server
    x = _ir.do_ocr([510, 16, 562, 46], 'digits', reverse=True)  # x
    y = _ir.do_ocr([588, 16, 640, 46], 'digits', reverse=True)  # y
    print('t: {}, s: {}, x: {}, y: {}'.format(t, s, x, y))

    return t


def find_verification_verify():
    # return _ir.match_image_box(get_image_path('btn_VerificationVerify', '_UIS'), precision=0.9)
    return _ir.match_image_box(get_image_path('btn_VerificationVerify', '_UIS'), [830, 470, 1738, 648], precision=0.9)


def do_verification_reward(precision=0.4):
    template = [946, 220, 1180, 272]
    image = [730, 280, 1190, 740]
    img_btn_OK = [1024, 754, 1190, 812]

    center_btn_OK = [1100, 786]
    center_btn_close = [756, 782]

    boxes = _ir.extract_templates(template)
    print('boxes at gui.py: {}'.format(boxes))

    if len(boxes) > 4 or boxes is False:
        print('too many templates')
        click_mouse(center_btn_close)
        return False

    centers = []
    for box in boxes:
        center = _ir.feature_image_box(box, image, precision, inverse=True)
        if center is False:
            print('no match image')
            click_mouse(center_btn_close)
            return False
        centers.append(center)
    
    print(centers)
    for center in centers:
        click_mouse(center)
        delay(1)

    click_mouse(center_btn_OK)

    return centers


def do_verification_rewards(precision=0.4, attempts=6):
    btn_verify = find_verification_verify()
    if btn_verify is False:
        return 0
    else:
        click_mouse(btn_verify)
        delay(5)

    center_btn_OK = [1104, 784]
    centers = do_verification_reward(precision)

    tries = 0

    if centers is False:
        tries += 1
        # print('no match image!')
        # if tries > attempts:
        #     do_verification_rewards()  ## 재시도@@@@@@@@@@

        # click_mouse([800, 120])  ## 인증 팝업 바깥쪽을 누름@@@@@
        delay(5)
        do_verification_rewards(precision, attempts)

    elif len(centers) > 4:
        tries += 1
        # print('too many templates!')
        # if tries > attempts:
        #     do_verification_rewards()  ## 재시도@@@@@@@@@@
        # click_mouse([800, 120])  ## 인증 팝업 바깥쪽을 누름@@@@@
        delay(5)
        do_verification_rewards(precision)

    delay(5)

    if find_verification_verify() is False:
        print(centers)
        return centers
    else:
        do_verification_rewards(precision, attempts)


def go_by_coordinate(location=[0,0]):
    """
    Brief: 지도에서 x, y 좌표를 입력하여 이동
    Args:
        location (list): 좌표
        viewmode (str): CITY_VIEW / WORLD_VIEW(min -> GLOBE)
    """
    #set_viewmode(viewmode)

    click_mouse(ui_xy['btn_LocationSearch'])  ## 좌표로 찾기 버튼
    click_mouse(ui_xy['btn_Pop_LocationSearch_X'])  ## X 좌표 필드
    click_mouse(ui_xy['npt_Pop_LocationSearch_Field'])  ## 텍스트 입력 필드
    pag.typewrite(str(location[0]))

    delay(1)

    click_mouse(ui_xy['btn_Pop_LocationSearch_Y'])  ## Y 좌표 필드
    click_mouse(ui_xy['btn_Pop_LocationSearch_Y'])  ## Y 좌표 필드
    click_mouse(ui_xy['npt_Pop_LocationSearch_Field'])  ## 텍스트 입력 필드
    pag.typewrite(str(location[1]))
    delay(1)

    click_mouse2(ui_xy['btn_Pop_LocationSearch_Go'])



def save_whole_maps(searchMode='Explore', zoom=320, max_size=_MAP['ONE_MAX']):
    """
    Brief: 지도 스크린샷 저장
    Args:
        searchMode (str): Alliance, Explore, Resources, Markers, Barbarian Stronghold
    """
    #set_fullscreen()
    #get_server_num()
    #set_searchmode()
    # _MAP : {
    #     'WHOLE': [1200, 1200],
    #     'ONE_MIN': [8, 6],
    #     'ONE_MAX': [320, 240],
    #     'EDGE': [210, 210, 1160, 940]
    # }
    server = '1621'

    ## edge 고려 안함
    # w = shotsize[0]
    # h = shotsize[1]
    # start = [w//2, h//2]
    box = _MAP['EDGE']
    ratio_x = _ENV['_MAX_X'] / _MAP['ONE_MAX'][0]
    ratio_y = _ENV['_MAX_Y'] / _MAP['ONE_MAX'][1]
    x1_ = math.floor(_MAP['EDGE'][0]/ratio_x)
    y1_ = math.floor(_MAP['EDGE'][1]/ratio_y)
    x2_ = math.floor((_ENV['_MAX_X'] - _MAP['EDGE'][2])/ratio_x)
    y2_ = math.floor((_ENV['_MAX_Y'] - _MAP['EDGE'][3])/ratio_y)
    w = _MAP['ONE_MAX'][0] - x2_ + x1_
    h = _MAP['ONE_MAX'][1] - y1_ + y2_
    # w = _MAP['ONE_MAX'][0] - x1_ - x2_
    # h = _MAP['ONE_MAX'][1] - y1_ - y2_
    start = [_MAP['ONE_MAX'][0]//2 - x1_, _MAP['ONE_MAX'][1]//2 - y2_]

    # w = (_MAP['EDGE'][2] - _MAP['EDGE'][0]) / ratio_x
    # h = (_MAP['EDGE'][3] - _MAP['EDGE'][1]) / ratio_y

    x_no = _MAP['WHOLE'][0]//w - 1
    y_no = _MAP['WHOLE'][1]//h - 3

    print('ratio_x: {}, ratio_y: {}'.format(ratio_x, ratio_y))
    print('w: {}, h: {}, x1_: {}, _x2: {}, _y1: {}, y2_: {}, start: {}'.format(w, h, x1_, x2_, y1_, y2_, start))
    print('x_no: {}, y_no: {}'.format(x_no, y_no))

    for j in range(0, y_no):
        for i in range(0, x_no):
            location = [start[0] + i*w, start[1] + j*h]
            #print(location)
            save_screenshot_map(location, searchMode, box, server)
            delay(1)

    return 0


def save_screenshot_map(location=[0, 0], searchMode='Explore', box=[], server=''):
    go_by_coordinate(location)
    #set_searchMode()
    #set_zoomMode(zoom)
    path = _PATH['_MAPS'] + server + '_' + searchMode + '_' + str(location[0]) + '_' + str(location[1]) + _ENV['_IMG_EXT']
    delay(3)
    _ir.save_screenshot(box, path)



def receive_village_gifts(location=[_MAP['ONE_MAX'][0]//2, _MAP['ONE_MAX'][1]//2], max_i=50):
    zoom_out()
    #go_by_coordinate(location)
    template = '../images/uis/img_ExploreVillage.png'  ##@@@@@@@@@@@@
    #coord = get_coordinate()

    for _ in range(0, max_i):
        center = _ir.wait_match_image(template, _MAP['EDGE'], precision=0.978, duration=15)
        #center = _ir.match_image_box(template, _MAP['EDGE'], precision=0.978)
        
        #if not center or coord == get_coordinate():

        # if not center:
        #     #coord = get_coordinate()
        #     drag_in_map([-100, 0])
        #     #receive_village_gifts()
        #     continue

        click_mouse(center)
        print(center)
        delay(1)
        click_mouse2([_ENV['_MAX_X']//2, _ENV['_MAX_Y']//2])
        delay(0.1)
        click_mouse([_ENV['_MAX_X']//2 - 200, _ENV['_MAX_Y']//2])
        delay(0.1)
        zoom_out()
        delay(0.01)



def explore_caves():
    pass


##@@@@========================================================================
##@@@@ Execute Test
if __name__ == "__main__":
    delay(5)
    #go_by_coordinate([500, 500])
    #get_clipboard()
    #drag_in_map([-_ENV['_MAX_X']//2, _ENV['_MAX_Y']//2])
    #drag_in_map([_ENV['_MAX_X']//2, 0])
    # print(_ENV['_MAX_X']//2)
    # pag.moveTo(_ENV['_MAX_X']//2, _ENV['_MAX_Y']//2, duration=0.0)
    # pag.dragRel(500, 400, duration=0.2, button='left')
    # pass
    #get_image_path('btn_GoWorldView')
    #print(get_viewmode())
    #zoom_out()
    #save_screenshot_map()
    #save_whole_maps()
    #print(_ENV['_MAX_X'] / _MAP['ONE_MAX'][0])
    #print(_ENV['_MAX_Y'] / _MAP['ONE_MAX'][1])
    #'EDGE': [210, 150, 1610, 940]
    #go_by_coordinate([125,89])
    # delay(3)
    # pag.moveTo(_MAP['EDGE'][2], _ENV['_MAX_Y']//2)
    # delay(0.1)
    # pag.mouseDown()
    # delay(0.3)
    # pag.moveTo(_MAP['EDGE'][0], _ENV['_MAX_Y']//2, duration=4.5)
    # delay(0.3)
    # pag.mouseUp()
    #drag_in_map([_ENV['_MAX_X']//2, 0])
    
    
    #template = '../images/uis/img_ExploreVillage.png'
    #image = '../images/maps/1621_Explore_125_89_.png'
    #mask = '../images/uis/mask_ExploreVillage.png'
    #template = '../images/uis/img_ExploreCave.png'
    # image = '../images/maps/1621_Explore_125_89.png'
    # mask = '../images/uis/mask_ExploreCave.png'
    # template = '../images/target.png'
    # image = '../images/image.png'
    # mask = '../images/mask.png'
    #centers = _ir.match_image_box(template, image, mask, precision=0.9983, show=True, multi=1)
    #centers = _ir.match_image_box(template, image, precision=0.99, show=True, multi=1)
    #centers = _ir.match_image_box(template, image, mask, precision=0.9983, show=True, multi=1)
    #centers = _ir.match_image_box(template, image, precision=0.998, show=True, multi=1)

    # for _ in range(0, 5):
    #     center = _ir.match_image_box(template, precision=0.997)
    #     delay(1)
    #     click_mouse(center)
    #     print(center)
    #     delay(5)
    #     click_mouse([-_ENV['_MAX_X']//2, _ENV['_MAX_Y']//2])
    #     delay(1)
    #     click_mouse([-_ENV['_MAX_X']//2 - 200, _ENV['_MAX_Y']//2])
    #     for _ in range(0, 40):
    #         pag.hotkey('ctrl', 'down')
    #         delay(0.1)
    #     delay(3)

    #centers = _ir.match_image_box(template, _MAP['EDGE'], precision=0.97, show=True, multi=1)
    # for _ in range(0, 100):
    #     center = _ir.match_image_box(template, _MAP['EDGE'], precision=0.97)
    #     if not center:
    #         continue 
    #     click_mouse(center)
    #     print(center)
    #     delay(3)
    #     click_mouse2([_ENV['_MAX_X']//2, _ENV['_MAX_Y']//2])
    #     delay(1)
    #     click_mouse([_ENV['_MAX_X']//2 - 200, _ENV['_MAX_Y']//2])
    #     delay(0.1)
    #     zoom_out()
    #     delay(0.01)

    # click_mouse(find_verification_verify())
    # delay(7)
    #do_verification_reward(0.7)
    #do_verification_rewards(0.7)
    receive_village_gifts([924, 212])
    #get_coordinate()