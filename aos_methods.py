from selenium import webdriver
import aos_locators as locators
from time import sleep
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import WebDriverException

import datetime

from selenium.webdriver.common.by import By

# from selenium.webdriver.chrome.options import Options


from faker import Faker

fake = Faker(locale='en_CA')

# options = Options()
# options.add_argument("--headless")
# options.add_argument("window-size=1400,1500")
# options.add_argument("--disable-gpu")
# options.add_argument("--no-sandbox")
# options.add_argument("start-maximized")
# options.add_argument("enable-automation")
# options.add_argument("--disable-infobars")
# options.add_argument("--disable-dev-shm-usage")

# driver = webdriver.Chrome(options=options)

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
    sleep(3)


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

    sleep(0.50)
    driver.find_element(By.ID, 'register_btnundefined').click()
    print("Successfully created a user")


# logout
def logout():
    sleep(0.50)
    driver.find_element(By.XPATH, '/html[1]/body[1]/header[1]/nav[1]/ul[1]/li[3]/a[1]/span[1]').click()
    driver.find_element(By.XPATH, '//div[ @ id = "loginMiniTitle"] / label[3]').click()
    name = driver.find_element(By.XPATH, '/html[1]/body[1]/header[1]/nav[1]/ul[1]/li[3]/a[1]/span[1]').text
    print(f'{name} logged out')
    # driver.find_element(By.XPATH,'//a[@id="menuUserLink"]/div[@]class=""mini-title]/label[contains
    # (.,"Sign out")]').click() #Tinu's code
    sleep(0.30)


# Login
def login():
    sleep(0.25)
    driver.find_element(By.XPATH, '//*[@id="hrefUserIcon"]').click()
    driver.find_element(By.NAME, 'username').send_keys(locators.user_name)
    driver.find_element(By.NAME, 'password').send_keys(locators.password)
    sleep(0.30)
    driver.find_element(By.ID, 'sign_in_btnundefined').click()
    print('Logged in as: ', locators.user_name)
    sleep(0.25)


# define validate text
def validate_text():
    # Check Speaker Text
    sleep(0.30)
    abc = driver.find_element(By.ID, 'speakersTxt').text
    if abc == locators.speaker_text:
        print(f'Value of Speaker text is displayed as : {locators.speaker_text}')
        assert driver.find_element(By.ID, 'speakersTxt').is_displayed()
    else:
        print("Value doesn't match")

    # Check Tablets Text
    abc = driver.find_element(By.ID, 'tabletsTxt').text
    if abc == locators.tablet_text:
        print(f'Value of Tablet text is displayed as : {locators.tablet_text}')
        assert driver.find_element(By.ID, 'tabletsTxt').is_displayed()
    else:
        print("Value doesn't match")

    # Check Laptops Text
    abc = driver.find_element(By.ID, 'laptopsTxt').text
    if abc == locators.laptop_text:
        print(f'Value of Laptop text is displayed as : {locators.laptop_text}')
        assert driver.find_element(By.ID, 'laptopsTxt').is_displayed()
    else:
        print("Value doesn't match")

    # Check Mice Text
    abc = driver.find_element(By.ID, 'miceTxt').text
    if abc == locators.mice_text:
        print(f'Value of Mice text is displayed as : {locators.mice_text}')
        assert driver.find_element(By.ID, 'miceTxt').is_displayed()
    else:
        print("Value doesn't match")

    # Check Headphones Text
    abc = driver.find_element(By.ID, 'headphonesTxt').text
    if abc == locators.headphones_txt:
        print(f'Value of Headphones text is displayed as : {locators.headphones_txt}')
        assert driver.find_element(By.ID, 'headphonesTxt').is_displayed()
    else:
        print("Value doesn't match")


# Click by SPECIAL OFFER, POPULAR ITEMS and CONTACT US links at the top nav menu are clickable.
def validate_top_menu():
    # Click link 1 of top menu
    try:
        driver.find_element(By.XPATH, f'//a[contains(.,"{locators.menu_item1}")]').click()
        print(f'Menu item {locators.menu_item1} is clickable')
    except WebDriverException:
        print(f'{locators.menu_item1} is not clickable')

    # Click link 2 of top menu
    try:
        driver.find_element(By.XPATH, f'//a[contains(.,"{locators.menu_item2}")]').click()
        print(f'Menu item {locators.menu_item2} is clickable')
    except WebDriverException:
        print(f'{locators.menu_item2} is not clickable')

    # Click link 3 of top menu
    try:
        driver.find_element(By.XPATH, f'//a[contains(.,"{locators.menu_item3}")]').click()
        print(f'Menu item {locators.menu_item3} is clickable')
    except WebDriverException:
        print(f'{locators.menu_item3} is not clickable')

    # Click link 4 of top menu
    try:
        driver.find_element(By.XPATH, f'//a[contains(.,"{locators.menu_item4}")]').click()
        print(f'Menu item {locators.menu_item4} is clickable')
    except WebDriverException:
        print(f'{locators.menu_item4} is not clickable')


# verify logo display
def verify_logo_display():
    assert driver.find_element(By.XPATH, '//span[contains(.,"dvantage")]').is_displayed()
    # if driver.find_element(By.XPATH, '//span[contains(.,"dvantage")]').is_displayed() == True:
    if driver.find_element(By.XPATH, '//span[contains(.,"dvantage")]').is_displayed():
        print("Logo is displayed")
    else:
        print('Logo is not displayed')

    sleep(0.25)


# Contact us
def validate_contact_us():
    sleep(0.25)
    print('Inside contact us method')
    sleep(2)
    # driver.find_element(By.NAME, 'go_up_btn').click()
    driver.find_element(By.XPATH, '//label[@translate="CHAT_WITH_US"]').click()
    print(driver.current_window_handle)
    handles = driver.window_handles  # all windows handles
    for handle in handles:
        driver.switch_to.window(handle)
        if driver.title == locators.chatbox_title:
            print(f'Inside window: {driver.title}')
            driver.close()
        elif driver.title == 'Advantage Shopping':
            locators.curr_handle = handle
    driver.switch_to.window(locators.curr_handle)
    try:
        Select(driver.find_element(By.NAME, 'categoryListboxContactUs')).select_by_visible_text('Mice')
    except:
        print('No such element found')
    # sleep(0.25)
    try:
        Select(driver.find_element(By.NAME, 'productListboxContactUs')).select_by_visible_text('Microsoft Sculpt Touch Mouse')
    except:
        print('No such element')
    # sleep(0.25)
    driver.find_element(By.NAME, 'emailContactUs').send_keys(locators.email)
    sleep(0.25)
    driver.find_element(By.NAME, 'subjectTextareaContactUs').send_keys(locators.subject_box)
    sleep(0.50)
    driver.find_element(By.ID, 'send_btnundefined').click()
    print('Successfully sent the message by clicking the send button')

# validate social media links
def validate_social_media():
    # assert driver.find_element(By.NAME, 'follow_facebook').is_displayed()
    locators.curr_handle = driver.current_window_handle
    print(f'\n Inside validate social media method. Current_handle: {locators.curr_handle}')
    sleep(0.25)
    #driver.find_element(By.NAME, 'go_up_btn').click()
    driver.find_element(By.NAME, 'follow_facebook').click()
    sleep(0.25)
    driver.find_element(By.NAME, 'follow_twitter').click()
    sleep(0.25)
    driver.find_element(By.NAME, 'follow_linkedin').click()
    sleep(0.25)
    handles = driver.window_handles  # all windows handles
    for handle in handles:
        driver.switch_to.window(handle)
        if driver.current_url.__contains__('facebook'):
            print(f'Successfully clicked Facebook page on a new tab with title : {driver.title}')
            driver.close()
        elif driver.current_url.__contains__('twitter'):
            print(f'Successfully clicked Twitter page on a new tab with title : {driver.title}')
            driver.close()
        elif driver.current_url.__contains__('linkedin'):
            print(f'Successfully clicked LindedIn page on a new tab with title : {driver.title}')
            driver.close()
    driver.switch_to.window(locators.curr_handle)

# Call methods from here
setUp()
create_new_user()
validate_text()
validate_top_menu()
verify_logo_display()
validate_contact_us()
validate_social_media()
logout()
login()
logout()
teardown()
