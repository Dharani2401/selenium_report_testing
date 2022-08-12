import pytest
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


def test_test_demo1(setup):	
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
	    driver.save_screenshot('D:\iTAP\Recorded_Scenarios\\test\\demo1\\page1.png')
	
	    
	
	    lines='//input[@name="user-name"]'
	    element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//input[@name="user-name"]')))
	    actions = ActionChains(driver)
	    actions.move_to_element(element).perform()
	    element.clear()
	    element.send_keys('standard_user')
	    steps += "\ntest_step_input " + 'standard_user'
	    xpath_list.append('//input[@name="user-name"]')
	    value_list.append('standard_user')
	    classname_list.append(element.get_attribute("className"))
	    text_list.append(element.text)
	    driver.save_screenshot('D:\iTAP\Recorded_Scenarios\\test\\demo1\\page2.png')
	    output['//input[@name="user-name"]'] =  "standard_user"
	    
	
	    lines='//input[@name="password"]'
	    element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//input[@name="password"]')))
	    actions = ActionChains(driver)
	    actions.move_to_element(element).perform()
	    element.clear()
	    element.send_keys('secret_sauce')
	    steps += "\ntest_step_input " + 'secret_sauce'
	    xpath_list.append('//input[@name="password"]')
	    value_list.append('secret_sauce')
	    classname_list.append(element.get_attribute("className"))
	    text_list.append(element.text)
	    driver.save_screenshot('D:\iTAP\Recorded_Scenarios\\test\\demo1\\page3.png')
	    output['//input[@name="password"]'] =  "secret_sauce"
	    
	
	    lines='//input[@name="login-button"]'
	    element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//input[@name="login-button"]')))
	    if element.text == '':
	        steps += "\ntest_step_click " + '//input[@name="login-button"]'
	    else:        
	        steps += "\ntest_step_click " + element.text
	    xpath_list.append('//input[@name="login-button"]')
	    value_list.append('')
	    classname_list.append(element.get_attribute("className"))
	    text_list.append(element.text)
	    actions = ActionChains(driver)
	    actions.move_to_element(element).perform()
	    driver.save_screenshot('D:\iTAP\Recorded_Scenarios\\test\\demo1\\page4.png')
	    output['//input[@name="login-button"]'] = element.text
	    try:
	        element.click()
	    except Exception :
	        driver.execute_script("arguments[0].click();", element)
	            
	
	    lines='//button[@name="add-to-cart-sauce-labs-backpack"]'
	    element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//button[@name="add-to-cart-sauce-labs-backpack"]')))
	    if element.text == '':
	        steps += "\ntest_step_click " + '//button[@name="add-to-cart-sauce-labs-backpack"]'
	    else:        
	        steps += "\ntest_step_click " + element.text
	    xpath_list.append('//button[@name="add-to-cart-sauce-labs-backpack"]')
	    value_list.append('')
	    classname_list.append(element.get_attribute("className"))
	    text_list.append(element.text)
	    actions = ActionChains(driver)
	    actions.move_to_element(element).perform()
	    driver.save_screenshot('D:\iTAP\Recorded_Scenarios\\test\\demo1\\page5.png')
	    output['//button[@name="add-to-cart-sauce-labs-backpack"]'] = element.text
	    try:
	        element.click()
	    except Exception :
	        driver.execute_script("arguments[0].click();", element)
	            
	
	    lines='//button[@name="add-to-cart-sauce-labs-bike-light"]'
	    element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//button[@name="add-to-cart-sauce-labs-bike-light"]')))
	    if element.text == '':
	        steps += "\ntest_step_click " + '//button[@name="add-to-cart-sauce-labs-bike-light"]'
	    else:        
	        steps += "\ntest_step_click " + element.text
	    xpath_list.append('//button[@name="add-to-cart-sauce-labs-bike-light"]')
	    value_list.append('')
	    classname_list.append(element.get_attribute("className"))
	    text_list.append(element.text)
	    actions = ActionChains(driver)
	    actions.move_to_element(element).perform()
	    driver.save_screenshot('D:\iTAP\Recorded_Scenarios\\test\\demo1\\page6.png')
	    output['//button[@name="add-to-cart-sauce-labs-bike-light"]'] = element.text
	    try:
	        element.click()
	    except Exception :
	        driver.execute_script("arguments[0].click();", element)
	            
	
	    lines='//button[@name="add-to-cart-sauce-labs-bolt-t-shirt"]'
	    element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//button[@name="add-to-cart-sauce-labs-bolt-t-shirt"]')))
	    if element.text == '':
	        steps += "\ntest_step_click " + '//button[@name="add-to-cart-sauce-labs-bolt-t-shirt"]'
	    else:        
	        steps += "\ntest_step_click " + element.text
	    xpath_list.append('//button[@name="add-to-cart-sauce-labs-bolt-t-shirt"]')
	    value_list.append('')
	    classname_list.append(element.get_attribute("className"))
	    text_list.append(element.text)
	    actions = ActionChains(driver)
	    actions.move_to_element(element).perform()
	    driver.save_screenshot('D:\iTAP\Recorded_Scenarios\\test\\demo1\\page7.png')
	    output['//button[@name="add-to-cart-sauce-labs-bolt-t-shirt"]'] = element.text
	    try:
	        element.click()
	    except Exception :
	        driver.execute_script("arguments[0].click();", element)
	            
	
	    lines='//button[@id="react-burger-menu-btn"]'
	    element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//button[@id="react-burger-menu-btn"]')))
	    if element.text == '':
	        steps += "\ntest_step_click " + '//button[@id="react-burger-menu-btn"]'
	    else:        
	        steps += "\ntest_step_click " + element.text
	    xpath_list.append('//button[@id="react-burger-menu-btn"]')
	    value_list.append('')
	    classname_list.append(element.get_attribute("className"))
	    text_list.append(element.text)
	    actions = ActionChains(driver)
	    actions.move_to_element(element).perform()
	    driver.save_screenshot('D:\iTAP\Recorded_Scenarios\\test\\demo1\\page8.png')
	    output['//button[@id="react-burger-menu-btn"]'] = element.text
	    try:
	        element.click()
	    except Exception :
	        driver.execute_script("arguments[0].click();", element)
	            
	
	    lines='//a[@id="about_sidebar_link"]'
	    element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//a[@id="about_sidebar_link"]')))
	    if element.text == '':
	        steps += "\ntest_step_click " + '//a[@id="about_sidebar_link"]'
	    else:        
	        steps += "\ntest_step_click " + element.text
	    xpath_list.append('//a[@id="about_sidebar_link"]')
	    value_list.append('')
	    classname_list.append(element.get_attribute("className"))
	    text_list.append(element.text)
	    actions = ActionChains(driver)
	    actions.move_to_element(element).perform()
	    driver.save_screenshot('D:\iTAP\Recorded_Scenarios\\test\\demo1\\page9.png')
	    output['//a[@id="about_sidebar_link"]'] = element.text
	    try:
	        element.click()
	    except Exception :
	        driver.execute_script("arguments[0].click();", element)
	            
	    xpath_list.append('page title')
	    value_list.append('')
	    classname_list.append('')
	    text_list.append('')
	    Title_element = driver.title
	    steps="\ntest_step_assert Page title is "+Title_element
	    message+="\n Action Performed : The page title is "+Title_element
	    driver.save_screenshot('D:\iTAP\Recorded_Scenarios\\test\\demo1\\page10.png')
	                
	    
	    with open("D:\iTAP\Recorded_Scenarios\\test\\demo1\\logfile.log", "w+") as external_file:
	        finish_time = datetime.now()
	        total = finish_time - start_time
	        total=str(total).split(".")[0]
	        final = "total time taken : " + total
	        external_file.write("test passed - no errors" + "\n" +steps + "\n"+message+ "\nxpath list " + str(xpath_list) + "\nvalue list " + str(value_list) +"\nclass name list " + str(classname_list) +"\ntext list " + str(text_list) +"\n" + final )
	        print('Test Passed', steps)
	    driver.close()
	except Exception as e:
	    print('Test Failed', e)
	    finish_time = datetime.now()
	    total = finish_time - start_time
	    total=str(total).split(".")[0]
	    path = open("D:\iTAP\Recorded_Scenarios\\test\\demo1\\logfile.log", 'w+')
	    path.write("failed:"+ str(e) + '\n' + steps +  "\n"+message+ "\n Execution stopped at : " +lines + "\nxpath list " + str(xpath_list) + "\nvalue list " + str(value_list) +"\nclass name list " + str(classname_list) +"\ntext list " + str(text_list) +" \n total time taken : "+total)
	    path.close()
	    driver.close()



def test_test_demo2(setup):	
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
	    driver.save_screenshot('D:\iTAP\Recorded_Scenarios\\test\\demo2\\page1.png')
	
	    
	
	    lines='//input[@name="firstname"]'
	    element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//input[@name="firstname"]')))
	    actions = ActionChains(driver)
	    actions.move_to_element(element).perform()
	    element.clear()
	    element.send_keys('sdgds')
	    steps += "\ntest_step_input " + 'sdgds'
	    xpath_list.append('//input[@name="firstname"]')
	    value_list.append('sdgds')
	    classname_list.append(element.get_attribute("className"))
	    text_list.append(element.text)
	    driver.save_screenshot('D:\iTAP\Recorded_Scenarios\\test\\demo2\\page2.png')
	    output['//input[@name="firstname"]'] =  "sdgds"
	    
	
	    lines='//input[@name="email"]'
	    element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//input[@name="email"]')))
	    actions = ActionChains(driver)
	    actions.move_to_element(element).perform()
	    element.clear()
	    element.send_keys('sgds')
	    steps += "\ntest_step_input " + 'sgds'
	    xpath_list.append('//input[@name="email"]')
	    value_list.append('sgds')
	    classname_list.append(element.get_attribute("className"))
	    text_list.append(element.text)
	    driver.save_screenshot('D:\iTAP\Recorded_Scenarios\\test\\demo2\\page3.png')
	    output['//input[@name="email"]'] =  "sgds"
	    
	
	    lines='//input[@name="checkbox2"]'
	    element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//input[@name="checkbox2"]')))
	    if element.text == '':
	        steps += "\ntest_step_click " + '//input[@name="checkbox2"]'
	    else:        
	        steps += "\ntest_step_click " + element.text
	    xpath_list.append('//input[@name="checkbox2"]')
	    value_list.append('')
	    classname_list.append(element.get_attribute("className"))
	    text_list.append(element.text)
	    actions = ActionChains(driver)
	    actions.move_to_element(element).perform()
	    driver.save_screenshot('D:\iTAP\Recorded_Scenarios\\test\\demo2\\page5.png')
	    output['//input[@name="checkbox2"]'] = element.text
	    try:
	        element.click()
	    except Exception :
	        driver.execute_script("arguments[0].click();", element)
	            
	
	    lines='(//input[@name="B"])[2]'
	    element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '(//input[@name="B"])[2]')))
	    if element.text == '':
	        steps += "\ntest_step_click " + '(//input[@name="B"])[2]'
	    else:        
	        steps += "\ntest_step_click " + element.text
	    xpath_list.append('(//input[@name="B"])[2]')
	    value_list.append('')
	    classname_list.append(element.get_attribute("className"))
	    text_list.append(element.text)
	    actions = ActionChains(driver)
	    actions.move_to_element(element).perform()
	    driver.save_screenshot('D:\iTAP\Recorded_Scenarios\\test\\demo2\\page6.png')
	    output['(//input[@name="B"])[2]'] = element.text
	    try:
	        element.click()
	    except Exception :
	        driver.execute_script("arguments[0].click();", element)
	            
	
	    lines='(//input[@name="C"])[3]'
	    element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '(//input[@name="C"])[3]')))
	    if element.text == '':
	        steps += "\ntest_step_click " + '(//input[@name="C"])[3]'
	    else:        
	        steps += "\ntest_step_click " + element.text
	    xpath_list.append('(//input[@name="C"])[3]')
	    value_list.append('')
	    classname_list.append(element.get_attribute("className"))
	    text_list.append(element.text)
	    actions = ActionChains(driver)
	    actions.move_to_element(element).perform()
	    driver.save_screenshot('D:\iTAP\Recorded_Scenarios\\test\\demo2\\page7.png')
	    output['(//input[@name="C"])[3]'] = element.text
	    try:
	        element.click()
	    except Exception :
	        driver.execute_script("arguments[0].click();", element)
	            
	
	    lines='//select[@name="Listbox1"]'
	    element = Select(driver.find_element_by_xpath('//select[@name="Listbox1"]'))
	    element.select_by_value('GTK2 Port')
	    o = element.first_selected_option
	    if o.text == '':
	        steps += "\ntest_step_click " + '//select[@name="Listbox1"]'
	    else:        
	        steps += "\ntest_step_click " + o.text
	    xpath_list.append('//select[@name="Listbox1"]')
	    value_list.append('GTK2 Port')
	    classname_list.append('')
	    text_list.append(o.text)
	    driver.save_screenshot('D:\iTAP\Recorded_Scenarios\\test\\demo2\\page8.png')
	    output['//select[@name="Listbox1"]'] =  "GTK2 Port"
	    
	    
	    with open("D:\iTAP\Recorded_Scenarios\\test\\demo2\\logfile.log", "w+") as external_file:
	        finish_time = datetime.now()
	        total = finish_time - start_time
	        total=str(total).split(".")[0]
	        final = "total time taken : " + total
	        external_file.write("test passed - no errors" + "\n" +steps + "\n"+message+ "\nxpath list " + str(xpath_list) + "\nvalue list " + str(value_list) +"\nclass name list " + str(classname_list) +"\ntext list " + str(text_list) +"\n" + final )
	        print('Test Passed', steps)
	    driver.close()
	except Exception as e:
	    print('Test Failed', e)
	    finish_time = datetime.now()
	    total = finish_time - start_time
	    total=str(total).split(".")[0]
	    path = open("D:\iTAP\Recorded_Scenarios\\test\\demo2\\logfile.log", 'w+')
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
