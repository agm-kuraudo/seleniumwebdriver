import pytest
from page_objects.login_page import LoginPage
from page_objects.login_success_page import LoggedInSuccessfullyPage


class TestPositiveScenarios:
    @pytest.mark.login
    @pytest.mark.positive
    def test_login(self, driver):
        # Navigate to webpage

        login_page = LoginPage(driver)

        login_page.open()

        login_page.execute_login("username", "Password123")

        logged_in_page = LoggedInSuccessfullyPage(driver)

        assert logged_in_page.expected_url == logged_in_page.current_url, "Actual URL is not the same as expected"
        assert logged_in_page.header == "Logged In Successfully", "Header is not expected"
        assert logged_in_page.is_logout_button_displayed(), "Logout button should be visible"