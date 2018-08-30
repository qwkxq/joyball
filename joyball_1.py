import numpy as np

import cv2

from appium import webdriver
from PIL import Image
import time, uuid

img_path = "d:/imgWork/uuid/"

# desired_caps = {}
# desired_caps['platformName'] = 'Android'
# desired_caps['automationName'] = "uiautomator2"  # 使用uiautomator2定位，必须，否则定位不到
# desired_caps['deviceName'] = 'e7c976f2'
# desired_caps['unicodeKeyboard'] = True
# desired_caps["resetKeyboard"] = False
# desired_caps["newCommandTimeout"] = 30
# desired_caps['fullReset'] = 'false'
# desired_caps['appPackage'] = 'com.tencent.mm'
# desired_caps['appActivity'] = 'com.tencent.mm.ui.LauncherUI'
# desired_caps['noReset'] = True
# # 设置超时时间，如果不设置，1分钟appium没接收到新请求就会关闭链接
# desired_caps['newCommandTimeout'] = 600
# driver = webdriver.Remote(command_executor='http://127.0.0.1:4723/wd/hub', desired_capabilities=desired_caps)
# time.sleep(3)
# driver.implicitly_wait(10)
# driver.find_element_by_xpath('//*[@text="发现"]').click()
# time.sleep(1)
# driver.swipe(100, 1200, 100, 900)
# driver.find_element_by_xpath('//*[@text="小程序"]').click()
# time.sleep(1)
# driver.find_element_by_xpath('//*[@text="欢乐球球"]').click()
# print("准备关闭广告.")
# time.sleep(8)
# driver.tap([[916, 554]])
# print("关闭成功.")
# print("准备开始游戏.")
# time.sleep(5)
# driver.tap([[527, 1531]])
# print("开始游戏.")
# time.sleep(1)
# driver.save_screenshot(img_path)
# time.sleep(5)
# driver.quit()

img_name = "test3.png";
img_src = img_path + img_name
img_dest = img_path + "dest/" + img_name

"""
img = cv2.imread(img_src)

# 切出图片中间位置，需要根据具体分辨率修改
roi = img[100:1000]

# 切后的图片写入文件，可查看效果
cv2.imwrite('d:/imgWork/uuid/cut.png', roi)


# 边缘识别
edges = cv2.Canny(roi, 50, 100)
cv2.imwrite('d:/imgWork/uuid/canny.png', edges)

# 通过霍夫圆变换识别棋子头部的圆, 圆的半径minRadius，maxRadius需要根据具体分辨率修改
circles1 = cv2.HoughCircles(edges, cv2.HOUGH_GRADIENT, 2, 400,
                            param1=100, param2=50, minRadius=10-1, maxRadius=10+1)

# 取出第一个圆
circles = circles1[0]

# 转化为uint16类型
circles = np.uint16(np.around(circles))
# np.around 四舍六入五成双

ring = circles[0]

"""

"""
im = Image.open(img_src)
global RGBList
RGBList = im.getdata()

startX, endX, initY = 0, 0, 0
xMinArray, xMaxArray = [], []
coord = {}

# 纵向查找X
orangeRgba = (255, 117, 70, 255)
backRgba = (59, 59, 59, 255)
ballRgba = (66, 204, 250, 255)
for y in range(700, 900):
    tempX = []
    for x in range(0, 1080):
        nowRgba = RGBList[y * 1080 + x]
        if nowRgba == orangeRgba:
            tempX.append(x)
    if len(tempX) > 0:
        minV = min(tempX)
        maxV = max(tempX)
        xMinArray.append(minV)
        xMaxArray.append(maxV)
        coord[maxV] = [y, minV]

if len(xMaxArray) > 0:
    endX = max(xMaxArray)
    startX = coord[endX][1]
    initY = coord[endX][0]
    print(endX, coord[endX])
    cs = coord[maxV]
    labelImg = cv2.imread(img_src)
    cv2.line(labelImg, (startX, initY), (endX, initY), (0, 255, 0), 10)
    cv2.imwrite(img_dest, labelImg)
else: #没找到色块
    print(1)

"""

im = Image.open("d:/imgWork/uuid/src/1.png")
ballRgba = (66, 204, 250, 255)
global RGBList
RGBList = im.getdata()
findBall = False
for y in range(0, 545):
    for x in range(530, 550):
        nowRgba = RGBList[y * 1080 + x]
        if nowRgba == ballRgba:
            findBall = True
            break
    if findBall:
        print(y)
        break

"""
labelEnd = False
finish = False
for y in range(0, 1090):
    for x in range(0, 1080):
        orangeRgba = (255, 117, 70, 255)
        nowRgba = RGBList[y * 1080 + x]

        if nowRgba == orangeRgba:
            if not labelEnd:
                labelEnd = True
                startX = x
            # print(x)
            # break
        elif nowRgba != orangeRgba and labelEnd:
            endX = x - 1
            labelEnd = False
            finish = True
    if finish:
        initY = y
        break
print(startX, ",", endX)
labelImg = cv2.imread(img_src)
cv2.line(labelImg, (startX, initY), (endX, initY), (0, 255, 0), 10)
cv2.imwrite(img_path + "dest/" + str(uuid.uuid1()) + ".png", labelImg)
"""
