from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class QaharborLoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def go_to_login_page(self, url):
        self.driver.get(url)

    def enter_email(self, email):
        self.wait.until(EC.presence_of_element_located((By.ID, "user_login"))).send_keys(email)

    def enter_password(self, password):
        self.driver.find_element(By.ID, "user_pass").send_keys(password)

    def click_login(self):
        self.driver.find_element(By.ID, "wp-submit").click()

    def is_login_successful(self):
        try:
            self.wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Logout")))
            return True
        except:
            return False
