import unittest
import time
from appium import webdriver
desired_caps = {}
desired_caps['platformName'] = 'Android' # test platform
desired_caps['deviceName'] = 'emulator-5554 '
desired_caps['platformVersion'] = '4.4.2'
desired_caps['appPackage']='com.izp.f2c'
desired_caps['appActivity']='activity.HomeActivity' #config the cap

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
driver.find_element_by_id('com.izp.f2c:id/home_rb_discover').click() # use uiautomatorviewer to find resource id
driver.find_element_by_id('com.izp.f2c:id/home_rb_mine').click()
driver.find_element_by_id('com.izp.f2c:id/nologin').click()
driver.find_element_by_id('com.izp.f2c:id/login_inputusername').click()
driver.press_keycode(51)
driver.press_keycode(43)
driver.press_keycode(40)
driver.press_keycode(34)
driver.press_keycode(36)
driver.press_keycode(49)
# input username 'wolfhu' please confirm your choice
driver.find_element_by_id('com.izp.f2c:id/login_inputpassword').click()
i=1
while i<=6:
    driver.press_keycode(8)
    i+=1
driver.press_keycode(29)
# input password '111111a'
driver.find_element_by_id('com.izp.f2c:id/login_login_button').click()
time.sleep(10)
driver.reset()
