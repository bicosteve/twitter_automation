import configparser

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

config = configparser.RawConfigParser()
config.read('./configurations/config.ini')


class RegisterPage:
    register_url = config.get('common data', 'base_url')
    register_button = config.get('auth_xpath', 'sign_up_button')
    phone_or_email_button = config.get(
        'auth_xpath', 'sign_up_with_email_phone')
    choose_email = config.get('register_form_xpath', 'sign_up_with_email')
    name_field = config.get('register_form_xpath', 'name_input')
    email_field = config.get('register_form_xpath', 'email_input')
    month_of_birth = config.get('register_form_xpath', 'month_of_birth')
    day_of_birth = config.get('register_form_xpath', 'day_of_birth')
    year_of_birth = config.get('register_form_xpath', 'year_of_birth')
    next_button = config.get('register_form_xpath', 'next_button')
    sign_up_button = config.get('register_form_xpath', 'sign_up_button')

    def __init__(self, driver):
        self.driver = driver

    def launch_login_page(self):
        self.driver.find_element(By.XPATH, self.register_button).click()

    def initalize_sign_up(self):
        self.driver.find_element(By.XPATH, self.phone_or_email_button).click()
        # choosing email field instead of phone number
        self.driver.find_element(By.XPATH, self.choose_email).click()

    def fill_name(self, name):
        self.driver.find_element(By.XPATH, self.name_field).click()
        self.driver.find_element(By.XPATH, self.name_field).send_keys(name)

    def set_email(self, email):
        self.driver.find_element(By.XPATH, self.email_field).click()
        self.driver.find_element(By.XPATH, self.email_field).send_keys(email)

    def set_dob(self, month, day, year):
        month_dropdown = self.driver.find_element(
            By.XPATH, self.month_of_birth)
        selected_month = Select(month_dropdown)
        selected_month.select_by_value(month)

        day_dropdown = self.driver.find_element(By.XPATH, self.day_of_birth)
        selected_day = Select(day_dropdown)
        selected_day.select_by_value(day)

        year_dropdown = self.driver.find_element(By.XPATH, self.year_of_birth)
        selected_year = Select(year_dropdown)
        selected_year.select_by_value(year)

    def click_next_button(self):
        self.driver.find_element(By.XPATH, self.next_button).click()
        self.driver.find_element(By.XPATH, self.next_button).click()
        # the 2nd next btn

    def click_register_button(self):
        self.driver.find_element(By.XPATH, self.sign_up_button).click()
