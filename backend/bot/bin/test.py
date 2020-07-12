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
#import time
# import keyboard
#from pynput.keyboard import Listener, Key
from pynput import keyboard


##@@@-------------------------------------------------------------------------
##@@@ Installed(conda/pip) Libraries
import pyautogui as pag

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

def on_press(key):
    try:
        print('alphanumeric key {0} pressed'.format(
            key.char))
    except AttributeError:
        print('special key {0} pressed'.format(
            key))

def on_release(key):
    print('{0} released'.format(
        key))
    if key == keyboard.Key.esc:
        # Stop listener
        return False

# while True:  # making a loop
#     try:  # used try so that if user pressed other than the given key error will not be shown
#         if keyboard.is_pressed('q'):  # if key 'q' is pressed 
#             print('You Pressed A Key!')
#             break  # finishing the loop
#         else:
#             pass
#     except:
#         break  # if user pressed a key other than the given key the loop will break

# def handlePress( key ):
#     print( 'Press: {}'.format( key ) )

# def handleRelease( key ):
#     print( 'Released: {}'.format( key ) )

#     # 종료
#     if key == Key.esc:
#         return False

# with Listener(on_press=handlePress, on_release=handleRelease) as listener:
#     listener.join()


# ##@@@@========================================================================
# ##@@@@ Execute Test
# if __name__ == "__main__":
#     # Collect events until released
#     with keyboard.Listener(
#             on_press=on_press,
#             on_release=on_release) as listener:
#         listener.join()

#     # while True:
#     #     pos = pag.position()
#     #     if pag.click():
#     #         print(pos)
#     #     try:
#     #         if keyboard.is_pressed('q'):
#     #             break
#     #         else:
#     #             pass
#     #     finally:
#     #         pass
