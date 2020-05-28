# from pynput import keyboard

# def on_press(key):
#     try:
#         print('alphanumeric key {0} pressed'.format(key.char))
#     except AttributeError:
#         print('special key {0} pressed'.format(key))

# def on_release(key):
#     print('{0} released'.format(key))
#     if key == keyboard.Key.esc:
#         # Stop listener
#         return False

# # Collect events until released
# with keyboard.Listener( on_press=on_press, on_release=on_release) as listener:
#     listener.join()

# # ...or, in a non-blocking fashion:
# listener = keyboard.Listener(on_press=on_press, on_release=on_release)
# listener.start()


# from pynput import keyboard
# import time
# import sys
import cv2

# def print_msg(msg='testing....', interrup):
#     while True:
#         print(msg)
#         time.sleep(2)


# def exit_by_esc(callback, msg):
#     # Collect events until released
#     #with keyboard.Listener(on_release=on_release) as listener:
#     #    listener.join()

#     # ...or, in a non-blocking fashion:
#     #listener = keyboard.Listener(on_release=on_release)
#     listener = keyboard.Listener(on_release=lambda key: key != keyboard.Key.esc)
#     listener.start()
#     listener.join()
#     callback(msg)

# #lambda x: keyboard.Key.esc
# exit_by_esc(print_msg('this is test message....'))



# from pynput import keyboard
# from time import sleep

# exit_flag = False

# def on_press(key):
#     try:
#         print('alphanumeric key {0} pressed'.format(key.char))
#     except AttributeError:
#         print('special key {0} pressed'.format(key))

# def on_release(key):
#     print('{0} released'.format(key))

#     if key == keyboard.Key.esc:
#         global exit_flag
#         exit_flag = True
#         print("SET EXIT TO {}".format(exit_flag))
#         return False

# with keyboard.Listener(on_press=on_press,
#     on_release=on_release) as listener:

#     print("listen...")

#     while not exit_flag:
#         print("do something...")
#         sleep(2)

#     listener.join()


# while True:
#     try:
#         print("do something")
#         time.sleep(10)
#     except KeyboardInterrupt:
#         print("to be able to exit script gracefully")
#         sys.exit()


while True:
    k = cv2.waitKey(0)
    if k == 27:
        print('I will be back')
        break
    # k = cv2.waitKey(0) & 0xFF
    # # press 'q' to exit
    # if k == ord('q'):
    #     print('I will be back')
    #     break
    # elif k == ord('b'):
    #     print('pressed B')
    # elif k == ord('k'):
    #     print('pressed K')

print('program is out')