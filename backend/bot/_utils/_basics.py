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
        - Image Recognition/OCR Functions
        - GUI Functions
        - Google Drive(gspread)

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
import re
import json
from datetime import date, timedelta, datetime

##@@@-------------------------------------------------------------------------
##@@@ Installed(conda/pip) Libraries
import pyperclip
import numpy as np
import cv2
import pytesseract
import matplotlib.image as mpimg
import matplotlib.pyplot as plt

import pyautogui as pag

import gspread  ## google drive gspread
from oauth2client.service_account import ServiceAccountCredentials  ## google drive gspread

from pynput.keyboard import Listener, Key

##@@@-------------------------------------------------------------------------
##@@@ User Libraries

##@@@@========================================================================
##@@@@ Constants


##@@@-------------------------------------------------------------------------
##@@@ External(.json/.py)
# _uis = file_to_json('../_config/uis.json', encoding='UTF-8')
# _vals = file_to_json('../_config/ui_boxes.json', encoding='UTF-8')

with open('../_config/uis.json', encoding='UTF-8') as f:
    _uis = json.load(f)
with open('../_config/ui_boxes.json', encoding='UTF-8') as f:
    _vals = json.load(f)

sys.path.append(os.path.join(os.path.dirname(sys.path[0]), '_config'))
from _settings import _ENV, _PATH, _MAP, _TESSERACT, _GOOGLE
from emulators import KEY_MAP as ui_key
from emulators import OBJECTS as ui_obj
from emulators import LOCATION_ROK_FULL as ui_xy
from emulators import IMAGE_ROK_FULL as ui_img

_imgs = _PATH['_UIS']
_shots = _PATH['SCREENSHOT']


##@@@-------------------------------------------------------------------------
##@@@ internal
## OCR TESSERACT(OSX)
# pytesseract.pytesseract.tesseract_cmd = '/usr/local/Cellar/tesseract/4.1.1/bin/tesseract'
# tessdata_dir_config = '--tessdata-dir "/usr/local/Cellar/tesseract-lang/4.0.0/share/tessdata/"'
pytesseract.pytesseract.tesseract_cmd = _TESSERACT['OSX']['EXE']
tessdata_dir_config = _TESSERACT['OSX']['DATA']

## Google Drive Spreadsheet
credentials = ServiceAccountCredentials.from_json_keyfile_name(_GOOGLE['JSON'], _GOOGLE['SCOPE'])
gc = gspread.authorize(credentials)

# 스프레스시트 문서 가져오기 
_FILE = gc.open_by_url(_GOOGLE['URLS']['TEST'])
_LOGS = gc.open_by_url(_GOOGLE['URLS']['LOGS'])

# 시트 선택하기
_SHEET = 'crop'
_SHEET = 'test'
_SHEET_LOGS = 'logs'

##@@@@========================================================================
##@@@@ Functions

##@@@-------------------------------------------------------------------------
##@@@ Basic Functions

##@@-------------------------------------------------------------------------
##@@ Data Management(File/Json/list/dict/Clipboard/Time)

def json_to_file(data, path, encoding='UTF-8'):
    """
    Brief: convert dictionary(json) to file
    Args:
        data (json): 
        path (str): file path included name
        encoding (str): encoding encoding(default: UTF-8)
    Returns:
    """
    with open(path, 'w', encoding=encoding) as file:
        file.write(json.dumps(data, indent=2, ensure_ascii=False, default=str))


def file_to_json(path, encoding='UTF-8'):
    """
    Brief: convert file to json
    Args:
        path (str): file path included name
        encoding (str): encoding encoding(default: UTF-8)
    Returns:
    """
    with open(path, encoding=encoding) as f:
        return json.load(f)


def write_file(path, data):
    """
    Brief: create a new file & write file
    Args:
        path (str): file path included name
        data (str): 
    Returns:
    """
    with open(path, 'w') as f:
        f.write(data)


def rename_all(path, callback):
    """
    Brief: rename all files in path
    Args:
        path (str): file path(directory)
        callback (func): 
    Usage:
      path = 'D:/moon/dev/projects/rok/_bot/done/'
      rename_all(path, lambda filename : re.sub(r'\D', '', filename) + '.png')
    """
    for filename in os.listdir(path):
        os.rename(path + filename, path + callback(filename))


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


def click_copy(position=[1002, 346]):
    """
    Brief: create a new file & write file
    Args:
        position (tuple): file path included name
        data (str): 
    Returns:
    """
    click_mouse(position)
    return pyperclip.paste()


## @@@@@@
# def do_infinite_loop(callback, hotkey=''):
#     while True:
#         callback()
#         print("All done!")

#     if cv2.waitKey(0)
#         sys.exit()


# def time.sleep(interval=_ENV['CLICK_INTERVAL'], rand=False):
#     """
#     Brief: delay intervals(sec)
#     Args:
#         interval (int): delay interval[sec].
#         rand (boolean): generate random time
#     Returns:
#     Note:
#         import time
#     """
#     if rand == True:
#         time.sleep(random.uniform(interval + 0.0101, interval+ 0.0299))
#     else:
#         time.sleep(interval)
#     return 0

def insert_coords_to_file(keys={'insert':Key.insert, 'enter':Key.enter, 'esc':Key.esc}, path='../_config/tests_160_100.txt', coords=[]):
    """
    Brief: 화면 좌표 저장('insert'키: )
    Args:
        keys : 자판 기능 설정('insert': 화면 좌표 입력 추가, 'enter': 입력 종료)
        path (str): 저장 파일 경로.이름
        coords (list): 좌표 저장 배열
    Returns:
        coords (list): 좌표 저장 배열
    Note:
        from pynput.keyboard import Listener, Key
    """

    def handleRelease(key):
        # print( 'Released: {}'.format(key) )

        if key == keys['insert']:
            x, y = pag.position()
            coords.append([x, y])
            return True
        elif key == keys['enter']:
            with open(path, 'w') as f:
                f.write(str(coords))
            return False
        else:
            return False

    with Listener(on_release=handleRelease) as listener:
        listener.join()

    return coords


##@@@-------------------------------------------------------------------------
##@@@ Datetime : default format['%Y%m%d%H%M']

##@@ brief:: 
##@@ note:: bgn=start time, gap=int, unit=[sec]) / time formate '%Y%m%d%H%M'
def add_datetime(bgn='', gap=300, f='%Y%m%d%H%M'):
    base = datetime.strptime(bgn, f) if type(bgn) is str else bgn
    return base + timedelta(seconds=gap)


def add_timedelta_to_now(td, f='%Y-%m-%d %H:%M:%S'):
    return (datetime.utcnow() + datetime_to_timedelta(time_str=td)).strftime(f)


##@@ brief:: 
##@@ note:: 
def gap_datetime(end='', bgn='', f='%Y%m%d%H%M'):
    _bgn = datetime.strptime(bgn, f) if type(bgn) is str else bgn
    _end = datetime.strptime(end, f) if type(end) is str else end
    return int((_end - _bgn).total_seconds())


def convert_time_to_sec(t='', f='%H:%M:%S'):
    base = datetime.strptime(bgn, f) if type(bgn) is str else bgn
    return base + timedelta(seconds=gap)


def datetime_to_timedelta(time_str='5d 14:22:33', f='%H:%M:%S'):
    time_arr = time_str.split('d ')

    if len(time_arr) > 1:
        time_arr2 = time_arr[1].split(':')
        if len(time_arr2) > 2:
            td = timedelta(days=int(time_arr[0]), hours=int(time_arr2[0]), minutes=int(time_arr2[1]), seconds=int(time_arr2[2]))
        elif len(time_arr2) > 1:
            td = timedelta(days=int(time_arr[0]), minutes=int(time_arr2[0]), seconds=int(time_arr2[1]))
    else:
        time_arr2 = time_str.split(':')
        if len(time_arr2) > 2:
            td = timedelta(hours=int(time_arr2[0]), minutes=int(time_arr2[1]), seconds=int(time_arr2[2]))
        elif len(time_arr2) > 1:
            td = timedelta(minutes=int(time_arr2[0]), seconds=int(time_arr2[1]))

    return td


# nowDatetime = now.strftime('%Y-%m-%d %H:%M:%S')
# print(nowDatetime)  # 2015-04-19 12:11:32
# datetime.utcnow()


##@@ brief:: 
##@@ note:: string: default format ['%Y%m%d%H%M'] -> datetime
def string_to_time(s, f='%Y%m%d%H%M'):
    return datetime.strptime(s, f)


##@@@-------------------------------------------------------------------------
##@@@ Image Recognition/OCR Functions

def set_cv_image(image=None, color='COLOR', show=False):
    """
    Brief: file path or screen area or file/area=> image
    Args:
        image (str: image file path / list: screen image area)
    Returns:
        opencv image array
    """
    if type(image) is str:    ## image file path
        if color == 'COLOR':
            img = cv2.imread(image, cv2.IMREAD_COLOR)
        elif color == 'GRAY':
            img = cv2.imread(image, cv2.IMREAD_GRAYSCALE)
        print('local image')
    elif type(image) is list: ## scren selected box
        time.sleep(3)  ##@@@@@@@@@@ delay
        img = snap_screenshot(image)
        print('screen area image')
    elif type(image) is dict: ## image file path and crop box {'path':path, 'box':[,,,]}
        if color == 'COLOR':
            img = cv2.imread(image['path'], cv2.IMREAD_COLOR)
        elif color == 'GRAY':
            img = cv2.imread(image['path'], cv2.IMREAD_GRAYSCALE)
        box = image['box']
        img = img[box[1]:box[3], box[0]:box[2]]
        #print('local image')
    else: ## image data are none or wrong
        img = snap_screenshot()
        #print('full screen image')
        #return []

    if show:
        cv2.imshow('image', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    return img


def filter_color(image, color='WHITE'):
    """
    Brief: color filter for image recognition or OCR
    Args:
        image (str: image file path / list: screen image area)
        color: 'WHITE', 'YELLOW', 'GREEN' @@@@@@@@
    Returns:
        opencv image array
    """
    if color == 'WHITE':
        lower = np.array([0,0,168])
        upper = np.array([172,111,255])
    else: ##@@@@@@@@@@@@@@@@ color에 따른 lower, upper 지정!!!
        lower = np.array([0,0,168])
        upper = np.array([172,111,255])

    img = set_cv_image(image)
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    # 색상 범위를 제한하여 mask 생성
    img_mask = cv2.inRange(img_hsv, lower, upper)
    # 원본 이미지를 가지고 Object 추출 이미지로 생성
    img_result = cv2.bitwise_and(img, img, mask=img_mask)
    # 결과 이미지 생성
    #imgplot = plt.imshow(img_result)
    #plt.show()
    return img_result


def compute_map_coords_of_screen(center, points):
    center_s = [_ENV['MAX_X']//2, _ENV['MAX_Y']//2]

    M = np.matrix(_MAP['S_M'])
    if type(points[0]) is list:  ## multi points [[960, 540], [1060, 540], [1060, 640], [960, 640]]
        pts = [[p[0] - center_s[0], p[1] - center_s[1]] for p in points]
        R = cv2.perspectiveTransform(np.array([tuple(tuple(point) for point in pts)], dtype=np.float32), M)
        R = np.reshape(R, (-1, 2))

        # R = [[int(round(p[0])), int(round(p[1]))] for p in R]
        R = [[int(p[0]) + center[0], int(p[1]) + center[1]] for p in R]
        #print('R From Multi Points: {}'.format(R))
    else:  ## 1 point @@@@ incorrect!!!!
        X = M.dot(np.array([points[0], points[1], 1]))
        X = np.asarray(X).reshape(-1)
        R = [round(X[0]/X[2]) + center[0], round(X[1]/X[2]) + center[1]]
        #print('R From One Point: {}'.format(R))

    return R

def transform_perspective(points, trans='inverse'):
    if trans == 'inverse':
        M = np.matrix(_MAP['M_R2P'])
    else:
        M = np.matrix(_MAP['M_P2R'])

    if type(points[0]) is list:  ## multi points [[960, 540], [1060, 540], [1060, 640], [960, 640]]
        R = cv2.perspectiveTransform(np.array([tuple(tuple(point) for point in points)], dtype=np.float32), M)
        R = np.reshape(R, (-1, 2))

        # R = [[int(round(p[0])), int(round(p[1]))] for p in R]
        R = [[int(p[0]), int(p[1])] for p in R]
        print('R From Multi Points: {}'.format(R))
    else:  ## 1 point
        X = M.dot(np.array([points[0], points[1], 1]))
        X = np.asarray(X).reshape(-1)
        R = [round(X[0]/X[2]), round(X[1]/X[2])]
        print('R From One Point: {}'.format(R))
    return R


def transform_center_relative(points, trans='inverse', center=[_ENV['MAX_X']//2,_ENV['MAX_Y']//2]):

    if type(points[0]) is list:  ## multi points [[960, 540], [1060, 540], [1060, 640], [960, 640]]
        ps = []
        for point in points:
            p = [point[0]-_ENV['MAX_X']//2, point[1]-_ENV['MAX_Y']//2]
            ps.append(p)
        return ps
    else:  ## 1 point
        return [points[0]-_ENV['MAX_X']//2, points[1]-_ENV['MAX_Y']//2]


def transform_perspective_relative(points, trans='inverse', center=[_ENV['MAX_X']//2,_ENV['MAX_Y']//2]):
    points = transform_perspective(points, trans='inverse')
    points = transform_center_relative(points, center=center)

    _y = _ENV['MAX_Y']//2 - 395

    if trans is not 'inverse':
        _y = -_y + 290

    if type(points[0]) is list:  ## multi points [[960, 540], [1060, 540], [1060, 640], [960, 640]]
        ps = []
        for point in points:
            p = [round(point[0]), round(point[1]) + _y]
            ps.append(p)
        return ps
    else:  ## 1 point
        return [round(point[0]), round(point[1]) + _y]


def snap_screenshot(box=[1, 1, _ENV['MAX_X'], _ENV['MAX_Y']]):
    """
    Brief: snap screenshot
    Args:
        box (list): 스크린샷 지정 영역(default: 전체 화면)
    Returns:
        opencv image array
    """
    x1 = box[0]
    y1 = box[1]
    width = box[2] - x1
    height = box[3] - y1

    img = cv2.cvtColor(np.array(pag.screenshot(region=(x1, y1, width, height))), cv2.COLOR_BGR2RGB)

    return img


def extract_templates(image):
    """
    Brief:
        - 이미지에서 독립된 그림 개체(template)들 추출
    Args:
        image (str: image file path / list: screen image area):
    Returns:
        boxes (list) : 독립된 이미지 박스들
    """
    origin = [0, 0]    ## 기준 좌표
    if type(image) is str:
        image = cv2.imread(image, cv2.IMREAD_COLOR)
    else: ## scren selected box
        origin = image.copy()
        image = snap_screenshot(image)

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (3, 3), 0)
    canny = cv2.Canny(blurred, 120, 255, 1)
    kernel = np.ones((5,5),np.uint8)
    dilate = cv2.dilate(canny, kernel, iterations=1)

    # Find contours
    cnts = cv2.findContours(dilate, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if len(cnts) == 2 else cnts[1]

    # template boxes 좌표 배열
    boxes = []

    # Iterate thorugh contours and filter for ROI
    for c in cnts:
        x, y, w, h = cv2.boundingRect(c)
        box = [x + origin[0], y + origin[1], x + w + origin[0], y + h + origin[1]]
        boxes.append(box)

    if boxes == []:
        return False
    else:
        boxes = sorted(boxes, key=lambda box: box[0])

    print('boxes at image_recognition.py: {}',format(boxes))
    return boxes


def save_screenshot(box=[1, 1, _ENV['MAX_X'], _ENV['MAX_Y']], path=None):
    """
    Brief: save screenshot
    Args:
        box (list): 스크린샷 지정 영역(default: 전체 화면)
        path (str): 저장 위치
    Returns:
        opencv image array
    """
    image = snap_screenshot(box)
    if path == None:
        path = _PATH['SCREENSHOT_FOLDER'] + str(box[0]) + '_' + str(box[1]) + '_' + str(box[2]) + '_' + str(box[3]) + '.png'
    print(path)
    cv2.imwrite(path, image)
    return 0


def save_file_crop(file, box, path=None):
    """
    Brief: save screenshot
    Args:
        file
        box (list): 스크린샷 지정 영역(default: 전체 화면)
        path (str): 저장 위치
    Returns:
        opencv image array
    """

    #image = cv2.imread(file.replace(" ", "\ "), cv2.IMREAD_COLOR)[box[1]:box[3], box[0]:box[2]]
    image = cv2.imread(file, cv2.IMREAD_COLOR)[box[1]:box[3], box[0]:box[2]]
    #cv2.imshow('image', image)
    cv2.imwrite(path, image)
    return 0


##@@-------------------------------------------------------------------------
##@@ Match Image Functions(이미지 비교: 방향, 크기 고려)

def match_image_box(template, image=None, mask=None, precision=0.98, method=cv2.TM_CCORR_NORMED, show=False, multi=0, color=None):
    """
    Brief:
        - 매칭 되는 이미지(>precision) 중앙 좌표 반환, 없으면 False
        -    match_image_box -> set_cv_image(template/image) + find_match_image_box
    Args:
        template (str: image file path / list: screen image area):
        offset (list) : 중앙 좌표 (이동)보정
        image (str: image file path / list: screen image area):
        mask: 마스크 이미지
        precision: 이미지 유사도
        method: 이미지 매칭 방법
        show:
        multi:
    Returns:
        center (list) : center of box[x1, y1]
    """
    offset = [0, 0]
    if type(image) is list:
        offset = [image[0], image[1]]

    img = set_cv_image(image)
    tpl = set_cv_image(template)

    if mask != None:
        mask = cv2.imread(mask, cv2.IMREAD_GRAYSCALE)

    if color != None:
        ## color filter 적용
        img = cv2.bitwise_and(img, img, mask=cv2.inRange(cv2.cvtColor(img, cv2.COLOR_BGR2HSV), np.array(color[0]), np.array(color[1])))
        tpl = cv2.bitwise_and(tpl, tpl, mask=cv2.inRange(cv2.cvtColor(tpl, cv2.COLOR_BGR2HSV), np.array(color[0]), np.array(color[1])))

        # cv2.imshow('img', img)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()

    return find_match_image_box(template=tpl, image=img, mask=mask, precision=precision, method=method, offset=offset, show=show, multi=multi)


#def find_match_image_box(template, image=None, mask=None, precision=0.3, method=cv2.TM_CCOEFF_NORMED, show=False, multi=0):
def find_match_image_box(template, image=None, mask=None, precision=0.98, method=cv2.TM_CCORR_NORMED, offset=[0,0], show=False, multi=0):
    """
    Brief: 매칭 되는 이미지(>precision) 중앙 좌표 반환, 없으면 False
    Args:
        template (cv2 image array):
        image (cv2 image array):
    """
    img_original = image.copy()
    image = cv2.cvtColor(img_original, cv2.COLOR_BGR2GRAY)
    template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)

    if mask is None:
        print('mask not exist!!!')
        res = cv2.matchTemplate(image, template, method)
    else:
        print('mask exist!!!')
        res = cv2.matchTemplate(image, template, method, mask=mask)

    print('template.shape: {}, multi: {}'.format(template.shape, multi))
    h, w = template.shape[:]

    if multi == 0:
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

        if max_val > precision:
            center = [max_loc[0] + w//2 + offset[0], max_loc[1] + h//2 + offset[1]]
            print('matched!!!: {}, center: {}'.format(max_val, center))
            if show == True:
                #cv2.rectangle(img_original, (max_loc[0], max_loc[1]), (max_loc[0]+w, max_loc[1]+h), (0, 0, 255), 2)
                cv2.rectangle(img_original, (max_loc[0], max_loc[1]), (max_loc[0]+w + offset[0], max_loc[1]+h + offset[1]), (0, 0, 255), 2)
                cv2.imshow('find image', img_original)
                cv2.waitKey(0)
                cv2.destroyAllWindows()
            return center
        else:
            #print('not matched: {}'.format(max_val))
            return False

    else: #### search multiple matching
        loc = np.where(res >= precision)
        num = len(loc)
        print('num: {}, res: {}'.format(num, res))
        #centers = [[0, 0] for _ in range(0, num)]
        centers = []


        ### 중복(중첩) 영역 제거용
        found = np.zeros(image.shape[:2], np.uint8)
        #i = 0
        last = -10
        for pt in zip(*loc[::-1]):
            #if abs(pt[0] - last) > 1:
            if found[pt[1] + h//2, pt[0] + w//2] != 255: ##@@ 새로운 영역이라면
                found[pt[1]:pt[1]+h, pt[0]:pt[0]+w] = 255  ##@@ 영역 등록
                #centers[i] = [pt[0] + w//2, pt[1] + h//2]
                centers.append([pt[0] + w//2 + offset[0], pt[1] + h//2 + offset[1]])
                #last = pt[0]
                #i += 1
                print('pt: {}, '.format(pt))
                cv2.rectangle(img_original, pt, (pt[0]+w, pt[1]+h), (0, 0, 255), 2)

        if show == True:
            #cv2.imshow('find images', img_original)
            #cv2.waitKey(0)
            #cv2.destroyAllWindows()
            imgplot = plt.imshow(img_original)
            plt.show()

        return centers


##@@-------------------------------------------------------------------------
##@@ Feature Image Functions(이미지 비교: 방향, 크기 무시)

def feature_image_box(template, image, precision=0.7, inverse=True):
    """
    Brief:
        - 매칭 되는 이미지(>precision) 중앙 좌표 반환, 없으면 False
        - feature_image_box -> find_feature_image_box + set_cv_image
    Args:
        template (str: image file path / list: screen image area):
        offset (list) : 중앙 좌표 (이동)보정
        image (str: image file path / list: screen image area):
        mask: 마스크 이미지
        precision: 이미지 유사도(default: 0.7)
        method: 이미지 매칭 방법
    Returns:
        center (list) : center of box[x1, y1]
    """
    origin = [0, 0]    ## 기준 좌표

    img = set_cv_image(image)
    tpl = set_cv_image(template, 'GRAY')

    if type(image) is list: ## scren selected box
        origin = [image[0], image[1]]    ## 기준 좌표

    if type(template) is list: ## scren selected box
        tpl = cv2.cvtColor(tpl, cv2.COLOR_BGR2GRAY)

    return find_feature_image_box(tpl, img, origin, precision, inverse)


def find_feature_image_box(template, image=None, origin=[0, 0], precision=0.7, inverse=True):
    """
    Brief:
        - 매칭 되는 이미지(>precision) 중앙 좌표 반환, 없으면 False
    Args:
        template (str: image file path / list: screen image area):
        offset (list) : 중앙 좌표 (이동)보정
        image (str: image file path / list: screen image area):
        mask: 마스크 이미지
        precision: 이미지 유사도(default: 0.7)
        method: 이미지 매칭 방법
    Returns:
        center (list) : center of box[x1, y1]
    """

    if inverse == True:
        template = ~template            # queryImage 색깔 반전!!!

    # Initiate SIFT detector
    #sift = cv2.SIFT_create()
    sift = cv2.xfeatures2d.SIFT_create()
    # find the keypoints and descriptors with SIFT
    kp1, des1 = sift.detectAndCompute(template, None)
    kp2, des2 = sift.detectAndCompute(image, None)
    # FLANN parameters
    FLANN_INDEX_KDTREE = 1
    index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
    search_params = dict(checks=50)     # or pass empty dictionary
    flann = cv2.FlannBasedMatcher(index_params,search_params)
    matches = flann.knnMatch(des1, des2, k=2)

    points_x = []
    points_y = []
    print('matches size: {}'.format(len(matches)))

    # ratio test as per Lowe's paper
    for i, (m, n) in enumerate(matches):

        if m.distance < precision*n.distance:

            points_x.append(kp2[m.trainIdx].pt[0] + origin[0])
            points_y.append(kp2[m.trainIdx].pt[1] + origin[1])
            print('orign_x: {}, orign_y: {}'.format(origin[0], origin[1]))
            print('matching points: {}'.format(kp2[m.trainIdx].pt))    ###### matching points

    # Not Found Feature
    if points_x == []:
        return False

    center = [(min(points_x) + max(points_x))//2, (min(points_y) + max(points_y))//2]
    #print('center: {}'.format(center))
    #print('-------------------------------')
    return center


def wait_match_image(template, image=None, precision=0.978, pause=3, duration=15):
    time.sleep(pause)
    center = match_image_box(template, image=image, precision=precision)
    _ITV_MATCH_IMAGE = 0.5
    if duration == 0:
        return center
    else:
        #n = duration // _ITV_MATCH_IMAGE
        for _ in range(0, duration):
            center = match_image_box(template, image=image, precision=precision)
            if center == False:
                time.sleep(_ITV_MATCH_IMAGE)
            else:
                return center
    return False

##@@@-------------------------------------------------------------------------
##@@@ OCR Functions(tesseract-ocr:: Character Recognition)

##@@-------------------------------------------------------------------------
##@@ tesseract-ocr

def do_ocr(image, color=None, lang='eng', path=None, reverse=True, gauss=3):
    """
    Brief:
        - 이미지(screen box 좌표 or file path 값) 문자인식
    Args:
        color : color filter
        image (str: image file path / list: screen image area):
        lang: 
        path: 문자인식 이미지 저장 위치.이름
        reverse: 
    """
    if color is not None:
        img = filter_color(image, color)
        print('image will be filtered!!')
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    else:
        img = set_cv_image(image, 'GRAY')

#    retval, img = cv2.threshold(img, 200, 255, cv2.THRESH_BINARY)
#    img = cv2.resize(img, (0, 0), fx=3, fy=3)
#    img = cv2.GaussianBlur(img, (11, 11),0)
#    img = cv2.medianBlur(img, 9)
    if reverse is True:
        img = ~img
    img = cv2.threshold(img, 200, 255, cv2.THRESH_BINARY)[1]
    #img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    # img = cv2.GaussianBlur(img, (1, 1), 0)  ## More Info
    img = cv2.GaussianBlur(img, (gauss, gauss), 0)  ## More Info Kill Details
#    img = cv2.medianBlur(img, 1)

    if reverse:
        img = ~img
    if img is []:
        return False
    
    if not path is None:
        cv2.imwrite(path, img)

    return pytesseract.image_to_string(img, lang, config = tessdata_dir_config)


def rectify_ocr(text, lang='digit'):
    """
    Brief:
        - OCR 결과 보정
    Args:
        text:
        lang: 
    """
    if lang is 'digit':
        s = ['i', 'I', 'l', 'o', 'O', ',']
        d = ['1', '1', '1', '0', '0', '']
        for i, v in enumerate(s):
            #print('s: {}, d: {}'.format(s[i], d[i]))
            text = text.replace(s[i], d[i])
    return text


##@@@-------------------------------------------------------------------------
##@@@ GUI Functions

def get_image_path(name, category='UIS'):
    return _PATH[category] + ui_img[name] + _ENV['IMG_EXT']


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


def compute_box_from_wh(wh):
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


def compute_wh_from_box(box):
    """
    Brief: get wh coordinate([x1, y1, w, h]) from box coordinate([x1:left, y1:top, x2:right, y2:bottom])
    Args:
        wh (list): wh coordinate([x1, y1, w, h])
    Returns:
        box (list): box coordinate
    """
    return [box[0], box[1], box[2] - box[0], box[3] - box[1]]


def compute_center_from_box(box):
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


def compute_box_from_center(center, wh):
    """
    Brief: get box from wh
        - box coordinate([x1:left, y1:top, x2:right, y2:bottom])
        - wh coordinate([x1, y1, w, h])
    Args:
        box (list): box coordinate
    Returns:
        wh (list): wh coordinate([x1, y1, w, h])
    """
    return [center[0] - wh[0]//2, center[1] - wh[1]//2, center[0] + wh[0]//2, center[1] + wh[1]//2]



def expand_box(box, offset=[0, 0, 0, 0]):
    """
        left, top, right, bottom
    """
    if len(box) == 2:
        box.append(box[0])
        box.append(box[1])

    if len(offset) == 1:
        for i in range(1, 4):
            offset.append(offset[0])
    if len(offset) == 2:
        offset.append(offset[0])
        offset.append(offset[1])

    for i, b in enumerate(box):
        if i < 2:
            box[i] = b - offset[i]
        else:
            box[i] = b + offset[i]

    box = fit_box_to_screen(box)
    print('box: {}'.format(box))
    return box


def fit_box_to_screen(box):
    if box[0] < 1:
        box[0] = 1
    if box[1] < 1:
        box[1] = 1
    if box[2] > _ENV['MAX_X']:
        box[2] = _ENV['MAX_X']
    if box[3] > _ENV['MAX_Y']:
        box[3] = _ENV['MAX_Y']
    return box


##@@-------------------------------------------------------------------------
##@@ control mouse

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


def move_mouse_direction(zeroPoint=[_ENV['MAX_X']//2,_ENV['MAX_Y']//2], callback=None, direction=[1,0]):
    pag.moveTo(zeroPoint[0], zeroPoint[1], duration=0.0)
    pag.mouseDown()
    time.sleep(0.1)
    pag.moveTo(zeroPoint[0] + direction[0], zeroPoint[1] + direction[1], duration=0.5)
    time.sleep(0.1)
    pag.mouseUp()
    #pag.dragRel(relPoint[0], relPoint[1], duration=0.02, button='left')
    time.sleep(0.5)
    return direction


# def drag_in_game(relPoint=[0, 0], zeroPoint=[_ENV['MAX_X']//2, _ENV['MAX_Y']//2], duration=_ENV['MOUSE_DURATION']):
#     """
#     Brief: dragInMap(게임 내에서 마우스 드래그)
#     Args:
#         relPoint (list): target point(relative)
#         zeroPoint (list): starting point(relative)
#         viewMode (str): _CASTLE / _ALLIANCE / _KINGDOM
#         duration (int):
#     """
#     pag.moveTo(zeroPoint[0], zeroPoint[1], duration=0.1)
#     pag.dragRel(relPoint[0], relPoint[1], duration=0.2, button='left')


##@@-------------------------------------------------------------------------
##@@ simple GUI Functions(pyautogui:: mouse/keyboard) 

def click_mouse_series(positions, interval=_ENV['CLICK_INTERVAL'], clicks=1):
    """
    Brief: click Mouse Series(마우스 연속 클릭)
    Args:
        positions (list): click positions
        interval (int): interval time[sec] for mouse click
        clicks (int): number of clicks
    """
    for position in positions:
        for _ in range(0, clicks):
            click = click_mouse(position)
            if click is False:
                return False
            time.sleep(interval)


def click_mouse(position=[0, 0], button='LEFT', duration=_ENV['MOUSE_DURATION'], pause=_ENV['MOUSE_CLICK_PAUSE']):
    """
    Brief: click Mouse(마우스 클릭)
    Args:
        position (list): click position
        button (str): mouse button of click
        duration (int):
    """
    if position is False:
        print('position is not selected!!!')
        return False

    time.sleep(pause[0])
    pag.moveTo(position[0], position[1], duration)
    time.sleep(0.05)
    #time.sleep(random.uniform(0.0101, 0.0299))
    pag.mouseDown()
    time.sleep(0.05)
    #time.sleep(random.uniform(0.0101, 0.0299))
    pag.mouseUp()
    time.sleep(pause[1])


def click_mouse2(position=[0, 0], button='LEFT', duration=_ENV['MOUSE_DURATION']):
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
##@@@ Google Drive(gspread)

def fetch_sheet(file_, sheet_):
    return gc.open_by_url(_GOOGLE['URLS'][file_]).worksheet(sheet_)


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
    return list_to_dict([v[find_first_filled_col(data)-1:] for v in remove_empty_list(data)][header:])


def get_dict_from_sheet(ws, header=0):
    """
    Brief: find first filled col
    Args: 
        data = ['', '', '', '', '', '', '', ''], ['', '', '', '', '', '', '', ''], ['', '', '', '', '', '', '', ''], ['', 'one', '', '', '', '', '', ''], ['', '03-01-1900', 'two', 'three', 'Buy', '', '', '']
        header : 공백 열 제거 후 header 열의 상대 위치(ex: 1 -> 다음 행)
    Returns: 2
    """
    return get_filled_dict(ws.get_all_values(), header)


def fill_sheet_from_dict(file, sheet, sheet_data, new=False):
    """
    Brief: google drive file 의 sheet에 sheet_data를 넣음
    Args: 
        data = [{'action':'action1', 'device':'device1', 'character':'character1', 'time':'time1', 'done':'done1', 'next':'next1'}, {'action':'action2', 'device':'device2', 'character':'character2', 'time':'time2', 'done':'done2', 'next':'next2'}]
        new : 기존 데이터가 없음
    """
    #ws = file.worksheet(sheet)
    headers = [key for key, val in sheet_data[0].items()]

    put_values = []

    if new is True:
        put_values.append(headers)

    for v in sheet_data:
        temp = []
        for h in headers:
            temp.append(v[h])
        put_values.append(temp)
    print(put_values)
    file.values_append(sheet, {'valueInputOption': 'USER_ENTERED'}, {'values': put_values})


##@@@-------------------------------------------------------------------------
##@@@ InGame Functions(Basic)

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

    time.sleep(1)

    click_mouse(ui_xy['btn_Pop_LocationSearch_Y'])  ## Y 좌표 필드
    click_mouse(ui_xy['btn_Pop_LocationSearch_Y'])  ## Y 좌표 필드
    click_mouse(ui_xy['npt_Pop_LocationSearch_Field'])  ## 텍스트 입력 필드
    pag.typewrite(str(location[1]))
    time.sleep(1)

    click_mouse2(ui_xy['btn_Pop_LocationSearch_Go'])

    time.sleep(3)  ## 지도 데어터 읽을 시간을 주장!!!


def get_coordinate():
    """
    Brief: 지도에서 x, y 좌표를 입력하여 이동
    Args:
        location (list): 좌표
        viewmode (str): CITY_VIEW / WORLD_VIEW(min -> GLOBE)
    """
    # @@@@@@@@@@@@@@@@@
    if get_viewmode() is 'CITY_VIEW':
        set_viewmode('WORLD_VIEW')

    #filter_color(image, color='WHITE')
    #t = do_ocr([400, 16, 642, 46], color='WHITE', lang='eng', reverse=True)  # 전체
    t = do_ocr([400, 16, 642, 46], lang='eng', reverse=True)  # 전체
    print('result ocr: {}'.format(t))

    #t = '#10 2 175   X:2 97Y:104'
    #print(t)
    ##@@@@@@@@@
    s = ['i', 'I', 'l', 'o', 'O', ',', '/']
    d = ['1', '1', '1', '0', '0', '', '7']
    for i, v in enumerate(s):
        #print('s: {}, d: {}'.format(s[i], d[i]))
        t = t.replace(s[i], d[i])
    t = re.sub(r'(\d) +(\d)', r'\1\2', t)
    t = re.sub(r'(\d) +(\d)', r'\1\2', t)

    t = re.sub(r'[a-zA-Z]', ' ', t)
    t = re.sub(r'[^0-9,\. ]+', '', t)
    t = re.sub(r' {2,}', ' ', t)

    t = " ".join(t.strip().split())

    arr = t.split(' ')

    for i, a in enumerate(arr):
        if len(a) > 4:
            print(a)
            arr[i] = a[len(a)-4:]

    if len(arr) == 3:
        return (int(arr[0]), int(arr[1]), int(arr[2]))
    else:
        return False


def get_viewmode():
    #cityview = get_center_match_image(get_image_path('btn_GoWorldView'), precision=0.9)
    cityview = match_image_box(template=get_image_path('btn_GoWorldView'), image=[10, 902, 174, 1070], precision=0.95)
    print('cityview: {}'.format(cityview))
    if type(cityview) is list:
        return 'CITY_VIEW'
    else:
        return 'WORLD_VIEW'


def set_viewmode(mode='CITY_VIEW'):
    if get_viewmode() != mode:
        click_mouse(ui_xy['btn_GoWorldView'])


def zoom_out(nth=_ENV['ZOOM_MAX']):
    pag.moveTo(_ENV['MAX_X']//2, _ENV['MAX_Y']//2)
    keys = ui_key[_ENV['OS']]['ZOOM_OUT']
    for _ in range(0, nth):
        for key in keys:
            pag.keyDown(key)
            time.sleep(0.02)
        for key in keys:
            pag.keyUp(key)
            time.sleep(0.01)
    time.sleep(2)


def click_tool_button(button='Search'):
    """
    """
    btn_img = _imgs + 'btn_Tool' + button + '.png'
    btn = match_image_box(template=btn_img)
    if not btn:
        click_mouse(_uis['btn_GoCityView'])
        time.sleep(2)
        btn = match_image_box(template=btn_img)
        if not btn:
            return False
        else:
            click_mouse(btn)
    else:
        click_mouse(btn)

    time.sleep(2)
    return btn


##@@@-------------------------------------------------------------------------
##@@@ InGame Functions(TurnOn, TurnOff / Errors)



##@@@-------------------------------------------------------------------------
##@@@ InGame Functions(Account/Character)

def create_new_character(server=None):
    """
    Brief: 새로운 계정 만들기
    Args:
        server: 서버
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
            continue
        else:
            print(btn)
            click_mouse(btn)
            time.sleep(10)
            break
        return False

    if server is None:
        kingdom = [600, 424] # 서버(왕국) 선택 버튼(last open)!!!
        # kingdom = [1280, 560] # 서버(왕국) 선택 버튼(4th last open)!!!
        click_mouse(kingdom)
    else:
        btn_server = _imgs + 'img_CreateNewCharacter_' + server + '.png'
        print(btn_server)
        btn = match_image_box(template=btn_server, precision=0.997)
        # print(btn)
        for _ in range(0, 40):
            if btn is False:
                move_mouse_direction(zeroPoint=[_ENV['MAX_X']//2, _ENV['MAX_Y']//2 + 300], direction=[0, -600])
                time.sleep(3)
                print('not Founded Server')
                btn = match_image_box(template=btn_server, precision=0.997)
                continue
            else:
                print('Founded Server: {}'.format(btn))
                click_mouse(btn)
                time.sleep(5)
                click_mouse([1220, 768]) # YES button
                return True

    return False


def do_scenario():
    """
    Brief: 초반 시나리오 완료
    """
    btn_skip = [1770, 50] # SKIP 버튼
    skip = [10, 540]
    btn_tool = [94, 810]
    btn_map = [84, 994] # map, castle toggle button
    btn_build = [400, 800]
    btn_military = [88, 774]
    btn_quests = [72, 250]
    btn_go = [1510, 364] # go, claim toggle button

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

    btn_img = _imgs + 'btn_Scenario_BarbarianAttack.png'
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
        btn_quests,
        btn_go,
        skip,
        skip,
        [964, 766], # city hall
        [1490, 830], # upgrade city hall
        skip,
        # skip,
        btn_quests,
        btn_go,
        skip,
        btn_go,
        skip,
    ]

    click_mouse_series(btns6, interval=3, clicks=1)
    time.sleep(5)

    btns7 = [
        btn_go,
        skip,
        skip,
        btn_tool,
        btn_military,
        btn_build, # build scout camp
        [1280, 402], # build button
        skip,
        skip,
        [1380, 828], # scout button
        match_image_box(template= _imgs + 'img_Buildings_ScoutCamp_0.png'), # scout builing
        match_image_box(template= _imgs + 'btn_ScoutCamp_Explore.png'), # scout builing
        # [1116, 623], # scout button
        # [1510, 480], # explore button
        [1210, 780], # explore2 button @@@@ 안개 지역이 있는 경우에만 해당!!!
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


    btn_ScoutCamp_Explore
    img_Buildings_ScoutCamp_0

    click_mouse_series(btns7, interval=3, clicks=1)
    time.sleep(10)



def remove_trees():
    """
    Brief: 도시내 나무 제거
    Args:
    Notes:
        맵 유형에 따른 나무 위치 고려해야 함!!!
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
    Brief: 도시내 나무 제거(Unit)
    Args:
        pos (list): 나무 위치
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
    Brief: 도시내 나무 제거(Unit)
    Args:
        tree (tuple): (나무 위치, 다음 나무 위치)
    """
    #set_standard_view()
    click_mouse(tree[0])
    time.sleep(2)
    click_mouse(tree[1])
    time.sleep(3)

    click_mouse([712, 770]) # YES button
    time.sleep(2)


##@@@-------------------------------------------------------------------------
##@@@ InGame Functions(Record / Log)

def record_test():
    return click_copy(position=[1002, 346])


def click_test():
    click_mouse(position=_uis['btn_Mod_Alliance_Members_Rank4_1'])  ## btn_Mod_Alliance_Members_Rank4_1 / btn_QuickloanchOsxROK -> btn_WallpaperEmulROKMax

# def ocr_test():
#     return do_ocr([1420, 308, 1564, 356])  ## 

def record_moreinfo_unit(level='R4', row=0, col=0):
    moreinfo = {'nick':''}

    prefix = 'val_Mod_Governor_Info_MoreInfo_'
    vals = ['Power', 'Kills', 'HighestPower', 'Victory', 'Defeat', 'Dead', 'ScoutTimes', 'ResourcesGathered', 'ResourceAssistance', 'AllianceHelpTimes']
    print('vals: {}'.format(vals))

    for val in vals:
        print('_vals[prefix + val]: {}'.format(_vals[prefix + val]))
        moreinfo[val] = do_ocr(_vals[prefix + val], color='WHITE', lang='digits', path='../images/test/' + val + '.png')

    ## More Info 내에 있는 Kill 상세 버튼
    click_mouse(position=[1290, 186])

    prefix = 'val_Pop_Governor_Info_MoreInfo_'
    tiers = ['Kills_1', 'Kills_2', 'Kills_3', 'Kills_4', 'Kills_5']
    #print('tiers: {}'.format(tiers))

    for tier in tiers:
        print('_tiers[prefix + tier]: {}'.format(_vals[prefix + tier]))
        moreinfo[tier] = do_ocr(_vals[prefix + tier], color='WHITE', lang='digits', path='../images/test/' + tier + '.png', reverse=False, gauss=7)

    #### btn_Mod_Governor_Info_MoreInfo_CopyNick
    position = compute_center_from_box(compute_box_from_wh([437, 171, 30, 30]))
    nick = click_copy(position=position)
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
        click_mouse(position=position)
        time.sleep(1.5)


def change_test():
    positions = [
        [74, 60],  ## btn_  Profile
        [1470, 800],  ## btn_ Settings
        [430, 572],  ## btn_ CharacterManagement
    ]

    for position in positions:
        click_mouse(position=position)
        time.sleep(1.5)

    btn_m004 = '../images/uis/btn_Character_m004.png'

    center = match_image_box(btn_m004)

    click_mouse(center)


##@@@-------------------------------------------------------------------------
##@@@ InGame Functions(NonDispatch Actions)

def tour_sunsetCanyon():
    """
    """
    pass


def tour_lostCanyon():
    """
    """
    pass



## @@brief:: VIP Point / Gift 수령 (period: 1day)
## @@note:: 
def receive_VIP():
    series = [
        _UI['VIP']['BUTTON']['xy'], 
        _UI['VIP']['POP_VIP']['BTN_ClaimPoints']['xy'], 
        _UI['VIP']['POP_VIP']['BTN_ClaimGifts']['xy']
    ]
    clickMouseSeries(series, 0.5, 2)
    clickMouse( _UI['VIP']['POP_VIP']['BTN_CLOSE']['xy'])
    return 0



## @@brief:: 연맹 자원 수령
## @@note:: 
def do_AllianceTerritory():
    # 하단 메뉴 펼침
    unfoldMenuBtn()
    # 클릭
    series = [
        _UI['MENU']['BTN_Alliance']['xy'], 
        _UI['MENU']['POP_Alliance']['BTN_Territory']['xy'], 
        _UI['MENU']['POP_Alliance_Territory']['BTN_Claim']['xy'],
        _UI['MENU']['POP_Alliance_Territory']['BTN_CLOSE']['xy'],
        _UI['MENU']['POP_Alliance']['BTN_CLOSE']['xy']
    ]
    clickMouseSeries(series, 2)  
    return 0


## @@brief:: VIP Point / Gift 수령 (period: 1day)
## @@note:: 
def do_AllianceHelp():
    # 하단 메뉴 펼침
    unfoldMenuBtn()
    # 클릭
    series = [
        _UI['MENU']['BTN_Alliance']['xy'], 
        _UI['MENU']['POP_Alliance']['BTN_Help']['xy'], 
        _UI['MENU']['POP_Alliance_Help']['BTN_Help']['xy'],
        _UI['MENU']['POP_Alliance_Help']['BTN_CLOSE']['xy'],
        _UI['MENU']['POP_Alliance']['BTN_CLOSE']['xy']
    ]
    clickMouseSeries(series, 0.5)  
    return 0


## @@brief:: 연맹 기술 지원@@@@@@@@@@@@@@@@@@
## @@note:: 
def do_AllianceTechnology():
    # 하단 메뉴 펼침
    unfoldMenuBtn()
    series = [_UI['MENU']['BTN_Alliance']['xy'], _UI['MENU']['POP_Alliance']['BTN_Technology']['xy']]
    clickMouseSeries(series, 2)
    ## 기술 지원 항목 찾기!!!
    #findAllianceTechnology()
    # 'POP_Alliance_Technology_Donate': {
    #     'BTN_CLOSE': {'xy': [1570, 150], 'fn':''},
    #     'BTN_Donate': {'xy': [1414, 812], 'fn':''},
    # },
    ## 팝업창 닫기
    series = [
        _UI['MENU']['POP_Alliance_Technology_Donate']['BTN_CLOSE']['xy'], 
        _UI['MENU']['POP_Alliance_Technology']['BTN_CLOSE']['xy'], 
        _UI['MENU']['POP_Alliance']['BTN_CLOSE']['xy']
    ]
    clickMouseSeries(series, 0.5)
    return 0


## @@brief:: 연맹 자원 수령
## @@note:: 
def do_AllianceGifts():
    # 하단 메뉴 펼침
    unfoldMenuBtn()

    # 선물 팝업 열기
    series = [
        _UI['MENU']['BTN_Alliance']['xy'], 
        _UI['MENU']['POP_Alliance']['BTN_Gifts']['xy'], 
        _UI['MENU']['POP_Alliance_Gifts']['TAB_Rare']['xy'],
        _UI['MENU']['POP_Alliance_Gifts']['ARR_Items']['first'],
    ]
    clickMouseSeries(series, 0.5)

    # 희귀 선물 클릭
    items = _UI['MENU']['POP_Alliance_Gifts']['ARR_Items']
    for _ in range(0, _ENV['_GIFT_MAX']//10 + 1):
        claim = matchImageBox(_ENV['_IMAGES_FOLDER'] + _UI['MENU']['POP_Alliance_Gifts']['BTN_Claim']['fn'])
        if not claim:
            print('claim buttons not exist!!')
            break
        else:
            for _ in range(0, 10):
                btn_2nd = [items['first'][0] + items['offset'][0], items['first'][1] + items['offset'][1]]
                clickMouse(btn_2nd)

    # 일반 선물 클릭
    series = [
        _UI['MENU']['POP_Alliance_Gifts']['TAB_Normal']['xy'],
        _UI['MENU']['POP_Alliance_Gifts']['BTN_ClaimAll']['xy']
    ]
    clickMouseSeries(series, 0.5)  

    # 팝업창 닫기
    series = [
        _UI['MENU']['POP_Alliance_Gifts']['BTN_Confirm']['xy'],
        _UI['MENU']['POP_Alliance_Gifts']['BTN_CLOSE']['xy'],
        _UI['MENU']['POP_Alliance']['BTN_CLOSE']['xy']
    ]
    clickMouseSeries(series, 0.5)  
    return 0


##@@@-------------------------------------------------------------------------
##@@@ InGame Functions(Dispatch Actions)


def click_dispatch_search(resource='Food', plus=0):
    """
    """
    # Cropland
    places = {
        'Food': 'Cropland',
        'Wood': 'LoggingCamp',
        'Stone': 'StoneDeposit',
        'Gold': 'GoldDeposit',
        'Barbarians': 'Barbarians'
    }

    click_mouse(_uis['btn_Search_' + places[resource]])
    place = 'btn_Mod_Search_' + places[resource]

    for _ in range(0, plus):
        click_mouse(_uis[place + '_Plus'])

    click_mouse(_uis[place + '_Search'])
    ### 찾는 자원이 있는지 확인
    time.sleep(3)
    click_mouse([_ENV['MAX_X']//2,_ENV['MAX_Y']//2])
    time.sleep(2)


def click_gather(hold_positoin=True):
    """
    """
    ## 채집(gather)
    btn_img = _imgs + 'btn_Gather.png' ##@@@@@@@@@@@@@@
    btn = match_image_box(template=btn_img)
    click_mouse(btn)
    time.sleep(2)


def click_attack(hold_positoin=True):
    """
    """
    ## Attack
    btn_img = _imgs + 'btn_Pop_DefeatBarbarians_Attack.png'
    btn = match_image_box(template=btn_img)
    click_mouse(btn)
    time.sleep(2)


def click_dispatch_army(nth=0, commandar=None, multi=False):
    """
    """
    btn_img = _imgs + 'btn_Pop_DispatchArmy_NewTroops.png' ##@@@
    btn = match_image_box(template=btn_img)

    if not btn: ## no new troops
        btn_img = _imgs + 'btn_Pop_DispatchArmy_March.png' ## 
        btn2 = match_image_box(template=btn_img)
        if not btn2:
            print('Error')
            return False
        else:
            ## @@@@ badge check 부대 상태에 따라, camp

            click_mouse(btn2)
    else:
        click_mouse(btn)

    time.sleep(2)

    if multi:  ## Multiple Selection
        pass

    if nth > 0 & nth < 6:
        click_mouse(_uis['btn_Mod_Amies_NewTroops_' + str(nth)])

    click_mouse(_uis['btn_Pop_DispatchArmy_March'])
    time.sleep(2)



def gather_resources(resource='Food', level=1):
    """
    """
    click_tool_button(button='Search')
    click_dispatch_search(resource=resource, level=level)
    click_gather()
    click_dispatch_army()



def hunt_barbarians(level=8, multi=False, potion=False, nth=0):
    """
    """
    click_tool_button(button='Search')
    click_dispatch_search_button(resource='Barbarians', level=level)
    click_attack()
    click_dispatch_army()


def rally_barbarianFort(level=1):
    """
    """
    search_barbarianFort(level=level)
    pass


def join_barbarianFort():
    """
    """
    pass


def defeat_guardian():
    """
    """
    pass


def recover_fog():
    """
    """
    pass


##@@@-------------------------------------------------------------------------
##@@@ InGame Functions(Quests / Events)



##@@@@========================================================================
##@@@@ Execute Test
if __name__ == "__main__":
    #time.sleep(5)

    time_gap_str = '34:27'
    add_timedelta_to_now(td=time_gap_str)
    print(add_timedelta_to_now(td=time_gap_str))
    # print((now + td).strftime('%Y-%m-%d %H:%M:%S'))

    # sheet_data = [{'action':'action1', 'character':'character1', 'time':'time1', 'device':'device1', 'done':'done1', 'next':'next1'},{'action':'action2', 'device':'device2', 'character':'character2', 'time':'time2', 'done':'done2', 'next':'next2'}]

    # fill_sheet_from_dict(_LOGS, _SHEET_LOGS, sheet_data, new=False)