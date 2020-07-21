#-*- coding:utf-8 -*-
import cv2
import numpy as np
from matplotlib import pyplot as plt

# image = cv2.imread('../images/test/perspective2.png')
# #image = cv2.imread('../images/test/perspective2_floor.png')
# img = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
# [x,y] 좌표점을 4x2의 행렬로 작성
# 좌표점은 좌상->좌하->우상->우하
## perspective box(perspective -> floor plane 좌상->좌하->우상->우하)

pts1 = np.float32([[406, 0], [0, 1079], [1513, 0], [1919, 1079]])

# (c[0], c[1]), [x[0], x[1]] -> [m[0], m[1]] : (지도 중앙 좌표), [스크린 좌표] -> [지도 좌표]
# (300, 300), [222, 900] -> [172, 212] / [222, 160] -> [114, 435] / [1642, 900] -> [418, 212] / [1680, 314] -> [449, 366]
# 좌표값 : 스크린 중앙 기준, 지도 [0, 0] 기준 보정: [960, 540] / (300, 300)



## perspective box(floor plane -> perspective 좌상->좌하->우상->우하)
#pts1 = np.float32([[24, 0], [420, 1079], [895, 0], [1499, 1079]])

# 좌표의 이동점[[0, 0], [0, 1079], [1919, 0], [1919, 1079]]
# pts2 = np.float32([[0, 0], [0, 1079], [1919, 0], [1919, 1079]])

# ## horizontal line
for i in range(1, 18):
    if i == 9:
        color = (255, 0, 0)
    else:
        color = (255, 255, 255)
    cv2.line(img, (0, i*60), (1919, i*60), color, 2)

## vertical line
for i in range(1, 32):
    if i == 16:
        color = (255, 0, 0)
    else:
        color = (255, 255, 255)
    cv2.line(img, (i*60, 0), (i*60, 1079), color, 2)


M = cv2.getPerspectiveTransform(pts1, pts2)
#M = np.linalg.inv(M)
#M = cv2.getPerspectiveTransform(pts2, pts1)

print(M)

#print('M: {}, type of M: {}'.format(M, type(M)))

### 한 점(1 point)
#p = [75, 148, 1]
#X = M.dot(np.array(p))
#print([round(X[0]/X[2]), round(X[1]/X[2])])


### 여러 점
# original = np.array([((75, 148), (112, 100), (150, 75))], dtype=np.float32)
# converted = cv2.perspectiveTransform(original, M)
# print(converted)


### 이미지
# dst = cv2.warpPerspective(img, M, (1920, 1080))
# cv2.imwrite('../images/test/perspective2_carsian.png', cv2.cvtColor(dst, cv2.COLOR_RGB2BGR))

# plt.subplot(121),plt.imshow(img),plt.title('Original(Perspective)')
# plt.subplot(122),plt.imshow(dst),plt.title('FloorPlan(Cartesian)')
# # plt.subplot(121),plt.imshow(img),plt.title('FloorPlan(Rectangular)')
# # plt.subplot(122),plt.imshow(dst),plt.title('Original(Perspective)')
# plt.show()