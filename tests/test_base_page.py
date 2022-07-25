from pages.base_page import BasePage
from time import sleep
import pytest



class TestPage:
    
    def test_open_privacy_link(self, mobile_driver):
        home_page = BasePage(mobile_driver)
        home_page.open_privacy_link()
        logcat = mobile_driver.get_log('logcat')
        c = '\n'.join([i['message'] for i in logcat])
        f = open('example_log01.txt','w')
        f.write(c)


    def test_click_ok_btn(self, mobile_driver):
        home_page = BasePage(mobile_driver)
        home_page.click_ok_btn()
        logcat = mobile_driver.get_log('logcat')
        c = '\n'.join([i['message'] for i in logcat])
        f = open('example_log02.txt','w')
        f.write(c)
    

