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

##@@@-------------------------------------------------------------------------
##@@@ User Libraries



##@@@@========================================================================
##@@@@ Constants


##@@@-------------------------------------------------------------------------
##@@@ External(.json/.py)
sys.path.append(os.path.join(os.path.dirname(sys.path[0]), '_config'))
from _settings import _ENV, _PATH, _MAP, _TESSERACT, _GOOGLE
from emulators import KEY_MAP as ui_key
from emulators import OBJECTS as ui_obj
from emulators import LOCATION_ROK_FULL as ui_xy
from emulators import IMAGE_ROK_FULL as ui_img


##@@@-------------------------------------------------------------------------
##@@@ internal
# _TESSERACT = {
#     'EXE': 'C:/Program Files/Tesseract-OCR/tesseract.exe',
#     'DATA': '--tessdata-dir "C:\\Program Files\\Tesseract-OCR\\tessdata"',
#     #'EXE': 'C:/Program Files (x86)/Tesseract-OCR/tesseract.exe',
#     #'DATA': '--tessdata-dir "C:\\Program Files (x86)\\Tesseract-OCR\\tessdata"', 
# }
# pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract.exe'
# tessdata_dir_config = '--tessdata-dir "C:\\Program Files (x86)\\Tesseract-OCR\\tessdata"'

pytesseract.pytesseract.tesseract_cmd = '/usr/local/Cellar/tesseract/4.1.1/bin/tesseract'
tessdata_dir_config = '--tessdata-dir "/usr/local/Cellar/tesseract-lang/4.0.0/share/tessdata/"'

# sudo cp digits.traineddata /usr/local/Cellar/tesseract-lang/4.0.0/share/tessdata/digits.traineddata

# pytesseract.pytesseract.tesseract_cmd = _TESSERACT['EXE']
# tessdata_dir_config = _TESSERACT['DATA']


credentials = ServiceAccountCredentials.from_json_keyfile_name(_GOOGLE['JSON'], _GOOGLE['SCOPE'])
gc = gspread.authorize(credentials)

# 스프레스시트 문서 가져오기 
_FILE = gc.open_by_url(_GOOGLE['URLS']['TEST'])

# 시트 선택하기
# _SHEET = doc.worksheet('crop')
_SHEET = 'crop'
_SHEET = 'test'




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
        print('local image')
    else: ## image data are none or wrong
        img = snap_screenshot()
        print('full screen image')
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


def transform_perspective(points, trans='inverse'):
    if trans == 'inverse':
        M = np.matrix(_MAP['M_R2P'])
    else:
        M = np.matrix(_MAP['M_P2R'])

    if type(points[0]) is list:  ## multi points [[960, 540], [1060, 540], [1060, 640], [960, 640]]
        R = cv2.perspectiveTransform(np.array([tuple(tuple(point) for point in points)], dtype=np.float32), M)
        R = np.reshape(R, (-1, 2))
        print('R From Multi Points: {}'.format(R))
    else:  ## 1 point
        X = M.dot(np.array([points[0], points[1], 1]))
        X = np.asarray(X).reshape(-1)
        R = [X[0]/X[2], X[1]/X[2]]
        print('R From One Point: {}'.format(R))
    return R


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

        cv2.imshow('img', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

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


##@@@-------------------------------------------------------------------------
##@@@ OCR Functions(tesseract-ocr:: Character Recognition)

##@@-------------------------------------------------------------------------
##@@ tesseract-ocr

def do_ocr(image, color=None, lang='eng', path=None, reverse=True, gauss=1):
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
    img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
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


def move_direction(zeroPoint=[_ENV['MAX_X']//2,_ENV['MAX_Y']//2], callback=None, direction=[1,0]):
    pag.moveTo(zeroPoint[0], zeroPoint[1], duration=0.0)
    pag.mouseDown()
    time.sleep(0.1)
    pag.moveTo(zeroPoint[0] + direction[0], zeroPoint[1] + direction[1], duration=0.5)
    time.sleep(0.1)
    pag.mouseUp()
    #pag.dragRel(relPoint[0], relPoint[1], duration=0.02, button='left')
    time.sleep(0.5)
    return direction


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
            click_mouse(position)
            time.sleep(interval)


def click_mouse(position=[0, 0], button='LEFT', duration=_ENV['MOUSE_DURATION']):
    """
    Brief: click Mouse(마우스 클릭)
    Args:
        position (list): click position
        button (str): mouse button of click
        duration (int):
    """
    pag.moveTo(position[0], position[1], duration)
    time.sleep(0.05)
    #time.sleep(random.uniform(0.0101, 0.0299))
    pag.mouseDown()
    time.sleep(0.05)
    #time.sleep(random.uniform(0.0101, 0.0299))
    pag.mouseUp()


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
    #return list_to_dict([v[find_first_filled_col(data)-1:] for v in data[find_first_filled_row(data)-1:]][header:])
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

##@@@@========================================================================
##@@@@ Execute Test
if __name__ == "__main__":
    #time.sleep(5)
    # sheet_data = [
    #     {'nick': 'test1', 'Power': '5', 'Kills': '207.662', 'HighestPower': '4174465', 'Victory': '562', 'Defeat': '1', 'Dead': '127074', 'ScoutTimes': '849', 'ResourcesGathered': '443.776.184', 'ResourceAssistance': '45596538', 'AllianceHelpTimes': '16', 'Kills_1': '', 'Kills_2': '', 'Kills_3': '', 'Kills_4': '25009', 'Kills_5': ''},
    #     {'nick': 'test2', 'Power': '6', 'Kills': '207662', 'HighestPower': '4465', 'Victory': '56', 'Defeat': '123', 'Dead': '124', 'ScoutTimes': '849', 'ResourcesGathered': '443.776.184', 'ResourceAssistance': '45596538', 'AllianceHelpTimes': '16', 'Kills_1': '5', 'Kills_2': '8', 'Kills_3': '92', 'Kills_4': '25009', 'Kills_5': '0'}
    # ]
    # fill_sheet_from_dict(_FILE, 'test', sheet_data, new=False)

    b = expand_box([100, 200, 10000, 20000], [10])
    print(b)