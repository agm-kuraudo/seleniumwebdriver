import time
import pytest
from selenium.webdriver.common.by import By
from page_objects.login_page import LoginPage
from page_objects.login_success_page import LoggedInSuccessfullyPage
from page_objects.exceptions_page import ExceptionsPage


class TestNegativeScenarios:
    @pytest.mark.login
    @pytest.mark.negative
    @pytest.mark.parametrize("username, password, expected_error_message",
                             [("incorrectUser", "Password123", "Your username is invalid!"),
                              ("student", "incorrectPassword", "Your password is invalid!")])
    def test_negative_login(self, driver, username, password, expected_error_message):

        login_page = LoginPage(driver)

        login_page.open()

        login_page.execute_login(username, password)

        assert login_page.get_error_message() == expected_error_message
