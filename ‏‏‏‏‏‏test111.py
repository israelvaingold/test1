
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
        self.driver.get("https://rebooks.org.il/?he_IL")
        time.sleep(3)

        self.driver.find_element_by_xpath('/html/body/header/div[1]/div[2]/div/input').click()

        self.driver.find_element_by_xpath('/html/body/header/div[1]/div[2]/div/input').send_keys("קהיליו9ת")
        self.driver.find_element_by_xpath('/html/body/header/div[1]/div[2]/div/div[1]/i').click()
        time.sleep(3)
        eror_message = self.driver.find_element(By.CSS_SELECTOR, "#booksList > div > div.font-size-1-5").text
        assert eror_message >= "לצערנו לא נמצאו תוצאות שתואמות את החיפוש."

    def test_file_login(self):
        self.driver.get("https://rebooks.org.il/?he_IL")
        time.sleep(3)

        self.driver.find_element_by_xpath('/html/body/header/div[1]/div[2]/div/input').click()

        self.driver.find_element_by_xpath('/html/body/header/div[1]/div[2]/div/input').send_keys("קהילות")
        self.driver.find_element_by_xpath('/html/body/header/div[1]/div[2]/div/div[1]/i').click()
        time.sleep(3)
        r_message = self.driver.find_element_by_xpath("//*[@id='booksList']/div[1]/div[2]/div[1]").text
        assert r_message <= "קהילות"

iclass = TestUntitled()
iclass.setup_method()
iclass.test_login()
iclass.test_file_login()
iclass.teardown_method()
