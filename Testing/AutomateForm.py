from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

serv_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj,options=chrome_options)

driver.get("https://itera-qa.azurewebsites.net/home/automation")
driver.maximize_window()

# Form Filling
driver.find_element(By.XPATH,"//input[@id='name']").send_keys("Abcd")

#find element with css selector tag and attribute
driver.find_element(By.CSS_SELECTOR,"input[aria-describedby=phone]").send_keys("8172566662")

#find element with css selector tag and id
driver.find_element(By.CSS_SELECTOR,"input#email").send_keys("abcd@1234.gmail.com")

#XPATH with OR
driver.find_element(By.XPATH,"//input[@id='password' or @placeholder = 'Password']").send_keys("abcd")
# XPATH WITH AND
# driver.find_element(By.XPATH,"//input[@id='password' and @placeholder = 'Password']").send_keys("abcd")

#Xpath with contains
# driver.find_element(By.XPATH,"//*[contains(@id,'add')]").send_keys("Bengaluru")

#starts-with
driver.find_element(By.XPATH,"//*[starts-with(@id,'add')]").send_keys("Bengaluru")

# using absolute XPATH
driver.find_element(By.XPATH,"/html/body/div/div[2]/div[2]/button").click()

#Radio buttons
driver.find_element(By.XPATH,"//input[@id='female']").click()

#Check box
#Selecting single checkbx
# driver.find_element(By.XPATH,"//label[normalize-space()='Monday']").click()

#MUltiple Checkbox
# checkboxes1 = driver.find_elements(By.XPATH,"//div[contains(@class,'form-check')]//input[@type = 'checkbox']")
checkboxes = driver.find_elements(By.XPATH,"//input[@type = 'checkbox' and contains(@id,'day')]")
for i in range(len(checkboxes)):
    checkboxes[i].click()

#Approach2
# for chekbox in checkboxes:
#     chekbox.click()

#DROPDOWN
drpcountry_ele = driver.find_element(By.XPATH,"//select[@class='custom-select']")
drpcuntry = Select(drpcountry_ele)

drpcuntry.select_by_visible_text("Norway")

rdio_buttons = driver.find_elements(By.XPATH,"//div[contains(@class,'custom-radio')]//label[@class='custom-control-label']")
for radio in rdio_buttons:
    year = radio.get_attribute('for')
    if year == '1year':
        radio.click()
# print(len(rdio_buttons))

new_chkbox = driver.find_elements(By.XPATH,"//div[contains(@class,'custom-checkbox')]//label[@class='custom-control-label' ]")
for newck in new_chkbox:
    tools = newck.get_attribute("for")
    if tools == "selenium" or tools == 'cucumber':
        newck.click()

#Uploading the file
s = driver.find_element(By.XPATH,"//input[@id='inputGroupFile02']")
s.send_keys("C:/Users/Suraj/Desktop/Sample WebsiteForPractice.txt")
