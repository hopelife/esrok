# import cv2
import numpy as np

# src = cv2.imread('../images/test/coordinate1.png')
# cv2.imshow('src', src)

# zeros = np.zeros((src.shape[0], src.shape[1]), dtype="uint8")
# #img_b, img_g, img_r = cv2.split(src)

# hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)
# h, s, v = cv2.split(hsv)

# #v2 = cv2.equalizeHist(v)
# #hsv2 = cv2.merge([h, s, v2])
# #dst = cv2.cvtColor(hsv2, cv2.COLOR_HSV2BGR)
# #cv2.imshow('dst', dst)
# #cv2.imshow('s', s)
# sv = cv2.merge([s, s, v])
# sv2 = cv2.cvtColor(sv, cv2.COLOR_HSV2BGR)
# #sv2 = cv2.merge([sv, sv, v])
# # sv3 = cv2.cvtColor(sv2, cv2.COLOR_HSV2BGR)
# # img_b, img_g, img_r = cv2.split(sv3)
# cv2.imshow('sv2', sv2)

# # img_r = cv2.merge([zeros, zeros, img_r])
# # cv2.imshow("R", img_r)

# cv2.waitKey()
# cv2.destroyAllWindows()


### RGB 채널 분리
# import cv2
# import numpy as np

# img_color = cv2.imread('Billiard.jpg', cv2.IMREAD_COLOR )

# img_b,img_g,img_r = cv2.split(img_color)

# zeros = np.zeros((img_color.shape[0], img_color.shape[1]), dtype="uint8")
# img_b = cv2.merge([img_b, zeros, zeros])
# img_g = cv2.merge([zeros, img_g, zeros])
# img_r = cv2.merge([zeros, zeros, img_r])

# cv2.imshow("BGR", img_color)
# cv2.imshow("B", img_b)
# cv2.imshow("G", img_g)
# cv2.imshow("R", img_r)

# cv2.waitKey(0)

# cv2.destroyAllWindows()


## 색상 마스크 적용
import cv2
import matplotlib.pyplot as plt
# matplotlib.image 를 사용하기 위해선 matplotlib 뿐만 아니라 pillow도 깔아야 한다
import matplotlib.image as mpimg

# # 색상 범위 설정
# lower_orange = (100, 200, 200)
# upper_orange = (140, 255, 255)

# lower_green = (30, 80, 80)
# upper_green = (70, 255, 255)

# lower_blue = (0, 180, 55)
# upper_blue = (20, 255, 200)

lower_white = np.array([0,0,168])
upper_white = np.array([172,111,255])


# 이미지 파일을 읽어온다
# img = mpimg.imread("../images/test/test1.png", cv2.IMREAD_COLOR)
img = mpimg.imread("../images/test/coordinate1.png", cv2.IMREAD_COLOR)
# BGR to HSV 변환
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
# 색상 범위를 제한하여 mask 생성
#img_mask = cv2.inRange(img_hsv, lower_orange, upper_orange)
img_mask = cv2.inRange(img_hsv, lower_white, upper_white)
# 원본 이미지를 가지고 Object 추출 이미지로 생성
img_result = cv2.bitwise_and(img, img, mask=img_mask)
# 결과 이미지 생성
imgplot = plt.imshow(img_result)
plt.show()