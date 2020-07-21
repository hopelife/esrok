# -*- coding:utf-8 -*-
##@@@@========================================================================
##@@@@ Libraries

##@@@-------------------------------------------------------------------------
##@@@ Basic Libraries

##@@@-------------------------------------------------------------------------
##@@@ User Libraries
# from _config import _ENV, oss, emulators
from basics import *
# from _actions import *

##@@@@========================================================================
##@@@@ Constants


##@@@-------------------------------------------------------------------------
##@@@ From:: External Files .py

#DATA_TYPES = file_to_json('../_files/res_data_type.json')
UIS = file_to_json('../_config/uis.json')

##@@@-------------------------------------------------------------------------
##@@@ From:: here itself
_OS = oss[_ENV['_OS']]
_UI = emulators[_ENV['_EMULATOR']]

##@@@@========================================================================
##@@@@ Functions

##@@@-------------------------------------------------------------------------
##@@@ TurnOn/Off, LogIn/Off, Catch Errors, 

def turnOn_emulator(os='', ):
    # checkOnoff()
    images = [
        '',
        '',
    ]
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


def scount(coord=[], scope='', direction=[1,0], angle=360):
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
        #         'BTN_CLOSE': {'xy': [1570, 150], 'fn':''},
        #         'BTN_Donate': {'xy': [1414, 812], 'fn':''},
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
        pass


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
        # receive_VIP()
        # time.sleep(2)
        # do_AllianceHelp()
        # time.sleep(2)
        # #do_AllianceTechnology()
        # #do_AllianceTerritory()
        # time.sleep(2)
        # do_AllianceGifts()
        print(UIS['btn_Mod_NewTroops_Title'])