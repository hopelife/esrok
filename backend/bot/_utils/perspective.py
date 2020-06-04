#-*- coding:utf-8 -*-
import cv2
import numpy as np
from matplotlib import pyplot as plt

# img = cv2.imread('images/perspective.jpg')
img = cv2.imread('../images/test/perspective1.png')
# [x,y] 좌표점을 4x2의 행렬로 작성
# 좌표점은 좌상->좌하->우상->우하
#pts1 = np.float32([[504,1003],[243,1525],[1000,1000],[1280,1685]])
pts1 = np.float32([[75, 148], [36, 228], [149, 148], [183, 228]])

# 좌표의 이동점
pts2 = np.float32([[10,10],[10,500],[500,10],[500,500]])

# pts1의 좌표에 표시. perspective 변환 후 이동 점 확인.
cv2.circle(img, (75, 148), 5, (255,0,0),-1)
cv2.circle(img, (36, 228), 5, (0,255,0),-1)
cv2.circle(img, (149, 148), 5, (0,0,255),-1)
cv2.circle(img, (183, 228), 5, (0,0,0),-1)

M = cv2.getPerspectiveTransform(pts1, pts2)

#print('M: {}, type of M: {}'.format(M, type(M)))

### 한 점(1 point)
p = [75, 148, 1]

#p = p.append(1)

#print(p)

X = M.dot(np.array(p))

print([round(X[0]/X[2]), round(X[1]/X[2])])


### 여러 점
# original = np.array([((75, 148), (112, 100), (150, 75))], dtype=np.float32)

# converted = cv2.perspectiveTransform(original, M)
# print(converted)


### 이미지
# dst = cv2.warpPerspective(img, M, (600,600))

# plt.subplot(121),plt.imshow(img),plt.title('image')
# plt.subplot(122),plt.imshow(dst),plt.title('Perspective')
# plt.show()