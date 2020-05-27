# -*- coding:utf-8 -*-
##@@@@========================================================================
##@@@@ Libraries

##@@@-------------------------------------------------------------------------
##@@@ Basic Libraries
import os
import sys
from pathlib import Path
import time
from datetime import date, timedelta, datetime
#from bson.json_util import dumps
import json
import re
import numpy as np
import random


##@@@-------------------------------------------------------------------------
##@@@ Installed(conda/pip) Libraries
import pyautogui as pag
import cv2


##@@@-------------------------------------------------------------------------
##@@@ User Libraries
sys.path.append(os.path.join(os.path.dirname(sys.path[0]), '_utils'))
from _basics import *

##@@@@========================================================================
##@@@@ Constants


##@@@-------------------------------------------------------------------------
##@@@ From:: External Files .py
# sys.path.append(os.path.join(os.path.dirname(sys.path[0]), '_utils'))
sys.path.append(os.path.join(os.path.dirname(sys.path[0]), '_config'))
from _settings import _ENV, _PATH



## @@brief::
## @@note::
def beginROK(civ='_CHINA'):
    series = [
        [1428, 890], # select nation : 중국
        [1580, 730], # receive starting commander :
        [1730, 78], # click skip :
        [150, 786], # farm1
        [432, 712],
        [1078, 542]
    ]
    clickMouseSeries(series, 0.5)
    print('testing....')
    delay(3)
    series = [
        [962, 674], # collect food
        [60, 1020],
    ]
    clickMouseSeries(series, 0.5)
    delay(3)
    return 0


## @@brief::
## @@note::
def login(account={'_ID':'', '_PW':''}, civ='_CHINA'):
    pass


## @@brief::
## @@note::
def createCharacter(account={'_ID':'', '_PW':''}, civ='_CHINA'):
    series = [
        [1428, 890], # select nation : 중국
        [1580, 730], # receive starting commander :
        [1730, 78] # click skip :
    ]
    clickMouseSeries(series, 0.5)
    pass



##@@@@========================================================================
##@@@@ Execute Test
if __name__ == "__main__":
    beginROK(civ='_CHINA')
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