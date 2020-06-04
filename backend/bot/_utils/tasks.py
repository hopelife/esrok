# -*- coding:utf-8 -*-
##@@@@========================================================================
##@@@@ Libraries

##@@@-------------------------------------------------------------------------
##@@@ Basic Libraries

##@@@-------------------------------------------------------------------------
##@@@ User Libraries
from _config import _ENV, oss, emulators
from _basics import *
from _actions import *

##@@@@========================================================================
##@@@@ Constants


##@@@-------------------------------------------------------------------------
##@@@ From:: External Files .py

#DATA_TYPES = file_to_json('../_files/res_data_type.json')

##@@@-------------------------------------------------------------------------
##@@@ From:: here itself
_OS = oss[_ENV['_OS']]
_UI = emulators[_ENV['_EMULATOR']]

##@@@@========================================================================
##@@@@ Functions

##@@@-------------------------------------------------------------------------
##@@@ TurnOn/Off, LogIn/Off, Catch Errors, 

def turnOn_emulator(os='', ):
  pass


def turnOff_emulator(os='', ):
  pass


def switch_account(id='', pw=''):
  pass


def login_character(id='', ):
  pass


def logoff_character(nick='', ):
  pass


def create_character(server='', civil='CHINA'):
  pass


def catch_errors():
  pass

##@@@-------------------------------------------------------------------------
##@@@ Scheduler




##@@@-------------------------------------------------------------------------
##@@@ Account / Character

## @@brief:: 
## @@note:: 


def select_nation(nation='china'):
    pass


def receive_starting_commander():
    pass


def build_building(building='farm', age='STONE'):
    pass


def upgrade_building(building='farm', level=2):
    pass


## @@brief:: VIP Point / Gift 수령 (period: 1day)
## @@note:: 
def receive_VIP():
    series = [
        _UI['VIP']['BUTTON']['xy'], 
        _UI['VIP']['POP_VIP']['BTN_ClaimPoints']['xy'], 
        _UI['VIP']['POP_VIP']['BTN_ClaimGifts']['xy']
    ]
    clickMouseSeries(series, 0.5, 2)
    clickMouse( _UI['VIP']['POP_VIP']['BTN_CLOSE']['xy'])
    return 0



## @@brief:: 연맹 자원 수령
## @@note:: 
def do_AllianceTerritory():
    # 하단 메뉴 펼침
    unfoldMenuBtn()
    # 클릭
    series = [
        _UI['MENU']['BTN_Alliance']['xy'], 
        _UI['MENU']['POP_Alliance']['BTN_Territory']['xy'], 
        _UI['MENU']['POP_Alliance_Territory']['BTN_Claim']['xy'],
        _UI['MENU']['POP_Alliance_Territory']['BTN_CLOSE']['xy'],
        _UI['MENU']['POP_Alliance']['BTN_CLOSE']['xy']
    ]
    clickMouseSeries(series, 2)  
    return 0



## @@brief:: VIP Point / Gift 수령 (period: 1day)
## @@note:: 
def do_AllianceHelp():
    # 하단 메뉴 펼침
    unfoldMenuBtn()
    # 클릭
    series = [
        _UI['MENU']['BTN_Alliance']['xy'], 
        _UI['MENU']['POP_Alliance']['BTN_Help']['xy'], 
        _UI['MENU']['POP_Alliance_Help']['BTN_Help']['xy'],
        _UI['MENU']['POP_Alliance_Help']['BTN_CLOSE']['xy'],
        _UI['MENU']['POP_Alliance']['BTN_CLOSE']['xy']
    ]
    clickMouseSeries(series, 0.5)  
    return 0


## @@brief:: 연맹 기술 지원@@@@@@@@@@@@@@@@@@
## @@note:: 
def do_AllianceTechnology():
    # 하단 메뉴 펼침
    unfoldMenuBtn()
    series = [_UI['MENU']['BTN_Alliance']['xy'], _UI['MENU']['POP_Alliance']['BTN_Technology']['xy']]
    clickMouseSeries(series, 2)
    ## 기술 지원 항목 찾기!!!
    #findAllianceTechnology()
    # 'POP_Alliance_Technology_Donate': {
    #     'BTN_CLOSE': {'xy': [1570, 150], 'fn':''},
    #     'BTN_Donate': {'xy': [1414, 812], 'fn':''},
    # },
    ## 팝업창 닫기
    series = [
        _UI['MENU']['POP_Alliance_Technology_Donate']['BTN_CLOSE']['xy'], 
        _UI['MENU']['POP_Alliance_Technology']['BTN_CLOSE']['xy'], 
        _UI['MENU']['POP_Alliance']['BTN_CLOSE']['xy']
    ]
    clickMouseSeries(series, 0.5)
    return 0


## @@brief:: 연맹 자원 수령
## @@note:: 
def do_AllianceGifts():
    # 하단 메뉴 펼침
    unfoldMenuBtn()

    # 선물 팝업 열기
    series = [
        _UI['MENU']['BTN_Alliance']['xy'], 
        _UI['MENU']['POP_Alliance']['BTN_Gifts']['xy'], 
        _UI['MENU']['POP_Alliance_Gifts']['TAB_Rare']['xy'],
        _UI['MENU']['POP_Alliance_Gifts']['ARR_Items']['first'],
    ]
    clickMouseSeries(series, 0.5)

    # 희귀 선물 클릭
    items = _UI['MENU']['POP_Alliance_Gifts']['ARR_Items']
    for _ in range(0, _ENV['_GIFT_MAX']//10 + 1):
        claim = matchImageBox(_ENV['_IMAGES_FOLDER'] + _UI['MENU']['POP_Alliance_Gifts']['BTN_Claim']['fn'])
        if not claim:
            print('claim buttons not exist!!')
            break
        else:
            for _ in range(0, 10):
                btn_2nd = [items['first'][0] + items['offset'][0], items['first'][1] + items['offset'][1]]
                clickMouse(btn_2nd)

    # 일반 선물 클릭
    series = [
        _UI['MENU']['POP_Alliance_Gifts']['TAB_Normal']['xy'],
        _UI['MENU']['POP_Alliance_Gifts']['BTN_ClaimAll']['xy']
    ]
    clickMouseSeries(series, 0.5)  

    # 팝업창 닫기
    series = [
        _UI['MENU']['POP_Alliance_Gifts']['BTN_Confirm']['xy'],
        _UI['MENU']['POP_Alliance_Gifts']['BTN_CLOSE']['xy'],
        _UI['MENU']['POP_Alliance']['BTN_CLOSE']['xy']
    ]
    clickMouseSeries(series, 0.5)  
    return 0



## @@brief:: 연맹 자원 수령
## @@note:: 
def do_CampaignGifts():
    # 하단 메뉴 펼침
    unfoldMenuBtn()




        ## Images
        'Images': {
            'resourceGem': 'img_resourceGem___100_82.png'
        }


## @@brief:: 보석 수집
## @@note:: 
def gatherGem(by='image'):
    findLocation()
    sendArmy()
    return 0


## @@brief:: 해당 좌표 찾기
## @@note:: 
def findLocationByImage(image='', viewMode='', sectors=[1, 1]):
    setViewMode(viewMode)
    findLocation()



# select nation	로마 [, ] 중국[1428, 890]
# starting commander	[1580, 730]
# click skip	[1730, 78]
# farm1	[150, 786]	[432, 712]	[1078, 542]	delay 5
# collect food	click	[962, 674]	
# skip	click		[60, 1020]	<5>
# go out of the city	click	[138, 946]	
# skip	click	[60, 1020]	<10>
# return to the city	click	[138, 946]
# skip	click	[60, 1020]	<5>
# infantry training	click	[782, 652]
# [964, 830] -> [1420, 862] -> (10) -> [780, 650] -> skip(2)
# upgrade wall	[958, 470] -> [940, 700] -> [1428, 800] -> skip(2)
# tavern	[130, 784]	[124, 752]	[420, 766]	[590, 340]
# recruit	[666, 732]	[1330, 876]	delay 10	[324, 882]	[588, 892]	[106, 90]	-> skip(2)

# defeat barbarian	[136, 952]	[130, 780]	[428, 708]	skip(2)	[940, 524]	[1325, 700]	[1464, 242]	[322, 668]	[152, 300]	[1345, 913]	delay 14	skip(3)
# defeat barbarian2	[876, 460]	[1230, 612]	[1454, 304]	delay(20)	skip(5)	[318, 880]	[138, 946]	skip(3)
# follow the quest	[118, 264]	[1444, 364]	[1036, 730]	[1422, 806]	delay(5)	[118, 264]	[1448, 366]	[1448, 366]	skip(2)	
# build a scout camp	[130, 786]	[136, 742]	[412, 747]	[1240, 406]	delay(5)	[1302, 798]	[1450, 488]	[1174, 758]	[1454, 270]	skip(2)
# quests	[136, 952]	[116, 270]	[1432, 	362]	[1432, 	362]	[134, 790]	
# lumber mill	[130, 784]	[420, 766]	[1496, 236]	delay(5)	[1392, 648]	[1412, 800]	delay(20)


# createNewCharacter
# recoverFog
# gatherFood
# gatherWood
# gatherStone
# gatherGold
# gatherGem
# trainTroops

# upgradeBuilding
# buildBuilding



def doAllianceHelp():
    pass
# doAllianceWar
# receiveAllianceGifts
# giveAllianceTechnology
# buyAllianceShop
# receiveAllianceTerritory

# huntBarbarians
# defeatBarbarianFort
# joinBarbarianFort
# tourSunsetCanyon
# tourLostCanyon




# hazard_cleanup
# the_gatherer
# the_lumberjack
# rock_star
# gold_digger
# sword_of_the_king
# horse_of_the_king
# the_great_physician
# help_each_other
# skillful_craftsman
# age_of_science
# strange_fate
# food_growth
# wood_growth
# do_more_with_less
# gathering_enhancement
# stone_growth
# gold_growth
# power_of_knowledge
# warrior_of_the_sun

if __name__ == "__main__":
    receive_VIP()
    time.sleep(2)
    do_AllianceHelp()
    time.sleep(2)
    #do_AllianceTechnology()
    #do_AllianceTerritory()
    time.sleep(2)
    do_AllianceGifts()