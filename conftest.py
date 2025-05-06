import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope='function')
def browser():
    options=Options()
    options.add_argument("--disable-infobars")  # optional
    options.add_experimental_option("prefs", {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False
    })
    options.add_experimental_option("detach",True)
    driver=webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.set_page_load_timeout(30)
    yield driver
    driver.quit()