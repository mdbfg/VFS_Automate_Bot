# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


base_url = "https://row1.vfsglobal.com/GlobalAppointment/Account/RegisteredLogin?q=shSA0YnE4pLF9Xzwon%2Fx%2FEpJs2NIweLgQQ8d%20rbZm2FGx5CHm%2Fl3tpvUMzs2dkBUvzmr37Un%201CH0C4%2F6fHwqQ%3D%3D&fbclid=IwAR22U08SNRmoReYg0_LbFDMTWFWayuuEioDmli0t2UboXkwa3DKUOxzhpjA"
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import concurrent.futures
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

proxyOne = '43.224.10.26:6666'
proxyTwo = '45.250.226.14:3128'

# webdriver.DesiredCapabilities.CHROME['proxy'] = {
#     "httpProxy": proxyTwo,
#     "ftpProxy": proxyTwo,
#     "sslProxy": proxyTwo,
#
#     "proxyType": "MANUAL",
#
# }
def page_one():
    options = Options()
    options.add_argument("--no-sandbox")
    # options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    driver.get(base_url)
    return driver

def test():
    data = pd.read_csv('data.csv')
    print(len(data))
    print(data.iloc[0,:]['Reference number'])
    for i in range(0,len(data)):
        print(data['Reference number'].values[i])
        print(str(data['Passport number'].values[i]))
        print(data['Mail'].values[i])
        print(str(data['phone number'].values[i]))
        # driver.switch_to.new_window('window')
        print()

def page_two(driver,data):
    password = str(data['longin Password '])
    # str(data['Passport number'].values[1])
    email = data['Mail']
    str(data['phone number'])
    email_field = driver.find_element_by_id("EmailId")
    pass_field = driver.find_element_by_id("Password")
    email_field.send_keys(email)
    pass_field.send_keys(password)
    captcha = driver.find_element_by_id("CaptchaImage")
    print(captcha.get_attribute("src"))
    time.sleep(10)
    driver.find_element_by_class_name("submitbtn").click()
    time.sleep(3)
    # page_two(driver, data.loc[1, :])
    # url = "https://row1.vfsglobal.com/GlobalAppointment/Home/Index"
    print(driver.find_element_by_class_name("leftpanel-links").find_elements_by_class_name("inactive-link")[3].text)
    driver.find_element_by_class_name("leftpanel-links").find_elements_by_class_name("inactive-link")[3].click()
    page_three(driver,data)



def page_three(driver,data):
    ref = driver.find_element_by_id("AURN")
    passport = driver.find_element_by_id("txtPassport")
    email = driver.find_element_by_id("PrimaryEmailId")
    phone = driver.find_element_by_id("txtContactNumber")
    # user data starts
    ref.send_keys(data['Reference number'])
    passport.send_keys(str(data['Passport number']))
    email.send_keys(data['Mail'])
    phone.send_keys(str(data['phone number']))
    driver.find_elements_by_class_name('submitbtn')[1].click()
    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME, "btn"))
        )
        element.click()
        time.sleep(3)
        driver.find_element_by_class_name('frm-button').find_element_by_class_name('submitbtn').click()
        time.sleep(3)
        driver.find_element_by_id('btnContinueService').click()
        time.sleep(3)
        month_year = driver.find_element_by_class_name('fc-header-title').text
        month = month_year.split(' ')[0]
        print(month)

        if month == data['targeted_month']:
            print("select date")
            selectDateAndTimeForAppointment(driver)
        else:
            return
    finally:
        print("Driver Quit")
    # end user data
    # time.sleep(3)
    # driver.find_element_by_class_name('btn').click()
def selectDateAndTimeForAppointment(driver):
    calender = driver.find_element_by_class_name("fc-content")
    weeks = driver.find_elements_by_class_name("fc-future")
    for days in weeks:
        days.click()
        try:
            # select time
            timeRange = driver.find_element_by_id("TimeBandsDiv").find_elements_by_tag_name("tr")
            timeRange[3].find_element_by_name("selectedTimeBand").click()
            # confirm
            driver.find_element_by_id("btnConfirm").click()
            break
        except:
            continue
if __name__ == '__main__':
    # Login
    driver = page_one()
    data = pd.read_csv('data.csv')
    # data['Reference number'].values[1]
    d = []
    for i in range(0,len(data)):
        d.append((driver,data.loc[i,:]))
        page_two(driver,data.loc[i,:])
        driver = page_one()
    # with concurrent.futures.ThreadPoolExecutor(max_workers=len(data)) as executor:
    #     executor.map(lambda p: page_two(*p), d)
    test()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
