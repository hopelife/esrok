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



##@@@@========================================================================
##@@@@ Constants


##@@@-------------------------------------------------------------------------
##@@@ External(.json/.py)
sys.path.append(os.path.join(os.path.dirname(sys.path[0]), '_config'))
from _settings import _ENV, _PATH, _TESSERACT

##@@@-------------------------------------------------------------------------
##@@@ internal
# _TESSERACT = {
#     '_EXE': 'C:/Program Files/Tesseract-OCR/tesseract.exe',
#     '_DATA': '--tessdata-dir "C:\\Program Files\\Tesseract-OCR\\tessdata"',
#     #'_EXE': 'C:/Program Files (x86)/Tesseract-OCR/tesseract.exe',
#     #'_DATA': '--tessdata-dir "C:\\Program Files (x86)\\Tesseract-OCR\\tessdata"', 
# }
# pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract.exe'
# tessdata_dir_config = '--tessdata-dir "C:\\Program Files (x86)\\Tesseract-OCR\\tessdata"'

pytesseract.pytesseract.tesseract_cmd = '/usr/local/Cellar/tesseract/4.1.1/bin/tesseract'
tessdata_dir_config = '--tessdata-dir "/usr/local/Cellar/tesseract-lang/4.0.0/share/tessdata/"'

# sudo cp digits.traineddata /usr/local/Cellar/tesseract-lang/4.0.0/share/tessdata/digits.traineddata

# pytesseract.pytesseract.tesseract_cmd = _TESSERACT['_EXE']
# tessdata_dir_config = _TESSERACT['_DATA']

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


def get_image(image=None, color='COLOR', show=False):
    """
    Brief: file path or screen area => image
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
    else: ## image data are none or wrong
        img = snap_screenshot()
        print('full screen image')
        #return []

    if show:
        cv2.imshow('image', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    return img


def snap_screenshot(box=[1, 1, _ENV['_MAX_X'], _ENV['_MAX_Y']]):
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
def save_screenshot(box=[1, 1, _ENV['_MAX_X'], _ENV['_MAX_Y']], path=None):
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
        path = _PATH['_SCREENSHOT_FOLDER'] + str(box[0]) + '_' + str(box[1]) + '_' + str(box[2]) + '_' + str(box[3]) + '.png'
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

    image = cv2.imread(file, cv2.IMREAD_COLOR)[box[1]:box[3], box[0]:box[2]]
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
def match_image_box(template, image=None, mask=None, precision=0.98, method=cv2.TM_CCORR_NORMED, show=False, multi=0):
    offset = [0, 0]
    if type(image) is list:
        offset = [image[0], image[1]]

    img = get_image(image)
    #tpl = get_image(template, color='GRAY')
    tpl = get_image(template)

    # cv2.imshow('image', img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    # cv2.imshow('tpl', tpl)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    """
    Brief:
        - 매칭 되는 이미지(>precision) 중앙 좌표 반환, 없으면 False
        -    match_image_box -> get_image(template/image) + find_match_image_box
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

    if mask != None:
        mask = cv2.imread(mask, 0)

    return find_match_image_box(tpl, img, mask, precision, method, offset, show, multi)


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
    #mask = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY)

    # cv2.imshow('template', template)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    # cv2.imshow('image', image)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    # image.astype(np.float32)
    # template.astype(np.float32)

    if mask is None:
        print('mask not exist!!!')
        res = cv2.matchTemplate(image, template, method)
    else:
        print('mask exist!!!')
        # cv2.imshow('mask', mask)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()
        res = cv2.matchTemplate(image, template, method, mask=mask)
        #res = cv2.matchTemplate(image, template, method, mask)

    print('template.shape: {}, multi: {}'.format(template.shape, multi))
    #w, h, _ = template.shape[::-1]
    #w, h, _ = template.shape[::]
    #w, h = template.shape[:]
    h, w = template.shape[:]


    if multi == 0:
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        print(max_val)

        if max_val < precision:
            return False
        else:
            center = [max_loc[0] + w//2 + offset[0], max_loc[1] + h//2 + offset[1]]
            print(center)
            if show == True:
                #cv2.rectangle(img_original, (max_loc[0], max_loc[1]), (max_loc[0]+w, max_loc[1]+h), (0, 0, 255), 2)
                cv2.rectangle(img_original, (max_loc[0], max_loc[1]), (max_loc[0]+w + offset[0], max_loc[1]+h + offset[1]), (0, 0, 255), 2)
                cv2.imshow('find image', img_original)
                cv2.waitKey(0)
                cv2.destroyAllWindows()
            return center
    else: #### search multiple matching
        loc = np.where(res >= precision)
        num = len(loc)
        print('num: {}'.format(num))
        #centers = [[0, 0] for _ in range(0, num)]
        centers = []

        #i = 0
        last = -10
        for pt in zip(*loc[::-1]):
            if abs(pt[0] - last) > 1:
                #centers[i] = [pt[0] + w//2, pt[1] + h//2]
                centers.append([pt[0] + w//2 + offset[0], pt[1] + h//2 + offset[1]])
                last = pt[0]
                #i += 1
                print('pt: {}'.format(pt))

                cv2.rectangle(img_original, pt, (pt[0]+w, pt[1]+h), (0, 0, 255), 2)

        if show == True:
            cv2.imshow('find images', img_original)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        print(centers)
        return centers



def wait_match_image(template, image=None, precision=0.978, duration=15):
    center = get_center_match_image(template, image, precision)
    _ITV_MATCH_IMAGE = 0.1
    if duration == 0:
        return center
    else:
        #n = duration // _ITV_MATCH_IMAGE
        for _ in range(0, duration):
            center = get_center_match_image(template, image, precision)
            if center == False:
                delay(_ITV_MATCH_IMAGE)
            else:
                return center
    return False


##@@@-------------------------------------------------------------------------
##@@@ Feature Image Functions(이미지 비교: 방향, 크기 무시)

def feature_image_box(template, image, precision=0.7, inverse=True):
    """
    Brief:
        - 매칭 되는 이미지(>precision) 중앙 좌표 반환, 없으면 False
        - feature_image_box -> find_feature_image_box + get_image
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

    img = get_image(image)
    tpl = get_image(template, 'GRAY')

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

##@@@-------------------------------------------------------------------------
##@@@ tesseract-ocr

## @@brief:: 이미지(screen box 좌표 or file path 값) 문자인식
## @@note::
def do_ocr(image, lang='eng', reverse=False):
    img = get_image(image, 'GRAY')
    if reverse:
        img = ~img
    if img is []:
        return False
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
    #get_image('../images/btn_GoWorldView.png')
    #time.sleep(5)
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

    ocr = do_ocr('../images/test/coordinate2.png')
    print(ocr)
