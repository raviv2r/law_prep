import logging
import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_open_url(driver):
    LOGGER = logging.getLogger(__name__)
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    driver.maximize_window()

def test_blank_username(driver):
    driver.get("https://katalon-demo-cura.herokuapp.com/")  # You might want to navigate to the page again
    link = driver.find_element(By.LINK_TEXT, "Make Appointment")
    link.click()

    username = driver.find_element(By.ID, "txt-username")
    username.send_keys("")

    password = driver.find_element(By.NAME, "password")
    password.send_keys("ThisIsNotAPassword")

    login_button = driver.find_element(By.ID, "btn-login").click()

    error_message = driver.find_element(By.CLASS_NAME, "lead text-dange")
    assert error_message.is_displayed(), "Login failed! Please ensure the username and password are valid."

def test_blank_password(driver):
    driver.get("https://katalon-demo-cura.herokuapp.com/")  # You might want to navigate to the page again
    link = driver.find_element(By.LINK_TEXT, "Make Appointment")
    link.click()

    username = driver.find_element(By.ID, "txt-username")
    username.send_keys("John Doe")

    password = driver.find_element(By.NAME, "password")
    password.send_keys("")

    login_button = driver.find_element(By.ID, "btn-login").click()

    error_message = driver.find_element(By.CLASS_NAME, "lead text-dange")
    assert error_message.is_displayed(), "Login failed! Please ensure the username and password are valid."

def test_valid_username(driver):
    driver.get("https://katalon-demo-cura.herokuapp.com/")  # You might want to navigate to the page again
    link = driver.find_element(By.LINK_TEXT, "Make Appointment")
    link.click()

    username = driver.find_element(By.ID, "txt-username")
    username.send_keys("John Doe")

    password = driver.find_element(By.NAME, "password")
    password.send_keys("ThisIsNotAPassword")

    login_button = driver.find_element(By.ID, "btn-login").click()

    time.sleep(15)
    try:
        driver.find_element(By.XPATH,'//*[@id="appointment"]/div/div/div/h2')
        isLogin = True
    except:
        isLogin = False
    print('Is I am login : ',isLogin)