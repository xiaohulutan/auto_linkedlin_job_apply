from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.common.exceptions import NoSuchElementException
import time

ACCOUNT = "your linkedin come"
PASSWORD =" your password"

# https://chromedriver.chromium.org/downloads
web_drive_path = "your path for chrome driver"
drive = webdriver.Chrome(executable_path=web_drive_path)

drive.get("paste the linkedin website with your target role in the search bar")
# click login in
login_button = drive.find_element_by_class_name("nav__button-secondary")
login_button.click()

# input account and password
time.sleep(3)
username = drive.find_element_by_id("username")
username.send_keys(ACCOUNT)
password = drive.find_element_by_id("password")
password.send_keys(PASSWORD)

# enter log in
password.send_keys(keys.Keys.ENTER)

# find all the jobs list
time.sleep(4)
easy_apply_list = drive.find_elements_by_css_selector(".job-card-container--clickable")

for each_job in easy_apply_list:
    each_job.click()

    try:
        time.sleep(2)
        easy_apply = drive.find_element_by_class_name("jobs-apply-button")
        easy_apply.click()
        # check this ad if meet conditions
        time.sleep(2)
        check_button = drive.find_element_by_css_selector("footer button")
        if check_button.text == "Next":
            close = drive.find_element_by_class_name("artdeco-modal__dismiss")
            close.click()

            discard = drive.find_element_by_class_name("artdeco-modal__confirm-dialog-btn")
            discard.click()
            print("contain next")
            # continue
        else:
            print(check_button.text)
            close = drive.find_element_by_class_name("artdeco-modal__dismiss")
            close.click()

            discard = drive.find_element_by_class_name("artdeco-modal__confirm-dialog-btn")
            discard.click()

    except NoSuchElementException:
            print("complicated application")
            # continue







