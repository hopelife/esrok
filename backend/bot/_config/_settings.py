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
    #'_OS': 'WIN',
    '_OS': 'OSX',
    '_MAX_X': 1920,
    '_MAX_Y': 1080,
    '_ZOOM_MAX': 20,
    '_IMG_EXT': '.png',
    '_EMULATOR': 'LDPLAYER',
    '_SCREENSHOT': 'shots/',
    '_MOUSE_DURATION': 0.5,
    '_CLICK_INTERVAL': 1,
}

_PATH = {
    '_ROOT': '../images/',
    '_UIS': '../images/uis/',  ## UI images
    '_MAPS': '../images/maps/',  ## map images
    '_SCREENSHOT': '../images/screenshots/'  ## screenshot images
}


_TESSERACT = {
    '_EXE': 'C:/Program Files/Tesseract-OCR/tesseract.exe',
    '_DATA': '--tessdata-dir "C:\\Program Files\\Tesseract-OCR\\tessdata"',
    #'_EXE': 'C:/Program Files (x86)/Tesseract-OCR/tesseract.exe',
    #'_DATA': '--tessdata-dir "C:\\Program Files (x86)\\Tesseract-OCR\\tessdata"', 
}


_GOOGLE = {
    '_JSON': '../_config/rok_service_account_googledrive.json',
    '_SCOPE': [
        'https://spreadsheets.google.com/feeds',
        'https://www.googleapis.com/auth/drive',
    ],
    '_URLS': {
        'TEST': 'https://docs.google.com/spreadsheets/d/1zwHf6FEcqb_vyHC-3uSlzzE0ln8zoMsW5-YwNzTryLU/edit#gid=0'
    }
}

_MAP = {
    'WHOLE': [1200, 1200],
    'ONE_MIN': [8, 6],
    'ONE_MAX': [320, 240],
    'EDGE': [230, 170, 1600, 900]
    #'EDGE': [210, 150, 1610, 940]
}
