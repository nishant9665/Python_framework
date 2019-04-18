from selenium import webdriver
import time
import unittest
import json
import logging
from Pages.LoginPage import LoginPage
from Pages.homePage import HomePagePage

logging.basicConfig(filename='C:/Users/nishant.narwade/PycharmProjects/Python_Framework2/Logs/jenkinLog.log',
level=logging.NOTSET,format='%(asctime)s:%(lineno)d:%(levelname)s:%(message)s')
with open('C:\\Users\\nishant.narwade\\PycharmProjects\\Python_Framework2\\Data\\data.json') as f:data = json.load(f)


class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(
        executable_path="C:/Users/nishant.narwade/PycharmProjects/Python_Framework2/All_driver/chromedriver.exe")
        cls.driver.implicitly_wait(5)
        cls.driver.maximize_window()



    def test_login_valid(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login")

        login = LoginPage(driver)
        login.enter_username(data["credentials"][0]["valid_data"]["uname"])
        login.enter_password("admin123")
        login.clickon_Loginbtn()

        home = HomePagePage(driver)
        home.homepage_welcomeBtn_xpath
        home.hoempage_logoutBtn_xpath
        time.sleep(2)



    @classmethod
    def tearDownClass(cls):

        cls.driver.close()
        cls.driver.quit()
        print("Test complete")

if __name__ == "__main__":
    unittest.main()




