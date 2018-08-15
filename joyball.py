from appium import webdriver
import time
import cv2

img_path = "d:/1.png";
img_cut_path = "d:/1_cut.png";

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['automationName'] = "uiautomator2" #使用uiautomator2定位，必须，否则定位不到
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
time.sleep(5)
driver.tap([[527, 1531]])
print("开始游戏.")
time.sleep(1)
driver.save_screenshot(img_path)
img = cv2.imread(img_path)
edges = cv2.Canny(img, 50, 100)
cv2.imwrite(img_cut_path, edges)
time.sleep(5)
driver.quit()
