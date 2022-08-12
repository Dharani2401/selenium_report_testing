from selenium import webdriver
import pytest
import unittest



from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import time
from datetime import date, datetime

# pytest -v --html=report.html test_report.py


@pytest.fixture()
def setup():
    global driver
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logger"])
    driver = webdriver.Chrome(options=options, executable_path="D:\\iTAP\\chromedriver.exe")
    driver.maximize_window()
    yield
    driver.close()

def test_pagetitle(setup):
    driver.get("https://www.saucedemo.com/")
    x = driver.title
    print(x)
    assert x == "Swag Labs"

def test_sample(setup):
    xpath_list = []
    value_list = []
    text_list = []
    classname_list = []
    lines = ''
    steps = ''
    message = ''
    step_no = 0
    output_list = []
    output = {}
    try:
        start_time = datetime.now()
        driver.get("https://www.saucedemo.com/")
        xpath_list.append('Open_Browser')
        value_list.append("https://www.saucedemo.com/")
        classname_list.append('')
        text_list.append('')
        driver.save_screenshot('D:\iTAP\Recorded_Scenarios\\demo\\test\\page1.png')
        driver.maximize_window()

        lines = '//input[@name="user-name"]'
        xpath_list.append('//input[@name="user-name"]')
        value_list.append('standard_user')
        element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//input[@name="user-name"]')))
        classname_list.append(element.get_attribute("className"))
        actions = ActionChains(driver)
        actions.move_to_element(element).perform()
        element.clear()
        element.send_keys('standard_user')
        steps += "\n" + "test_step_inputstandard_user"
        text_list.append(element.text)
        driver.save_screenshot('D:\iTAP\Recorded_Scenarios\\demo\\test\\page2.png')
        output['//input[@name="user-name"]'] = "standard_user"

        lines = '//input[@name="password"]'
        xpath_list.append('//input[@name="password"]')
        value_list.append('secret_sauce')
        element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//input[@name="password"]')))
        classname_list.append(element.get_attribute("className"))
        actions = ActionChains(driver)
        actions.move_to_element(element).perform()
        element.clear()
        element.send_keys('secret_sauce')
        steps += "\n" + "test_step_inputsecret_sauce"
        text_list.append(element.text)
        driver.save_screenshot('D:\iTAP\Recorded_Scenarios\\demo\\test\\page3.png')
        output['//input[@name="password"]'] = "secret_sauce"

        lines = '//input[@name="login-button"]'
        xpath_list.append('//input[@name="login-button"]')
        value_list.append('')
        element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//input[@name="login-button"]')))
        classname_list.append(element.get_attribute("className"))
        steps += "\n" + "test_step_click" + element.text
        text_list.append(element.text)
        actions = ActionChains(driver)
        actions.move_to_element(element).perform()
        driver.save_screenshot('D:\iTAP\Recorded_Scenarios\\demo\\test\\page4.png')
        output['//input[@name="login-button"]'] = element.text
        try:
            element.click()
        except Exception:
            driver.execute_script("arguments[0].click();", element)

        with open("D:\iTAP\Recorded_Scenarios\\demo\\test\\logfile.log", "w+") as external_file:
            finish_time = datetime.now()
            total = finish_time - start_time
            total = str(total).split(".")[0]
            final = "total time taken : " + total
            external_file.write("test passed - no errors" + "\n" + steps + "\n" + message + "\nxpath list " + str(
                xpath_list) + "\nvalue list " + str(value_list) + "\nclass name list " + str(
                classname_list) + "\ntext list " + str(text_list) + "\n" + final)
        print("Test Passed", steps)
    except Exception as e:
        print(e)
        finish_time = datetime.now()
        total = finish_time - start_time
        total = str(total).split(".")[0]
        path = open("D:\iTAP\Recorded_Scenarios\\demo\\test\\logfile.log", 'w+')
        path.write("failed:" + str(
            e) + '\n' + steps + "\n" + message + "\n Execution stopped at : " + lines + "\nxpath list " + str(
            xpath_list) + "\nvalue list " + str(value_list) + "\nclass name list " + str(
            classname_list) + "\ntext list " + str(text_list) + " \n total time taken : " + total)
        path.close()


def test_sample1(setup):
    xpath_list = []
    value_list = []
    text_list = []
    classname_list = []
    lines = ''
    steps = ''
    message = ''
    step_no = 0
    output_list = []
    output = {}
    try:
        start_time = datetime.now()
        driver.get("https://www.saucedemo.com/")
        xpath_list.append('Open_Browser')
        value_list.append("https://www.saucedemo.com/")
        classname_list.append('')
        text_list.append('')
        driver.save_screenshot('D:\iTAP\Recorded_Scenarios\\demo\\test\\page1.png')
        driver.maximize_window()

        lines = '//input[@name="user-name"]'
        xpath_list.append('//input[@name="user-name"]')
        value_list.append('standard_user')
        element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//input[@name="use"]')))
        classname_list.append(element.get_attribute("className"))
        actions = ActionChains(driver)
        actions.move_to_element(element).perform()
        element.clear()
        element.send_keys('standard_user')
        steps += "\n" + "test_step_inputstandard_user"
        text_list.append(element.text)
        driver.save_screenshot('D:\iTAP\Recorded_Scenarios\\demo\\test\\page2.png')
        output['//input[@name="user-name"]'] = "standard_user"

        lines = '//input[@name="password"]'
        xpath_list.append('//input[@name="password"]')
        value_list.append('secret_sauce')
        element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//input[@name="password"]')))
        classname_list.append(element.get_attribute("className"))
        actions = ActionChains(driver)
        actions.move_to_element(element).perform()
        element.clear()
        element.send_keys('secret_sauce')
        steps += "\n" + "test_step_inputsecret_sauce"
        text_list.append(element.text)
        driver.save_screenshot('D:\iTAP\Recorded_Scenarios\\demo\\test\\page3.png')
        output['//input[@name="password"]'] = "secret_sauce"

        lines = '//input[@name="login-button"]'
        xpath_list.append('//input[@name="login-button"]')
        value_list.append('')
        element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//input[@name="login-button"]')))
        classname_list.append(element.get_attribute("className"))
        steps += "\n" + "test_step_click" + element.text
        text_list.append(element.text)
        actions = ActionChains(driver)
        actions.move_to_element(element).perform()
        driver.save_screenshot('D:\iTAP\Recorded_Scenarios\\demo\\test\\page4.png')
        output['//input[@name="login-button"]'] = element.text
        try:
            element.click()
        except Exception:
            driver.execute_script("arguments[0].click();", element)
    except Exception as e:
        print(e)
        finish_time = datetime.now()
        total = finish_time - start_time
        total = str(total).split(".")[0]
        path = open("D:\iTAP\Recorded_Scenarios\\demo\\test\\logfile.log", 'w+')
        path.write("failed:" + str(
            e) + '\n' + steps + "\n" + message + "\n Execution stopped at : " + lines + "\nxpath list " + str(
            xpath_list) + "\nvalue list " + str(value_list) + "\nclass name list " + str(
            classname_list) + "\ntext list " + str(text_list) + " \n total time taken : " + total)
        path.close()


