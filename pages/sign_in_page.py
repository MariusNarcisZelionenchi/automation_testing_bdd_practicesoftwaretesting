import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base_page import BasePage
import string
import random
from faker import Faker


class SignInPage(BasePage):
    BTN_SIGN_IN = (By.XPATH, '//a[@data-test="nav-sign-in"]')
    FIELD_EMAIL = (By.XPATH, '//input[@id="email"]')
    FIELD_PASSWORD = (By.XPATH, '//input[@id="password"]')
    BTN_LOGIN = (By.XPATH, '//input[@value="Login"]')
    BTN_REGISTER_NEW_ACCOUNT = (By.XPATH, '//a[@href="#/auth/register"]')
    ERR_EMAIL = (By.XPATH, '//div[@id="email-error"]/div')
    ERR_CREDENTIALS = (By.XPATH, '//div[@class="help-block"]')
    ERR_PASSWORD = (By.XPATH, '//div[contains(text(), "Password length is invalid")]')
    BTN_USER = (By.XPATH, '//a[@id="menu"]')
    INPUT_FIRST_NAME = (By.ID, 'first_name')
    INPUT_LAST_NAME = (By.ID, 'last_name')
    INPUT_DOB = (By.ID, 'dob')
    INPUT_ADDRESS = (By.ID, 'address')
    INPUT_POST_CODE = (By.ID, 'postcode')
    INPUT_CITY = (By.ID, 'city')
    INPUT_STATE = (By.ID, 'state')
    INPUT_COUNTRY = (By.ID, 'country')
    INPUT_PHONE = (By.ID, 'phone')
    INPUT_EMAIL = (By.ID, 'email')
    INPUT_PASSWORD = (By.ID, 'password')
    BTN_SUBMIT = (By.XPATH, '//button[@type="submit"]')
    BTN_USER_DROPDOWN = (By.ID, 'menu')
    BTN_SIGN_OUT = (By.XPATH, '//a[@data-test="nav-sign-out"]')
    fake = Faker(locale='ro')
    fake_password = fake.password(10, True, True, True, True)
    fake_email = fake.email()

    def navigate_to_sign_in_from_home(self):
        self.url(self.URL_HOME)
        self.click_elem(self.BTN_SIGN_IN)
        WebDriverWait(self.driver, 2).until(EC.url_matches(self.URL_SIGN_IN))  # trebuie sa astept pentru ca pag sa se incarce
        assert self.actual_url() == self.URL_SIGN_IN

    def navigate_to_home(self):
        self.url(self.URL_HOME)

    def navigate_to_register(self):
        self.url(self.URL_REGISTER)

    def navigate_to_sign_in(self):
        self.url(self.URL_SIGN_IN)

    def insert_invalid_credentials(self, email, password, email_err):
        if email == 'blank':
            email = chr(32)
            self.write_txt(self.FIELD_EMAIL, email)
            self.write_txt(self.FIELD_PASSWORD, password)
            self.click_login()
            assert email_err == self.read_txt(self.ERR_EMAIL)
            self.clear_fields()
        elif email == 'no_email':
            self.write_txt(self.FIELD_EMAIL, email)
            self.write_txt(self.FIELD_PASSWORD, password)
            self.click_login()
            assert email_err == self.read_txt(self.ERR_EMAIL)
            self.clear_fields()
        elif email == 'registered_email':
            for i in range(3):
                email = self.random_email
                self.write_txt(self.FIELD_EMAIL, email)
                self.write_txt(self.FIELD_PASSWORD, password)
                self.click_login()
                WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.ERR_CREDENTIALS))
                assert email_err == self.read_txt(self.ERR_CREDENTIALS)
                self.clear_fields()
                i += 1
        else:
            pass

    def click_login(self):
        self.click_elem(self.BTN_LOGIN)

    def check_email_err_msg(self,email, email_err):
        if email == 'blank':
            assert email_err == self.read_txt(self.ERR_EMAIL)
        elif email == 'no_email':
            assert email_err == self.read_txt(self.ERR_EMAIL)
        elif email == 'registered_email':
            assert email_err == self.read_txt(self.ERR_CREDENTIALS)

    def check_credentials_err(self, credentials_err):
        assert self.is_elem_displayed(self.ERR_CREDENTIALS), credentials_err in self.read_txt(self.ERR_CREDENTIALS)

    # pagina nu accepta password < 3 char, deci imi trb o functie care sa introduca parole < 3 char
    def insert_too_short_password(self, email):
        password = ''
        for i in range(10):
            character = random.choice(string.ascii_letters)
            password += character
            self.write_txt(self.FIELD_EMAIL, email)
            self.write_txt(self.FIELD_PASSWORD, password)
            self.click_elem(self.BTN_LOGIN)
            self.clear_fields()
            if len(password) >= 2:
                break

    def check_password_err_msg(self, password_err):
        assert self.is_elem_displayed(self.ERR_PASSWORD), password_err in self.read_txt(self.ERR_PASSWORD)

    def clear_fields(self):
        self.clear_input(self.FIELD_EMAIL)
        self.clear_input(self.FIELD_PASSWORD)

    def check_url_account(self):
        WebDriverWait(self.driver, 5).until(EC.url_matches(self.URL_ACCOUNT))  # trebuie sa ast pentru ca pag sa se incarce
        assert self.actual_url() == self.URL_ACCOUNT

    def check_url_sign_in(self):
        WebDriverWait(self.driver, 10).until(EC.url_matches(self.URL_SIGN_IN))  # trebuie sa ast pentru ca pag sa se incarce
        assert self.actual_url() == self.URL_SIGN_IN

    ##################  REGISTER NEW ACCOUNT  ###################

    ##################        PARAMETERS      ###################

    def click_register_new_account_btn(self):
        self.click_elem(self.BTN_REGISTER_NEW_ACCOUNT)

    def input_first_name(self, prenume):
        self.write_txt(self.INPUT_FIRST_NAME, prenume)

    def input_last_name(self, nume):
        self.write_txt(self.INPUT_LAST_NAME, nume)

    def input_dob(self, data_nasterii):
        self.write_txt(self.INPUT_DOB, data_nasterii)

    def input_address(self, adresa):
        self.write_txt(self.INPUT_ADDRESS, adresa)

    def input_post_code(self, cod_postal):
        self.write_txt(self.INPUT_POST_CODE, cod_postal)

    def input_city(self, oras):
        self.write_txt(self.INPUT_CITY, oras)

    def input_state(self, judet):
        self.write_txt(self.INPUT_STATE, judet)

    def input_phone(self, telefon):
        self.write_txt(self.INPUT_PHONE, telefon)

    def input_random_email(self):
        email = self.random_email
        self.write_txt(self.INPUT_EMAIL, email)

    def input_random_password(self):
        password = self.random_password
        self.write_txt(self.INPUT_PASSWORD, password)

    ##################         FAKER         ###################

    def input_fake_first_name(self):
        first_name = self.fake.first_name()
        self.write_txt(self.INPUT_FIRST_NAME, first_name)

    def input_fake_last_name(self):
        last_name = self.fake.last_name()
        self.write_txt(self.INPUT_LAST_NAME, last_name)

    def input_fake_address(self):
        address = self.fake.address()
        self.write_txt(self.INPUT_ADDRESS, address)

    def input_fake_postal_code(self):
        postal_code = self.fake.postcode()
        self.write_txt(self.INPUT_POST_CODE, postal_code)

    def input_fake_city(self):
        city = self.fake.city()
        self.write_txt(self.INPUT_CITY, city)

    def input_fake_state(self):
        state = self.fake.state()
        self.write_txt(self.INPUT_STATE, state)

    def input_country(self, tara):
        # self.write_txt(self.INPUT_ADDRESS, 'Romania')
        self.select_dropdown_by_txt(self.INPUT_COUNTRY, tara)  # iau numele tarii din lista

    def input_fake_phone(self):
        phone_number = self.fake.phone_number()
        phone_number_no_spaces = phone_number.replace(' ', '')
        self.write_txt(self.INPUT_PHONE, phone_number_no_spaces)

    def input_fake_email(self):
        self.write_txt(self.INPUT_EMAIL, self.fake_email)

    def input_fake_password(self):
        self.write_txt(self.INPUT_PASSWORD, self.fake_password)

    def click_register_btn(self):
        self.click_elem(self.BTN_SUBMIT)

    def fill_form(self):
        form_data = {
            self.INPUT_FIRST_NAME: 'my_username',
            self.INPUT_LAST_NAME: 'my_password',
            self.INPUT_DOB: '01012000',
            self.INPUT_ADDRESS: 'my_address',
            self.INPUT_POST_CODE: '010101',
            self.INPUT_CITY: 'my_city',
            self.INPUT_STATE: 'my_state',
            self.INPUT_COUNTRY: self.select_dropdown_by_txt(self.INPUT_COUNTRY, 'Romania'),
            self.INPUT_PHONE: '0101010101',
            self.INPUT_EMAIL: self.random_email,
            self.INPUT_PASSWORD: self.random_password,
        }
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.BTN_SUBMIT))
            for field_name, value in form_data.items():
                try:
                    # Find the input field by name attribute and fill it
                    input_element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(field_name))
                    input_element.clear()
                    input_element.send_keys(value)
                except Exception as e:
                    print(f'Could not fill in the field {field_name}: {e}')
        finally:
            self.click_elem(self.BTN_SUBMIT)

    def check_url_register(self):
        WebDriverWait(self.driver, 5).until(EC.url_matches(self.URL_REGISTER))  # trebuie sa astept pentru ca pag sa se incarce
        assert self.actual_url() == self.URL_REGISTER

    def insert_registered_email_and_password(self):
        self.write_txt(self.FIELD_EMAIL, self.random_email)
        self.write_txt(self.FIELD_PASSWORD, self.random_password)
        time.sleep(1)

    def insert_registered_fake_email_and_password(self):
        self.write_txt(self.FIELD_EMAIL, self.fake_email)
        self.write_txt(self.FIELD_PASSWORD, self.fake_password)
        time.sleep(1)

    def sign_out(self):
        self.click_elem(self.BTN_USER_DROPDOWN)
        self.click_elem(self.BTN_SIGN_OUT)