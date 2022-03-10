from selenium import webdriver
import aos_locators as locators
from time import sleep
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import datetime
import sys
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.options import Options

# from selenium.webdriver.common.keys import Keys
from faker import Faker

fake = Faker(locale='en_CA')

s = Service(executable_path='C:\\Tools\\chromedriver.exe')
driver = webdriver.Chrome(service=s)

# setup
def setUp():
    print(f'Launch {locators.app} App')
    print('--------------------~*~--------------------')
    # Make browser full screen
    driver.maximize_window()
    # Give browser up to 30 seconds to respond
    driver.implicitly_wait(30)
    # Navigate to Moodle app website
    driver.get(locators.url)
    # Check that Moodle URL and the home page title are displayed
    if driver.current_url == locators.url and driver.title == locators.title:
        print(f'Yey! {locators.app} Launched Successfully')
        print(f'{locators.app} homepage URL: {driver.current_url}\nHome Page Title: {driver.title}')
        sleep(0.25)
    else:
        print(f'{locators.app}  did not launch. Check your code or application!')
        print(f'Current URL: {driver.current_url}, Page Title: {driver.title}')
    sleep(2)

# teardown
def teardown():
    if driver is not None:
        print('-------------------------------')
        print(f'The test is completed at: {datetime.datetime.now()}')
        driver.close()
        driver.quit()


# Create new users
def create_new_user():
    sleep(0.25)
    driver.find_element(By.XPATH, '//*[@id="hrefUserIcon"]').click()
    print('Successfully clicked user icon')
    sleep(3)
    driver.find_element(By.LINK_TEXT, 'CREATE NEW ACCOUNT').click()
    sleep(0.20)

    for i in range(len(locators.list_ids)):
        ids, val = locators.list_ids[i], locators.list_val[i]
        driver.find_element(By.NAME, ids).send_keys(val)
        sleep(0.25)

    # Country DDB
    try:
        sleep(1)
        if driver.find_element(By.NAME, 'countryListboxRegisterPage').is_displayed():
            Select(driver.find_element(By.NAME, 'countryListboxRegisterPage')).select_by_visible_text("Canada")
            sleep(0.20)
    except NoSuchElementException:
        print(f'Couldn\'t locate web-element country')
        pass

    # I agree checkbox
    try:
        sleep(1)
        if driver.find_element(By.NAME, 'i_agree').is_displayed():
            driver.find_element(By.NAME, 'i_agree').click()
            sleep(0.20)
    except NoSuchElementException:
        print(f'Couldn\'t locate {driver.find_element(By.NAME, "i_agree")}')
        pass

    driver.find_element(By.ID, 'register_btnundefined').click()
    print("Successfully created a user")


#logout
def logout():
    sleep(0.50)
    driver.find_element(By.XPATH, '/html[1]/body[1]/header[1]/nav[1]/ul[1]/li[3]/a[1]/span[1]').click()
    driver.find_element(By.XPATH, '//div[ @ id = "loginMiniTitle"] / label[3]').click()
    name = driver.find_element(By.XPATH, '/html[1]/body[1]/header[1]/nav[1]/ul[1]/li[3]/a[1]/span[1]').text
    print(f'{name} logged out')
    #driver.find_element(By.XPATH,'//a[@id="menuUserLink"]/div[@]class=""mini-title]/label[contains(.,"Sign out")]').click() #Tinu's code
    sleep(0.25)


# Login
def login():
    sleep(0.25)
    driver.find_element(By.XPATH, '//*[@id="hrefUserIcon"]').click()
    driver.find_element(By.NAME, 'username').send_keys(locators.user_name)
    driver.find_element(By.NAME, 'password').send_keys(locators.password)
    driver.find_element(By.ID, 'sign_in_btnundefined').click()
    print('Logged in as: ', locators.user_name)
    sleep(0.25)

# Call methods from here
# setUp()
# sleep(1)
# create_new_user()
# logout()
# sleep(0.25)
# login()
# logout()
# teardown()

