from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# location of the webdriver where it is installed
browser = webdriver.Chrome(
    "C:/Users/Acer/Downloads/chromedriver_win322/chromedriver")
browser.get("https://web.whatsapp.com/")
wait = WebDriverWait(browser, 600)
#name = input("name to be entered")
target = '"user name"'
#message = input("enter the message to be send")
string = "message to be sent"
x_arg = '//span[contains(@title,' + target + ')]'
target = wait.until(ec.presence_of_element_located((By.XPATH, x_arg)))
target.click()

input_box = browser.find_element_by_class_name("_3uMse")

for i in range(999):
    input_box.send_keys(string + Keys.ENTER)
