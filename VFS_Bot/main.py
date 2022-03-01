# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


base_url = "https://row1.vfsglobal.com/GlobalAppointment/Account/RegisteredLogin?q=shSA0YnE4pLF9Xzwon%2Fx%2FEpJs2NIweLgQQ8d%20rbZm2FGx5CHm%2Fl3tpvUMzs2dkBUvzmr37Un%201CH0C4%2F6fHwqQ%3D%3D&fbclid=IwAR22U08SNRmoReYg0_LbFDMTWFWayuuEioDmli0t2UboXkwa3DKUOxzhpjA"
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd
def page_one():
    options = Options()
    options.add_argument("--no-sandbox")
    # options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    driver.get(base_url)
    return driver
def page_two(driver):
    url = "https://row1.vfsglobal.com/GlobalAppointment/Home/Index"
    print(driver.find_element_by_class_name("leftpanel-links").find_elements_by_class_name("inactive-link")[3].text)
    driver.find_element_by_class_name("leftpanel-links").find_elements_by_class_name("inactive-link")[3].click()
    data = pd.read_csv('data.csv')
    ref = driver.find_element_by_id("AURN")
    passport = driver.find_element_by_id("txtPassport")
    email = driver.find_element_by_id("PrimaryEmailId")
    phone = driver.find_element_by_id("txtContactNumber")
    print(data['Passport number'].values[0])
    ref.send_keys(data['Reference number'].values[0])
    passport.send_keys(str(data['Passport number'].values[0]))
    email.send_keys(data['Mail'].values[0])
    phone.send_keys(str(data['phone number'].values[0]))
    driver.find_elements_by_class_name('submitbtn')[1].click()
    time.sleep(3)
    driver.find_element_by_class_name('btn').click()
    time.sleep(3)
    driver.find_element_by_class_name('frm-button').find_element_by_class_name('submitbtn').click()
    time.sleep(3)
    driver.find_element_by_id('btnContinueService').click()
    time.sleep(3)
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Login
    driver = page_one()
    email_field = driver.find_element_by_id("EmailId")
    pass_field = driver.find_element_by_id("Password")
    email_field.send_keys("Jeamscreative@gmailni.com")
    pass_field.send_keys("Jeams@22")
    captcha = driver.find_element_by_id("CaptchaImage")
    print(captcha.get_attribute("src"))
    time.sleep(10)
    driver.find_element_by_class_name("submitbtn").click()
    time.sleep(3)
    page_two(driver)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
