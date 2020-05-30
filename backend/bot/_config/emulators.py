# -*- coding:utf-8 -*-
"""
Function: Set Of Game Bot Emulator Configurations

Structure:
  - Constants
    - settings
    - items
    - 


Usage: from config.emulators import *
"""

# total_map_size: 1200 * 1200
# one_screen_size(min): 8*6
# one_screen_size(max): 320*240

KEY_MAP = {
    'OSX': {
        'ZOOM_IN': ['up'],
        'ZOOM_OUT': ['down'],
    },
    'WIN': {
        'ZOOM_IN': ['ctrl', 'up'],
        'ZOOM_IN': ['ctrl', 'down'],
    },
}


LOCATION_ROK_FULL = {
    'btn_GoWorldView': [], ## 월드뷰로 가기 버튼
    'btn_LocationSearch': [670, 38], ## 좌표로 찾기 버튼
    'btn_Pop_LocationSearch_Server': [686, 216],  ## Server 필드
    'btn_Pop_LocationSearch_X': [924, 216],  ## X 좌표 필드
    'btn_Pop_LocationSearch_Y': [1168, 216],  ## Y 좌표 필드
    'npt_Pop_LocationSearch_Field':  [50, 988],  ## 텍스트 입력 필드
    'btn_Pop_LocationSearch_Go': [1330, 214]  ## 좌표로 가기 버튼
}


IMAGE_ROK_FULL = {
    'btn_GoCityView':'btn_GoCityView',
    'btn_GoWorldView':'btn_GoWorldView',
}

# _ENV = {
#     '_OS': 'WIN',
#     '_MAX_X': 1920,
#     '_MAX_Y': 1080,
#     '_EMULATOR': 'LDPLAYER',
#     '_IMAGES_FOLDER': 'images/',
#     '_SCREENSHOT': 'shots/',
#     '_MOUSE_DURATION': 0.5,
#     '_CLICK_INTERVAL': 1,
#     '_AREA_MARGIN': 50,
#     '_GIFT_MAX': 100
# }

# # Operating Systems
# oss = {
#     'WIN': {
#         'OS': {
#             'version': 'windows10'
#         },
#         'DISPLAY': {
#             'resolution': [1920, 1080],
#             'dpi': 0
#         },
#         'ROK_WALLPAPER': {'xy': [110, 866], 'fn':''},
#         'ROK_QUICKLOANCHER': {'xy': [0,0], 'fn':''},
#     }, 
#     'OSX': {
#         'OS': {
#             'version': 'high_sierra'
#         },
#         'DISPLAY': {
#             'resolution': [1920, 1080],
#             'dpi': 0
#         },
#         'BUTTONS': {
#             'ROK_WALLPAPER': {'xy': [110, 866], 'fn':''},
#             'ROK_QUICKLOANCHER': {'xy': [0,0], 'fn':''},
#             'POPUP_AVAST': [1900, 900],
#         }
#     }
# }