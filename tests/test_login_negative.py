import time
import pytest
from selenium.webdriver.common.by import By


class TestNegativeScenarios:
    @pytest.mark.login
    @pytest.mark.negative
    @pytest.mark.parametrize("username, password, expected_error_message",
                             [("incorrectUser", "Password123", "Your username is invalid!"),
                              ("student", "incorrectPassword", "Your password is invalid!")])
    def test_negative_login(self, driver, username, password, expected_error_message):
        # Open page
        driver.get("https://practicetestautomation.com/practice-test-login/")

        # Type username incorrectUser into Username field
        username_locator = driver.find_element(By.ID, "username")
        username_locator.send_keys(username)

        # Type password Password123 into Password field
        password_locator = driver.find_element(By.NAME, "password")
        password_locator.send_keys(password)

        # Push Submit button
        submit_button_locator = driver.find_element(By.XPATH, "//button[@class='btn']")
        submit_button_locator.click()
        time.sleep(2)

        # Verify error message is displayed
        error_message_locator = driver.find_element(By.ID, "error")
        assert error_message_locator.is_displayed(), "Error message is not displayed, but it should be"

        # Verify error message text is Your username is invalid!
        error_message = error_message_locator.text
        assert error_message == expected_error_message, "Error message is not expected"

    # @pytest.mark.login
    # @pytest.mark.negative
    # def test_wrong_username(self, driver):
    #     # Open Browser
    #
    #     time.sleep(3)
    #
    #     # Navigate to webpage
    #     driver.get("https://practicetestautomation.com/practice-test-login/")
    #
    #     # //input[@id='username']
    #     #
    #     # /html//input[@id='password']
    #     time.sleep(2)
    #     # Type username student into Username field
    #     username_locator = driver.find_element(By.ID, "username")
    #
    #     username_locator.send_keys("incorrect_username")
    #
    #     # Type password Password123 into Password field
    #     password_locator = driver.find_element(By.NAME, "password")
    #     password_locator.send_keys("Password123")
    #     # Push Submit button
    #     submit_locator = driver.find_element(By.XPATH, "//button[@class='btn']")
    #     submit_locator.click()
    #     time.sleep(2)
    #
    #
    #     error_locator = driver.find_element(By.ID, "error")
    #     #Verify error message is displayed
    #     assert error_locator.is_displayed(), "Error not displayed"
    #
    #     #Verify error message text is Your username is invalid!
    #     assert error_locator.text == "Your username is invalid!", "incorrect error text"
    #
    # @pytest.mark.login
    # @pytest.mark.negative
    # def test_wrong_password(self, driver):
    #
    #     time.sleep(3)
    #
    #     # Navigate to webpage
    #     driver.get("https://practicetestautomation.com/practice-test-login/")
    #
    #     # //input[@id='username']
    #     #
    #     # /html//input[@id='password']
    #     time.sleep(2)
    #     # Type username student into Username field
    #     username_locator = driver.find_element(By.ID, "username")
    #
    #     username_locator.send_keys("student")
    #
    #     # Type password Password123 into Password field
    #     password_locator = driver.find_element(By.NAME, "password")
    #     password_locator.send_keys("incorrect_password")
    #     # Push Submit button
    #     submit_locator = driver.find_element(By.XPATH, "//button[@class='btn']")
    #     submit_locator.click()
    #     time.sleep(2)
    #
    #
    #     error_locator = driver.find_element(By.ID, "error")
    #     #Verify error message is displayed
    #     assert error_locator.is_displayed(), "Error not displayed"
    #
    #     #Verify error message text is Your username is invalid!
    #     assert error_locator.text == "Your password is invalid!", "incorrect error text"