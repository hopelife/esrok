import numpy as np

# a = [['A,B,C,D'], ['1,2,3,4'], ['5,6,7,8']]
# a = [i[0].split(',') for i in a]
# a = [['A','B','C','D'], [1,2,3,4], [5,6,7,8]]
# print([dict(zip(a[0], v)) for v in a[1:]])


data = [['', '', '', '', '', '', '', ''], ['', '', '', '', '', '', '', ''], ['', '', '', '', '', '', '', ''], ['', '', '', '', '', '', '', ''], ['', 'one', '', '', '', '', '', ''], ['', '03-01-1900', 'two', 'three', 'Buy', '', '', ''], ['', 'timestamp', '', '6', 'Sell', '', '', ''], ['', '', 'value', 'one', 'two', '', 'three', ''], ['', '', '', '', '', '', '', ''], ['', '', '', '', '', '', '', ''], ['', '', '', '', '', '', '', ''], ['', '09-04-2019', '10', '', '2', '', '', '3'], ['', '09-03-2019', '2', '', 'Sell', '', '', ''], ['', '', '', '', '', '', '', ''], ['', '', '', '', '', '', '', ''], ['', '', '', 'something', '', '', '', '']]


len_cols = len(data[0])
len_rows = len(data)
f_data = np.array(data).flatten()


#print(data)
print(f_data)
# print('len_cols: {}, len_rows: {}'.format(len_cols, len_rows))

# ## find first filled row
# for i, v in enumerate(f_data):
#     if v != '':
#         print('i: {}, v: {}'.format(i, v))
#         print((i+1)//len_cols + 1)
#         first_filled_row = (i+1)//len_cols + 1
#         break

# #[x+1 for x in l if x >= 45 else x+5]
# #a = next(i for i in userInput if i in wordsTask)

# ## find first filled column
# findit = False
# for j in range(0, len_rows):
#     for i, v in enumerate(f_data[j::len_cols]):
#         print('j: {}, v: {}'.format(j, v))
#         if v != '':
#             print(j+1)
#             first_filled_col = j + 1
#             findit = True
#             break
#     if findit == True:
#         findit = False
#         break


# data2 = data[first_filled_row-1:]
# print(data2)
# data3 = [v[first_filled_col-1:] for v in data2]
# print(data3)

# ## find header
# for i, row in enumerate(data):
#     if v != '':
#         print('i: {}, v: {}'.format(i, v))
#         print((i+1)//len_cols + 1)
#         first_filled_row = (i+1)//len_cols + 1
#         break

# ## 
# # import numpy as np
# # import cv2 as cv
# # drawing = False # true if mouse is pressed
# # mode = True # if True, draw rectangle. Press 'm' to toggle to curve
# # ix,iy = -1,-1

# # # mouse callback function
# # def draw_circle(event,x,y,flags,param):
# #     global ix,iy,drawing,mode
# #     if event == cv.EVENT_LBUTTONDOWN:
# #         drawing = True
# #         ix,iy = x,y
# #     elif event == cv.EVENT_MOUSEMOVE:
# #         if drawing == True:
# #             if mode == True:
# #                 #cv.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)
# #                 cv.line(img,(ix,iy),(x,y),(0,0,255),10)
# #             else:
# #                 cv.circle(img,(x,y),5,(0,0,255),-1)
# #     elif event == cv.EVENT_LBUTTONUP:
# #         drawing = False
# #         if mode == True:
# #             #cv.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)
# #             cv.line(img,(ix,iy),(x,y),(0,0,255),10)
# #         else:
# #             cv.circle(img,(x,y),5,(0,0,255),-1)


# # # cv2.line(img,(ix,iy),(x,y),(0,0,255),10)
# # # ix=x
# # # iy=y

# # img = np.zeros((512,512,3), np.uint8)
# # cv.namedWindow('image')
# # cv.setMouseCallback('image',draw_circle)
# # while(1):
# #     cv.imshow('image',img)
# #     k = cv.waitKey(1) & 0xFF
# #     if k == ord('m'):
# #         mode = not mode
# #     elif k == 27:
# #         break
# # cv.destroyAllWindows()

# # # sheet_data = [{
# # #     "timestamp": "09-04-2019",
# # #     "value": "10.0",
# # #     "company_name": "Xbox",
# # #     "product": "Buy"
# # # }, {
# # #     "timestamp": "09-03-2019",
# # #     "value": "2.0",
# # #     "company_name": "something",
# # #     "product": "Sell"
# # # }]

# # # headers = [key for key, val in sheet_data[0].items()]

# # # print(headers)