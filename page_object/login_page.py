import configparser

from selenium.webdriver.common.by import By

config = configparser.RawConfigParser()
config.read('./configurations/config.ini')


class LoginPage:
    base_url = config.get('common data', 'base_url')
    login_button = config.get('auth_xpath', 'login_button')
    username_field = config.get('login_form_xpath', 'username')
    next_button = config.get('login_form_xpath', 'next_button')
    password_field = config.get('login_form_xpath', 'password')
    login = config.get('login_form_xpath', 'login_button')

    def __init__(self, driver):
        self.driver = driver

    def launch_login_page(self):
        self.driver.find_element(By.XPATH, self.login_button).click()

    def set_username(self, username):
        self.driver.find_element(By.XPATH, self.username_field).clear()
        self.driver.find_element(
            By.XPATH, self.username_field).send_keys(username)

    def click_next(self):
        self.driver.find_element(By.XPATH, self.next_button).click()

    def set_password(self, password):
        self.driver.find_element(By.XPATH, self.password_field).clear()
        self.driver.find_element(
            By.XPATH, self.password_field).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(By.XPATH, self.login).click()
