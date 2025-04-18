import pytest
import sys
import os
from dotenv import load_dotenv

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from pages.register_page import QaharborRegisterPage
from pages.login_page import QaharborLoginPage



load_dotenv()

USER_NAME = os.getenv("USER_NAME")
EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
PASSWORD = os.getenv("PASSWORD")
CONFIRM_PASSWORD = os.getenv("CONFIRM_PASSWORD")

@pytest.mark.register
def test_register(browser):
    register_page = QaharborRegisterPage(browser)
    register_page.go_to_register_page("https://labsqajobs.qaharbor.com/candidate-registration/")
    register_page.enter_username(USER_NAME)
    register_page.enter_email_address(EMAIL_ADDRESS)
    register_page.enter_password(PASSWORD)
    register_page.enter_confirm_password(CONFIRM_PASSWORD)
    register_page.submit_register_button()
    assert register_page.is_registration_successful(), "register failed!"


    login_page = QaharborLoginPage(browser)
    login_page.go_to_login_page("https://labsqajobs.qaharbor.com/login/")
    login_page.enter_email(EMAIL_ADDRESS)
    login_page.enter_password(PASSWORD)
    login_page.click_login()

    assert login_page.is_login_successful(), "Login failed!"
