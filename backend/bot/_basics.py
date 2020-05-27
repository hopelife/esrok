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
    - Image Functions
    - OCR Functions
    - Google Drive / Spreadsheet Functions
 
    - Main Function
 
Usage: import _basics
"""
 
##@@@@========================================================================
##@@@@ Libraries
 
##@@@-------------------------------------------------------------------------
##@@@ Basic Libraries
 
 
 
##@@@-------------------------------------------------------------------------
##@@@ Installed(conda/pip) Libraries
 
 
##@@@-------------------------------------------------------------------------
##@@@ User Libraries
 
 
##@@@@========================================================================
##@@@@ Constants
 
 
##@@@-------------------------------------------------------------------------
##@@@ External(.json/.py)
 
 
##@@@-------------------------------------------------------------------------
##@@@ internal
 
 
##@@@@========================================================================
##@@@@ Functions
 
##@@@-------------------------------------------------------------------------
##@@@ Basic Functions
 
def delay(interval=_ENV['_CLICK_INTERVAL'], random=False):
    """
    Brief: delay intervals(sec)
    Args:
        interval (int): delay interval[sec].
        random (boolean): generate random time
    Returns:
    Note:
        import time
    """
    if random == True:
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
            clickMouse(position)
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
    pag.dragRel(relPoint[0], relPoint[1], delay)
 
 
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
 
 
##@@@-------------------------------------------------------------------------
##@@@ Image Functions(opencv:: Image Recognition)
 
def get_image(image, color='COLOR'):
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
        img = snap_screenshot(image)
        print('screen image')
    else: ## image data are none or wrong
        return []
    
    return img
 
 
def get_center_match_image(template, offset=[0, 0], image=None, mask=None, precision=0.9, method=cv2.TM_CCOEFF_NORMED):
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
        clickMouse(point)
        return point
    else:
        return False
 
 
def match_image_box(template, image=None, mask=None, precision=0.9, method=cv2.TM_CCOEFF_NORMED, show=False, multi=0):
    img = get_image(image)
    tpl = get_image(template)
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
 
    return find_match_image_box(tpl, img, mask, precision, method, show, multi)
 
 
def find_match_image_box(template, image, mask=None, precision=0.9, method=cv2.TM_CCOEFF_NORMED, show=False, multi=0):
    """
    Brief: 매칭 되는 이미지(>precision) 중앙 좌표 반환, 없으면 False
    Args:
        template (cv2 image array): 
        image (cv2 image array): 
    """
    img_original = image.copy()
    image = cv2.cvtColor(img_original, cv2.COLOR_BGR2GRAY)
 
    if type(mask) == list:
        res = cv2.matchTemplate(image, template, method, mask)
    else:
        res = cv2.matchTemplate(image, template, method)
 
    w, h = template.shape[::-1]
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
 
    print(max_val)
 
    if multi == 0:
        if max_val < precision:
            return False
        else:
            center = [max_loc[0] + w//2, max_loc[1] + h//2]
            print(center)
            if show == True:
                cv2.rectangle(img_original, (max_loc[0], max_loc[1]), (max_loc[0]+w, max_loc[1]+h), (0, 0, 255), 2)
                cv2.imshow('find image', img_original)
                cv2.waitKey(0)
                cv2.destroyAllWindows()
            return center
    else: #### search multiple matching
        loc = np.where(res >= precision)
        num = len(loc)
        centers = [[0, 0] for _ in range(0, num)]
 
        i = 0
        for pt in zip(*loc[::-1]):
            centers[i] = [pt[0] + w//2, pt[1] + h//2]
            i += 1
            if show == True:
                cv2.rectangle(img_original, pt, (pt[0]+w, pt[1]+h), (0, 0, 255), 2)
                cv2.imshow('find images', img_original)
                cv2.waitKey(0)
                cv2.destroyAllWindows()
            return centers
 
 
## @@brief:: 유사(방향, 크기 무관) 이미지(>precision) 중앙 좌표 반환, 없으면 False
## @@note:: template, image는 screen box 좌표 or file path 값
def feature_image_box(template, image, precision=0.7, inverse=True):
    origin = [0, 0]    ## 기준 좌표
 
    img = get_image(image)
    tpl = get_image(template, 'GRAY')
 
    if type(image) is list: ## scren selected box
        origin = [image[0], image[1]]    ## 기준 좌표
 
    if type(template) is list: ## scren selected box
        tpl = cv2.cvtColor(tpl, cv2.COLOR_BGR2GRAY)
 
    return find_feature_image_box(tpl, img, origin, precision, inverse)
 
 
## @@brief:: 유사(방향, 크기 무관) 이미지(>precision) 중앙 좌표 반환, 없으면 False
## @@note:: template, image는 cv2 배열
def find_feature_image_box(template, image, origin=[0, 0], precision=0.7, inverse=True):
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
    matches = flann.knnMatch(des1,des2,k=2)
 
    points_x = []
    points_y = []
    # ratio test as per Lowe's paper
    for i, (m, n) in enumerate(matches):
        if m.distance < precision*n.distance:
 
            points_x.append(kp2[m.trainIdx].pt[0] + origin[0])
            points_y.append(kp2[m.trainIdx].pt[1] + origin[1])
            print('matching points: {}'.format(kp2[m.trainIdx].pt))    ###### matching points
 
    # Not Found Feature
    if points_x == []:
        return False
 
    center = [(min(points_x) + max(points_x))//2, (min(points_y) + max(points_y))//2]
    print('center: {}'.format(center))
    print('-------------------------------')
    return center
 
 
## @@brief:: 스크린 샷 실행
## @@note:: box default: 전체 화면
def snap_screenshot(box=[1, 1, _ENV['_MAX_X'], _ENV['_MAX_Y']]):
    if box == None:
        box=[1, 1, _ENV['_MAX_X'], _ENV['_MAX_Y']]
    x1 = box[0]
    y1 = box[1]
    width = box[2] - x1
    height = box[3] - y1
 
    print('(x1={}, y1={}, x2={}, y2={})'.format(box[0], box[1], box[2], box[3]))
    print('(x1={}, y1={}, width={}, height={})'.format(x1, y1, width, height))
    img = cv2.cvtColor(np.array(pag.screenshot(region=(x1, y1, width, height))), cv2.COLOR_BGR2RGB)
    print('img type:' + str(type(img)))
    return img
 
 
## @@brief:: 스크린 샷 저장
## @@note:: box default: 전체 화면
def save_screenshot(box=[1, 1, _ENV['_MAX_X'], _ENV['_MAX_Y']], path=None):
    image = snap_screenshot(box)
    if path == None:
        path = _ENV['_SCREENSHOT_FOLDER'] + str(box[0]) + '_' + str(box[1]) + '_' + str(box[2]) + '_' + str(box[3]) + '.png'
        print(path)
        cv2.imwrite(path, image)
    return 0
 
 
## @@brief:: 이미지 비교(Feature::SIFT)
## @@note:: https://docs.google.com/document/d/1modbLT_NaEsGxkBs6SARH4pEH2BYiUJYTzZ1zmfFICA/edit
 
def compare_image_feature(template, image, type='SIFT'):
    img1 = cv2.imread(template, 0)
    img2 = cv2.imread(image, 0)
 
    sift = cv2.xfeatures2d.SIFT_create()
 
    kp1, des1 = sift.detectAndCompute(img1, None)
    kp2, des2 = sift.detectAndCompute(img2, None)
    
    bf = cv2.BFMatcher()
    matches = bf.knnMatch(des1, des2, k=2)
    
    good = []
    for m,n in matches:
        if m.distance < 0.3*n.distance:
            good.append([m])
    
    img3 = cv2.drawMatchesKnn(template, kp1, img2, kp2, good, None, flags=2)
    
    plt.imshow(img3),plt.show()
 
 
## @@brief:: 이미지에서 template 추출
## @@note:: image는 screen box 좌표 or file path 값
def extract_templates(image):
    origin = [0, 0]    ## 기준 좌표
    if type(image) is str:
        image = cv2.imread(image, cv2.IMREAD_COLOR)
        print('local image')
    else: ## scren selected box
        origin = image.copy()
        image = snap_screenshot(image)
        print('screen image')
 
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
 
    print(boxes)
    return boxes
 
 
##@@@-------------------------------------------------------------------------
##@@@ OCR Functions(tesseract-ocr:: Character Recognition)
 
 
##@@@-------------------------------------------------------------------------
##@@@ GoogleDrive Functions(oauth2client, gspread:: Google Drive / Spreadsheet Functions)
 
 
##@@@@========================================================================
##@@@@ Execute Test
if __name__ == "__main__":
    pass
