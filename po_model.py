#coding=utf-8
from  selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

class Page(object):
    '''
    基础类，用于页面对象类的继承
    '''
    login_url = 'http://mail.dianbaobao.com'

    def __init__(self,selenium_driver,base_url=login_url):
        self.base_url = base_url
        self.driver = selenium_driver
        self.timeout = 30

    def on_page(self):
        return self.driver.current_url == (self.base_url + self.url)

    def _open(self, url):
        url = self.base_url + url
        self.driver.get(url)
        assert self.on_page(), 'Did not land on %s' % url

    def open(self):
        self._open(self.url)

    def find_element(self, *loc):
        return self.driver.find_element(*loc)

class LoginPage(Page):
    '''
    126邮箱登陆页面模型
    '''
    url = '/'

    #定位器
    username_loc = (By.ID, "qquin")
    password_loc = (By.ID, "pp")
    submit_loc = (By.CLASS_NAME, "login_btn")

    #Action
    def type_username(self,username):
        self.find_element(*self.username_loc).send_keys(username)

    def type_password(self,password):
        self.find_element(*self.password_loc).send_keys(password)

    def submit(self):
        self.find_element(*self.submit_loc).click()

def test_user_login(driver,username,password):
    """
    测试获取的用户名/密码是否可以登陆
    """
    login_page = LoginPage(driver)
    login_page.open()
    login_page.type_username(username)
    login_page.type_password(password)
    login_page.submit()

def main():
    try:
        driver = webdriver.Firefox()
        username = 'username'
        password = '123456'
        test_user_login(driver,username,password)
        sleep(3)
        text = driver.find_element_by_xpath("/html/body/form/div/div[2]/div[2]/div/div[2]/div/div[2]/span/input").text
        assert (text == '')
    finally:
        driver.close()

if __name__ == '__main__':
    main()




