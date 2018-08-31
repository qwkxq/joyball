import numpy as np

import cv2

from appium import webdriver
from PIL import Image
import time, uuid

BLACK_RGBA = [(57, 57, 57), (58, 58, 58), (59, 59, 59)]

img_path = "D:/imgWork/uuid/src/5.png"
hsv_path = "D:/imgWork/uuid/src/dst/hsv"

# fullImgRgba = Image.open("D:/imgWork/uuid/src/0.png").getdata()
fullImgRgba = Image.open(img_path).getdata()
# fullImgRgba = Image.open("D:/imgWork/uuid/src/5.png").getdata()
# fullImgRgba = Image.open("D:/imgWork/uuid/src/7.png").getdata()

# img = cv2.imread(img_path)
# if img is not None:
#     kernel_2 = np.ones((2, 2), np.uint8)  # 2x2的卷积核
#     kernel_3 = np.ones((3, 3), np.uint8)  # 3x3的卷积核
#     kernel_4 = np.ones((4, 4), np.uint8)  # 4x4的卷积核
#     HSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)  # 把BGR图像转换为HSV格式
#     Lower = np.array([0, 0, 0])  # 要识别颜色的下限
#     Upper = np.array([160, 60, 60])  # 要识别的颜色的上限
#     # mask是把HSV图片中在颜色范围内的区域变成白色，其他区域变成黑色
#     mask = cv2.inRange(HSV, Lower, Upper)
#     # 下面四行是用卷积进行滤波
#     erosion = cv2.erode(mask, kernel_4, iterations=1)
#     erosion = cv2.erode(erosion, kernel_4, iterations=1)
#     dilation = cv2.dilate(erosion, kernel_4, iterations=1)
#     dilation = cv2.dilate(dilation, kernel_4, iterations=1)
#     # target是把原图中的非目标颜色区域去掉剩下的图像
#     img = cv2.bitwise_and(img, img, mask=dilation)
#     hsv_url = hsv_path + str(uuid.uuid1()) + ".png"
#     cv2.imwrite(hsv_url, img)
#     fullImgRgba = Image.open(hsv_url).getdata()

# """
findY = False
couldDelte = False
xGroups = []
coordMap = {}
for y in range(500, 1100):
    for x in range(0, 1080):
        nowRgba = fullImgRgba[y * 1080 + x]
        if nowRgba == BLACK_RGBA[0] or nowRgba == BLACK_RGBA[1] or nowRgba == BLACK_RGBA[2]:
            # if x not in coordMap.keys():
            #     coordMap[y] = [x]
            # if findGapX:
            #     break
            if y not in coordMap.keys():
                coordMap[y] = [x]
            else:
                coordMap[y].append(x)

            xGroups.append(x)

            if not findY:
                findY = True
        else:
            if findY:
                if nowRgba[0] < 170 or nowRgba[0] > 200:
                    if y in coordMap.keys():
                        del coordMap[y]
                findY = False
                break
print(max(xGroups))
print(coordMap)

for y in coordMap:
    startX = min(coordMap[y])
    endX = max(coordMap[y])
    labelImg = cv2.imread(img_path)
    cv2.line(labelImg, (startX, y), (endX, y), (0, 255, 0), 10)
    cv2.imwrite("D:/imgWork/xxx/" + str(uuid.uuid1()) + ".png", labelImg)

    # """
