#-*- coding:utf-8 -*-
import cv2
import numpy as np

# (c[0], c[1]), [x[0], x[1]] -> [m[0], m[1]] : (지도 중앙 좌표), [스크린 좌표] -> [지도 좌표]
# (300, 300), [222, 900] -> [172, 212] / [222, 160] -> [114, 435] / [1642, 900] -> [418, 212] / [1680, 314] -> [449, 366]
# 좌표값 : 스크린 중앙 기준, 지도 [0, 0] 기준 보정: [960, 540] / (300, 300)


# points1 = [[222, 900], [222, 160], [1642, 900], [1680, 314]]
# points2 = [[172, 212], [114, 435], [418, 212], [449, 366]]

# points1 = [[220, 928], [240, 180], [1708, 924], [1586, 254]]
# points2 = [[176, 208], [124, 424], [426, 208], [446, 395]]
# center_s = [960, 540]
# center_m = [300, 300]

## samples: 1760 server mysterious caves
points1 = [[266, 812], [627, 186], [1811, 825], [1421, 273]]
points2 = [[79, 223], [37, 33], [267, 189], [310, 20]]
center_s = [960, 540]
center_m = [160, 100]

points1_r = [[p1[0] - center_s[0], p1[1] - center_s[1]] for p1 in points1]
points2_r = [[p2[0] - center_m[0], p2[1] - center_m[1]] for p2 in points2]

print(points1_r)
print(points2_r)

## perspective box(floor plane -> perspective 좌상->좌하->우상->우하)
pts1 = np.float32(points1_r)

# 좌표의 이동점[[0, 0], [0, 1079], [1919, 0], [1919, 1079]]
pts2 = np.float32(points2_r)


M = cv2.getPerspectiveTransform(pts1, pts2)
print(M)

#print('M: {}, type of M: {}'.format(M, type(M)))

## 한 점(1 point)
# S_M = [
#     [ 1.98421171e-01,  1.14607521e-02, -9.16548312e-01],
#     [-3.41189154e-03, -2.81860890e-01,  4.84412021e-01],
#     [ 3.87714948e-05,  4.09896098e-04,  1.00000000e+00]
# ]

# p = [-740, 388, 1]
# p = [0, 0, 1]
# # p = [626, -286, 1]

# # M = np.matrix(S_M)
# X = M.dot(np.array(p))
# # print(M)
# print(X)
# print([round(X[0]/X[2]), round(X[1]/X[2])])
# # X = M.dot(np.array(p))
# # print([round(X[0]/X[2]), round(X[1]/X[2])])


# ## 여러 점
# # original = np.array([((75, 148), (112, 100), (150, 75))], dtype=np.float32)
# original = np.array([((-740, 388), (-720, -360), (748, 384), (626, -286))], dtype=np.float32)
# converted = cv2.perspectiveTransform(original, M)
# print(converted)
