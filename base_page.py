import random

from selenium.webdriver.support.select import Select

from browser import Browser


# Clasa cu metode ce vor simplifica codul ulterior(din pages si steps)
class BasePage(Browser):
    URL_HOME = 'https://practicesoftwaretesting.com/#/'
    URL_SIGN_IN = 'https://practicesoftwaretesting.com/#/auth/login'
    URL_ACCOUNT = 'https://practicesoftwaretesting.com/#/account'
    URL_REGISTER = 'https://practicesoftwaretesting.com/#/auth/register'

    random_number = random.randint(0, 999_999_999)
    random_email = f'correct_email.{random_number}@mail.com'
    random_password = f'KEY{random_number}x!'

    # metoda ce deschide un link:
    def url(self, link):
        self.driver.get(link)

    # metoda ce citeste url-ul curent:
    def actual_url(self):
        return self.driver.current_url

    # metoda ce identifica un elem folosind ca parametru un locator(o constanta definita la inceputul clasei)
    def identify_elem(self, locator):
        return self.driver.find_element(*locator)

    # metoda ce verif daca un elem e afisat
    def is_elem_displayed(self, locator):
        return self.identify_elem(locator).is_displayed()

    # metoda ce da click pe un elem
    def click_elem(self, locator):
        self.identify_elem(locator).click()

    # metoda ce citeste textul de pe un element:
    def read_txt(self, locator):
        return self.identify_elem(locator).text

    # metoda ce scrie text pe un element:
    def write_txt(self, locator, txt):
        self.identify_elem(locator).send_keys(txt)

    # metoda care sterge campurile scrise cu metoda write_text
    def clear_input(self, locator):
        self.identify_elem(locator).clear()

    # metoda ce da click pe un element dintr-o lista de tip dropdown
    def select_dropdown_by_txt(self, dropdown_locator, txt):
        dropdown_elem = self.identify_elem(dropdown_locator)
        select = Select(dropdown_elem)
        select.select_by_visible_text(txt)
