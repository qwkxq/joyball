from appium import webdriver
import time, os, re
# from appium.webdriver.common.touch_action import TouchAction

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['automationName'] = "uiautomator2"
#desired_caps['automationName'] = 'appium'
desired_caps['deviceName'] = 'e7c976f2'
desired_caps['unicodeKeyboard'] = True
desired_caps["resetKeyboard"] = True
desired_caps["newCommandTimeout"] = 30
desired_caps['fullReset'] = 'false'
desired_caps['appPackage'] = 'com.tencent.mm'
desired_caps['appActivity'] = 'com.tencent.mm.ui.LauncherUI'
desired_caps['recreateChromeDriverSessions'] = True
desired_caps['noReset'] = True
desired_caps['newCommandTimeout'] = 10
desired_caps['chromeOptions'] = {'androidProcess': 'com.tencent.mm:appbrand0'}
'''

desired_caps = {}
desired_caps['platformName'] = "Android"         # 声明是ios还是Android系统
desired_caps['automationName'] = "uiautomator2"  # 这里是使用uiautomator2的元素定位方法
desired_caps['platformVersion'] = '8.0.0'        # Android内核版本号，可以在夜神模拟器设置中查看
desired_caps['deviceName'] = 'e7c976f2'   # 连接的设备名称
desired_caps['appPackage'] = 'com.tencent.mm'    # apk的包名
#desired_caps['app'] = PATH(r"E:\tests\GuoYuB2B_2.1.apk")#app安装包路径
desired_caps['appActivity'] = 'com.tencent.mm.ui.LauncherUI'
desired_caps['fullReset'] = 'false'
desired_caps['noReset'] = True
'''
driver = webdriver.Remote(command_executor='http://127.0.0.1:4723/wd/hub', desired_capabilities=desired_caps)
time.sleep(2)
time.sleep(1)
driver.implicitly_wait(10)
driver.find_element_by_xpath('//*[@text="发现"]').click()
time.sleep(1)
driver.swipe(100, 1200, 100, 900)
driver.find_element_by_xpath('//*[@text="小程序"]').click()
time.sleep(1)

driver.find_element_by_xpath('//*[@text="欢乐球球"]').click()
time.sleep(5)
# driver.switch_to.context("WEBVIEW_com.tencent.mm:appbrand0")
'''
driver.find_element_by_android_uiautomator(
    "new UiSelector().ClassName(\"com.tencent.mm\").instance(8)")
    '''
time.sleep(2)
contexts = driver.contexts
print
contexts
# time.sleep(2)
# driver.switch_to.context('WEBVIEW_com.tencent.mm:appbrand0')
# driver.switch_to.context('NATIVE_APP')
# print
# '切换成功'
driver.tap([[916, 554]])
time.sleep(5)
# driver.tap([(889, 281)], 500)
# print
# driver.current_context
# all_handles = driver.window_handles
# print
# len(all_handles)
# for handle in all_handles:
#     try:
#         driver.switch_to_window(handle)
#         print
#         driver.page_source
#         driver.find_element_by_css_selector('.filter-select.flex-center')  # 定位“筛选 ”按钮
#         print
#         '定位成功'
#         break
#     except Exception as e:
#         print
#         e
# driver.find_element_by_css_selector('.filter-select.flex-center').click()
# time.sleep(5)
driver.quit()
