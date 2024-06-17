import time

from selenium.webdriver.common.by import By
from base_page import BasePage
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select
from pynput.keyboard import Key, Controller

class HomePage(BasePage):

    BTN_HAMMER = (By.XPATH, '//label[normalize-space()="Hammer"]')
    BTN_SAW = (By.XPATH, '//label[normalize-space()="Saw"]')
    BTN_TOOL_BELTS = (By.XPATH, '//label[normalize-space()="Tool Belts"]')
    PRODUCT_NAME = (By.CLASS_NAME, 'card-title')
    BTN_SORT_BY = (By.CLASS_NAME, 'form-select')
    BTN_PRICE_MIN = (By.XPATH, '//span[contains(@class,"slider-pointer-min")]')
    BTN_PRICE_MAX = (By.XPATH, '//span[contains(@class,"slider-pointer-max")]')
    PRODUCT_PRICE = (By.XPATH, '//span[@data-test="product-price"]')
    CONTACT_BTN = (By.XPATH, '//a[normalize-space()="Contact"]')
    FIRST_NAME_INPUT = (By.XPATH, '//input[@id="first_name"]')
    LAST_NAME_INPUT = (By.XPATH, '//input[@id="last_name"]')
    EMAIL_INPUT = (By.XPATH, '//input[@id="email"]')
    SELECT_SUBJECT_DROPDOWN = (By.XPATH, '//select[@id="subject"]')
    MESSAGE_INPUT = (By.XPATH, '//textarea[@id="message"]')
    CHOOSE_FILE = (By.XPATH, '//input[@id="attachment"]')
    SEND_BTN = (By.XPATH, '//input[@value="Send"]')
    CONTACT_MSG = (By.XPATH, '//div[@role="alert"]')

    def navigate_to_home(self):
        self.url(self.URL_HOME)

    def click_contact_btn(self):
        self.click_elem(self.CONTACT_BTN)

    def input_info(self, first_name, last_name, email):
        self.write_txt(self.FIRST_NAME_INPUT, first_name)
        self.write_txt(self.LAST_NAME_INPUT, last_name)
        self.write_txt(self.EMAIL_INPUT, email)

    def select_subject(self):
        subject = Select(self.identify_elem(self.SELECT_SUBJECT_DROPDOWN))
        subject.select_by_visible_text('Payments')

    def insert_msg(self, text):
        self.write_txt(self.MESSAGE_INPUT, text)

    def choose_file_to_upload(self):
        self.click_elem(self.CHOOSE_FILE)
        time.sleep(2)  #trebuie time.sleep pentru ca wait nu functioneaza pe OS
        keyboard = Controller()
        keyboard.type('C:\\Users\\MNZ\\Desktop\\upload_file_TA\\upload.txt')
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)

    def click_send(self):
        self.click_elem(self.SEND_BTN)

    def is_contact_msg_displayed(self, msg):
        assert self.is_elem_displayed(self.CONTACT_MSG) and self.read_txt(self.CONTACT_MSG) == msg

    def select_product(self, product):
        if product == "Hammer":
            self.click_checkbox(self.BTN_HAMMER)
        elif product == "Saw":
            self.click_checkbox(self.BTN_SAW)
        elif product == "Tool Belts":
            self.click_checkbox(self.BTN_TOOL_BELTS)

    def sort_products_by_price(self):
        sort = Select(self.identify_elem(self.BTN_SORT_BY))
        sort.select_by_visible_text('Price (High - Low)')

    # def check_if_prices_are_reordered(self):
    #     products_price_list = []
    #     products_list = self.driver.find_elements(*self.PRODUCT_PRICE)
    #     for item in products_list:
    #         product_price = float(self.read_txt(item[1:]))
    #         products_price_list.append(product_price)
    #     ordered_products_price_list = sorted(products_price_list)
    #     assert products_price_list == ordered_products_price_list

    def check_if_prices_are_reordered(self):
        products_price_list = []
        products_list = self.driver.find_elements(*self.PRODUCT_PRICE)
        for item in products_list:
            product_price = self.read_txt(item)
            product_price = float(product_price.replace('$', ''))
            products_price_list.append(product_price)
        ordered_products_price_list = sorted(products_price_list)
        assert products_price_list == ordered_products_price_list

    def modify_max_price(self):
        action = ActionChains(self.driver).drag_and_drop_by_offset(self.identify_elem(self.BTN_PRICE_MAX), -116, 0)
        action.perform()

    # def check_if_prices_are_lower_than_max_price(self):
    #     products_price_list = []
    #     for item in self.driver.find_elements(self.PRODUCT_PRICE):
    #         product_price = float(self.read_txt(self.PRODUCT_PRICE)[1:])
    #         products_price_list.append(product_price)
    #     max_price_value = float(self.identify_elem(self.BTN_PRICE_MAX).get_attribute("aria-valuenow"))
    #     for item in products_price_list:
    #         assert item <= max_price_value
