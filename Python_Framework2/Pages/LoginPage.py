from selenium import webdriver
from Locators.Locators import Locator
class LoginPage():
    def __init__(self,driver):
        self.driver = driver


    def enter_username(self,username):
            self.driver.find_element_by_xpath(Locator.username_xpath).clear()
            self.driver.find_element_by_xpath(Locator.username_xpath).send_keys(username)

    def enter_password(self, password):
                self.driver.find_element_by_xpath(Locator.password_xpath).clear()
                self.driver.find_element_by_xpath(Locator.password_xpath).send_keys(password)

    def clickon_Loginbtn(self):
                self.driver.find_element_by_xpath(Locator.loginbtn_xpath).click()

