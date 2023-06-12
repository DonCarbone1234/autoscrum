from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
import threading


def findNameAndNumber(url):

    for x in url:

        email = ""
        password = ""

        chrome_options = Options()
        chrome_options.add_argument("--headless")

        driver = webdriver.Chrome(options=chrome_options)

        driver.get(f"{x}")

        while driver.find_element(By.NAME, "username") is None:
            time.sleep(0.25)

        driver.find_element(By.NAME, "username").send_keys(email)
        time.sleep(0.1)
        driver.find_element(By.ID, "login-submit").click()
        time.sleep(0.1)
        driver.find_element(By.NAME, "password").send_keys(password)
        time.sleep(0.1)
        driver.find_element(By.ID, "login-submit").click()
        time.sleep(4)
        print(driver.title.replace(" - Jira", ""))

        driver.quit()
