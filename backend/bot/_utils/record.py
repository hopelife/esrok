# -*- coding:utf-8 -*-
"""
Brief: Record Module Functions

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


### find_unit => 이미지 비교(문자 인식) 1개
# name(key): 기록 객체 이름 / target: 비교 대상(기준, 이미지 or 문자열 or None) / image: 비교 대상(현재 이미지, 좌표) / skill: 이미지 비교 or 문자 인식

### find_units => 이미지 비교를 여러번(행렬 방식 이미지 배열) 반복해야 하는 경우 이동 방법(mouse 단순 이동, scroll 이동) 제시
## objects [{'name':'', 'target':'', 'skill':''}]
## positions x*y, box[x0, y0, x1, y1], number of objects = 
## skips : 건너뛰는 항목
##### example
## 'Economic-Buffs' : [{'Building-Speed': [{'Alliance-Technology': {'name': 'lbl_Alliance-Technology', 'image':[], }

### items
### label(key) => 문자 인식 + 비교 or 이미지 비교 / value(val) => 문자 인식 + 인식 결과 교정
### 



def who_am_i(prop=['id', 'nick']):
    """
    Brief: Find out Character's properties. id, nick, civilization, age, cityhall level, etc
    Args:
    Returns:
    """
    pass


def Findout_buildings(prop=['id', 'nick']):
    """
    Brief: Find(Figure) out buildings properties by scanning screen. level, coordinate, etc
    Args:
    Returns:
    """
    pass


def Findout_Special_Object(prop=['caves', 'villages']):
    """
    Brief: 
    Args:
    Returns:
    """
    pass


def Findout_commanders(prop=['id', 'nick']):
    """
    Brief: Find(Figure) out buildings properties by scanning screen. level, coordinate, etc
    Args:
    Returns:
    """
    pass


def find_records_alliance():
    pass


def find_records_alliances():
    pass


def find_member_record():
  pass


def find_member_records():
  pass


def find_event_list():
  pass


def find_records_alliance_members():
  pass