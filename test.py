from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
import threading


def findNameAndNumber(url):
    email = ""
    password = ""


    chrome_options = Options()
    chrome_options.add_argument("--headless")

    driver = webdriver.Chrome(options=chrome_options)


    driver.get(f"{url}")

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

    # titleAndNumber = driver.find_element(By.XPATH, "/html/head/title")
    # print(titleAndNumber)
    # ticketNumber = driver.find_elements(By.CLASS_NAME, "css-1gd7hga")
    # time.sleep(3)
    # ticketName = driver.find_element(By.CLASS_NAME, "_1wyb1tcg _vwz41f4h")
    #
    # print(f"{ticketNumber[3].text} dash {ticketName.text}")
    # print(ticketNumber[3].text)
    # print(ticketName.text)

    driver.quit()
#findNameAndNumber()



















