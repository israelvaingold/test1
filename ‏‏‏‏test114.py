
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(5)
driver.get("https://www.amazon.com/")

search = driver.find_element_by_id("twotabsearchtextbox")
search.send_keys('ebook', Keys.ENTER)

expected_text = '"e-book"'
actual_text = driver.find_element_by_xpath("//*[@id='search']/span/div/h1/div/div[1]/div/div/span[3]").text
assert expected_text == actual_text, f'Error. Expected_text: {expected_text}, but actual_text: {actual_text}'

