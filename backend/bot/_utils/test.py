import numpy as np
import cv2 as cv
drawing = False # true if mouse is pressed
mode = True # if True, draw rectangle. Press 'm' to toggle to curve
ix,iy = -1,-1

# mouse callback function
def draw_circle(event,x,y,flags,param):
    global ix,iy,drawing,mode
    if event == cv.EVENT_LBUTTONDOWN:
        drawing = True
        ix,iy = x,y
    elif event == cv.EVENT_MOUSEMOVE:
        if drawing == True:
            if mode == True:
                #cv.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)
                cv.line(img,(ix,iy),(x,y),(0,0,255),10)
            else:
                cv.circle(img,(x,y),5,(0,0,255),-1)
    elif event == cv.EVENT_LBUTTONUP:
        drawing = False
        if mode == True:
            #cv.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)
            cv.line(img,(ix,iy),(x,y),(0,0,255),10)
        else:
            cv.circle(img,(x,y),5,(0,0,255),-1)


# cv2.line(img,(ix,iy),(x,y),(0,0,255),10)
# ix=x
# iy=y

img = np.zeros((512,512,3), np.uint8)
cv.namedWindow('image')
cv.setMouseCallback('image',draw_circle)
while(1):
    cv.imshow('image',img)
    k = cv.waitKey(1) & 0xFF
    if k == ord('m'):
        mode = not mode
    elif k == 27:
        break
cv.destroyAllWindows()

# sheet_data = [{
#     "timestamp": "09-04-2019",
#     "value": "10.0",
#     "company_name": "Xbox",
#     "product": "Buy"
# }, {
#     "timestamp": "09-03-2019",
#     "value": "2.0",
#     "company_name": "something",
#     "product": "Sell"
# }]

# headers = [key for key, val in sheet_data[0].items()]

# print(headers)