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
import re

##@@@-------------------------------------------------------------------------
##@@@ Installed(conda/pip) Libraries
import pyautogui as pag
import cv2
import pytesseract
import matplotlib.image as mpimg
import matplotlib.pyplot as plt

##@@@-------------------------------------------------------------------------
##@@@ User Libraries



##@@@@========================================================================
##@@@@ Constants


##@@@-------------------------------------------------------------------------
##@@@ External(.json/.py)
sys.path.append(os.path.join(os.path.dirname(sys.path[0]), '_config'))
from _settings import _ENV, _PATH, _MAP, _TESSERACT

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

##@@@@========================================================================
##@@@@ Functions

##@@@-------------------------------------------------------------------------
##@@@ Basic Functions


# def remove_neighbor(arr):
#     num = len(arr) // 2
#     for _ in arr:


def sort_coords_by_x(coords):
    ss = sorted(coords, key=lambda coord: coord[0])
    return ss


def remove_coupling_boxes(centers, wh):
    centers = sorted(centers, key=lambda center: center[0])
    #centers = sorted(centers, key=lambda center: center[0]+center[1])
    _center = [-1000, -1000]
    partial = []
    for center in centers:
        dist_x = abs(center[0] - _center[0])
        dist_y = abs(center[1] - _center[1])
        if dist_x > wh[0] or dist_y > wh[1]:
            _center = center
            _centers.append(center)
    
    return _centers


# def merge_overlapping_zones(zones,delta_overpap = 30):

# index = 0

# if zones is None: return zones
# while index < len(zones):
#     no_Over_Lap = False
#     while no_Over_Lap == False and len(zones) > 1 and index < len(zones):
#         zone1 = zones[index]
#         tmpZones = np.delete(zones, index, 0)
#         tmpZones = [tImageZone(*a) for a in tmpZones]

#         for i in range(0, len(tmpZones)):
#             zone2 = tmpZones[i]

#             # check left side broken
#             if zone2.x >= delta_overpap and zone2.y >= delta_overpap:
#                 t = tImageZone(zone2.x - delta_overpap, zone2.y - delta_overpap, zone2.w + 2 * delta_overpap,
#                                zone2.h + 2 * delta_overpap)
#             elif zone2.x >= delta_overpap:
#                 t = tImageZone(zone2.x - delta_overpap, zone2.y, zone2.w + 2 * delta_overpap,
#                                zone2.h + 2 * delta_overpap)
#             else:
#                 t = tImageZone(zone2.x, zone2.y - delta_overpap, zone2.w + 2 * delta_overpap,
#                                zone2.h + 2 * delta_overpap)

#             if (is_zone_overlap(zone1, t) or is_zone_overlap(zone1, zone2)):
#                 tmpZones[i] = merge_zone(zone1, zone2)
#                 zones = tmpZones
#                 no_Over_Lap = False
#                 break

#             no_Over_Lap = True
#     index += 1

# return zones



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


def transform_perspective(points, trans='inverse'):
    if trans == 'inverse':
        M = np.matrix(_MAP['M_R2P'])
    else:
        M = np.matrix(_MAP['M_P2R'])

    if type(points[0]) is list:  ## multi points [[960, 540], [1060, 540], [1060, 640], [960, 640]]
        R = cv2.perspectiveTransform(np.array([tuple(tuple(point) for point in points)], dtype=np.float32), M)
        #R = np.asarray(R).reshape(-1)
        #R = np.asarray(R).flatten()
        #R_ = [[] for in R]
        R = np.reshape(R, (-1, 2))
        print('R From Multi Points: {}'.format(R))
    else:  ## 1 point
        X = M.dot(np.array([points[0], points[1], 1]))
        X = np.asarray(X).reshape(-1)
        #R = [round(X[0]/X[2]), round(X[1]/X[2])]
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


## @@brief:: 이미지에서 template 추출
## @@note:: image는 screen box 좌표 or file path 값
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


## @@brief:: 스크린 샷 저장
## @@note:: box default: 전체 화면
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


## @@brief:: 이미지 파일 crop -> save
## @@note:: 
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
##@@@-------------------------------------------------------------------------
##@@@ Match Image Functions(이미지 비교: 방향, 크기 고려)

def get_center_match_image(template, offset=[0, 0], image=None, mask=None, precision=0.95, method=cv2.TM_CCOEFF_NORMED):
    """
    Brief:
        - 매칭 되는 이미지(>precision) 중앙 좌표 반환, 없으면 False
        - get_center_match_image -> match_image_box + offset
    Args:
        template (str: image file path / list: screen image area):
        offset (list) : 중앙 좌표 (이동)보정
        image (str: image file path / list: screen image area):
        mask: 마스크 이미지
        precision: 이미지 유사도
        method: 이미지 매칭 방법
    Returns:
        center (list) : center of box[x1, y1]
    """
    center = match_image_box(template, image, mask, precision, method)
    if center:
        point = [center[0] + offset[0], center[1] + offset[1]]
        #click_mouse(point)  ##@@@@@@@@@@@@@
        return point
    else:
        return False


#def match_image_box(template, image=None, mask=None, precision=0.9, method=cv2.TM_CCOEFF_NORMED, show=False, multi=0):
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
        # cv2.imshow('mask', mask)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()
        # msk = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY)
        # method = cv2.TM_CCOEFF_NORMED
        res = cv2.matchTemplate(image, template, method, mask=mask)
        #res = cv2.matchTemplate(image, template, method, mask)

    print('template.shape: {}, multi: {}'.format(template.shape, multi))
    #w, h, _ = template.shape[::-1]
    #w, h, _ = template.shape[::]
    #w, h = template.shape[:]
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


def click_match_image(template, image=None, precision=0.978, duration=15, offset=[0,0]):
    pass


def wait_match_image(template, image=None, precision=0.978, duration=15):
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


def filter_color(image, color='WHITE'):
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

##@@@-------------------------------------------------------------------------
##@@@ Feature Image Functions(이미지 비교: 방향, 크기 무시)

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


def test_color_filter(image=[710, 390, 1210, 690], color=[[5, 18, 18], [25, 255, 255]], loop=False):
    img = set_cv_image(image)
    path = '../images/test/_original.png'
    cv2.imwrite(path, img)
    # ..images/objects/img_VillageUnvisited_min.png
    # cv2.imwrite('', img)
    if not loop:
        img = cv2.bitwise_and(img, img, mask=cv2.inRange(cv2.cvtColor(img, cv2.COLOR_BGR2HSV), np.array(color[0]), np.array(color[1])))
        path = '../images/test/filter_' + '_'.join(list(map(str, color[0])))+ '_' + '_'.join(list(map(str, color[1]))) + '.png'
        cv2.imwrite(path, img)
    else:

        #color=[[20, 20, 20], [40, 255, 255]]

        #### @@@@ filter_5_12_12_36_255_255 ~ filter_14_12_12_50_255_255
        #### not good [[5, 5, 5], [35, 255, 255]] ~ 3 for 1,000
        #color=[[5, 20, 20], [25, 255, 255]]
        #color=[[5, 60, 60], [26, 255, 255]]
        _color = [color[0].copy(), color[1].copy()]
        #_color = color.copy()
        #color=[[16, 70, 70], [26, 255, 255]]
        ## color filter 적용(h변화)20_70_70_247_255_255
        for i in range(0, 10):
            for j in range(0, 10):
                for k in range(0, 10):
                    img = cv2.bitwise_and(img, img, mask=cv2.inRange(cv2.cvtColor(img, cv2.COLOR_BGR2HSV), np.array(color[0]), np.array(color[1])))
                    path = '../images/test/filter_' + '_'.join(list(map(str, color[0])))+ '_' + '_'.join(list(map(str, color[1]))) + '.png'
                    cv2.imwrite(path, img)
                    color[0][1] = color[0][1] + 2
                    color[0][2] = color[0][2] + 2
                color[1][0] = color[1][0] + 2
                color[0][1] = _color[0][1]
                color[0][2] = _color[0][2]
            color[0][0] = color[0][0] + 2
            color[1][0] = _color[1][0]

    # color=[[15, 10, 10], [30, 255, 255]]
    # ## color filter 적용(s변화)20_70_70_247_255_255
    # for i in range(0, 20):
    #     color[0][1] = color[0][1] + 5
    #     # color[1][1] = 22
    #     # for j in range(0, 10):
    #     #color[1][1] = color[1][1] + 1
    #     img = cv2.bitwise_and(img, img, mask=cv2.inRange(cv2.cvtColor(img, cv2.COLOR_BGR2HSV), np.array(color[0]), np.array(color[1])))
    #     path = '../images/test/filter_' + '_'.join(list(map(str, color[0])))+ '_' + '_'.join(list(map(str, color[1]))) + '.png'
    #     cv2.imwrite(path, img)

    #color=[[15, 10, 10], [30, 255, 255]]
    ## color filter 적용(s변화)20_70_70_247_255_255
    # for i in range(0, 20):
    #     color[0][2] = color[0][2] + 5
    #     # color[1][1] = 22
    #     # for j in range(0, 10):
    #     #color[1][1] = color[1][1] + 1
    #     img = cv2.bitwise_and(img, img, mask=cv2.inRange(cv2.cvtColor(img, cv2.COLOR_BGR2HSV), np.array(color[0]), np.array(color[1])))
    #     path = '../images/test/filter_' + '_'.join(list(map(str, color[0])))+ '_' + '_'.join(list(map(str, color[1]))) + '.png'
    #     cv2.imwrite(path, img)
##@@@-------------------------------------------------------------------------
##@@@ OCR Functions(tesseract-ocr:: Character Recognition)

##@@@-------------------------------------------------------------------------
##@@@ tesseract-ocr

## @@brief:: 이미지(screen box 좌표 or file path 값) 문자인식
## @@note::
def do_ocr(image, lang='eng', reverse=False):
    img = set_cv_image(image, 'GRAY')
    retval, img = cv2.threshold(img,200,255, cv2.THRESH_BINARY)
    img = cv2.resize(img,(0,0),fx=3,fy=3)
    img = cv2.GaussianBlur(img,(11,11),0)
    img = cv2.medianBlur(img,9)
    if reverse:
        img = ~img
    if img is []:
        return False
    return pytesseract.image_to_string(img, lang, config = tessdata_dir_config)


def do_ocr_filtered(image, color='WHITE', lang='eng', reverse=False):
    img = filter_color(image, color)
    #img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    retval, img = cv2.threshold(img,200,255, cv2.THRESH_BINARY)
    img = cv2.resize(img,(0,0),fx=3,fy=3)
    img = cv2.GaussianBlur(img,(11,11),0)
    img = cv2.medianBlur(img,9)
    if reverse:
        img = ~img
    if img is []:
        return False
    imgplot = plt.imshow(img)
    plt.show()
    return pytesseract.image_to_string(img, lang, config = tessdata_dir_config)


## @@brief:: 이미지(screen box 좌표 or file path 값) 문자인식
## @@note::
def rectify_ocr(text, lang='digit'):
    if lang is 'digit':
        s = ['i', 'I', 'l', 'o', 'O', ',']
        d = ['1', '1', '1', '0', '0', '']
        for i, v in enumerate(s):
            #print('s: {}, d: {}'.format(s[i], d[i]))
            text = text.replace(s[i], d[i])
    return text


##@@@@========================================================================
##@@@@ Execute Test
if __name__ == "__main__":
    #save_screenshot([1, 1, 500, 300])
    #print(do_ocr([524, 214, 1096, 270], 'kor+eng'))
    #set_cv_image('../images/btn_GoWorldView.png')
    time.sleep(5)
    #get_center_match_image('../images/btn_GoWorldView.png')
    #print(get_center_match_image(os.path.abspath('../images/btn_GoWorldView.png')))
    #print(match_image_box(os.path.abspath('../images/btn_GoWorldView.png')))
    #print(match_image_box('../images/btn_GoWorldView.png'))

    # template = '../images/target.png'
    # image = '../images/image.png'
    # mask = '../images/mask.png'
    # test_match_image_box(template, image, mask)
    # coords = [[123, 56], [234, 1], [56, 890], [1, 789], [678, 123], [35, 98]]
    # sort_coords_by_x(coords)

    # ocr = do_ocr('../images/test/coordinate2.png')
    # print(ocr)

    #transform_perspective(points=[960, 540], trans='inverse')
    #transform_perspective(points=((960, 540), (1060, 540), (1060, 640), (960, 640)), trans='inverse')
    #center = [960, 540]
    #step =         [-1,0],
    #points = [center, [-1, 0], [0, -1], [1, 0], [0, 1]]
    # points=[
    #     [960, 540],  #center
    #     [1060, 540],  # 우 right 
    #     [960, 640],  # 하 bottom
    #     [860, 540],  # 좌 left
    #     [960, 440]  # 상 top
    # ]
    # #transform_perspective(points, trans='inverse')
    # transform_perspective(points, trans='normal')

    # inverse=[
    #     [ 959.8659   395.19412]  # 
    #     [1033.05     395.19412]  # [(1033-960:73)/(1060-960), ]
    #     [ 959.8851   492.9006 ]  # [, (492-396:96)/()]
    #     [ 886.6818   395.19412]  # [(960-886:74)/860, ]
    #     [ 959.8486   306.7489]  # [, (396-308:88)/100]
    # ]
    # normal=[
    #     [ 960.13403  684.7339 ]
    #     [1086.9365   684.7339 ]
    #     [ 960.104    773.09326]
    #     [ 833.3314   684.7339 ]
    #     [ 960.1672   587.1271 ]
    # ]

    #tu = tuple(ls)
    #print(tu)


    #filter_color([400, 16, 642, 46], color='WHITE')
    # centers = [[0, 100], [50, 30], [5, 95], [40, 40], [39, 41], [38, 42], [1, 93]]
    # wh = [10, 10]

    # _centers = remove_coupling_boxes(centers, wh)

    # print(_centers)

    #test_color_filter()


    # image = {'path':'C:/Users/ORM005/Downloads/screenshot/map_min01.png', 'box':[710, 390, 1210, 690]}
    # #cv2.imshow('image', image)
    # #set_cv_image(image, show=True)
    # # test_color_filter(image, color=[[20, 100, 100], [30, 255, 255]], loop=False)

    # tpl = '../images/objects/img_VillageUnvisited_min.png'
    # centers = match_image_box(tpl, image=image, mask=None, precision=0.9971, show=True, multi=1, color=None)
    # print(centers)

    #file = 'D:/moon/dev/projects/esrok/backend/bot/images/test/_original.png'
    #file = "D:\\moon\\dev\\projects\\rok\\_bot\\image_full\\스크린샷 2020-05-18 오후 11.18.04.png"
    #file = 'D:/moon/dev/projects/rok/_bot/image_full/스크린샷_2020-05-17_23.59.42.png'
    # file = 'D:/moon/dev/projects/rok/_bot/image_full/_original2.png'
    # box = [1012, 634, 1060, 682]
    # path = '../images/_uis/chk_Pop_DefeatBarbarians_HoldPosition.png'
    # save_file_crop(file, box, path=None)



    path = 'D:/moon/dev/projects/rok/_bot/done/'
    for filename in os.listdir(path):
        os.rename(path + filename, path + re.sub(r'\D', '', filename) + '.png')
    # for filename in os.listdir(path):
    #     os.rename(path + filename, path + filename + '.png')