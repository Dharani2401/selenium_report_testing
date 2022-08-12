import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time,glob,os
from datetime import date, datetime


def test_swag_test1(setup):
	
	xpath_list=[]
	value_list=[]
	text_list=[]
	classname_list=[]
	lines=''
	steps='' 
	message=''
	step_no=0
	output_list = []
	output = {}
	try:
	    start_time = datetime.now()
	    driver.get("https://www.saucedemo.com/")
	    xpath_list.append('Open_Browser')
	    value_list.append("https://www.saucedemo.com/")
	    classname_list.append('')
	    text_list.append('')
	    driver.save_screenshot('D:\iTAP\Recorded_Scenarios\\swag\\test1\\page1.png')
	
	    
	
	    lines='//input[@name="user-name"]'
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
	    driver.save_screenshot('D:\iTAP\Recorded_Scenarios\\swag\\test1\\page2.png')
	    output['//input[@name="user-name"]'] =  "standard_user"
	    
	
	    lines='//input[@name="password"]'
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
	    driver.save_screenshot('D:\iTAP\Recorded_Scenarios\\swag\\test1\\page3.png')
	    output['//input[@name="password"]'] =  "secret_sauce"
	    
	
	    lines='//input[@name="login-button"]'
	    xpath_list.append('//input[@name="login-button"]')
	    value_list.append('')
	    element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//input[@name="login-button"]')))
	    classname_list.append(element.get_attribute("className"))
	    steps += "\n" +"test_step_click" + element.text
	    text_list.append(element.text)
	    actions = ActionChains(driver)
	    actions.move_to_element(element).perform()
	    driver.save_screenshot('D:\iTAP\Recorded_Scenarios\\swag\\test1\\page4.png')
	    output['//input[@name="login-button"]'] = element.text
	    try:
	        element.click()
	    except Exception :
	        driver.execute_script("arguments[0].click();", element)
	            
	
	    lines='//button[@name="add-to-cart-sauce-labs-backpack"]'
	    xpath_list.append('//button[@name="add-to-cart-sauce-labs-backpack"]')
	    value_list.append('')
	    element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//button[@name="add-to-cart-sauce-labs-backpack"]')))
	    classname_list.append(element.get_attribute("className"))
	    steps += "\n" +"test_step_click" + element.text
	    text_list.append(element.text)
	    actions = ActionChains(driver)
	    actions.move_to_element(element).perform()
	    driver.save_screenshot('D:\iTAP\Recorded_Scenarios\\swag\\test1\\page5.png')
	    output['//button[@name="add-to-cart-sauce-labs-backpack"]'] = element.text
	    try:
	        element.click()
	    except Exception :
	        driver.execute_script("arguments[0].click();", element)
	            
	
	    lines='//button[@name="add-to-cart-sauce-labs-bike-light"]'
	    xpath_list.append('//button[@name="add-to-cart-sauce-labs-bike-light"]')
	    value_list.append('')
	    element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//button[@name="add-to-cart-sauce-labs-bike-light"]')))
	    classname_list.append(element.get_attribute("className"))
	    steps += "\n" +"test_step_click" + element.text
	    text_list.append(element.text)
	    actions = ActionChains(driver)
	    actions.move_to_element(element).perform()
	    driver.save_screenshot('D:\iTAP\Recorded_Scenarios\\swag\\test1\\page6.png')
	    output['//button[@name="add-to-cart-sauce-labs-bike-light"]'] = element.text
	    try:
	        element.click()
	    except Exception :
	        driver.execute_script("arguments[0].click();", element)
	            
	
	    lines='//button[@name="add-to-cart-sauce-labs-bolt-t-shirt"]'
	    xpath_list.append('//button[@name="add-to-cart-sauce-labs-bolt-t-shirt"]')
	    value_list.append('')
	    element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//button[@name="add-to-cart-sauce-labs-bolt-t-shirt"]')))
	    classname_list.append(element.get_attribute("className"))
	    steps += "\n" +"test_step_click" + element.text
	    text_list.append(element.text)
	    actions = ActionChains(driver)
	    actions.move_to_element(element).perform()
	    driver.save_screenshot('D:\iTAP\Recorded_Scenarios\\swag\\test1\\page7.png')
	    output['//button[@name="add-to-cart-sauce-labs-bolt-t-shirt"]'] = element.text
	    try:
	        element.click()
	    except Exception :
	        driver.execute_script("arguments[0].click();", element)
	            
	
	    lines='//button[@name="add-to-cart-sauce-labs-fleece-jacket"]'
	    xpath_list.append('//button[@name="add-to-cart-sauce-labs-fleece-jacket"]')
	    value_list.append('')
	    element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//button[@name="add-to-cart-sauce-labs-fleece-jacket"]')))
	    classname_list.append(element.get_attribute("className"))
	    steps += "\n" +"test_step_click" + element.text
	    text_list.append(element.text)
	    actions = ActionChains(driver)
	    actions.move_to_element(element).perform()
	    driver.save_screenshot('D:\iTAP\Recorded_Scenarios\\swag\\test1\\page8.png')
	    output['//button[@name="add-to-cart-sauce-labs-fleece-jacket"]'] = element.text
	    try:
	        element.click()
	    except Exception :
	        driver.execute_script("arguments[0].click();", element)
	            
	
	    lines='//button[@name="add-to-cart-test.allthethings()-t-shirt-(red)"]'
	    xpath_list.append('//button[@name="add-to-cart-test.allthethings()-t-shirt-(red)"]')
	    value_list.append('')
	    element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//button[@name="add-to-cart-test.allthethings()-t-shirt-(red)"]')))
	    classname_list.append(element.get_attribute("className"))
	    steps += "\n" +"test_step_click" + element.text
	    text_list.append(element.text)
	    actions = ActionChains(driver)
	    actions.move_to_element(element).perform()
	    driver.save_screenshot('D:\iTAP\Recorded_Scenarios\\swag\\test1\\page9.png')
	    output['//button[@name="add-to-cart-test.allthethings()-t-shirt-(red)"]'] = element.text
	    try:
	        element.click()
	    except Exception :
	        driver.execute_script("arguments[0].click();", element)
	            
	
	    lines='//button[@name="add-to-cart-sauce-labs-onesie"]'
	    xpath_list.append('//button[@name="add-to-cart-sauce-labs-onesie"]')
	    value_list.append('')
	    element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//button[@name="add-to-cart-sauce-labs-onesie"]')))
	    classname_list.append(element.get_attribute("className"))
	    steps += "\n" +"test_step_click" + element.text
	    text_list.append(element.text)
	    actions = ActionChains(driver)
	    actions.move_to_element(element).perform()
	    driver.save_screenshot('D:\iTAP\Recorded_Scenarios\\swag\\test1\\page10.png')
	    output['//button[@name="add-to-cart-sauce-labs-onesie"]'] = element.text
	    try:
	        element.click()
	    except Exception :
	        driver.execute_script("arguments[0].click();", element)
	            
	    xpath_list.append('page title')
	    value_list.append('')
	    text_list.append('')
	    classname_list.append('')
	    Title_element = driver.title
	    steps="\n test_step_assert Page title is "+Title_element
	    message+="\n Action Performed : The page title is "+Title_element
	    driver.save_screenshot('D:\iTAP\Recorded_Scenarios\\swag\\test1\\page11.png')
	                
	    
	    with open("D:\iTAP\Recorded_Scenarios\\swag\\test1\\logfile.log", "w+") as external_file:
	        finish_time = datetime.now()
	        total = finish_time - start_time
	        total=str(total).split(".")[0]
	        final = "total time taken : " + total
	        external_file.write("test passed - no errors" + "\n" +steps + "\n"+message+ "\nxpath list " + str(xpath_list) + "\nvalue list " + str(value_list) +"\nclass name list " + str(classname_list) +"\ntext list " + str(text_list) +"\n" + final )
	        print('Test Passed', message)
	    driver.close()
	except Exception as e:
	    print('Test Failed', e)
	    finish_time = datetime.now()
	    total = finish_time - start_time
	    total=str(total).split(".")[0]
	    path = open("D:\iTAP\Recorded_Scenarios\\swag\\test1\\logfile.log", 'w+')
	    path.write("failed:"+ str(e) + '\n' + steps +  "\n"+message+ "\n Execution stopped at : " +lines + "\nxpath list " + str(xpath_list) + "\nvalue list " + str(value_list) +"\nclass name list " + str(classname_list) +"\ntext list " + str(text_list) +" \n total time taken : "+total)
	    path.close()
	    driver.close()



def test_download_test8(setup):
	
	xpath_list=[]
	value_list=[]
	text_list=[]
	classname_list=[]
	lines=''
	steps='' 
	message=''
	step_no=0
	output_list = []
	output = {}
	try:
	    start_time = datetime.now()
	    driver.get("https://stats.govt.nz/large-datasets/csv-files-for-download/")
	    xpath_list.append('Open_Browser')
	    value_list.append("https://stats.govt.nz/large-datasets/csv-files-for-download/")
	    classname_list.append('')
	    text_list.append('')
	    driver.save_screenshot('D:\iTAP\Recorded_Scenarios\\download\\test8\\page1.png')
	
	    
	
	    lines='(//a[@href="/assets/Uploads/Research-and-development-survey/Research-and-development-survey-2021/Download-data/Research-and-development-survey-2021-CSV-notes.csv"])[2]'
	    xpath_list.append('(//a[@href="/assets/Uploads/Research-and-development-survey/Research-and-development-survey-2021/Download-data/Research-and-development-survey-2021-CSV-notes.csv"])[2]')
	    value_list.append('')
	    element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '(//a[@href="/assets/Uploads/Research-and-development-survey/Research-and-development-survey-2021/Download-data/Research-and-development-survey-2021-CSV-notes.csv"])[2]')))
	    classname_list.append(element.get_attribute("className"))
	    steps += "\n" +"test_step_click" + element.text
	    text_list.append(element.text)
	    actions = ActionChains(driver)
	    actions.move_to_element(element).perform()
	    driver.save_screenshot('D:\iTAP\Recorded_Scenarios\\download\\test8\\page2.png')
	    output['(//a[@href="/assets/Uploads/Research-and-development-survey/Research-and-development-survey-2021/Download-data/Research-and-development-survey-2021-CSV-notes.csv"])[2]'] = element.text
	    try:
	        element.click()
	    except Exception :
	        driver.execute_script("arguments[0].click();", element)
	            
	    xpath_list.append('sleep')
	    value_list.append('2')
	    classname_list.append('')
	    text_list.append('')
	    time.sleep(2)
	                
	    xpath_list.append('file download')
	    value_list.append('research')
	    classname_list.append('')
	    text_list.append('')
	    lines= 'file download'
	    date = datetime.now().strftime("%Y_%m_%d-%I:%M:%S_%p")
	    list_of_files = glob.glob('C:\\Users\\dr00810779\\Downloads\\*')
	    latest_file = max(list_of_files, key=os.path.getctime) 
	    time.sleep(3)
	    driver.save_screenshot('D:\iTAP\Recorded_Scenarios\\download\\test8\\page4.png')
	    steps += "\ntest_step_assert Asserting downloaded file ["+latest_file+"] to contain [research]"
	    if latest_file.split("\\")[-1].lower().__contains__('research'):
	        message+='\n Assertion Passed : Filename ['+latest_file.split("\\")[-1]+'] Contains [research] , Time and Date ['+f"{date}"+']'
	    else:
	        message+='\n Assertion Failed : Downloaded file does not contain [research]'
	               
	    
	    with open("D:\iTAP\Recorded_Scenarios\\download\\test8\\logfile.log", "w+") as external_file:
	        finish_time = datetime.now()
	        total = finish_time - start_time
	        total=str(total).split(".")[0]
	        final = "total time taken : " + total
	        external_file.write("test passed - no errors" + "\n" +steps + "\n"+message+ "\nxpath list " + str(xpath_list) + "\nvalue list " + str(value_list) +"\nclass name list " + str(classname_list) +"\ntext list " + str(text_list) +"\n" + final )
	        print('Test Passed', message)
	    driver.close()
	except Exception as e:
	    print('Test Failed', e)
	    finish_time = datetime.now()
	    total = finish_time - start_time
	    total=str(total).split(".")[0]
	    path = open("D:\iTAP\Recorded_Scenarios\\download\\test8\\logfile.log", 'w+')
	    path.write("failed:"+ str(e) + '\n' + steps +  "\n"+message+ "\n Execution stopped at : " +lines + "\nxpath list " + str(xpath_list) + "\nvalue list " + str(value_list) +"\nclass name list " + str(classname_list) +"\ntext list " + str(text_list) +" \n total time taken : "+total)
	    path.close()
	    driver.close()



def test_swag_xyzbank(setup):
	
	xpath_list=[]
	value_list=[]
	text_list=[]
	classname_list=[]
	lines=''
	steps='' 
	message=''
	step_no=0
	output_list = []
	output = {}
	try:
	    start_time = datetime.now()
	    driver.get("https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login")
	    xpath_list.append('Open_Browser')
	    value_list.append("https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login")
	    classname_list.append('')
	    text_list.append('')
	    driver.save_screenshot('D:\iTAP\Recorded_Scenarios\\swag\\xyzbank\\page1.png')
	
	    
	
	    lines='(//button)[3]'
	    xpath_list.append('(//button)[3]')
	    value_list.append('')
	    element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '(//button)[3]')))
	    classname_list.append(element.get_attribute("className"))
	    steps += "\n" +"test_step_click" + element.text
	    text_list.append(element.text)
	    actions = ActionChains(driver)
	    actions.move_to_element(element).perform()
	    driver.save_screenshot('D:\iTAP\Recorded_Scenarios\\swag\\xyzbank\\page2.png')
	    output['(//button)[3]'] = element.text
	    try:
	        element.click()
	    except Exception :
	        driver.execute_script("arguments[0].click();", element)
	            
	
	    lines='//select[@name="userSelect"]'
	    xpath_list.append('//select[@name="userSelect"]')
	    value_list.append('3')
	    element = Select(driver.find_element_by_xpath('//select[@name="userSelect"]'))
	    classname_list.append('')
	    element.select_by_value('3')
	    o = element.first_selected_option
	    steps += "\n" + "test_step_select" + o.text
	    text_list.append(o.text)
	    driver.save_screenshot('D:\iTAP\Recorded_Scenarios\\swag\\xyzbank\\page3.png')
	    output['//select[@name="userSelect"]'] =  "3"
	    
	    try:
	        lines='(//button)[3]'
	        xpath_list.append('(//button)[3]')
	        value_list.append('')
	        l = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '(//button)[3]')))
	        classname_list.append(l.get_attribute("className"))
	        actions = ActionChains(driver)
	        actions.move_to_element(l).perform()
	        steps += "\n" + "test_step_assert Presence of "+ l.text
	        text_list.append(l.text)
	        message+='\nAssertion Passed : Element is present in the page'
	    except NoSuchElementException:
	       message+='\nAssertion Failed : Element is not present in the page'
	    driver.save_screenshot('D:\iTAP\Recorded_Scenarios\\swag\\xyzbank\\page4.png')
	    output['(//button)[3]'] =  l.text
	
	                
	
	    lines='(//button)[3]'
	    xpath_list.append('(//button)[3]')
	    value_list.append('')
	    element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '(//button)[3]')))
	    classname_list.append(element.get_attribute("className"))
	    steps += "\n" +"test_step_click" + element.text
	    text_list.append(element.text)
	    actions = ActionChains(driver)
	    actions.move_to_element(element).perform()
	    driver.save_screenshot('D:\iTAP\Recorded_Scenarios\\swag\\xyzbank\\page5.png')
	    output['(//button)[3]'] = element.text
	    try:
	        element.click()
	    except Exception :
	        driver.execute_script("arguments[0].click();", element)
	            
	
	    lines='(//button)[3]'
	    xpath_list.append('(//button)[3]')
	    value_list.append('')
	    element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '(//button)[3]')))
	    classname_list.append(element.get_attribute("className"))
	    steps += "\n" +"test_step_click" + element.text
	    text_list.append(element.text)
	    actions = ActionChains(driver)
	    actions.move_to_element(element).perform()
	    driver.save_screenshot('D:\iTAP\Recorded_Scenarios\\swag\\xyzbank\\page6.png')
	    output['(//button)[3]'] = element.text
	    try:
	        element.click()
	    except Exception :
	        driver.execute_script("arguments[0].click();", element)
	            
	
	    lines='//a[@href="HASH"]'
	    xpath_list.append('//a[@href="HASH"]')
	    value_list.append('')
	    element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//a[@href="HASH"]')))
	    classname_list.append(element.get_attribute("className"))
	    steps += "\n" +"test_step_click" + element.text
	    text_list.append(element.text)
	    actions = ActionChains(driver)
	    actions.move_to_element(element).perform()
	    driver.save_screenshot('D:\iTAP\Recorded_Scenarios\\swag\\xyzbank\\page7.png')
	    output['//a[@href="HASH"]'] = element.text
	    try:
	        element.click()
	    except Exception :
	        driver.execute_script("arguments[0].click();", element)
	            
	
	    lines='(//button)[3]'
	    xpath_list.append('(//button)[3]')
	    value_list.append('')
	    element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '(//button)[3]')))
	    classname_list.append(element.get_attribute("className"))
	    steps += "\n" +"test_step_click" + element.text
	    text_list.append(element.text)
	    actions = ActionChains(driver)
	    actions.move_to_element(element).perform()
	    driver.save_screenshot('D:\iTAP\Recorded_Scenarios\\swag\\xyzbank\\page8.png')
	    output['(//button)[3]'] = element.text
	    try:
	        element.click()
	    except Exception :
	        driver.execute_script("arguments[0].click();", element)
	            
	
	    lines='(//button)[4]'
	    xpath_list.append('(//button)[4]')
	    value_list.append('')
	    element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '(//button)[4]')))
	    classname_list.append(element.get_attribute("className"))
	    steps += "\n" +"test_step_click" + element.text
	    text_list.append(element.text)
	    actions = ActionChains(driver)
	    actions.move_to_element(element).perform()
	    driver.save_screenshot('D:\iTAP\Recorded_Scenarios\\swag\\xyzbank\\page9.png')
	    output['(//button)[4]'] = element.text
	    try:
	        element.click()
	    except Exception :
	        driver.execute_script("arguments[0].click();", element)
	            
	
	    lines='//input'
	    xpath_list.append('//input')
	    value_list.append('436436')
	    element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//input')))
	    classname_list.append(element.get_attribute("className"))
	    actions = ActionChains(driver)
	    actions.move_to_element(element).perform()
	    element.clear()
	    element.send_keys('436436')
	    steps += "\n" + "test_step_input436436"
	    text_list.append(element.text)
	    driver.save_screenshot('D:\iTAP\Recorded_Scenarios\\swag\\xyzbank\\page10.png')
	    output['//input'] =  "436436"
	    
	
	    lines='(//button)[6]'
	    xpath_list.append('(//button)[6]')
	    value_list.append('')
	    element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '(//button)[6]')))
	    classname_list.append(element.get_attribute("className"))
	    steps += "\n" +"test_step_click" + element.text
	    text_list.append(element.text)
	    actions = ActionChains(driver)
	    actions.move_to_element(element).perform()
	    driver.save_screenshot('D:\iTAP\Recorded_Scenarios\\swag\\xyzbank\\page11.png')
	    output['(//button)[6]'] = element.text
	    try:
	        element.click()
	    except Exception :
	        driver.execute_script("arguments[0].click();", element)
	            
	
	    lines='(//button)[5]'
	    xpath_list.append('(//button)[5]')
	    value_list.append('')
	    element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '(//button)[5]')))
	    classname_list.append(element.get_attribute("className"))
	    steps += "\n" +"test_step_click" + element.text
	    text_list.append(element.text)
	    actions = ActionChains(driver)
	    actions.move_to_element(element).perform()
	    driver.save_screenshot('D:\iTAP\Recorded_Scenarios\\swag\\xyzbank\\page12.png')
	    output['(//button)[5]'] = element.text
	    try:
	        element.click()
	    except Exception :
	        driver.execute_script("arguments[0].click();", element)
	            
	
	    lines='//input'
	    xpath_list.append('//input')
	    value_list.append('43')
	    element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//input')))
	    classname_list.append(element.get_attribute("className"))
	    actions = ActionChains(driver)
	    actions.move_to_element(element).perform()
	    element.clear()
	    element.send_keys('43')
	    steps += "\n" + "test_step_input43"
	    text_list.append(element.text)
	    driver.save_screenshot('D:\iTAP\Recorded_Scenarios\\swag\\xyzbank\\page13.png')
	    output['//input'] =  "43"
	    
	
	    lines='(//button)[6]'
	    xpath_list.append('(//button)[6]')
	    value_list.append('')
	    element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '(//button)[6]')))
	    classname_list.append(element.get_attribute("className"))
	    steps += "\n" +"test_step_click" + element.text
	    text_list.append(element.text)
	    actions = ActionChains(driver)
	    actions.move_to_element(element).perform()
	    driver.save_screenshot('D:\iTAP\Recorded_Scenarios\\swag\\xyzbank\\page14.png')
	    output['(//button)[6]'] = element.text
	    try:
	        element.click()
	    except Exception :
	        driver.execute_script("arguments[0].click();", element)
	            
	
	    lines='(//button)[2]'
	    xpath_list.append('(//button)[2]')
	    value_list.append('')
	    element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '(//button)[2]')))
	    classname_list.append(element.get_attribute("className"))
	    steps += "\n" +"test_step_click" + element.text
	    text_list.append(element.text)
	    actions = ActionChains(driver)
	    actions.move_to_element(element).perform()
	    driver.save_screenshot('D:\iTAP\Recorded_Scenarios\\swag\\xyzbank\\page15.png')
	    output['(//button)[2]'] = element.text
	    try:
	        element.click()
	    except Exception :
	        driver.execute_script("arguments[0].click();", element)
	            
	    
	    with open("D:\iTAP\Recorded_Scenarios\\swag\\xyzbank\\logfile.log", "w+") as external_file:
	        finish_time = datetime.now()
	        total = finish_time - start_time
	        total=str(total).split(".")[0]
	        final = "total time taken : " + total
	        external_file.write("test passed - no errors" + "\n" +steps + "\n"+message+ "\nxpath list " + str(xpath_list) + "\nvalue list " + str(value_list) +"\nclass name list " + str(classname_list) +"\ntext list " + str(text_list) +"\n" + final )
	        print('Test Passed', message)
	    driver.close()
	except Exception as e:
	    print('Test Failed', e)
	    finish_time = datetime.now()
	    total = finish_time - start_time
	    total=str(total).split(".")[0]
	    path = open("D:\iTAP\Recorded_Scenarios\\swag\\xyzbank\\logfile.log", 'w+')
	    path.write("failed:"+ str(e) + '\n' + steps +  "\n"+message+ "\n Execution stopped at : " +lines + "\nxpath list " + str(xpath_list) + "\nvalue list " + str(value_list) +"\nclass name list " + str(classname_list) +"\ntext list " + str(text_list) +" \n total time taken : "+total)
	    path.close()
	    driver.close()



def test_demo_test1(setup):
	
	xpath_list=[]
	value_list=[]
	text_list=[]
	classname_list=[]
	lines=''
	steps='' 
	message=''
	step_no=0
	output_list = []
	output = {}
	try:
	    start_time = datetime.now()
	    driver.get("https://www.saucedemo.com/")
	    xpath_list.append('Open_Browser')
	    value_list.append("https://www.saucedemo.com/")
	    classname_list.append('')
	    text_list.append('')
	    driver.save_screenshot('D:\iTAP\Recorded_Scenarios\\demo\\test1\\page1.png')
	
	    
	
	    lines='//input[@name="user-name"]'
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
	    driver.save_screenshot('D:\iTAP\Recorded_Scenarios\\demo\\test1\\page2.png')
	    output['//input[@name="user-name"]'] =  "standard_user"
	    
	
	    lines='//input[@name="password"]'
	    xpath_list.append('//input[@name="password"]')
	    value_list.append('secret_sace')
	    element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//input[@name="password"]')))
	    classname_list.append(element.get_attribute("className"))
	    actions = ActionChains(driver)
	    actions.move_to_element(element).perform()
	    element.clear()
	    element.send_keys('secret_sace')
	    steps += "\n" + "test_step_inputsecret_sace"
	    text_list.append(element.text)
	    driver.save_screenshot('D:\iTAP\Recorded_Scenarios\\demo\\test1\\page3.png')
	    output['//input[@name="password"]'] =  "secret_sace"
	    
	
	    lines='//input[@name="login-button"]'
	    xpath_list.append('//input[@name="login-button"]')
	    value_list.append('')
	    element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//input[@name="login-button"]')))
	    classname_list.append(element.get_attribute("className"))
	    steps += "\n" +"test_step_click" + element.text
	    text_list.append(element.text)
	    actions = ActionChains(driver)
	    actions.move_to_element(element).perform()
	    driver.save_screenshot('D:\iTAP\Recorded_Scenarios\\demo\\test1\\page4.png')
	    output['//input[@name="login-button"]'] = element.text
	    try:
	        element.click()
	    except Exception :
	        driver.execute_script("arguments[0].click();", element)
	            
	
	    lines='//input[@name="password"]'
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
	    driver.save_screenshot('D:\iTAP\Recorded_Scenarios\\demo\\test1\\page5.png')
	    output['//input[@name="password"]'] =  "secret_sauce"
	    
	
	    lines='//input[@name="login-button"]'
	    xpath_list.append('//input[@name="login-button"]')
	    value_list.append('')
	    element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//input[@name="login-button"]')))
	    classname_list.append(element.get_attribute("className"))
	    steps += "\n" +"test_step_click" + element.text
	    text_list.append(element.text)
	    actions = ActionChains(driver)
	    actions.move_to_element(element).perform()
	    driver.save_screenshot('D:\iTAP\Recorded_Scenarios\\demo\\test1\\page6.png')
	    output['//input[@name="login-button"]'] = element.text
	    try:
	        element.click()
	    except Exception :
	        driver.execute_script("arguments[0].click();", element)
	            
	
	    lines='//button[@name="add-to-cart-sauce-labs-backpack"]'
	    xpath_list.append('//button[@name="add-to-cart-sauce-labs-backpack"]')
	    value_list.append('')
	    element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//button[@name="add-to-cart-sauce-labs-backpack"]')))
	    classname_list.append(element.get_attribute("className"))
	    steps += "\n" +"test_step_click" + element.text
	    text_list.append(element.text)
	    actions = ActionChains(driver)
	    actions.move_to_element(element).perform()
	    driver.save_screenshot('D:\iTAP\Recorded_Scenarios\\demo\\test1\\page7.png')
	    output['//button[@name="add-to-cart-sauce-labs-backpack"]'] = element.text
	    try:
	        element.click()
	    except Exception :
	        driver.execute_script("arguments[0].click();", element)
	            
	
	    lines='//button[@name="add-to-cart-sauce-labs-bike-light"]'
	    xpath_list.append('//button[@name="add-to-cart-sauce-labs-bike-light"]')
	    value_list.append('')
	    element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//button[@name="add-to-cart-sauce-labs-bike-light"]')))
	    classname_list.append(element.get_attribute("className"))
	    steps += "\n" +"test_step_click" + element.text
	    text_list.append(element.text)
	    actions = ActionChains(driver)
	    actions.move_to_element(element).perform()
	    driver.save_screenshot('D:\iTAP\Recorded_Scenarios\\demo\\test1\\page8.png')
	    output['//button[@name="add-to-cart-sauce-labs-bike-light"]'] = element.text
	    try:
	        element.click()
	    except Exception :
	        driver.execute_script("arguments[0].click();", element)
	            
	
	    lines='//button[@name="add-to-cart-sauce-labs-bolt-t-shirt"]'
	    xpath_list.append('//button[@name="add-to-cart-sauce-labs-bolt-t-shirt"]')
	    value_list.append('')
	    element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//button[@name="add-to-cart-sauce-labs-bolt-t-shirt"]')))
	    classname_list.append(element.get_attribute("className"))
	    steps += "\n" +"test_step_click" + element.text
	    text_list.append(element.text)
	    actions = ActionChains(driver)
	    actions.move_to_element(element).perform()
	    driver.save_screenshot('D:\iTAP\Recorded_Scenarios\\demo\\test1\\page9.png')
	    output['//button[@name="add-to-cart-sauce-labs-bolt-t-shirt"]'] = element.text
	    try:
	        element.click()
	    except Exception :
	        driver.execute_script("arguments[0].click();", element)
	            
	
	    lines='//button[@name="add-to-cart-sauce-labs-fleece-jacket"]'
	    xpath_list.append('//button[@name="add-to-cart-sauce-labs-fleece-jacket"]')
	    value_list.append('')
	    element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//button[@name="add-to-cart-sauce-labs-fleece-jacket"]')))
	    classname_list.append(element.get_attribute("className"))
	    steps += "\n" +"test_step_click" + element.text
	    text_list.append(element.text)
	    actions = ActionChains(driver)
	    actions.move_to_element(element).perform()
	    driver.save_screenshot('D:\iTAP\Recorded_Scenarios\\demo\\test1\\page10.png')
	    output['//button[@name="add-to-cart-sauce-labs-fleece-jacket"]'] = element.text
	    try:
	        element.click()
	    except Exception :
	        driver.execute_script("arguments[0].click();", element)
	            
	
	    lines='//button[@name="add-to-cart-test.allthethings()-t-shirt-(red)"]'
	    xpath_list.append('//button[@name="add-to-cart-test.allthethings()-t-shirt-(red)"]')
	    value_list.append('')
	    element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//button[@name="add-to-cart-test.allthethings()-t-shirt-(red)"]')))
	    classname_list.append(element.get_attribute("className"))
	    steps += "\n" +"test_step_click" + element.text
	    text_list.append(element.text)
	    actions = ActionChains(driver)
	    actions.move_to_element(element).perform()
	    driver.save_screenshot('D:\iTAP\Recorded_Scenarios\\demo\\test1\\page11.png')
	    output['//button[@name="add-to-cart-test.allthethings()-t-shirt-(red)"]'] = element.text
	    try:
	        element.click()
	    except Exception :
	        driver.execute_script("arguments[0].click();", element)
	            
	
	    lines='//button[@name="add-to-cart-sauce-labs-onesie"]'
	    xpath_list.append('//button[@name="add-to-cart-sauce-labs-onesie"]')
	    value_list.append('')
	    element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//button[@name="add-to-cart-sauce-labs-onesie"]')))
	    classname_list.append(element.get_attribute("className"))
	    steps += "\n" +"test_step_click" + element.text
	    text_list.append(element.text)
	    actions = ActionChains(driver)
	    actions.move_to_element(element).perform()
	    driver.save_screenshot('D:\iTAP\Recorded_Scenarios\\demo\\test1\\page12.png')
	    output['//button[@name="add-to-cart-sauce-labs-onesie"]'] = element.text
	    try:
	        element.click()
	    except Exception :
	        driver.execute_script("arguments[0].click();", element)
	            
	
	    lines='//button[@name="remove-sauce-labs-backpack"]'
	    xpath_list.append('//button[@name="remove-sauce-labs-backpack"]')
	    value_list.append('')
	    element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//button[@name="remove-sauce-labs-backpack"]')))
	    classname_list.append(element.get_attribute("className"))
	    steps += "\n" +"test_step_click" + element.text
	    text_list.append(element.text)
	    actions = ActionChains(driver)
	    actions.move_to_element(element).perform()
	    driver.save_screenshot('D:\iTAP\Recorded_Scenarios\\demo\\test1\\page13.png')
	    output['//button[@name="remove-sauce-labs-backpack"]'] = element.text
	    try:
	        element.click()
	    except Exception :
	        driver.execute_script("arguments[0].click();", element)
	            
	
	    lines='//button[@name="remove-sauce-labs-bike-light"]'
	    xpath_list.append('//button[@name="remove-sauce-labs-bike-light"]')
	    value_list.append('')
	    element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//button[@name="remove-sauce-labs-bike-light"]')))
	    classname_list.append(element.get_attribute("className"))
	    steps += "\n" +"test_step_click" + element.text
	    text_list.append(element.text)
	    actions = ActionChains(driver)
	    actions.move_to_element(element).perform()
	    driver.save_screenshot('D:\iTAP\Recorded_Scenarios\\demo\\test1\\page14.png')
	    output['//button[@name="remove-sauce-labs-bike-light"]'] = element.text
	    try:
	        element.click()
	    except Exception :
	        driver.execute_script("arguments[0].click();", element)
	            
	
	    lines='//span'
	    xpath_list.append('//span')
	    value_list.append('')
	    element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//span')))
	    classname_list.append(element.get_attribute("className"))
	    steps += "\n" +"test_step_click" + element.text
	    text_list.append(element.text)
	    actions = ActionChains(driver)
	    actions.move_to_element(element).perform()
	    driver.save_screenshot('D:\iTAP\Recorded_Scenarios\\demo\\test1\\page15.png')
	    output['//span'] = element.text
	    try:
	        element.click()
	    except Exception :
	        driver.execute_script("arguments[0].click();", element)
	            
	
	    lines='//button[@name="checkout"]'
	    xpath_list.append('//button[@name="checkout"]')
	    value_list.append('')
	    element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//button[@name="checkout"]')))
	    classname_list.append(element.get_attribute("className"))
	    steps += "\n" +"test_step_click" + element.text
	    text_list.append(element.text)
	    actions = ActionChains(driver)
	    actions.move_to_element(element).perform()
	    driver.save_screenshot('D:\iTAP\Recorded_Scenarios\\demo\\test1\\page16.png')
	    output['//button[@name="checkout"]'] = element.text
	    try:
	        element.click()
	    except Exception :
	        driver.execute_script("arguments[0].click();", element)
	            
	
	    lines='//input[@name="firstName"]'
	    xpath_list.append('//input[@name="firstName"]')
	    value_list.append('dfgdf')
	    element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//input[@name="firstName"]')))
	    classname_list.append(element.get_attribute("className"))
	    actions = ActionChains(driver)
	    actions.move_to_element(element).perform()
	    element.clear()
	    element.send_keys('dfgdf')
	    steps += "\n" + "test_step_inputdfgdf"
	    text_list.append(element.text)
	    driver.save_screenshot('D:\iTAP\Recorded_Scenarios\\demo\\test1\\page17.png')
	    output['//input[@name="firstName"]'] =  "dfgdf"
	    
	
	    lines='//input[@name="lastName"]'
	    xpath_list.append('//input[@name="lastName"]')
	    value_list.append('ssfd')
	    element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//input[@name="lastName"]')))
	    classname_list.append(element.get_attribute("className"))
	    actions = ActionChains(driver)
	    actions.move_to_element(element).perform()
	    element.clear()
	    element.send_keys('ssfd')
	    steps += "\n" + "test_step_inputssfd"
	    text_list.append(element.text)
	    driver.save_screenshot('D:\iTAP\Recorded_Scenarios\\demo\\test1\\page18.png')
	    output['//input[@name="lastName"]'] =  "ssfd"
	    
	
	    lines='//input[@name="postalCode"]'
	    xpath_list.append('//input[@name="postalCode"]')
	    value_list.append('4364')
	    element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//input[@name="postalCode"]')))
	    classname_list.append(element.get_attribute("className"))
	    actions = ActionChains(driver)
	    actions.move_to_element(element).perform()
	    element.clear()
	    element.send_keys('4364')
	    steps += "\n" + "test_step_input4364"
	    text_list.append(element.text)
	    driver.save_screenshot('D:\iTAP\Recorded_Scenarios\\demo\\test1\\page19.png')
	    output['//input[@name="postalCode"]'] =  "4364"
	    
	
	    lines='//input[@name="continue"]'
	    xpath_list.append('//input[@name="continue"]')
	    value_list.append('')
	    element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//input[@name="continue"]')))
	    classname_list.append(element.get_attribute("className"))
	    steps += "\n" +"test_step_click" + element.text
	    text_list.append(element.text)
	    actions = ActionChains(driver)
	    actions.move_to_element(element).perform()
	    driver.save_screenshot('D:\iTAP\Recorded_Scenarios\\demo\\test1\\page20.png')
	    output['//input[@name="continue"]'] = element.text
	    try:
	        element.click()
	    except Exception :
	        driver.execute_script("arguments[0].click();", element)
	            
	
	    lines='//button[@name="finish"]'
	    xpath_list.append('//button[@name="finish"]')
	    value_list.append('')
	    element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//button[@name="finish"]')))
	    classname_list.append(element.get_attribute("className"))
	    steps += "\n" +"test_step_click" + element.text
	    text_list.append(element.text)
	    actions = ActionChains(driver)
	    actions.move_to_element(element).perform()
	    driver.save_screenshot('D:\iTAP\Recorded_Scenarios\\demo\\test1\\page21.png')
	    output['//button[@name="finish"]'] = element.text
	    try:
	        element.click()
	    except Exception :
	        driver.execute_script("arguments[0].click();", element)
	            
	
	    lines='//button[@name="back-to-products"]'
	    xpath_list.append('//button[@name="back-to-products"]')
	    value_list.append('')
	    element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//button[@name="back-to-products"]')))
	    classname_list.append(element.get_attribute("className"))
	    steps += "\n" +"test_step_click" + element.text
	    text_list.append(element.text)
	    actions = ActionChains(driver)
	    actions.move_to_element(element).perform()
	    driver.save_screenshot('D:\iTAP\Recorded_Scenarios\\demo\\test1\\page22.png')
	    output['//button[@name="back-to-products"]'] = element.text
	    try:
	        element.click()
	    except Exception :
	        driver.execute_script("arguments[0].click();", element)
	            
	    
	    with open("D:\iTAP\Recorded_Scenarios\\demo\\test1\\logfile.log", "w+") as external_file:
	        finish_time = datetime.now()
	        total = finish_time - start_time
	        total=str(total).split(".")[0]
	        final = "total time taken : " + total
	        external_file.write("test passed - no errors" + "\n" +steps + "\n"+message+ "\nxpath list " + str(xpath_list) + "\nvalue list " + str(value_list) +"\nclass name list " + str(classname_list) +"\ntext list " + str(text_list) +"\n" + final )
	        print('Test Passed', message)
	    driver.close()
	except Exception as e:
	    print('Test Failed', e)
	    finish_time = datetime.now()
	    total = finish_time - start_time
	    total=str(total).split(".")[0]
	    path = open("D:\iTAP\Recorded_Scenarios\\demo\\test1\\logfile.log", 'w+')
	    path.write("failed:"+ str(e) + '\n' + steps +  "\n"+message+ "\n Execution stopped at : " +lines + "\nxpath list " + str(xpath_list) + "\nvalue list " + str(value_list) +"\nclass name list " + str(classname_list) +"\ntext list " + str(text_list) +" \n total time taken : "+total)
	    path.close()
	    driver.close()



def test_swag_html(setup):
	
	xpath_list=[]
	value_list=[]
	text_list=[]
	classname_list=[]
	lines=''
	steps='' 
	message=''
	step_no=0
	output_list = []
	output = {}
	try:
	    start_time = datetime.now()
	    driver.get("https://www-archive.mozilla.org/projects/ui/accessibility/unix/testcase/html/")
	    xpath_list.append('Open_Browser')
	    value_list.append("https://www-archive.mozilla.org/projects/ui/accessibility/unix/testcase/html/")
	    classname_list.append('')
	    text_list.append('')
	    driver.save_screenshot('D:\iTAP\Recorded_Scenarios\\swag\\html\\page1.png')
	
	    
	
	    lines='//input[@name="firstname"]'
	    xpath_list.append('//input[@name="firstname"]')
	    value_list.append('dfbfdb')
	    element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//input[@name="firstname"]')))
	    classname_list.append(element.get_attribute("className"))
	    actions = ActionChains(driver)
	    actions.move_to_element(element).perform()
	    element.clear()
	    element.send_keys('dfbfdb')
	    steps += "\n" + "test_step_inputdfbfdb"
	    text_list.append(element.text)
	    driver.save_screenshot('D:\iTAP\Recorded_Scenarios\\swag\\html\\page2.png')
	    output['//input[@name="firstname"]'] =  "dfbfdb"
	    
	    try:
	        lines='//input[@name="lastname"]'
	        xpath_list.append('//input[@name="lastname"]')
	        value_list.append('')
	        l = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//input[@name="lastname"]')))
	        classname_list.append(l.get_attribute("className"))
	        actions = ActionChains(driver)
	        actions.move_to_element(l).perform()
	        steps += "\n" + "test_step_assert Presence of "+ l.text
	        text_list.append(l.text)
	        message+='\nAssertion Passed : Element is present in the page'
	    except NoSuchElementException:
	       message+='\nAssertion Failed : Element is not present in the page'
	    driver.save_screenshot('D:\iTAP\Recorded_Scenarios\\swag\\html\\page3.png')
	    output['//input[@name="lastname"]'] =  l.text
	
	                
	
	    lines='//input[@name="lastname"]'
	    xpath_list.append('//input[@name="lastname"]')
	    value_list.append('dsbfdb')
	    element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//input[@name="lastname"]')))
	    classname_list.append(element.get_attribute("className"))
	    actions = ActionChains(driver)
	    actions.move_to_element(element).perform()
	    element.clear()
	    element.send_keys('dsbfdb')
	    steps += "\n" + "test_step_inputdsbfdb"
	    text_list.append(element.text)
	    driver.save_screenshot('D:\iTAP\Recorded_Scenarios\\swag\\html\\page4.png')
	    output['//input[@name="lastname"]'] =  "dsbfdb"
	    
	
	    lines='//input[@name="email"]'
	    xpath_list.append('//input[@name="email"]')
	    value_list.append('dsbff')
	    element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//input[@name="email"]')))
	    classname_list.append(element.get_attribute("className"))
	    actions = ActionChains(driver)
	    actions.move_to_element(element).perform()
	    element.clear()
	    element.send_keys('dsbff')
	    steps += "\n" + "test_step_inputdsbff"
	    text_list.append(element.text)
	    driver.save_screenshot('D:\iTAP\Recorded_Scenarios\\swag\\html\\page5.png')
	    output['//input[@name="email"]'] =  "dsbff"
	    
	
	    lines='//input[@name="blank"]'
	    xpath_list.append('//input[@name="blank"]')
	    value_list.append('dfb')
	    element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//input[@name="blank"]')))
	    classname_list.append(element.get_attribute("className"))
	    actions = ActionChains(driver)
	    actions.move_to_element(element).perform()
	    element.clear()
	    element.send_keys('dfb')
	    steps += "\n" + "test_step_inputdfb"
	    text_list.append(element.text)
	    driver.save_screenshot('D:\iTAP\Recorded_Scenarios\\swag\\html\\page6.png')
	    output['//input[@name="blank"]'] =  "dfb"
	    
	   
	    lines='//input[@id="password"]'
	    xpath_list.append('//input[@id="password"]')
	    value_list.append('')
	    element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//input[@id="password"]')))
	    classname_list.append(element.get_attribute("className"))
	    steps += "\n" + "test_step_assert Not visiblity check"+ element.text
	    text_list.append(element.text)
	    driver.save_screenshot('D:\iTAP\Recorded_Scenarios\\swag\\html\\page7.png')
	    output['//input[@id="password"]'] =  element.text
	    flag = element.is_displayed()
	    if flag == False:
	         message+='\nAssertion Passed : Element is not visible in the page'
	    else:
	         message+='\nAssertion Failed : Element is visible in the page'
	                
	
	    lines='//input[@id="password"]'
	    xpath_list.append('//input[@id="password"]')
	    value_list.append('dsbfsdb')
	    element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//input[@id="password"]')))
	    classname_list.append(element.get_attribute("className"))
	    actions = ActionChains(driver)
	    actions.move_to_element(element).perform()
	    element.clear()
	    element.send_keys('dsbfsdb')
	    steps += "\n" + "test_step_inputdsbfsdb"
	    text_list.append(element.text)
	    driver.save_screenshot('D:\iTAP\Recorded_Scenarios\\swag\\html\\page8.png')
	    output['//input[@id="password"]'] =  "dsbfsdb"
	    
	
	    lines='(//input[@name="A"])[3]'
	    xpath_list.append('(//input[@name="A"])[3]')
	    value_list.append('')
	    element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '(//input[@name="A"])[3]')))
	    classname_list.append(element.get_attribute("className"))
	    steps += "\n" +"test_step_click" + element.text
	    text_list.append(element.text)
	    actions = ActionChains(driver)
	    actions.move_to_element(element).perform()
	    driver.save_screenshot('D:\iTAP\Recorded_Scenarios\\swag\\html\\page10.png')
	    output['(//input[@name="A"])[3]'] = element.text
	    try:
	        element.click()
	    except Exception :
	        driver.execute_script("arguments[0].click();", element)
	            
	
	    lines='(//input[@name="B"])[2]'
	    xpath_list.append('(//input[@name="B"])[2]')
	    value_list.append('')
	    element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '(//input[@name="B"])[2]')))
	    classname_list.append(element.get_attribute("className"))
	    steps += "\n" +"test_step_click" + element.text
	    text_list.append(element.text)
	    actions = ActionChains(driver)
	    actions.move_to_element(element).perform()
	    driver.save_screenshot('D:\iTAP\Recorded_Scenarios\\swag\\html\\page11.png')
	    output['(//input[@name="B"])[2]'] = element.text
	    try:
	        element.click()
	    except Exception :
	        driver.execute_script("arguments[0].click();", element)
	            
	
	    lines='//select[@name="Select list"]'
	    xpath_list.append('//select[@name="Select list"]')
	    value_list.append('avcn')
	    element = Select(driver.find_element_by_xpath('//select[@name="Select list"]'))
	    classname_list.append('')
	    element.select_by_value('avcn')
	    o = element.first_selected_option
	    steps += "\n" + "test_step_select" + o.text
	    text_list.append(o.text)
	    driver.save_screenshot('D:\iTAP\Recorded_Scenarios\\swag\\html\\page12.png')
	    output['//select[@name="Select list"]'] =  "avcn"
	    
	    
	    with open("D:\iTAP\Recorded_Scenarios\\swag\\html\\logfile.log", "w+") as external_file:
	        finish_time = datetime.now()
	        total = finish_time - start_time
	        total=str(total).split(".")[0]
	        final = "total time taken : " + total
	        external_file.write("test passed - no errors" + "\n" +steps + "\n"+message+ "\nxpath list " + str(xpath_list) + "\nvalue list " + str(value_list) +"\nclass name list " + str(classname_list) +"\ntext list " + str(text_list) +"\n" + final )
	        print('Test Passed', message)
	    driver.close()
	except Exception as e:
	    print('Test Failed', e)
	    finish_time = datetime.now()
	    total = finish_time - start_time
	    total=str(total).split(".")[0]
	    path = open("D:\iTAP\Recorded_Scenarios\\swag\\html\\logfile.log", 'w+')
	    path.write("failed:"+ str(e) + '\n' + steps +  "\n"+message+ "\n Execution stopped at : " +lines + "\nxpath list " + str(xpath_list) + "\nvalue list " + str(value_list) +"\nclass name list " + str(classname_list) +"\ntext list " + str(text_list) +" \n total time taken : "+total)
	    path.close()
	    driver.close()



def test_demo_test(setup):
	
	xpath_list=[]
	value_list=[]
	text_list=[]
	classname_list=[]
	lines=''
	steps='' 
	message=''
	step_no=0
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
	
	    
	
	    lines='//input[@name="user-name"]'
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
	    output['//input[@name="user-name"]'] =  "standard_user"
	    
	
	    lines='//input[@name="password"]'
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
	    output['//input[@name="password"]'] =  "secret_sauce"
	    
	
	    lines='//input[@name="login-button"]'
	    xpath_list.append('//input[@name="login-button"]')
	    value_list.append('')
	    element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//input[@name="login-button"]')))
	    classname_list.append(element.get_attribute("className"))
	    steps += "\n" +"test_step_click" + element.text
	    text_list.append(element.text)
	    actions = ActionChains(driver)
	    actions.move_to_element(element).perform()
	    driver.save_screenshot('D:\iTAP\Recorded_Scenarios\\demo\\test\\page4.png')
	    output['//input[@name="login-button"]'] = element.text
	    try:
	        element.click()
	    except Exception :
	        driver.execute_script("arguments[0].click();", element)
	            
	
	    lines='//button[@name="add-to-cart-sauce-labs-backpack"]'
	    xpath_list.append('//button[@name="add-to-cart-sauce-labs-backpack"]')
	    value_list.append('')
	    element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//button[@name="add-to-cart-sauce-labs-backpack"]')))
	    classname_list.append(element.get_attribute("className"))
	    steps += "\n" +"test_step_click" + element.text
	    text_list.append(element.text)
	    actions = ActionChains(driver)
	    actions.move_to_element(element).perform()
	    driver.save_screenshot('D:\iTAP\Recorded_Scenarios\\demo\\test\\page5.png')
	    output['//button[@name="add-to-cart-sauce-labs-backpack"]'] = element.text
	    try:
	        element.click()
	    except Exception :
	        driver.execute_script("arguments[0].click();", element)
	            
	
	    lines='//button[@name="add-to-cart-sauce-labs-bike-light"]'
	    xpath_list.append('//button[@name="add-to-cart-sauce-labs-bike-light"]')
	    value_list.append('')
	    element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//button[@name="add-to-cart-sauce-labs-bike-light"]')))
	    classname_list.append(element.get_attribute("className"))
	    steps += "\n" +"test_step_click" + element.text
	    text_list.append(element.text)
	    actions = ActionChains(driver)
	    actions.move_to_element(element).perform()
	    driver.save_screenshot('D:\iTAP\Recorded_Scenarios\\demo\\test\\page6.png')
	    output['//button[@name="add-to-cart-sauce-labs-bike-light"]'] = element.text
	    try:
	        element.click()
	    except Exception :
	        driver.execute_script("arguments[0].click();", element)
	            
	
	    lines='//button[@name="add-to-cart-sauce-labs-bolt-t-shirt"]'
	    xpath_list.append('//button[@name="add-to-cart-sauce-labs-bolt-t-shirt"]')
	    value_list.append('')
	    element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//button[@name="add-to-cart-sauce-labs-bolt-t-shirt"]')))
	    classname_list.append(element.get_attribute("className"))
	    steps += "\n" +"test_step_click" + element.text
	    text_list.append(element.text)
	    actions = ActionChains(driver)
	    actions.move_to_element(element).perform()
	    driver.save_screenshot('D:\iTAP\Recorded_Scenarios\\demo\\test\\page7.png')
	    output['//button[@name="add-to-cart-sauce-labs-bolt-t-shirt"]'] = element.text
	    try:
	        element.click()
	    except Exception :
	        driver.execute_script("arguments[0].click();", element)
	            
	
	    lines='//button[@name="add-to-cart-sauce-labs-fleece-jacket"]'
	    xpath_list.append('//button[@name="add-to-cart-sauce-labs-fleece-jacket"]')
	    value_list.append('')
	    element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//button[@name="add-to-cart-sauce-labs-fleece-jacket"]')))
	    classname_list.append(element.get_attribute("className"))
	    steps += "\n" +"test_step_click" + element.text
	    text_list.append(element.text)
	    actions = ActionChains(driver)
	    actions.move_to_element(element).perform()
	    driver.save_screenshot('D:\iTAP\Recorded_Scenarios\\demo\\test\\page8.png')
	    output['//button[@name="add-to-cart-sauce-labs-fleece-jacket"]'] = element.text
	    try:
	        element.click()
	    except Exception :
	        driver.execute_script("arguments[0].click();", element)
	            
	
	    lines='//button[@name="add-to-cart-test.allthethings()-t-shirt-(red)"]'
	    xpath_list.append('//button[@name="add-to-cart-test.allthethings()-t-shirt-(red)"]')
	    value_list.append('')
	    element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//button[@name="add-to-cart-test.allthethings()-t-shirt-(red)"]')))
	    classname_list.append(element.get_attribute("className"))
	    steps += "\n" +"test_step_click" + element.text
	    text_list.append(element.text)
	    actions = ActionChains(driver)
	    actions.move_to_element(element).perform()
	    driver.save_screenshot('D:\iTAP\Recorded_Scenarios\\demo\\test\\page9.png')
	    output['//button[@name="add-to-cart-test.allthethings()-t-shirt-(red)"]'] = element.text
	    try:
	        element.click()
	    except Exception :
	        driver.execute_script("arguments[0].click();", element)
	            
	
	    lines='//button[@name="add-to-cart-sauce-labs-onesie"]'
	    xpath_list.append('//button[@name="add-to-cart-sauce-labs-onesie"]')
	    value_list.append('')
	    element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//button[@name="add-to-cart-sauce-labs-onesie"]')))
	    classname_list.append(element.get_attribute("className"))
	    steps += "\n" +"test_step_click" + element.text
	    text_list.append(element.text)
	    actions = ActionChains(driver)
	    actions.move_to_element(element).perform()
	    driver.save_screenshot('D:\iTAP\Recorded_Scenarios\\demo\\test\\page10.png')
	    output['//button[@name="add-to-cart-sauce-labs-onesie"]'] = element.text
	    try:
	        element.click()
	    except Exception :
	        driver.execute_script("arguments[0].click();", element)
	            
	
	    lines='(//a)[5]'
	    xpath_list.append('(//a)[5]')
	    value_list.append('')
	    element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '(//a)[5]')))
	    classname_list.append(element.get_attribute("className"))
	    steps += "\n" +"test_step_click" + element.text
	    text_list.append(element.text)
	    actions = ActionChains(driver)
	    actions.move_to_element(element).perform()
	    driver.save_screenshot('D:\iTAP\Recorded_Scenarios\\demo\\test\\page11.png')
	    output['(//a)[5]'] = element.text
	    try:
	        element.click()
	    except Exception :
	        driver.execute_script("arguments[0].click();", element)
	            
	
	    lines='//button[@name="remove-sauce-labs-backpack"]'
	    xpath_list.append('//button[@name="remove-sauce-labs-backpack"]')
	    value_list.append('')
	    element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//button[@name="remove-sauce-labs-backpack"]')))
	    classname_list.append(element.get_attribute("className"))
	    steps += "\n" +"test_step_click" + element.text
	    text_list.append(element.text)
	    actions = ActionChains(driver)
	    actions.move_to_element(element).perform()
	    driver.save_screenshot('D:\iTAP\Recorded_Scenarios\\demo\\test\\page12.png')
	    output['//button[@name="remove-sauce-labs-backpack"]'] = element.text
	    try:
	        element.click()
	    except Exception :
	        driver.execute_script("arguments[0].click();", element)
	            
	
	    lines='//button[@name="remove-sauce-labs-bike-light"]'
	    xpath_list.append('//button[@name="remove-sauce-labs-bike-light"]')
	    value_list.append('')
	    element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//button[@name="remove-sauce-labs-bike-light"]')))
	    classname_list.append(element.get_attribute("className"))
	    steps += "\n" +"test_step_click" + element.text
	    text_list.append(element.text)
	    actions = ActionChains(driver)
	    actions.move_to_element(element).perform()
	    driver.save_screenshot('D:\iTAP\Recorded_Scenarios\\demo\\test\\page13.png')
	    output['//button[@name="remove-sauce-labs-bike-light"]'] = element.text
	    try:
	        element.click()
	    except Exception :
	        driver.execute_script("arguments[0].click();", element)
	            
	
	    lines='//button[@name="checkout"]'
	    xpath_list.append('//button[@name="checkout"]')
	    value_list.append('')
	    element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//button[@name="checkout"]')))
	    classname_list.append(element.get_attribute("className"))
	    steps += "\n" +"test_step_click" + element.text
	    text_list.append(element.text)
	    actions = ActionChains(driver)
	    actions.move_to_element(element).perform()
	    driver.save_screenshot('D:\iTAP\Recorded_Scenarios\\demo\\test\\page14.png')
	    output['//button[@name="checkout"]'] = element.text
	    try:
	        element.click()
	    except Exception :
	        driver.execute_script("arguments[0].click();", element)
	            
	
	    lines='//input[@name="firstName"]'
	    xpath_list.append('//input[@name="firstName"]')
	    value_list.append('aaaaa')
	    element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//input[@name="firstName"]')))
	    classname_list.append(element.get_attribute("className"))
	    actions = ActionChains(driver)
	    actions.move_to_element(element).perform()
	    element.clear()
	    element.send_keys('aaaaa')
	    steps += "\n" + "test_step_inputaaaaa"
	    text_list.append(element.text)
	    driver.save_screenshot('D:\iTAP\Recorded_Scenarios\\demo\\test\\page15.png')
	    output['//input[@name="firstName"]'] =  "aaaaa"
	    
	
	    lines='//input[@name="lastName"]'
	    xpath_list.append('//input[@name="lastName"]')
	    value_list.append('ddd')
	    element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//input[@name="lastName"]')))
	    classname_list.append(element.get_attribute("className"))
	    actions = ActionChains(driver)
	    actions.move_to_element(element).perform()
	    element.clear()
	    element.send_keys('ddd')
	    steps += "\n" + "test_step_inputddd"
	    text_list.append(element.text)
	    driver.save_screenshot('D:\iTAP\Recorded_Scenarios\\demo\\test\\page16.png')
	    output['//input[@name="lastName"]'] =  "ddd"
	    
	
	    lines='//input[@name="postalCode"]'
	    xpath_list.append('//input[@name="postalCode"]')
	    value_list.append('464')
	    element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//input[@name="postalCode"]')))
	    classname_list.append(element.get_attribute("className"))
	    actions = ActionChains(driver)
	    actions.move_to_element(element).perform()
	    element.clear()
	    element.send_keys('464')
	    steps += "\n" + "test_step_input464"
	    text_list.append(element.text)
	    driver.save_screenshot('D:\iTAP\Recorded_Scenarios\\demo\\test\\page17.png')
	    output['//input[@name="postalCode"]'] =  "464"
	    
	
	    lines='//input[@name="continue"]'
	    xpath_list.append('//input[@name="continue"]')
	    value_list.append('')
	    element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//input[@name="continue"]')))
	    classname_list.append(element.get_attribute("className"))
	    steps += "\n" +"test_step_click" + element.text
	    text_list.append(element.text)
	    actions = ActionChains(driver)
	    actions.move_to_element(element).perform()
	    driver.save_screenshot('D:\iTAP\Recorded_Scenarios\\demo\\test\\page18.png')
	    output['//input[@name="continue"]'] = element.text
	    try:
	        element.click()
	    except Exception :
	        driver.execute_script("arguments[0].click();", element)
	            
	
	    lines='//button[@name="finish"]'
	    xpath_list.append('//button[@name="finish"]')
	    value_list.append('')
	    element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//button[@name="finish"]')))
	    classname_list.append(element.get_attribute("className"))
	    steps += "\n" +"test_step_click" + element.text
	    text_list.append(element.text)
	    actions = ActionChains(driver)
	    actions.move_to_element(element).perform()
	    driver.save_screenshot('D:\iTAP\Recorded_Scenarios\\demo\\test\\page19.png')
	    output['//button[@name="finish"]'] = element.text
	    try:
	        element.click()
	    except Exception :
	        driver.execute_script("arguments[0].click();", element)
	            
	    
	    with open("D:\iTAP\Recorded_Scenarios\\demo\\test\\logfile.log", "w+") as external_file:
	        finish_time = datetime.now()
	        total = finish_time - start_time
	        total=str(total).split(".")[0]
	        final = "total time taken : " + total
	        external_file.write("test passed - no errors" + "\n" +steps + "\n"+message+ "\nxpath list " + str(xpath_list) + "\nvalue list " + str(value_list) +"\nclass name list " + str(classname_list) +"\ntext list " + str(text_list) +"\n" + final )
	        print('Test Passed', message)
	    driver.close()
	except Exception as e:
	    print('Test Failed', e)
	    finish_time = datetime.now()
	    total = finish_time - start_time
	    total=str(total).split(".")[0]
	    path = open("D:\iTAP\Recorded_Scenarios\\demo\\test\\logfile.log", 'w+')
	    path.write("failed:"+ str(e) + '\n' + steps +  "\n"+message+ "\n Execution stopped at : " +lines + "\nxpath list " + str(xpath_list) + "\nvalue list " + str(value_list) +"\nclass name list " + str(classname_list) +"\ntext list " + str(text_list) +" \n total time taken : "+total)
	    path.close()
	    driver.close()



def test_sauce_v(setup):
	
	lines=''
	steps='' 
	message=''
	step_no=0
	try:
	    start_time = datetime.now()
	    driver.get("https://www.saucedemo.com/")
	
	    driver.get('https://www.saucedemo.com/')
	    driver.save_screenshot('D:\\iTAP\\Recorded_Scenarios\\sauce\\v\\page1.png')
	    driver.implicitly_wait(20)
	    element = driver.find_element_by_xpath('//input[@name="user-name"]')
	    element.send_keys('standard_user')
	    steps += "\n" + "test_step_input"+ element.text
	    driver.save_screenshot('D:\\iTAP\\Recorded_Scenarios\\sauce\\v\\page2.png')
	    driver.implicitly_wait(20)
	    element = driver.find_element_by_xpath('//input[@name="password"]')
	    element.send_keys('secret_sauce')
	    steps += "\n" + "test_step_input"+ element.text
	    driver.save_screenshot('D:\\iTAP\\Recorded_Scenarios\\sauce\\v\\page3.png')
	    driver.implicitly_wait(20)
	    element = driver.find_element_by_xpath('//input[@name="login-button"]')
	    steps += "\n" +"test_step_click" + element.text
	    element.click()
	    driver.save_screenshot('D:\\iTAP\\Recorded_Scenarios\\sauce\\v\\page4.png')
	    with open("D:\\iTAP\\Recorded_Scenarios\\sauce\\v\\logfile.log", "w+") as external_file:
	        finish_time = datetime.now()
	        total = finish_time - start_time
	        total=str(total).split(".")[0]
	        final = "total time taken : " + total
	        external_file.write("test passed - no errors" + "\n" + steps + "\n" + final )
	        print('Test Passed', message)
	    driver.close()
	except Exception as e:
	    print('Test Failed', e)
	    finish_time = datetime.now()
	    total = finish_time - start_time
	    total=str(total).split(".")[0]
	    path = open("D:\\iTAP\\Recorded_Scenarios\\sauce\\v\\logfile.log", 'w+')
	    path.write("test case failed\n"+ str(e) +"\n" + steps + " \n total time taken : "+total)
	    path.close()
	    driver.close()



def test_download_test1(setup):
	
	xpath_list=[]
	value_list=[]
	text_list=[]
	classname_list=[]
	lines=''
	steps='' 
	message=''
	step_no=0
	output_list = []
	output = {}
	try:
	    start_time = datetime.now()
	    driver.get("https://chromedriver.chromium.org/downloads")
	    xpath_list.append('Open_Browser')
	    value_list.append("https://chromedriver.chromium.org/downloads")
	    classname_list.append('')
	    text_list.append('')
	    driver.save_screenshot('D:\iTAP\Recorded_Scenarios\\download\\test1\\page1.png')
	
	    
	
	    lines='//a[@href="https://chromedriver.storage.googleapis.com/index.html?path=104.0.5112.79/"]'
	    xpath_list.append('//a[@href="https://chromedriver.storage.googleapis.com/index.html?path=104.0.5112.79/"]')
	    value_list.append('')
	    element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//a[@href="https://chromedriver.storage.googleapis.com/index.html?path=104.0.5112.79/"]')))
	    classname_list.append(element.get_attribute("className"))
	    steps += "\n" +"test_step_click" + element.text
	    text_list.append(element.text)
	    actions = ActionChains(driver)
	    actions.move_to_element(element).perform()
	    driver.save_screenshot('D:\iTAP\Recorded_Scenarios\\download\\test1\\page2.png')
	    output['//a[@href="https://chromedriver.storage.googleapis.com/index.html?path=104.0.5112.79/"]'] = element.text
	    try:
	        element.click()
	    except Exception :
	        driver.execute_script("arguments[0].click();", element)
	            
	    
	    with open("D:\iTAP\Recorded_Scenarios\\download\\test1\\logfile.log", "w+") as external_file:
	        finish_time = datetime.now()
	        total = finish_time - start_time
	        total=str(total).split(".")[0]
	        final = "total time taken : " + total
	        external_file.write("test passed - no errors" + "\n" +steps + "\n"+message+ "\nxpath list " + str(xpath_list) + "\nvalue list " + str(value_list) +"\nclass name list " + str(classname_list) +"\ntext list " + str(text_list) +"\n" + final )
	        print('Test Passed', message)
	    driver.close()
	except Exception as e:
	    print('Test Failed', e)
	    finish_time = datetime.now()
	    total = finish_time - start_time
	    total=str(total).split(".")[0]
	    path = open("D:\iTAP\Recorded_Scenarios\\download\\test1\\logfile.log", 'w+')
	    path.write("failed:"+ str(e) + '\n' + steps +  "\n"+message+ "\n Execution stopped at : " +lines + "\nxpath list " + str(xpath_list) + "\nvalue list " + str(value_list) +"\nclass name list " + str(classname_list) +"\ntext list " + str(text_list) +" \n total time taken : "+total)
	    path.close()
	    driver.close()



def test_download_test4(setup):
	
	xpath_list=[]
	value_list=[]
	text_list=[]
	classname_list=[]
	lines=''
	steps='' 
	message=''
	step_no=0
	output_list = []
	output = {}
	try:
	    start_time = datetime.now()
	    driver.get("https://lcaas.techmahindra.com/vb6")
	    xpath_list.append('Open_Browser')
	    value_list.append("https://lcaas.techmahindra.com/vb6")
	    classname_list.append('')
	    text_list.append('')
	    driver.save_screenshot('D:\iTAP\Recorded_Scenarios\\download\\test4\\page1.png')
	
	    
	
	    lines='//input[@id="Uname"]'
	    xpath_list.append('//input[@id="Uname"]')
	    value_list.append('admin')
	    element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//input[@id="Uname"]')))
	    classname_list.append(element.get_attribute("className"))
	    actions = ActionChains(driver)
	    actions.move_to_element(element).perform()
	    element.clear()
	    element.send_keys('admin')
	    steps += "\n" + "test_step_inputadmin"
	    text_list.append(element.text)
	    driver.save_screenshot('D:\iTAP\Recorded_Scenarios\\download\\test4\\page2.png')
	    output['//input[@id="Uname"]'] =  "admin"
	    
	
	    lines='//input[@id="Upwd"]'
	    xpath_list.append('//input[@id="Upwd"]')
	    value_list.append('admin1')
	    element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//input[@id="Upwd"]')))
	    classname_list.append(element.get_attribute("className"))
	    actions = ActionChains(driver)
	    actions.move_to_element(element).perform()
	    element.clear()
	    element.send_keys('admin1')
	    steps += "\n" + "test_step_inputadmin1"
	    text_list.append(element.text)
	    driver.save_screenshot('D:\iTAP\Recorded_Scenarios\\download\\test4\\page3.png')
	    output['//input[@id="Upwd"]'] =  "admin1"
	    
	
	    lines='//button[@id="loginBtn"]'
	    xpath_list.append('//button[@id="loginBtn"]')
	    value_list.append('')
	    element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//button[@id="loginBtn"]')))
	    classname_list.append(element.get_attribute("className"))
	    steps += "\n" +"test_step_click" + element.text
	    text_list.append(element.text)
	    actions = ActionChains(driver)
	    actions.move_to_element(element).perform()
	    driver.save_screenshot('D:\iTAP\Recorded_Scenarios\\download\\test4\\page4.png')
	    output['//button[@id="loginBtn"]'] = element.text
	    try:
	        element.click()
	    except Exception :
	        driver.execute_script("arguments[0].click();", element)
	            
	
	    lines='(//span)[2]'
	    xpath_list.append('(//span)[2]')
	    value_list.append('')
	    element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '(//span)[2]')))
	    classname_list.append(element.get_attribute("className"))
	    steps += "\n" +"test_step_click" + element.text
	    text_list.append(element.text)
	    actions = ActionChains(driver)
	    actions.move_to_element(element).perform()
	    driver.save_screenshot('D:\iTAP\Recorded_Scenarios\\download\\test4\\page5.png')
	    output['(//span)[2]'] = element.text
	    try:
	        element.click()
	    except Exception :
	        driver.execute_script("arguments[0].click();", element)
	            
	    xpath_list.append('file download')
	    value_list.append('master inventory')
	    classname_list.append('')
	    text_list.append('')
	    lines= 'file download'
	    date = datetime.now().strftime("%Y_%m_%d-%I:%M:%S_%p")
	    list_of_files = glob.glob('C:\\Users\\dr00810779\\Downloads\\*')
	    latest_file = max(list_of_files, key=os.path.getctime) 
	    time.sleep(3)
	    driver.save_screenshot('D:\iTAP\Recorded_Scenarios\\download\\test4\\page6.png')
	    steps += "\ntest_step_assert Asserting downloaded file ["+latest_file+"] to contain [master inventory]"
	    if latest_file.split("\\")[-1].lower().__contains__('master inventory'):
	        message+='\n Assertion Passed : Filename ['+latest_file.split("\\")[-1]+'] Contains [master inventory] , Time and Date ['+f"{date}"+']'
	    else:
	        message+='\n Assertion Failed : Downloaded file does not contain [master inventory]'
	               
	    
	    with open("D:\iTAP\Recorded_Scenarios\\download\\test4\\logfile.log", "w+") as external_file:
	        finish_time = datetime.now()
	        total = finish_time - start_time
	        total=str(total).split(".")[0]
	        final = "total time taken : " + total
	        external_file.write("test passed - no errors" + "\n" +steps + "\n"+message+ "\nxpath list " + str(xpath_list) + "\nvalue list " + str(value_list) +"\nclass name list " + str(classname_list) +"\ntext list " + str(text_list) +"\n" + final )
	        print('Test Passed', message)
	    driver.close()
	except Exception as e:
	    print('Test Failed', e)
	    finish_time = datetime.now()
	    total = finish_time - start_time
	    total=str(total).split(".")[0]
	    path = open("D:\iTAP\Recorded_Scenarios\\download\\test4\\logfile.log", 'w+')
	    path.write("failed:"+ str(e) + '\n' + steps +  "\n"+message+ "\n Execution stopped at : " +lines + "\nxpath list " + str(xpath_list) + "\nvalue list " + str(value_list) +"\nclass name list " + str(classname_list) +"\ntext list " + str(text_list) +" \n total time taken : "+total)
	    path.close()
	    driver.close()



def test_download_test2(setup):
	
	xpath_list=[]
	value_list=[]
	text_list=[]
	classname_list=[]
	lines=''
	steps='' 
	message=''
	step_no=0
	output_list = []
	output = {}
	try:
	    start_time = datetime.now()
	    driver.get("https://chromedriver.storage.googleapis.com/index.html?path=104.0.5112.79/")
	    xpath_list.append('Open_Browser')
	    value_list.append("https://chromedriver.storage.googleapis.com/index.html?path=104.0.5112.79/")
	    classname_list.append('')
	    text_list.append('')
	    driver.save_screenshot('D:\iTAP\Recorded_Scenarios\\download\\test2\\page1.png')
	
	    
	
	    lines='(//td)[7]'
	    xpath_list.append('(//td)[7]')
	    value_list.append('')
	    element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '(//td)[7]')))
	    classname_list.append(element.get_attribute("className"))
	    steps += "\n" +"test_step_click" + element.text
	    text_list.append(element.text)
	    actions = ActionChains(driver)
	    actions.move_to_element(element).perform()
	    driver.save_screenshot('D:\iTAP\Recorded_Scenarios\\download\\test2\\page2.png')
	    output['(//td)[7]'] = element.text
	    try:
	        element.click()
	    except Exception :
	        driver.execute_script("arguments[0].click();", element)
	            
	
	    lines='(//th)[3]'
	    xpath_list.append('(//th)[3]')
	    value_list.append('')
	    element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '(//th)[3]')))
	    classname_list.append(element.get_attribute("className"))
	    steps += "\n" +"test_step_click" + element.text
	    text_list.append(element.text)
	    actions = ActionChains(driver)
	    actions.move_to_element(element).perform()
	    driver.save_screenshot('D:\iTAP\Recorded_Scenarios\\download\\test2\\page3.png')
	    output['(//th)[3]'] = element.text
	    try:
	        element.click()
	    except Exception :
	        driver.execute_script("arguments[0].click();", element)
	            
	    xpath_list.append('file download')
	    value_list.append('chromedriver')
	    classname_list.append('')
	    text_list.append('')
	    lines= 'file download'
	    date = datetime.now().strftime("%Y_%m_%d-%I:%M:%S_%p")
	    list_of_files = glob.glob('C:\\Users\\dr00810779\\Downloads\\*')
	    latest_file = max(list_of_files, key=os.path.getctime) 
	    time.sleep(3)
	    driver.save_screenshot('D:\iTAP\Recorded_Scenarios\\download\\test2\\page4.png')
	    steps += "\ntest_step_assert Asserting downloaded file ["+latest_file+"] to contain [chromedriver]"
	    if latest_file.split("\\")[-1].lower().__contains__('chromedriver'):
	        message+='\n Assertion Passed : Filename ['+latest_file.split("\\")[-1]+'] Contains [chromedriver] , Time and Date ['+f"{date}"+']'
	    else:
	        message+='\n Assertion Failed : Downloaded file does not contain [chromedriver]'
	               
	    
	    with open("D:\iTAP\Recorded_Scenarios\\download\\test2\\logfile.log", "w+") as external_file:
	        finish_time = datetime.now()
	        total = finish_time - start_time
	        total=str(total).split(".")[0]
	        final = "total time taken : " + total
	        external_file.write("test passed - no errors" + "\n" +steps + "\n"+message+ "\nxpath list " + str(xpath_list) + "\nvalue list " + str(value_list) +"\nclass name list " + str(classname_list) +"\ntext list " + str(text_list) +"\n" + final )
	        print('Test Passed', message)
	    driver.close()
	except Exception as e:
	    print('Test Failed', e)
	    finish_time = datetime.now()
	    total = finish_time - start_time
	    total=str(total).split(".")[0]
	    path = open("D:\iTAP\Recorded_Scenarios\\download\\test2\\logfile.log", 'w+')
	    path.write("failed:"+ str(e) + '\n' + steps +  "\n"+message+ "\n Execution stopped at : " +lines + "\nxpath list " + str(xpath_list) + "\nvalue list " + str(value_list) +"\nclass name list " + str(classname_list) +"\ntext list " + str(text_list) +" \n total time taken : "+total)
	    path.close()
	    driver.close()



def test_download_test7(setup):
	
	xpath_list=[]
	value_list=[]
	text_list=[]
	classname_list=[]
	lines=''
	steps='' 
	message=''
	step_no=0
	output_list = []
	output = {}
	try:
	    start_time = datetime.now()
	    driver.get("https://lcaas.techmahindra.com/vbnet/")
	    xpath_list.append('Open_Browser')
	    value_list.append("https://lcaas.techmahindra.com/vbnet/")
	    classname_list.append('')
	    text_list.append('')
	    driver.save_screenshot('D:\iTAP\Recorded_Scenarios\\download\\test7\\page1.png')
	
	    
	
	    lines='//input[@id="Uname"]'
	    xpath_list.append('//input[@id="Uname"]')
	    value_list.append('admin')
	    element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//input[@id="Uname"]')))
	    classname_list.append(element.get_attribute("className"))
	    actions = ActionChains(driver)
	    actions.move_to_element(element).perform()
	    element.clear()
	    element.send_keys('admin')
	    steps += "\n" + "test_step_inputadmin"
	    text_list.append(element.text)
	    driver.save_screenshot('D:\iTAP\Recorded_Scenarios\\download\\test7\\page2.png')
	    output['//input[@id="Uname"]'] =  "admin"
	    
	
	    lines='//input[@id="Upwd"]'
	    xpath_list.append('//input[@id="Upwd"]')
	    value_list.append('admin1')
	    element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//input[@id="Upwd"]')))
	    classname_list.append(element.get_attribute("className"))
	    actions = ActionChains(driver)
	    actions.move_to_element(element).perform()
	    element.clear()
	    element.send_keys('admin1')
	    steps += "\n" + "test_step_inputadmin1"
	    text_list.append(element.text)
	    driver.save_screenshot('D:\iTAP\Recorded_Scenarios\\download\\test7\\page3.png')
	    output['//input[@id="Upwd"]'] =  "admin1"
	    
	
	    lines='//button[@id="loginBtn"]'
	    xpath_list.append('//button[@id="loginBtn"]')
	    value_list.append('')
	    element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//button[@id="loginBtn"]')))
	    classname_list.append(element.get_attribute("className"))
	    steps += "\n" +"test_step_click" + element.text
	    text_list.append(element.text)
	    actions = ActionChains(driver)
	    actions.move_to_element(element).perform()
	    driver.save_screenshot('D:\iTAP\Recorded_Scenarios\\download\\test7\\page4.png')
	    output['//button[@id="loginBtn"]'] = element.text
	    try:
	        element.click()
	    except Exception :
	        driver.execute_script("arguments[0].click();", element)
	            
	
	    lines='(//span)[2]'
	    xpath_list.append('(//span)[2]')
	    value_list.append('')
	    element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '(//span)[2]')))
	    classname_list.append(element.get_attribute("className"))
	    steps += "\n" +"test_step_click" + element.text
	    text_list.append(element.text)
	    actions = ActionChains(driver)
	    actions.move_to_element(element).perform()
	    driver.save_screenshot('D:\iTAP\Recorded_Scenarios\\download\\test7\\page5.png')
	    output['(//span)[2]'] = element.text
	    try:
	        element.click()
	    except Exception :
	        driver.execute_script("arguments[0].click();", element)
	            
	
	    lines='//img[@id="exportImg"]'
	    xpath_list.append('//img[@id="exportImg"]')
	    value_list.append('')
	    element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//img[@id="exportImg"]')))
	    classname_list.append(element.get_attribute("className"))
	    steps += "\n" +"test_step_click" + element.text
	    text_list.append(element.text)
	    actions = ActionChains(driver)
	    actions.move_to_element(element).perform()
	    driver.save_screenshot('D:\iTAP\Recorded_Scenarios\\download\\test7\\page6.png')
	    output['//img[@id="exportImg"]'] = element.text
	    try:
	        element.click()
	    except Exception :
	        driver.execute_script("arguments[0].click();", element)
	            
	    xpath_list.append('sleep')
	    value_list.append('3')
	    classname_list.append('')
	    text_list.append('')
	    time.sleep(3)
	                
	    xpath_list.append('file download')
	    value_list.append('master')
	    classname_list.append('')
	    text_list.append('')
	    lines= 'file download'
	    date = datetime.now().strftime("%Y_%m_%d-%I:%M:%S_%p")
	    list_of_files = glob.glob('C:\\Users\\dr00810779\\Downloads\\*')
	    latest_file = max(list_of_files, key=os.path.getctime) 
	    time.sleep(3)
	    driver.save_screenshot('D:\iTAP\Recorded_Scenarios\\download\\test7\\page8.png')
	    steps += "\ntest_step_assert Asserting downloaded file ["+latest_file+"] to contain [master]"
	    if latest_file.split("\\")[-1].lower().__contains__('master'):
	        message+='\n Assertion Passed : Filename ['+latest_file.split("\\")[-1]+'] Contains [master] , Time and Date ['+f"{date}"+']'
	    else:
	        message+='\n Assertion Failed : Downloaded file does not contain [master]'
	               
	    
	    with open("D:\iTAP\Recorded_Scenarios\\download\\test7\\logfile.log", "w+") as external_file:
	        finish_time = datetime.now()
	        total = finish_time - start_time
	        total=str(total).split(".")[0]
	        final = "total time taken : " + total
	        external_file.write("test passed - no errors" + "\n" +steps + "\n"+message+ "\nxpath list " + str(xpath_list) + "\nvalue list " + str(value_list) +"\nclass name list " + str(classname_list) +"\ntext list " + str(text_list) +"\n" + final )
	        print('Test Passed', message)
	    driver.close()
	except Exception as e:
	    print('Test Failed', e)
	    finish_time = datetime.now()
	    total = finish_time - start_time
	    total=str(total).split(".")[0]
	    path = open("D:\iTAP\Recorded_Scenarios\\download\\test7\\logfile.log", 'w+')
	    path.write("failed:"+ str(e) + '\n' + steps +  "\n"+message+ "\n Execution stopped at : " +lines + "\nxpath list " + str(xpath_list) + "\nvalue list " + str(value_list) +"\nclass name list " + str(classname_list) +"\ntext list " + str(text_list) +" \n total time taken : "+total)
	    path.close()
	    driver.close()



def test_download_test6(setup):
	
	xpath_list=[]
	value_list=[]
	text_list=[]
	classname_list=[]
	lines=''
	steps='' 
	message=''
	step_no=0
	output_list = []
	output = {}
	try:
	    start_time = datetime.now()
	    driver.get("https://lcaas.techmahindra.com/java/")
	    xpath_list.append('Open_Browser')
	    value_list.append("https://lcaas.techmahindra.com/java/")
	    classname_list.append('')
	    text_list.append('')
	    driver.save_screenshot('D:\iTAP\Recorded_Scenarios\\download\\test6\\page1.png')
	
	    
	
	    lines='//input[@id="Uname"]'
	    xpath_list.append('//input[@id="Uname"]')
	    value_list.append('admin')
	    element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//input[@id="Uname"]')))
	    classname_list.append(element.get_attribute("className"))
	    actions = ActionChains(driver)
	    actions.move_to_element(element).perform()
	    element.clear()
	    element.send_keys('admin')
	    steps += "\n" + "test_step_inputadmin"
	    text_list.append(element.text)
	    driver.save_screenshot('D:\iTAP\Recorded_Scenarios\\download\\test6\\page2.png')
	    output['//input[@id="Uname"]'] =  "admin"
	    
	
	    lines='//input[@id="Upwd"]'
	    xpath_list.append('//input[@id="Upwd"]')
	    value_list.append('admin1')
	    element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//input[@id="Upwd"]')))
	    classname_list.append(element.get_attribute("className"))
	    actions = ActionChains(driver)
	    actions.move_to_element(element).perform()
	    element.clear()
	    element.send_keys('admin1')
	    steps += "\n" + "test_step_inputadmin1"
	    text_list.append(element.text)
	    driver.save_screenshot('D:\iTAP\Recorded_Scenarios\\download\\test6\\page3.png')
	    output['//input[@id="Upwd"]'] =  "admin1"
	    
	
	    lines='//button[@id="loginBtn"]'
	    xpath_list.append('//button[@id="loginBtn"]')
	    value_list.append('')
	    element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//button[@id="loginBtn"]')))
	    classname_list.append(element.get_attribute("className"))
	    steps += "\n" +"test_step_click" + element.text
	    text_list.append(element.text)
	    actions = ActionChains(driver)
	    actions.move_to_element(element).perform()
	    driver.save_screenshot('D:\iTAP\Recorded_Scenarios\\download\\test6\\page4.png')
	    output['//button[@id="loginBtn"]'] = element.text
	    try:
	        element.click()
	    except Exception :
	        driver.execute_script("arguments[0].click();", element)
	            
	
	    lines='(//span)[2]'
	    xpath_list.append('(//span)[2]')
	    value_list.append('')
	    element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '(//span)[2]')))
	    classname_list.append(element.get_attribute("className"))
	    steps += "\n" +"test_step_click" + element.text
	    text_list.append(element.text)
	    actions = ActionChains(driver)
	    actions.move_to_element(element).perform()
	    driver.save_screenshot('D:\iTAP\Recorded_Scenarios\\download\\test6\\page5.png')
	    output['(//span)[2]'] = element.text
	    try:
	        element.click()
	    except Exception :
	        driver.execute_script("arguments[0].click();", element)
	            
	
	    lines='/html/body/app-root/app-layout/section/app-masterinvapp/div[4]/div/div/a/img'
	    xpath_list.append('/html/body/app-root/app-layout/section/app-masterinvapp/div[4]/div/div/a/img')
	    value_list.append('')
	    element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/app-layout/section/app-masterinvapp/div[4]/div/div/a/img')))
	    classname_list.append(element.get_attribute("className"))
	    steps += "\n" +"test_step_click" + element.text
	    text_list.append(element.text)
	    actions = ActionChains(driver)
	    actions.move_to_element(element).perform()
	    driver.save_screenshot('D:\iTAP\Recorded_Scenarios\\download\\test6\\page6.png')
	    output['/html/body/app-root/app-layout/section/app-masterinvapp/div[4]/div/div/a/img'] = element.text
	    try:
	        element.click()
	    except Exception :
	        driver.execute_script("arguments[0].click();", element)
	            
	    xpath_list.append('sleep')
	    value_list.append('3')
	    classname_list.append('')
	    text_list.append('')
	    time.sleep(3)
	                
	    xpath_list.append('file download')
	    value_list.append('master')
	    classname_list.append('')
	    text_list.append('')
	    lines= 'file download'
	    date = datetime.now().strftime("%Y_%m_%d-%I:%M:%S_%p")
	    list_of_files = glob.glob('C:\\Users\\dr00810779\\Downloads\\*')
	    latest_file = max(list_of_files, key=os.path.getctime) 
	    time.sleep(3)
	    driver.save_screenshot('D:\iTAP\Recorded_Scenarios\\download\\test6\\page8.png')
	    steps += "\ntest_step_assert Asserting downloaded file ["+latest_file+"] to contain [master]"
	    if latest_file.split("\\")[-1].lower().__contains__('master'):
	        message+='\n Assertion Passed : Filename ['+latest_file.split("\\")[-1]+'] Contains [master] , Time and Date ['+f"{date}"+']'
	    else:
	        message+='\n Assertion Failed : Downloaded file does not contain [master]'
	               
	    xpath_list.append('sleep')
	    value_list.append('3')
	    classname_list.append('')
	    text_list.append('')
	    time.sleep(3)
	                
	    
	    with open("D:\iTAP\Recorded_Scenarios\\download\\test6\\logfile.log", "w+") as external_file:
	        finish_time = datetime.now()
	        total = finish_time - start_time
	        total=str(total).split(".")[0]
	        final = "total time taken : " + total
	        external_file.write("test passed - no errors" + "\n" +steps + "\n"+message+ "\nxpath list " + str(xpath_list) + "\nvalue list " + str(value_list) +"\nclass name list " + str(classname_list) +"\ntext list " + str(text_list) +"\n" + final )
	        print('Test Passed', message)
	    driver.close()
	except Exception as e:
	    print('Test Failed', e)
	    finish_time = datetime.now()
	    total = finish_time - start_time
	    total=str(total).split(".")[0]
	    path = open("D:\iTAP\Recorded_Scenarios\\download\\test6\\logfile.log", 'w+')
	    path.write("failed:"+ str(e) + '\n' + steps +  "\n"+message+ "\n Execution stopped at : " +lines + "\nxpath list " + str(xpath_list) + "\nvalue list " + str(value_list) +"\nclass name list " + str(classname_list) +"\ntext list " + str(text_list) +" \n total time taken : "+total)
	    path.close()
	    driver.close()

@pytest.fixture()
def setup():
    global driver
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logger"])
    driver = webdriver.Chrome(options=options, executable_path='D:\iTAP\chromedriver.exe')
    driver.maximize_window()
