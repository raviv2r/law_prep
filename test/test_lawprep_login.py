# import logging
# import requests
#
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# def driver():
#     driver = webdriver.Chrome()
#     yield driver
#
#
# def lawprep_login(driver):
#     Logger = logging.getLogger(__name__)
#     driver.get("https://courses.lawpreptutorial.com/")
#     driver.maximize_window()
#
#     mobile_number = driver.find_element(By.ID,"mobile_number")
#     mobile_number.send_Key('8559933187')
#
#     password = driver.find_element(By.ID,"password")
#     password.send_keys("123456")
#
#     login = driver.find_element(By.__class__,"btn btn-submit btn-primary btn-block")
#
#
#

import logging
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_open_url(driver):
    LOGGER = logging.getLogger(__name__)
    driver.get("https://courses.lawpreptutorial.com/")
    driver.maximize_window()

    wait = WebDriverWait(driver, 10)

    # mobile_number = driver.find_element(By.ID,'mobile_number')
    # mobile_number.send_Key('8559933187')

    mobile_number = wait.until(EC.presence_of_element_located((By.ID, "mobile_number")))
    mobile_number.send_keys('8559933187')

    password = driver.find_element(By.ID,'password')
    password.send_keys("123456")

    # login = driver.find_element(By.__class__,'btn btn-submit btn-primary btn-block')

    login_button = driver.find_element(By.CLASS_NAME, "btn-submit")  # Using the class name to find the button
    login_button.click()

