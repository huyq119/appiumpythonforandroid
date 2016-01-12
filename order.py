# coding:utf-8
# coding:gb2312

import time

from appium import webdriver

desired_caps = {}
desired_caps['platformName'] = 'Android'  # test platform
desired_caps['deviceName'] = 'emulator-5554 '
desired_caps['platformVersion'] = '4.4.2'
desired_caps['appPackage'] = 'com.izp.f2c'
desired_caps['appActivity'] = 'activity.HomeActivity'  # config the cap
desired_caps['newCommandTimeout'] = '30'  # set the session wait time


dr = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
dr.find_element_by_id('com.izp.f2c:id/home_rb_discover').click()
# use ui automator viewer to find resource id
dr.find_element_by_id('com.izp.f2c:id/home_rb_mine').click()
dr.find_element_by_id('com.izp.f2c:id/nologin').click()
utext = dr.find_element_by_id('com.izp.f2c:id/login_inputusername')
utext.send_keys('wolfhu')
# input username 'wolfhu' please confirm your choice
ptext = dr.find_element_by_id('com.izp.f2c:id/login_inputpassword')
ptext.send_keys('111111a')
# input password '111111a'
dr.find_element_by_id('com.izp.f2c:id/login_login_button').click()
time.sleep(10)
dr.find_element_by_id('com.izp.f2c:id/home_rb_home').click()
time.sleep(10)
dr.find_element_by_id('com.izp.f2c:id/top_tv_left').click()
time.sleep(20)
dr.find_element_by_android_uiautomator('new UiSelector().text("流行饰品")').click()
time.sleep(20)

dr.reset()
