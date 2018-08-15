```python
import cv2
import numpy as np
import math
from appium import webdriver
from time import sleep



# 需要修改的值都在这里
CUT_X1 = 600
CUT_X2 = 1500       # CUT两个常量为减少图像干扰，切出即将要跳跃的这部分图像
R = 30              # 棋子头部圆的半径大小，不同的分辨率会有差异
CH = 159            # 棋子头部圆中心距底部中心的距离
TAP = [300, 1000]   # 跳跃时，点击的屏幕位置，任意位置即可，只要不点击到底部的分享等按钮
V = '7.1.1'         # 你手机的安卓版本
START = [500, 1500] # 点击开始游戏按钮，这个范围很大，根据具体手机设置即可
T = 1.365           # 跳跃系数，也就是单位距离的按压时间
H1 = 10
H2 = 15             # 游戏到后期，图像越来越小，为了增加容错率，需要将计算的物件中心点稍微上移一点，屏幕分辨率低
                    # 于1080*1920的，适当调小几个像素即可
IMG_PATH = 'e:/1/1.png' # 从手机上的截图存放的位置
ID = 'com.tencent.mm:id/g_'   #小程序的ID定位语句，所有小程序都是这个ID
ID_NUM = 0                    # 由于所有小程序的ID都一样，因此需要输入第几个小程序，在第一个就是0

def slide(driver, direction):
    """滑动函数, 为了点击小程序按钮"""
    size = driver.get_window_size()
    if direction == 'left':
        # 从右往左滑动, 相当于往右边翻页    y轴保持不变 x开始点大于x结束点
        start_x = int(size['width'] * 0.9)
        start_y = int(size['height'] * 0.5)
        end_x = int(size['width'] * 0.1)
        end_y = start_y
    elif direction == 'right':
        # 从左往右滑动,相当于向左翻页      y轴保持不变 x结束点大于x开始点
        start_x = int(size['width'] * 0.1)
        start_y = int(size['height'] * 0.5)
        end_x = int(size['width'] * 0.9)
        end_y = start_y
    elif direction == 'up':
        # 从下往上滑动,相当于向上翻页      x轴保持不变 y开始点大于y结束点
        start_x = int(size['width'] * 0.5)
        start_y = int(size['height'] * 0.8)
        end_x = start_x
        end_y = int(size['height'] * 0.2)
    elif direction == 'down':
        # 从下往上滑动,相当于向上翻页      x轴保持不变 y结束点大于y开始点
        start_x = int(size['width'] * 0.5)
        start_y = int(size['height'] * 0.2)
        end_x = start_x
        end_y = int(size['height'] * 0.8)
    else:
        raise ValueError('请输入left, right, up, down等方向！')
    driver.swipe(start_x, start_y, end_x, end_y)


def get_dt(image_name, coe, la):
    # 读取图片
    img = cv2.imread(image_name)

    # 切出图片中间位置，需要根据具体分辨率修改
    #roi = img[600:1500, 0:1080]
    roi = img[CUT_X1: CUT_X2]

    # 切后的图片写入文件，可查看效果
    cv2.imwrite('./tyt/tyt_cut.png', roi)

    # 边缘识别
    edges = cv2.Canny(roi, 50, 100)
    cv2.imwrite('./tyt/tyt_canny.png', edges)

    # 通过霍夫圆变换识别棋子头部的圆, 圆的半径minRadius，maxRadius需要根据具体分辨率修改
    circles1 = cv2.HoughCircles(edges, cv2.HOUGH_GRADIENT, 2, 400,
                                param1=100, param2=50, minRadius=R-1, maxRadius=R+1)

    # 取出第一个圆
    circles = circles1[0]

    # 转化为uint16类型
    circles = np.uint16(np.around(circles))
    # np.around 四舍六入五成双

    ring = circles[0]

    # 去掉棋子头部的轮廓。
    # 根据圆心，计算圆周围的矩阵，然后全部设置为0，相当于把包括圆在内的所有轮廓消除
    # 圆的半径多加5个像素

    # 圆上部
    ryt = ring[1] - R + 5
    # 圆下部
    ryb = ring[1] + R + 5
    # 圆左边
    ryl = ring[0] - R + 5
    # 圆右边
    ryr = ring[0] + R + 5

    edges[ryt:ryb, ryl:ryr] = 0

    # 棋子的中心点大约在识别的圆y轴+=159的位置，需要根据具体分辨率修改
    ring[1] += CH

    # edges == 255 取edges数组中值为255（白色）的所有下标
    # edges中排列的[纵坐标,横坐标]的顺序，因此xy要交换一下位置
    y, x = np.where(edges == 255)

    # 找到y轴最小值，y轴最小值的时候就是x轴的中心点
    index = np.argmin(y)
    xmin = x[index]

    # 找到x轴最大的点，即最右端的点，此时的y坐标就是y的中心点
    # la为游戏后期物件变小，偏移量600需要根据具体分辨率修改
    ymax = y[np.argmax(x[index:index + CUT_X1])] - la

    # xmin和ymax就是新物件的中心点

    # 计算棋子底部中心点。并计算中心点与新物件的中心点的直线距离。
    # 抛物线上两点之间的距离为"根号((x2-x1) ** 2 + (y2-y1) ** 2)"
    dt = math.sqrt((xmin - ring[0]) ** 2 + (ymax - ring[1]) ** 2)

    # 用系数coe来确定单位像素距离需要按压的时间，大致在1-2.5之间。
    # 分辨率不同需要自行尝试并调整，1080*1920的屏幕大致在1.365
    ds = int(dt * coe)
    print('棋子中心点：({bottom_x}, {bottom_y}) | 新物件中心点：({x}, {y}) | 距离：{dt} | 时间：{ds}'
          .format(bottom_x=ring[0], bottom_y=ring[1],
                  x=xmin, y=ymax,
                  dt=dt, ds=ds))
    return ds


def jump(driver, img, coe, la=0):
    # 截图
    driver.save_screenshot(img)
    # 调用计算距离时间比的函数,根据距离得到点击时间
    ds = get_dt(img, coe, la)
    # 根据计算出的点击时间进行点击
    driver.tap([TAP], ds)


if __name__ == '__main__':
    # 打开微信
    desired_capabilities = {
        'platformName': 'Android',
        'deviceName': 'devices',
        'platformVersion': V,
        'appPackage': 'com.tencent.mm',
        'appActivity': 'com.tencent.mm.ui.LauncherUI',
        'noReset': 'true',
        # 设置超时时间，如果不设置，1分钟appium没接收到新请求就会关闭链接
        'newCommandTimeout': 600
    }
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_capabilities)

    sleep(3)
    slide(driver, 'down')
    sleep(1)
    # 跳一跳在第几个就写第几个
    driver.find_elements_by_id(ID)[ID_NUM].click()
    sleep(5)
    # 点击开始游戏按钮，需要根据具体分辨率修改
    driver.tap([START])
    sleep(3)

    s = 0
    la = 0
    try:
        while True:
            # 后期物件变小，会导致定位不准，因此需要将y坐标稍微上移
            if s > 60:
                la = H1
            elif s > 120:
                la = H2
            jump(driver, IMG_PATH, T, la)
            s += 1
            print('当前跳跃次数：', s)
            # 需要适当等待，获取加分和避免超越好友时的动画对图像识别的干扰
            sleep(2)
    finally:
        print('总次数：', s)
```