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
        - Complex Functions

    - Main Function

Usage: import 
"""

##@@@@========================================================================
##@@@@ Libraries

##@@@-------------------------------------------------------------------------
##@@@ Basic Libraries


##@@@-------------------------------------------------------------------------
##@@@ Installed(conda/pip) Libraries


##@@@-------------------------------------------------------------------------
##@@@ User Libraries
import _basics as _bs


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


##@@@-------------------------------------------------------------------------
##@@@ Complex Functions






##@@@-------------------------------------------------------------------------
##@@@ complex GUI Functions(pyautogui:: mouse/keyboard)

def get_image_path(name, category='UIS'):
    return _PATH[category] + ui_img[name] + _ENV['IMG_EXT']


def get_viewmode():
    #cityview = _bs.get_center_match_image(get_image_path('btn_GoWorldView'), precision=0.9)
    cityview = _bs.match_image_box(template=get_image_path('btn_GoWorldView'), image=[10, 902, 174, 1070], precision=0.95)
    print('cityview: {}'.format(cityview))
    if type(cityview) is list:
        return 'CITY_VIEW'
    else:
        return 'WORLD_VIEW'


def set_viewmode(mode='CITY_VIEW'):
    if get_viewmode() != mode:
        click_mouse(ui_xy['btn_GoWorldView'])


def set_mode_explore():
    chk_explore = _bs.match_image_box('../images/uis/chk_Explore.png', [10, 238, 60, 288], precision=0.99)
    if type(chk_explore) is list:
        print('already explore mode')
    elif not chk_explore: 
        click_mouse([36, 260])
        print('click explore mode')


def shot_zoom_out():
    keys = ui_key[_ENV['OS']]['ZOOM_OUT']
    pag.moveTo(_ENV['MAX_X']//2, _ENV['MAX_Y']//2)
    for i in range(0, 34):
        pag.keyDown(keys[0])
        delay_secs(0.1)
        pag.keyUp(keys[0])
        delay_secs(1)
        _bs.save_screenshot(path='../images/test/02/zoom_' + str(i) + '.png')
        delay_secs(0.2)


def zoom_out(nth=_ENV['ZOOM_MAX']):
    pag.moveTo(_ENV['MAX_X']//2, _ENV['MAX_Y']//2)
    keys = ui_key[_ENV['OS']]['ZOOM_OUT']
    for _ in range(0, nth):
        for key in keys:
            pag.keyDown(key)
            delay_secs(0.02)
        for key in keys:
            pag.keyUp(key)
            delay_secs(0.01)
    delay_secs(2)


def drag_in_map(relPoint=[0, 0], zeroPoint=[_ENV['MAX_X']//2, _ENV['MAX_Y']//2], viewMode='CASTLE', duration=_ENV['MOUSE_DURATION']):
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
    # @@@@@@@@@@@@@@@@@
    if get_viewmode() is 'CITY_VIEW':
        set_viewmode('WORLD_VIEW')

    #_bs.filter_color(image, color='WHITE')
    t = _bs.do_ocr([400, 16, 642, 46], 'eng', reverse=True)  # 전체
    
    #t = '#10 2 175   X:2 97Y:104'
    print(t)
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
    # s = _bs.do_ocr([418, 16, 484, 46], 'digits', reverse=True)  # server
    # x = _bs.do_ocr([510, 16, 562, 46], 'digits', reverse=True)  # x
    # y = _bs.do_ocr([588, 16, 640, 46], 'digits', reverse=True)  # y
    #print('t: {}, s: {}, x: {}, y: {}'.format(t, s, x, y))



def find_verification_verify():
    # return _bs.match_image_box(get_image_path('btn_VerificationVerify', 'UIS'), precision=0.9)
    return _bs.match_image_box(get_image_path('btn_VerificationVerify', 'UIS'), [830, 470, 1738, 648], precision=0.9)


def do_verification_reward(precision=0.4):
    template = [946, 220, 1180, 272]
    image = [730, 280, 1190, 740]
    img_btn_OK = [1024, 754, 1190, 812]

    center_btn_OK = [1100, 786]
    center_btn_close = [756, 782]

    boxes = _bs.extract_templates(template)
    print('boxes at gui.py: {}'.format(boxes))

    if len(boxes) > 4 or boxes is False:
        print('too many templates')
        click_mouse(center_btn_close)
        return False

    centers = []
    for box in boxes:
        center = _bs.feature_image_box(box, image, precision, inverse=True)
        if center is False:
            print('no match image')
            click_mouse(center_btn_close)
            return False
        centers.append(center)
    
    print(centers)
    for center in centers:
        click_mouse(center)
        delay_secs(1)

    click_mouse(center_btn_OK)

    return centers


def do_verification_rewards(precision=0.4, attempts=6):
    btn_verify = find_verification_verify()
    if btn_verify is False:
        return 0
    else:
        click_mouse(btn_verify)
        delay_secs(5)

    center_btn_OK = [1104, 784]
    centers = do_verification_reward(precision)

    tries = 0

    if centers is False:
        tries += 1
        # print('no match image!')
        # if tries > attempts:
        #     do_verification_rewards()  ## 재시도@@@@@@@@@@

        # click_mouse([800, 120])  ## 인증 팝업 바깥쪽을 누름@@@@@
        delay_secs(5)
        do_verification_rewards(precision, attempts)

    elif len(centers) > 4:
        tries += 1
        # print('too many templates!')
        # if tries > attempts:
        #     do_verification_rewards()  ## 재시도@@@@@@@@@@
        # click_mouse([800, 120])  ## 인증 팝업 바깥쪽을 누름@@@@@
        delay_secs(5)
        do_verification_rewards(precision)

    delay_secs(5)

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

    delay_secs(1)

    click_mouse(ui_xy['btn_Pop_LocationSearch_Y'])  ## Y 좌표 필드
    click_mouse(ui_xy['btn_Pop_LocationSearch_Y'])  ## Y 좌표 필드
    click_mouse(ui_xy['npt_Pop_LocationSearch_Field'])  ## 텍스트 입력 필드
    pag.typewrite(str(location[1]))
    delay_secs(1)

    click_mouse2(ui_xy['btn_Pop_LocationSearch_Go'])

    delay_secs(3)  ## 지도 데어터 읽을 시간을 주장!!!



# def save_whole_maps(searchMode='Explore', zoom=320, max_size=_MAP['ONE_MAX']):
#     """
#     Brief: 지도 스크린샷 저장
#     Args:
#         searchMode (str): Alliance, Explore, Resources, Markers, Barbarian Stronghold
#     """
#     #set_fullscreen()
#     #get_server_num()
#     #set_searchmode()
#     # _MAP : {
#     #     'WHOLE': [1200, 1200],
#     #     'ONE_MIN': [8, 6],
#     #     'ONE_MAX': [320, 240],
#     #     'EDGE': [210, 210, 1160, 940]
#     # }
#     server = '1621'

#     ## edge 고려 안함
#     # w = shotsize[0]
#     # h = shotsize[1]
#     # start = [w//2, h//2]
#     box = _MAP['EDGE']
#     ratio_x = _ENV['MAX_X'] / _MAP['ONE_MAX'][0]
#     ratio_y = _ENV['MAX_Y'] / _MAP['ONE_MAX'][1]
#     x1_ = math.floor(_MAP['EDGE'][0]/ratio_x)
#     y1_ = math.floor(_MAP['EDGE'][1]/ratio_y)
#     x2_ = math.floor((_ENV['MAX_X'] - _MAP['EDGE'][2])/ratio_x)
#     y2_ = math.floor((_ENV['MAX_Y'] - _MAP['EDGE'][3])/ratio_y)
#     w = _MAP['ONE_MAX'][0] - x2_ + x1_
#     h = _MAP['ONE_MAX'][1] - y1_ + y2_
#     # w = _MAP['ONE_MAX'][0] - x1_ - x2_
#     # h = _MAP['ONE_MAX'][1] - y1_ - y2_
#     start = [_MAP['ONE_MAX'][0]//2 - x1_, _MAP['ONE_MAX'][1]//2 - y2_]

#     # w = (_MAP['EDGE'][2] - _MAP['EDGE'][0]) / ratio_x
#     # h = (_MAP['EDGE'][3] - _MAP['EDGE'][1]) / ratio_y

#     x_no = _MAP['WHOLE'][0]//w - 1
#     y_no = _MAP['WHOLE'][1]//h - 3

#     print('ratio_x: {}, ratio_y: {}'.format(ratio_x, ratio_y))
#     print('w: {}, h: {}, x1_: {}, _x2: {}, _y1: {}, y2_: {}, start: {}'.format(w, h, x1_, x2_, y1_, y2_, start))
#     print('x_no: {}, y_no: {}'.format(x_no, y_no))

#     for j in range(0, y_no):
#         for i in range(0, x_no):
#             location = [start[0] + i*w, start[1] + j*h]
#             #print(location)
#             save_screenshot_map(location, searchMode, box, server)
#             delay_secs(1)

#     return 0


def save_whole_maps(searchMode='Explore', zoom=320, max_size=_MAP['ONE_MAX']):
    """
    Brief: 지도 스크린샷 저장
    Args:
        searchMode (str): Alliance, Explore, Resources, Markers, Barbarian Stronghold
    """
    server = '1621'

    ## edge 고려 안함
    # w = shotsize[0]
    # h = shotsize[1]
    # start = [w//2, h//2]
    box = _MAP['EDGE']
    ratio_x = _ENV['MAX_X'] / _MAP['ONE_MAX'][0]
    ratio_y = _ENV['MAX_Y'] / _MAP['ONE_MAX'][1]
    w = math.floor((_MAP['EDGE'][2] - _MAP['EDGE'][0])/ratio_x) + 37
    h = math.floor((_MAP['EDGE'][3] - _MAP['EDGE'][1])/ratio_y)
    start = [165, 131]

    print('ratio_x: {}, ratio_y: {}'.format(ratio_x, ratio_y))
    print('w: {}, h: {}, start: {}'.format(w, h, start))

    for j in range(0, 2):
        for i in range(0, 3):
            location = [start[0] + i*w, start[1] + j*h]
            #print(location)
            save_screenshot_map(location, searchMode, box, server)
            delay_secs(1)

    return 0


def save_move_direction(zeroPoint=[_ENV['MAX_X']//2, _ENV['MAX_Y']//2], direction=[-10, 0]):
    x_ = direction[0]
    y_ = direction[1]
    for i in range(1, 6):
        path = _PATH['MAPS'] + 'move_' + str(direction[0]) + '_' + str(direction[1]) + _ENV['IMG_EXT']
        delay_secs(3)
        _bs.save_screenshot(path=path)
        direction[0] += x_
        direction[1] += y_
        move_direction(zeroPoint=zeroPoint, direction=[x_, y_])
        delay_secs(1)


def save_screenshot_map(location=[0, 0], searchMode='Explore', box=[], server=''):
    go_by_coordinate(location)
    #set_searchMode()
    #set_zoomMode(zoom)
    path = _PATH['MAPS'] + server + '_' + searchMode + '_' + str(location[0]) + '_' + str(location[1]) + _ENV['IMG_EXT']
    delay_secs(3)
    _bs.save_screenshot(box, path)



def receive_village_gifts(location=[_MAP['ONE_MAX'][0]//2, _MAP['ONE_MAX'][1]//2], max_i=2):
    zoom_out()
    #go_by_coordinate(location)
    template = '../images/uis/img_ExploreVillage.png'  ##@@@@@@@@@@@@
    #coord = get_coordinate()
    set_mode_explore()

    for _ in range(0, max_i):
        start = time.time()  # 시작 시간 저장
        center = _bs.wait_match_image(template, _MAP['EDGE'], precision=0.978, duration=15)
        print("time :", time.time() - start)  ## 실행 속도 측정

        if not center:
            #coord = get_coordinate()
            drag_in_map([-100, 0])
            #receive_village_gifts()
            continue

        click_mouse(center)
        print(center)
        delay_secs(0.1)
        click_mouse2([_ENV['MAX_X']//2, _ENV['MAX_Y']//2])
        delay_secs(0.1)
        click_mouse([_ENV['MAX_X']//2 - 200, _ENV['MAX_Y']//2])
        delay_secs(0.1)
        zoom_out()
        delay_secs(0.01)


def visit_village(coord={'loc': [1166, 682], 'center': [250, 250]}):
    go_by_coordinate(coord['center'])
    click_mouse(coord['loc'])
    delay_secs(0.1)
    click_mouse2([_ENV['MAX_X']//2, _ENV['MAX_Y']//2])
    delay_secs(0.1)

    great = _bs.match_image_box()

    if type(great) is list:
        click_mouse(great)
        _coord = get_coordinate()
        click_mouse([_ENV['MAX_X']//2 - 200, _ENV['MAX_Y']//2])
        delay_secs(0.1)
        zoom_out()
        delay_secs(0.01)
        return _coord

    return False


def find_village_location(coord={'loc': [1166, 682], 'center': [250, 250]}):
    go_by_coordinate(coord['center'])
    click_mouse(coord['loc'])
    delay_secs(0.1)
    click_mouse2([_ENV['MAX_X']//2, _ENV['MAX_Y']//2])
    delay_secs(0.1)
    _coord = get_coordinate()
    return [_coord[1], _coord[2]]


def search_objects_in_map(obj='village_unvisited', location=[500, 300], box=_MAP['SCAN_BOX'], precision=0.62, ms='min'):
    #go_by_coordinate(location)
    #delay_secs(3)

    #yellow filter: cvScalar(23,41,133), cvScalar(40,150,255)
    # yellow_lower = [20, 100, 100]
    # yellow_upper = [30, 255, 255]
    yellow_lower = [15, 70, 70]
    yellow_upper = [28, 255, 255]
    #template = '../images/uis/img_ExploreVillage.png'  ##@@@@@@@@@@@@
    template = _PATH['OBJECTS'] + ui_obj[obj]['img_' + ms] + _ENV['IMG_EXT']
    mask = None
    if 'msk_' + ms in ui_obj[obj]:
        mask = _PATH['OBJECTS'] + ui_obj[obj]['msk_' + ms] + _ENV['IMG_EXT']

    return _bs.match_image_box(template=template, image=box, mask=mask, precision=precision, show=True, multi=1, color=(yellow_lower, yellow_upper))


def search_villages(location, box):
    go_by_coordinate(location)
    template = '../images/uis/img_ExploreVillage.png'  ##@@@@@@@@@@@@

    #return _bs.match_image_box(template=template, image=box, precision=0.97, show=True, multi=1)
    return _bs.match_image_box(template=template, image=box, precision=0.97, multi=1)


def explore_caves():
    pass



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
                delay_secs(_ITV_MATCH_IMAGE)
            else:
                return center
    return False

##@@@@========================================================================
##@@@@ Execute Test
if __name__ == "__main__":
    pass