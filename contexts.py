#coding:utf-8
#coding:gb2312
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
# how about ou?
driver.find_element_by_id("com.izp.f2c:id/home_rb_discover").click()
driver.find_element_by_id('com.izp.f2c:id/home_rb_home').click()

print driver.contexts
# 打印页面元素，太棒了呵呵
