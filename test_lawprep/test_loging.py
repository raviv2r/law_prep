import logging
import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_open_url(driver):
    LOGGER = logging.getLogger(__name__)
    driver.get("https://lawpreptutorial.com/")
    driver.maximize_window()


def test_student_redirection(driver):
    driver.get("https://lawpreptutorial.com/")

    # Wait for the "Student Portal" link to be visible
    student_portal_link = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.LINK_TEXT, 'Student Portal'))
    )
    student_portal_link.click()

    # Wait for the page to load
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, 'Login'))
    )

    # Locate and click the "Login" link
    login_link = driver.find_element(By.LINK_TEXT, 'Login')
    assert login_link.is_displayed(), "Login link should be displayed"
    time.sleep(15)  # This might not be necessary, but you can use it for debugging purposes




def test_course_law_prep_login(driver):
    driver.get("https://courses.lawpreptutorial.com/")
    login_portal_link = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.LINK_TEXT, 'Login'))
    )
    login_portal_link.click()

def test_lank_mobilenumber(driver):
    driver.get("https://courses.lawpreptutorial.com/")
    login_portal_link = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.LINK_TEXT, 'Login'))
    )
    login_portal_link.click()


    mobilenumber = driver.find_element(By.ID, "mobile_number")
    mobilenumber.send_keys("")

    password =driver.find_element(By.ID,"password")
    password.send_keys("123456")

    login_button = driver.find_element(By.XPATH,'//*[@id="auth-modal___BV_modal_body_"]/div/div/div/div[1]/form/div[3]/button').click()

    error_message =driver.find_element(By.CLASS_NAME,"#__BVID__187 > div > div.mt-2.mb-3.d-block.invalid-feedback")
    assert error_message.is_displayed(),"Please enter a valid mobile number."

def test_blank_password(driver):
    driver.get("https://courses.lawpreptutorial.com/")
    login_portal_link = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.LINK_TEXT, 'Login'))
    )
    login_portal_link.click()


    mobilenumber = driver.find_element(By.ID, "mobile_number")
    mobilenumber.send_keys("8559933187")

    password =driver.find_element(By.ID,"password")
    password.send_keys("")

    login_button = driver.find_element(By.XPATH,'//*[@id="auth-modal___BV_modal_body_"]/div/div/div/div[1]/form/div[3]/button').click()

    error_message =driver.find_element(By.CLASS_NAME,"#__BVID__187 > div > div.mt-2.mb-3.d-block.invalid-feedback")
    assert error_message.is_displayed(),"The new password field is required."

def test_both_blank(driver):
    driver.get("https://courses.lawpreptutorial.com/")
    login_portal_link = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.LINK_TEXT, 'Login'))
    )
    login_portal_link.click()


    mobilenumber = driver.find_element(By.ID, "mobile_number")
    mobilenumber.send_keys("")

    password =driver.find_element(By.ID,"")
    password.send_keys("")

    login_button = driver.find_element(By.XPATH,'//*[@id="auth-modal___BV_modal_body_"]/div/div/div/div[1]/form/div[3]/button').click()

    error_message =driver.find_element(By.CLASS_NAME,"#__BVID__187 > div > div.mt-2.mb-3.d-block.invalid-feedback")
    assert error_message.is_displayed(),"Please enter a valid mobile number.""The new password field is required."

def test_sucess_login(driver):
    driver.get("https://courses.lawpreptutorial.com/")
    login_portal_link = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.LINK_TEXT, 'Login'))
    )
    login_portal_link.click()


    mobilenumber = driver.find_element(By.ID, "mobile_number")
    mobilenumber.send_keys("8559933187")

    password =driver.find_element(By.ID,"password")
    password.send_keys("123456")

    login_button = driver.find_element(By.XPATH,'//*[@id="auth-modal___BV_modal_body_"]/div/div/div/div[1]/form/div[3]/button').click()

    time.sleep(15)
    try:
        driver.find_element(By.XPATH, '//*[@id="auth-modal___BV_modal_body_"]/div/div/div/div[1]/form/div[3]/button')
        isLogin = True
    except:
        isLogin = False
    print('Is I am login : ', isLogin)
