from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

import time


class QaharborRegisterPage:

    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver,10)

    def go_to_register_page(self,url):
        self.driver.get(url)

    # def click_register_button(self):
    #     self.wait.until(EC.element_to_be_clickable((By.XPATH,"(//span[text()='Sign Up'])[2]"))).click()
    #
    # def click_candidate_button(self):
    #     self.wait.until(EC.presence_of_element_located((By.XPATH,"//span[text()='Candidate']"))).click()

    def enter_username(self,name):
        self.wait.until(EC.presence_of_element_located((By.XPATH,"//input[@placeholder='Username']"))).send_keys(name)

    def enter_email_address(self,email):
        self.wait.until(EC.presence_of_element_located((By.XPATH,"//input[@placeholder='Email Address']"))).send_keys(email)

    def enter_password(self,password):
        self.wait.until(EC.presence_of_element_located((By.XPATH,"//input[@placeholder='Password']"))).send_keys(password)

    def enter_confirm_password(self,confirmpass):
        self.wait.until(EC.presence_of_element_located((By.XPATH,"//input[@placeholder='Confirm Password']"))).send_keys(confirmpass)

    def submit_register_button(self):
        button = self.wait.until(EC.presence_of_element_located((By.XPATH, "//button[text()='REGISTER NOW']")))

        actions = ActionChains(self.driver)
        actions.move_to_element(button).perform()

        button.click()

        time.sleep(5)

    def is_registration_successful(self):
        try:
            self.wait.until(lambda driver: "success" in driver.current_url)
            return True
        except:
            return False

