"""
Open page
Click Add button
Verify Row 2 input field is displayed
"""

import time
import pytest
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class TestExceptionScenarios:

    @pytest.mark.exceptions
    def test_add_row(self, driver):
        # Open page
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")

        # Type username incorrectUser into Username field
        #/ html // button[ @ id = 'add_btn']
        add_btn_locator = driver.find_element(By.ID, "add_btn")
        add_btn_locator.click()

        # Verify row 2 is displayed
        wait = WebDriverWait(driver, 10)
        row2_locator = wait.until(ec.presence_of_element_located((By.XPATH, "//div[@id='row2']/input")))

        #row2_locator = driver.find_element(By.XPATH, "//div[@id='row2']/input")
        assert row2_locator.is_displayed(), "Row 2 is not displayed, but it should be"

    def test_save_new_row(self, driver):
        # Open page

        driver.get("https://practicetestautomation.com/practice-test-exceptions/")

        #Click Add button

        add_btn_locator = driver.find_element(By.ID, "add_btn")
        add_btn_locator.click()

#//div[@id='rows']/div[3]/div[@class='row']/button[@id='save_btn']
        #Wait for the second row to load
        wait = WebDriverWait(driver, 10)

        row2_locator = wait.until(ec.presence_of_element_located((By.XPATH, "//div[@id='row2']/input")))
        assert row2_locator.is_displayed(), "Row 2 is not displayed, but it should be"

        #Type text into the second input field
        row2_locator.send_keys("Whatever")

        #Push Save button using locator By.name(“Save”)
        save_btn_locator = driver.find_element(By.XPATH, "//div[@id='row2']/button[@id='save_btn']")
        save_btn_locator.click()

        # Verify text saved
        confirmation_element = wait.until(ec.visibility_of_element_located((By.ID, "confirmation")))
        confirmation_message = confirmation_element.text
        assert confirmation_message == "Row 2 was saved", "Confirmation message is not expected"


    @pytest.mark.exceptions
    def test_invalid_element_state_exception(self, driver):
        # Open page
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")

        # Clear input field
        row_1_edit_button = driver.find_element(By.ID, "edit_btn")
        row_1_edit_button.click()

        row_1_input_element = driver.find_element(By.XPATH, "//div[@id='row1']/input")
        wait = WebDriverWait(driver, 10)
        wait.until(ec.element_to_be_clickable(row_1_input_element))
        row_1_input_element.clear()

        # Type text into the input field
        row_1_input_element.send_keys("Sushi")

        row_1_save_button = driver.find_element(By.ID, "save_btn")
        row_1_save_button.click()

        # Verify text saved
        confirmation_element = wait.until(ec.visibility_of_element_located((By.ID, "confirmation")))
        confirmation_message = confirmation_element.text
        assert confirmation_message == "Row 1 was saved", "Confirmation message is not expected"