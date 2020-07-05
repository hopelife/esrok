# -*- coding:utf-8 -*-
"""
Function: Set Of Game Bot Emulator Configurations

Structure:
    - _ENV
    - _PATH
    - _TESSERACT
    - _GOOGLE

Usage: from config._settings import *
"""

_ENV = {
    #'OS': 'WIN',
    'OS': 'OSX',
    'MAX_X': 1920,
    'MAX_Y': 1080,
    'ZOOM_MAX': 50,
    'IMG_EXT': '.png',
    'EMULATOR': 'LDPLAYER',
    'MOUSE_DURATION': 0.5,
    'CLICK_INTERVAL': 1,
}

_PATH = {
    'ROOT': '../images/',
    'UIS': '../images/uis/',  ## UI images
    '_UIS': '../images/_uis/',  ## UI images
    'OBJECTS': '../images/objects/',  ## UI images
    'MAPS': '../images/maps/',  ## map images
    'SCREENSHOT': '../images/screenshots/'  ## screenshot images
}

_TESSERACT = {
    'WIN': {
        'EXE': 'C:/Program Files/Tesseract-OCR/tesseract.exe',
        'DATA': '--tessdata-dir "C:\\Program Files\\Tesseract-OCR\\tessdata"',
    #'EXE': 'C:/Program Files (x86)/Tesseract-OCR/tesseract.exe',
    #'DATA': '--tessdata-dir "C:\\Program Files (x86)\\Tesseract-OCR\\tessdata"', 
    },
    'OSX': {
        'EXE': '/usr/local/Cellar/tesseract/4.1.1/bin/tesseract',
        'DATA': '--tessdata-dir "/usr/local/Cellar/tesseract-lang/4.0.0/share/tessdata/"',
    }
}


_GOOGLE = {
    'JSON': '../_config/rok_service_account_googledrive.json',
    'SCOPE': [
        'https://spreadsheets.google.com/feeds',
        'https://www.googleapis.com/auth/drive',
    ],
    'URLS': {
        'TEST': 'https://docs.google.com/spreadsheets/d/1zwHf6FEcqb_vyHC-3uSlzzE0ln8zoMsW5-YwNzTryLU/edit#gid=0'
    }
}

_MAP = {
    'WHOLE': [1200, 1200],
    'ONE_MIN': [8, 6],
    'ONE_MAX': [320, 240],
    'EDGE': [230, 170, 1600, 900],
    #'EDGE': [210, 150, 1610, 940]
    ## Transformation Matrix Carsian(Rectangular) Coordinate To Perspective Coordinate
    'M_R2P': [
        [ 5.76862949e-01, -3.76274328e-01,  4.06000000e+02],
        [ 3.69449873e-17,  5.76862949e-01,  1.24374716e-13],
        [-2.51155380e-20, -3.92156673e-04,  1.00000000e+00]
    ],
    ## Transformation Matrix Perspective Coordinate Coordinate To Carsian(Rectangular)
    'M_P2R': [
        [ 1.73351400e+00,  6.52276816e-01, -7.03806685e+02],
        [-1.11022302e-16,  1.73351400e+00, -1.70530257e-13],
        [ 0.00000000e+00,  6.79809084e-04,  1.00000000e+00]
    ],
    'CLOCKWISE' : [
        [0, 0],
        [-0.725, 0],  # 우 right
        [0, -0.95],  # 하 bottom
        [0.73, 0],  # 좌 left
        [0.73, 0],  # 좌 left
        [0, 1.353],  # 상 top
        [0, 1.353],  # 상 top
        [-0.726, 0],  # 우 right
        [-0.726, 0],  # 우 right
        [0, -0.942],  # 하 bottom
    ],
    'R_UNITS' : [
        [0, 0],
        [-1, 0],  # 우 right
        [0, -1],  # 하 bottom
        [1, 0],  # 좌 left
        [1, 0],  # 좌 left
        [0, 1],  # 상 top
        [0, 1],  # 상 top
        [-1, 0],  # 우 right
        [-1, 0],  # 우 right
    ],
    'SCAN_BOX': [710, 390, 1210, 690]  # 부족 마을, 동굴 탐험용 scan box (minimum size map, 좌표 100 이동 기준)

}


_FILTER : {
    'yellow_lower': [20, 100, 100],
    'yellow_upper': [30, 255, 255],
}