#!/usr/bin/env python
# -*- coding: utf-8 -*-
from configure.H5device import *
from configure.H5device import BaseCase
import sys
from selenium import webdriver
import time
import unittest


# 日志
class test_01_Search(BaseCase):
    logging.info(sys._getframe().f_code.co_filename.center(100, '='))


    #首页搜索
    def test_01_Search(self):
        mobileEmulation = {'deviceName': 'iPhone 8'}
        options = webdriver.ChromeOptions()
        options.add_experimental_option('mobileEmulation', mobileEmulation)

        driver = webdriver.Chrome(executable_path='chromedriver.exe', chrome_options=options)




        driver.get("http://m.elong.com/")

        print("设置浏览器的宽480，高800显示")
        driver.set_window_size(400,800)
        time.sleep(5)
        print("点击搜索按钮")
        #self.assertIsNotNone(self.find_element("/html/body/div/div/div[1]/div[2]/div/div"), '无搜索按钮,搜索失败,Fail')
        driver.find_element_by_xpath("/html/body/div/div/div[1]/div[2]/div/div").click()
        time.sleep(3)

        # 因为对find_element单个控件的获取做了封装，所以断言的时候这样使用，可以得到封装里面的日志信息，未能找到具体的元素id，这是我李升杰的风格

        driver.find_element_by_xpath("//*[@id='uniq22']/header/a[2]").click()






    #点击登录按钮
    #def test_02_login_L(self):
#        driver.find_element_by_xpath("//*[@id='uniq22']/header/a[2]").click()
        #self.assertIsNotNone(self.find_element("//*[@id='uniq22']/header/a[2]"), '无定位按钮,定位失败,Fail')
        time.sleep(4)



