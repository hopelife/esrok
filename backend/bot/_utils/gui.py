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

##@@@-------------------------------------------------------------------------
##@@@ Installed(conda/pip) Libraries
import pyautogui as pag
import pyperclip

##@@@-------------------------------------------------------------------------
##@@@ User Libraries


##@@@@========================================================================
##@@@@ Constants


##@@@-------------------------------------------------------------------------
##@@@ External(.json/.py)
sys.path.append(os.path.join(os.path.dirname(sys.path[0]), '_config'))
from _settings import _ENV, _PATH

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


def get_screen_center():
    """
    Brief: get screen center
    """
    return [_ENV['_MAX_X']//2,_ENV['_MAX_Y']//2]


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

##@@@-------------------------------------------------------------------------
##@@@ GUI Functions(pyautogui:: mouse/keyboard)

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


def go_by_coordinate(location=[0,0]):
    positions = [
        [670, 38],  ## 좌표로 찾기 버튼
        [686, 216],  ## Server 필드
        [924, 216],  ## X 좌표 필드
        [1168, 216],  ## Y 좌표 필드
        [50, 988],  ## 텍스트 입력 필드
        [1330, 214]  ## 좌표로 가기 버튼
    ]
    click_mouse_series(positions, 2)
    pass


##@@@@========================================================================
##@@@@ Execute Test
if __name__ == "__main__":
    time.sleep(5)
    go_by_coordinate()
    #get_clipboard()
    #drag_in_map([_ENV['_MAX_X']//2, 0])
    # print(_ENV['_MAX_X']//2)
    # pag.moveTo(_ENV['_MAX_X']//2, _ENV['_MAX_Y']//2, duration=0.0)
    # pag.dragRel(500, 400, duration=0.2, button='left')
    # pass
