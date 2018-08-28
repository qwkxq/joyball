import numpy as np

import cv2

from appium import webdriver
from PIL import Image
import time

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


"""
img_src = img_path + "test2.png"

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

im = Image.open(img_src)
global RGBList
RGBList = im.getdata()

for x in range(0, 1080):
    orangeRgba = (255, 117, 70, 255)
    nowRgba = RGBList[742 * 1080 + x]
    if nowRgba == orangeRgba:
        print(x)
        # break
