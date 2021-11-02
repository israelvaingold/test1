
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager


class TestUntitled():
    def setup_method(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.vars = {}

    def teardown_method(self):
        self.driver.quit()

    def test_login(self):
        self.driver.get("https://e-services.clalit.co.il/OnlineWeb/General/Login.aspx?ReturnUrl=%2fOnlineWeb%2fServices%2fFamilyHomePage.aspx")
        self.driver.find_element_by_name("ctl00$cphBody$_loginView$tbUserId").send_keys("039758398")
        self.driver.find_element_by_name("ctl00$cphBody$_loginView$tbUserName").send_keys("il48762")
        self.driver.find_element_by_name("ctl00$cphBody$_loginView$tbPassword").send_keys("b038810172")
        self.driver.find_element(By.ID, "ctl00_cphBody__loginView_lblSend").click()
        eror_message = self.driver.find_element(By.ID, "ctl00_cphBody__loginView_cvUserId").text
        assert eror_message == "מספר תעודת הזהות לא תקין"



    def test_file_login(self):
        self.driver.get("https://e-services.clalit.co.il/OnlineWeb/General/Login.aspx?ReturnUrl=%2fOnlineWeb%2fServices%2fFamilyHomePage.aspx")
        self.driver.find_element_by_name("ctl00$cphBody$_loginView$tbUserId").send_keys("039758396")
        self.driver.find_element_by_name("ctl00$cphBody$_loginView$tbUserName").send_keys("il48762")
        self.driver.find_element_by_name("ctl00$cphBody$_loginView$tbPassword").send_keys("b038810172")
        self.driver.find_element(By.ID, "ctl00_cphBody__loginView_lblSend").click()
        eror_message = self.driver.find_element(By.CSS_SELECTOR, ".FamilySliderFamilyNameTxt").text
        assert eror_message == "ויינגולד"


iclass = TestUntitled()
# time.sleep(10)
iclass.setup_method()
# time.sleep(10)
iclass.test_login()
# time.sleep(10)
iclass.test_file_login()
# time.sleep(10)
iclass.teardown_method()
# time.sleep(3)
