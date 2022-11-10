import configparser

from selenium.webdriver.common.by import By

config = configparser.RawConfigParser()
config.read('./configurations/config.ini')


class RegisterPage:
    base_url = config.get('common data', 'base_url')
    register_button = config.get('auth_xpath', 'sign_up_button')

    def __init__(self, driver):
        self.driver = driver

    def launch_login_page(self):
        self.driver.find_element(By.XPATH, self.register_button).click()
