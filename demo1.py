from selenium import webdriver
from selenium.webdriver.support.select import Select
import time

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.implicitly_wait(5)

driver.get("http://automationpractice.com/index.php/")
driver.maximize_window()
driver.find_element_by_xpath("//a[contains(text(),'Sign in')]").click()
driver.find_element_by_name("email_create").send_keys("allanphilip971@gmail.com")
driver.find_element_by_xpath("//button[@id='SubmitCreate']").click()

#YOUR PERSONAL INFORMATION
driver.find_element_by_id("id_gender1").click()
driver.find_element_by_xpath("//input[@id='customer_firstname']").send_keys("ALLAN")
driver.find_element_by_xpath("//input[@id='customer_lastname']").send_keys("PHILIP")
driver.find_element_by_xpath("//input[@id='passwd']").send_keys("123qwert!")
dropdown = Select(driver.find_element_by_id("days"))
dropdown.select_by_value("15")
dropdown = Select(driver.find_element_by_id("months"))
dropdown.select_by_value("3")
dropdown = Select(driver.find_element_by_id("years"))
dropdown.select_by_value("1995")
driver.find_element_by_id("newsletter").click()
driver.find_element_by_id("optin").click()

#YOUR ADDRESS
driver.find_element_by_xpath("//input[@id = 'firstname']").send_keys("ALLAN")
driver.find_element_by_xpath("//input[@id = 'lastname']").send_keys("PHILIP")
driver.find_element_by_xpath("//input[@id = 'company']").send_keys("QUEENS CONSOLIDATES")
driver.find_element_by_css_selector("input[id = 'address1']").send_keys("655 Richmond Ave,Staten Island,NY 10314")
driver.find_element_by_xpath("//input[@id='city']").send_keys("Staten Island")
dropdown = Select(driver.find_element_by_id("id_state"))
dropdown.select_by_value("32")
driver.find_element_by_css_selector("input[id='postcode']").send_keys("10314")
driver.find_element_by_id("other").send_keys("9349386221")
driver.find_element_by_id("phone").send_keys("1234567")
driver.find_element_by_id("phone_mobile").send_keys("9995480020")
driver.find_element_by_id("alias").clear()
driver.find_element_by_id("alias").send_keys("55 Richmond ")
driver.find_element_by_xpath("//*[@id = 'submitAccount']").click()
time.sleep(5)
if(driver.find_element_by_css_selector ("a.account").is_displayed()):
    print("Register successfully")
else:
    print("registration failed")
driver.close()










