from appium import webdriver
from PIL import Image
import time, uuid
import cv2
import numpy as np

# BALL_RGBA = (66, 204, 250, 255)
BALL_RGBA = (57, 177, 217, 255)
BALL_HIGHEST_Y = 400
BALL_SCAN_X_RANGE = range(400, 600)
BALL_SCAN_Y_RANGE = range(530, 550)
SCRERN_SHOT_W = 1080
SCRERN_SHOT_H = 1920
SCRERN_BALL_CUT_X = [300, 700]
SCRERN_BALL_CUT_Y = [0, 1920]

SCRERN_BLOCK_CUT_X = [0, 1080]
SCRERN_BLOCK_CUT_Y = [500, 1000]


def findWarnBlockMaxX(img_path):
    # """
    img = cv2.imread(img_path)
    maxX = 0
    if img is not None:
        kernel_2 = np.ones((2, 2), np.uint8)  # 2x2的卷积核
        kernel_3 = np.ones((3, 3), np.uint8)  # 3x3的卷积核
        kernel_4 = np.ones((4, 4), np.uint8)  # 4x4的卷积核
        HSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)  # 把BGR图像转换为HSV格式
        Lower = np.array([0, 185, 250])  # 要识别颜色的下限
        Upper = np.array([255, 200, 255])  # 要识别的颜色的上限
        # mask是把HSV图片中在颜色范围内的区域变成白色，其他区域变成黑色
        mask = cv2.inRange(HSV, Lower, Upper)
        # 下面四行是用卷积进行滤波
        erosion = cv2.erode(mask, kernel_4, iterations=1)
        erosion = cv2.erode(erosion, kernel_4, iterations=1)
        dilation = cv2.dilate(erosion, kernel_4, iterations=1)
        dilation = cv2.dilate(dilation, kernel_4, iterations=1)
        # target是把原图中的非目标颜色区域去掉剩下的图像
        img = cv2.bitwise_and(img, img, mask=dilation)
        # cv2.imwrite("d:/"+str(uuid.uuid1())+".png",img)

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
        binary, contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        xGroups = []
        if contours is not None and len(contours) > 0:
            blockCoords = contours[0]
            for coord in blockCoords:
                xGroups.append(coord[0][0])
        if len(xGroups) > 0:
            maxX = max(xGroups)
    print(maxX)
    return maxX
    # cv2.imwrite("d:/orange.png", img)
    # """

    """
    # 获取整张图片所有坐标点rgba
    fullImgRgba = Image.open(img_path).getdata()
    startX, endX, initY = 0, 0, 0
    labelEnd = False
    finish = False
    for y in range(0, SCRERN_SHOT_H):
        for x in range(0, SCRERN_SHOT_W):
            orangeRgba = (255, 117, 70, 255)
            nowRgba = fullImgRgba[y * SCRERN_SHOT_W + x]

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
                break
        if finish:
            initY = y
            break
    print("find warn block : ", startX, ",", endX)
    return (startX, endX, initY)
    # labelImg = cv2.imread(img_src)
    # cv2.line(labelImg, (startX, initY), (endX, initY), (0, 255, 0), 10)
    # cv2.imwrite(img_path + "dest/" + str(uuid.uuid1()) + ".png", labelImg)
    """


# 获得缺口横轴位置
def getGapX(img_path):
    img = cv2.imread(img_path)
    maxX = 0
    if img is not None:
        img = img[SCRERN_BLOCK_CUT_Y[0]:SCRERN_BLOCK_CUT_Y[1], SCRERN_BLOCK_CUT_X[0]:SCRERN_BLOCK_CUT_X[1]]
        # cv2.imwrite("d:/imgWork/xxx/" + str(uuid.uuid1()) + ".png",img)

        kernel_2 = np.ones((2, 2), np.uint8)  # 2x2的卷积核
        kernel_3 = np.ones((3, 3), np.uint8)  # 3x3的卷积核
        kernel_4 = np.ones((4, 4), np.uint8)  # 4x4的卷积核
        HSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)  # 把BGR图像转换为HSV格式
        Lower = np.array([0, 0, 0])  # 要识别颜色的下限
        Upper = np.array([160, 60, 60])  # 要识别的颜色的上限
        # mask是把HSV图片中在颜色范围内的区域变成白色，其他区域变成黑色
        mask = cv2.inRange(HSV, Lower, Upper)
        # 下面四行是用卷积进行滤波
        erosion = cv2.erode(mask, kernel_4, iterations=1)
        erosion = cv2.erode(erosion, kernel_4, iterations=1)
        dilation = cv2.dilate(erosion, kernel_4, iterations=1)
        dilation = cv2.dilate(dilation, kernel_4, iterations=1)
        # target是把原图中的非目标颜色区域去掉剩下的图像
        img = cv2.bitwise_and(img, img, mask=dilation)
        # cv2.imwrite("d:/imgWork/xxx/" + str(uuid.uuid1()) + ".png", img)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
        binary, contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        xGroups = []
        if contours is not None and len(contours) > 0:
            blockCoords = contours[0]
            for coord in blockCoords:
                xGroups.append(coord[0][0])
        if len(xGroups) > 0:
            maxX = max(xGroups)
    print(maxX)
    return maxX
# 判断球是否在最高点
def ballAtHighest(img_path):
    img = cv2.imread(img_path)
    if img is not None:
        img = img[SCRERN_BALL_CUT_Y[0]:SCRERN_BALL_CUT_Y[1],
              SCRERN_BALL_CUT_X[0]:SCRERN_BALL_CUT_X[1]]  # y: 0-1920, x: 300-700

        kernel_2 = np.ones((2, 2), np.uint8)  # 2x2的卷积核
        kernel_3 = np.ones((3, 3), np.uint8)  # 3x3的卷积核
        kernel_4 = np.ones((4, 4), np.uint8)  # 4x4的卷积核
        HSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)  # 把BGR图像转换为HSV格式
        Lower = np.array([0, 0, 255])  # 要识别颜色的下限
        Upper = np.array([255, 255, 255])  # 要识别的颜色的上限
        # mask是把HSV图片中在颜色范围内的区域变成白色，其他区域变成黑色
        mask = cv2.inRange(HSV, Lower, Upper)
        # 下面四行是用卷积进行滤波
        erosion = cv2.erode(mask, kernel_4, iterations=1)
        erosion = cv2.erode(erosion, kernel_4, iterations=1)
        dilation = cv2.dilate(erosion, kernel_4, iterations=1)
        dilation = cv2.dilate(dilation, kernel_4, iterations=1)
        # target是把原图中的非目标颜色区域去掉剩下的图像
        img = cv2.bitwise_and(img, img, mask=dilation)

        edges = cv2.Canny(img, 50, 100)

        circles1 = cv2.HoughCircles(edges, cv2.HOUGH_GRADIENT, 2, 400, param1=100, param2=50, minRadius=40,
                                    maxRadius=50)
        if circles1 is not None:
            # 取出第一个圆
            circles = circles1[0]
            # 转化为uint16类型
            circles = np.uint16(np.around(circles))
            fstCircle = (0, 0, 0)
            if len(circles) > 1:
                fstCircle = circles[1]
            else:
                fstCircle = circles[0]
            print(fstCircle)

            # 在原图用指定颜色标记出圆的位置
            # destImg = cv2.circle(img, (fstCircle[0], fstCircle[1]), fstCircle[2], (0, 0, 255), -1)
            # cv2.imwrite("D:/imgWork/uuid/src/dst/" + str(uuid.uuid1()) + ".png", destImg)
            isHighest = fstCircle[1] < BALL_HIGHEST_Y
            # tipRgb = (0, 0, 0)
            # if isHighest:
            #     tipRgb = (0, 0, 255)
            # imgSrc = cv2.imread(img_path)
            # destImg = cv2.circle(imgSrc, (fstCircle[0] + SCRERN_CUT_X[0], fstCircle[1]), fstCircle[2], tipRgb, -1)
            # cv2.imwrite("D:/imgWork/uuid/src/dst/" + str(uuid.uuid1()) + ".png", destImg)
            return isHighest
    return False
    """
    # 获取整张图片所有坐标点rgba
    fullImgRgba = Image.open(img_path).getdata()
    
    findBall = False
    retX, retY = 0, 0
    while True:
        for y in BALL_SCAN_X_RANGE:
            for x in BALL_SCAN_Y_RANGE:
                nowRgba = fullImgRgba[y * SCRERN_SHOT_W + x]
                if nowRgba == BALL_RGBA:
                    findBall = True
                    retX = x
                    retY = y
                    break
            if findBall:
                # print(y)
                break
        if 0 < retY < BALL_HIGHEST_Y:
            print("ball is highest at:", retX, ",", retY)
            return True
    """


if __name__ == '__main__':
    # warnBlockMaxX = findWarnBlockMaxX("D:/imgWork/uuid/src/0.png")
    # warnCoord = findWarnBlockMaxX("D:/imgWork/uuid/test.png")
    # warnCoord = findWarnBlockMaxX("D:/imgWork/uuid/test3.png")
    getGapX("D:/imgWork/uuid/src/0.png")
    getGapX("D:/imgWork/uuid/src/1.png")
    getGapX("D:/imgWork/uuid/test3.png")

    """
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['automationName'] = "uiautomator2"  # 使用uiautomator2定位，必须，否则定位不到
    desired_caps['deviceName'] = 'e7c976f2'
    desired_caps['unicodeKeyboard'] = True
    desired_caps["resetKeyboard"] = False
    desired_caps["newCommandTimeout"] = 30
    desired_caps['fullReset'] = 'false'
    desired_caps['appPackage'] = 'com.tencent.mm'
    desired_caps['appActivity'] = 'com.tencent.mm.ui.LauncherUI'
    desired_caps['noReset'] = True
    # 设置超时时间，如果不设置，1分钟appium没接收到新请求就会关闭链接
    desired_caps['newCommandTimeout'] = 600
    driver = webdriver.Remote(command_executor='http://127.0.0.1:4723/wd/hub', desired_capabilities=desired_caps)
    time.sleep(3)
    driver.implicitly_wait(10)
    driver.find_element_by_xpath('//*[@text="发现"]').click()
    time.sleep(1)
    driver.swipe(100, 1200, 100, 900)
    driver.find_element_by_xpath('//*[@text="小程序"]').click()
    time.sleep(1)
    driver.find_element_by_xpath('//*[@text="欢乐球球"]').click()

    print("准备关闭广告.")
    time.sleep(8)
    driver.tap([[916, 554]])
    print("关闭成功.")
    print("准备开始游戏.")

    print("准备关闭广告.")
    time.sleep(1)
    driver.tap([[916, 554]])
    print("关闭成功.")
    print("准备开始游戏.")

    time.sleep(5)
    driver.tap([[527, 1531]])
    print("开始游戏.")
    time.sleep(1)

    initNum = 0
    while True:
        # img_path = "D:/imgWork/uuid/src/" + str(uuid.uuid1()) + ".png"
        img_path = "D:/imgWork/uuid/src/" + str(initNum) + ".png"
        driver.save_screenshot(img_path)
        isHighest = ballAtHighest(img_path)
        if isHighest:
            warnBlockMaxX = int(findWarnBlockMaxX(img_path))
            startSwipeX = int(SCRERN_SHOT_W / 2)
            if warnBlockMaxX > 0:
                if startSwipeX > warnBlockMaxX:
                    driver.swipe(startSwipeX, 0, warnBlockMaxX, 0)
                initNum = initNum + 1
            else:
                driver.swipe(int(SCRERN_SHOT_W / 2), 0, int(warnBlockMaxX), 0)
    """

    # img = cv2.imread(img_path)
    # edges = cv2.Canny(img, 50, 100)
    # cv2.imwrite(img_cut_path, edges)
    # time.sleep(5)
    # driver.quit()

    """
    for n in range(1, 100):
        img_path = "D:/imgWork/uuid/src/test (" + str(n) + ").png"
        isHighest = ballAtHighest(img_path)
        print(isHighest)
    """
