#coding=utf-8
from  selenium import webdriver
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

login_url = 'http://mail.dianbaobao.com'

driver = webdriver.Firefox()

driver.get(login_url)
'''
driver.find_element_by_id('qquin').send_keys('username')
driver.find_element_by_id('pp').send_keys('123456')
driver.find_element_by_class_name('login_btn').click()
'''

text = driver.find_element_by_xpath("/html/body/form/div/div[2]/div[2]/div/div[2]/div/div[2]/span/input").get_attribute('type')

print text

