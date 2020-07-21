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
##@@@ Mysterious Caves / Tribal Villages


def save_screenshot_map_explore():
    zoom_out(nth=60)
    center = [80, 52]
    for i in range(0, 4):
        for j in range(0, 4):
            #center = [80 + 100*i, 52]
            center = [160 + 320*j, 100 + 320*i]
            go_by_coordinate(center)
            time.sleep(3)
            path = _shots + 'map_min_full_' + str(center[0]) + '_' + str(center[1]) + '.png'
            save_screenshot(box=[1, 1, _ENV['MAX_X'], _ENV['MAX_Y']], path=path)
        # path2 += 'map_min_area_' + str(center[0]) + '_' + str(center[1]) + '.png'
        # save_screenshot(box=_MAP['SCAN_BOX'], path=path2)
    # for i in range(10, 11):
    #     center = [80 + 100*i, 52]
    #     locs = search_objects_in_map(location=center)
    #     coords = search_coords_in_map(center=center, locs=locs)
    #     print({'c':center, 'l':coords})


def search_objects_in_map(obj='village_unvisited', location=[500, 300], box=_MAP['SCAN_BOX'], precision=0.51, ms='min'):
    zoom_out(nth=60)
    go_by_coordinate(location)
    time.sleep(3)

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

    #coords = match_image_box(template=template, image=box, mask=mask, precision=precision, show=True, multi=1, color=(yellow_lower, yellow_upper))
    coords = match_image_box(template=template, image=box, mask=mask, precision=precision, show=False, multi=1, color=(yellow_lower, yellow_upper))

    print(coords)

    return coords


def search_coords_in_map(center=[500, 300], locs=[[916, 399], [1192, 420], [1131, 443], [886, 446], [820, 566]]):

    _coords = []
    coords = [] # map coords
    for loc in locs:
        time.sleep(1)
        zoom_out(nth=60)
        time.sleep(1)
        go_by_coordinate(center)
        time.sleep(1)
        click_mouse(loc)
        time.sleep(5)
        click_mouse([_ENV['MAX_X']//2, _ENV['MAX_Y']//2])
        time.sleep(1)
        marker = add_marker_village()
        # coord = catch_village()
        # if marker is not False:
        #     # _coords.append(coord)
        #     coord = get_coordinate()
        #     coords.append(coord)
        #     # add_marker_village()
        #     print('village: {}'.format(coord))

    #print(_coords)
    # return coords


def visit_villages_by_coords(coords=[]):
    for coord in coords:
        if get_viewmode() is 'CITY_VIEW':
            set_viewmode('WORLD_VIEW')

        go_by_coordinate(coord)
        #time.sleep(1)
        btn = _imgs + 'img_TribalVillage.png'
        village = match_image_box(template=btn, image=[_ENV['MAX_X']//2-350, _ENV['MAX_Y']//2-250, _ENV['MAX_X']//2+350, _ENV['MAX_Y']//2+250], precision=0.98)
        print('village is at {}'.format(village))
        click_mouse(village)
        click_mouse(village)
        click_mouse(village)
        #time.sleep(1)




def catch_village():
    btn_welcome = _imgs + 'btn_TribalVillage_TribalVillage.png'
    return match_image_box(template=btn_welcome, precision=0.98)


def add_marker_village():
    # btns = [
    #     match_image_box(template=_imgs + 'btn_Set_Marker.png', precision=0.99),
    #     [966, 790]
    #     #match_image_box(template=_imgs + 'btn_AddMarker_Confirm.png', precision=0.995)
    # ]
    btn = match_image_box(template=_imgs + 'btn_Set_Marker.png', precision=0.99)
    if click_mouse(btn) is not False:
        time.sleep(3)
        click_mouse([966, 790]) #Add Marker Confirm
    time.sleep(2)
    # click_mouse_series(btns, interval=4, clicks=1)



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

    # points = [[_ENV['MAX_X']//2,_ENV['MAX_Y']//2], [0, 0], [0,_ENV['MAX_Y']],[_ENV['MAX_X'],0]]
    # #points = [[960, 540], [1060, 540], [1060, 640], [960, 640]]
    # #trans = transform_perspective(points, trans='inverse')
    # print(points)
    #trans = transform_perspective([_ENV['MAX_X']//2,_ENV['MAX_Y']//2])
    # trans = transform_perspective(points, trans='normal')
    #trans = transform_perspective(points)
    #trans = transform_perspective_relative(points, trans='inverse', center=[_ENV['MAX_X']//2,_ENV['MAX_Y']//2])
    # trans = transform_perspective_relative(points, trans='normal', center=[_ENV['MAX_X']//2,_ENV['MAX_Y']//2])
    # # trans2 = [round(trans[0]), round(trans[1])+540-395]
    # print(trans)
    # print(trans2)
    # print([round(trans[0]), round(trans[1])+540-395])

#     #points1 = [[220, 928], [240, 180], [1708, 924], [1586, 254], [0, 0], [960, 540]]
#     #points1 = [896, 97]
#     points1 = [[252, 859], [298, 751], [304, 661], [285, 598], [290, 479], [363, 408], [367, 388], [376, 334]]
#     #points2 = [[176, 208], [124, 424], [426, 208], [446, 395]]
#     ### caves
#     points1 = [[266, 812], [385, 586], [431, 303], [439, 288], [627, 185], [594, 396], [604, 558], [426, 861], [943, 675], [816, 283], [966, 293], [1191, 257], [1278, 362], [1348, 362], [1309, 492], [1422, 271], [1190, 256], [1502, 620], [1662, 928], [1781, 859], [1809, 826], [1660, 399], [1421, 271]]
#     #points2 = [[38, 43], [48, 98], [40, 186], [41, 191], [79, 232], [81, 153], [89, 105], [68, 32], [157, 75], [127, 193], [160, 189], [213, 203], [229, 165], [244, 165], [231, 123], [266, 198], [212, 204], [264, 88], [278, 18], [302, 32], [309, 39], [310, 153], [266, 198]]
#     #points2 = [[79, 233], [72, 204], [26, 131], [23, 124], [37, 43], [80, 155], [101, 192], [100, 233], [155, 201], [116, 95], [159, 88], [232,
# 42], [237, 102], [256, 97], [225, 149], [311, 29], [232, 41], [245, 173], [237, 214], [258, 204], [266, 199], [332, 93], [310, 29]]
#     mcs = compute_map_coords_of_screen([160, 110], points1)
#     print(mcs)
