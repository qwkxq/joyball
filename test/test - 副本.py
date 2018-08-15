from appium import webdriver

desired_caps = {}
desired_caps['platformName'] = "Android"         # 声明是ios还是Android系统
desired_caps['automationName'] = "uiautomator2"  # 这里是使用uiautomator2的元素定位方法
desired_caps['platformVersion'] = '8.0.0'        # Android内核版本号，可以在夜神模拟器设置中查看
desired_caps['deviceName'] = 'e7c976f2'   # （MI6）连接的设备名称
desired_caps['appPackage'] = 'com.tencent.mm'    # apk的包名
#desired_caps['app'] = PATH(r"E:\tests\GuoYuB2B_2.1.apk")#app安装包路径
'''获取Activity的方法：进入adb，使用monkey -p 包名 -v -v -v 1后，cmp="appActivity"'''
desired_caps['appActivity'] = 'com.tencent.mm.ui.LauncherUI'  # apk的launcherActivity

appdriver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)