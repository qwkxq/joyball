from appium import webdriver

desired_caps = {
            'platformName': 'Android',
            'fastReset': 'false',
            'deviceName': 'e7c976f2',
            'appPackage': 'com.tencent.mm',
            'appActivity': '.ui.LauncherUI',
            'fullReset': 'false',
            'unicodeKeyboard': 'True',
            'resetKeyboard': 'True',
            'chromeOptions': {
                'androidProcess': 'com.tencent.mm:appbrand0'
                }
            }
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
driver.find_element_by_name("发现").click()
driver.find_element_by_name("小程序").click()
driver.find_element_by_name("X东购物").click()
driver.switch_to.context('WEBVIEW_com.tencent.mm:appbrand0')
time.sleep(5)
print(driver.page_source)