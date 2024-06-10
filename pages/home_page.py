from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from base_page import BasePage


class HomePage(BasePage):

    def navigate_to_home(self):
        self.url(self.URL_HOME)

    def check_url_sign_in(self):
        WebDriverWait(self.driver, 10).until(EC.url_matches(self.URL_SIGN_IN))  # trebuie sa ast pentru ca pag sa se incarce
        assert self.actual_url() == self.URL_SIGN_IN
