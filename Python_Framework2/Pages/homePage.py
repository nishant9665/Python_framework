class HomePagePage():

    def __init__(self, driver):
        self.driver = driver

        self.homepage_welcomeBtn_xpath = "//a[@id='welcome']"
        self.hoempage_logoutBtn_xpath = "//a[contains(text(),'Logout')]"
        self.homepage_homepage_AssignLeave_xpath = "//img[@src='/webres_5ca6658021cd89.53008077/orangehrmLeavePlugin/images/ApplyLeave.png']"
        self.homepage_DashBoard_Xpath = "//b[contains(text(),'Dashboard')]"
        self.homepage_Admin_xpath = "//b[contains(text(),'Admin')]"
        self.homepage_Pim_xpath = "// b[contains(text(), 'PIM')]"
        self.homepage_Leave_xpath = "//b[contains(text(),'Leave')]"
        self.homepage_Time_xpath = "//b[contains(text(),'Time')]"
        self.homepage_Recruitment_xpath = "//b[contains(text(),'Recruitment')]"
        self.homepage_Performance_xpath = "//b[contains(text(),'Performance')]"
        self.homepage_Directory_xpath = "//b[contains(text(),'Directory')]"
        self.homepage_Maintenance_xpath = "//b[contains(text(),'Maintenance')]"
        self.homepage_MP_Link_xpath = "//input[@id='MP_link']"


    def click_welcome(self):
        self.driver.find_element_by_xpath(self.homepage_welcomeBtn_xpath).click()


    def click_Onlogout(self):
        self.driver.find_element_by_xpath(self.hoempage_logoutBtn_xpath).click()









