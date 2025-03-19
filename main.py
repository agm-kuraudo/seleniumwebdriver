from selenium import webdriver
import time

from selenium.webdriver.common.by import By

# Open Browser
driver = webdriver.Chrome()

time.sleep(3)

# Navigate to webpage
driver.get("https://practicetestautomation.com/practice-test-login/")

#//input[@id='username']
#
#/html//input[@id='password']
time.sleep(2)
#Type username student into Username field
username_locator = driver.find_element(By.ID, "username")

username_locator.send_keys("student")

#Type password Password123 into Password field
password_locator = driver.find_element(By.NAME, "password")
password_locator.send_keys("Password123")
#Push Submit button
submit_locator = driver.find_element(By.XPATH, "//button[@class='btn']")
submit_locator.click()
time.sleep(2)

#Verify new page URL contains practicetestautomation.com/logged-in-successfully/
actual_url = driver.current_url
assert actual_url == "https://practicetestautomation.com/logged-in-successfully/"


login_message_locator = driver.find_element(By.TAG_NAME, "h1")
actual_text = login_message_locator.text
assert actual_text == "Logged In Successfully"
#Verify new page contains expected text ('Congratulations' or 'successfully logged in')

logout_button_selector = driver.find_element(By.LINK_TEXT, "Log out")
assert logout_button_selector.is_displayed()
#Verify button Log out is displayed on the new page
