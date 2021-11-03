
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
        self.driver.get("https://www.e-vrit.co.il/")
        self.driver.find_element_by_xpath('//*[@id="body"]/div[2]/div/div[3]/div[1]/a').click()
        self.driver.find_element_by_id("emailLogin").send_keys("123456@gmail.com")
        self.driver.find_element_by_id("passwordLogin").send_keys("00000000")
        self.driver.find_element_by_xpath('//*[@id="body"]/div[6]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/form/div[3]/button').click()
        time.sleep(3)
        eror_message = self.driver.find_element_by_xpath ("//*[@id='body']/div[6]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/form/div[3]/div").text
        assert eror_message == "שם המשתמש או הסיסמה לא נכונים"


    def test_file_login(self):
        self.driver.get("https://www.e-vrit.co.il/")
        self.driver.find_element_by_xpath('//*[@id="body"]/div[2]/div/div[3]/div[1]/a').click()
        self.driver.find_element_by_id("emailLogin").send_keys("7653732@gmail.com")
        self.driver.find_element_by_id("passwordLogin").send_keys("Zz000000")
        self.driver.find_element_by_xpath('//*[@id="body"]/div[6]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/form/div[3]/button').click()
        time.sleep(3)
        self.driver.find_element_by_xpath('//*[@id="body"]/div[2]/div/div[3]/div[3]/a/i').click()
        r_message = self.driver.find_element(By.CSS_SELECTOR, "span.rdbText").text
        assert r_message == "הכל"

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
