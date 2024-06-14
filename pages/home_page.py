from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from base_page import BasePage
# from selenium.webdriver.support.select import Select
from selenium.webdriver import Keys, ActionChains
from selenium import webdriver
from selenium.webdriver.support.ui import Select


class HomePage(BasePage):

    BTN_HAMMER = (By.XPATH, '//label[normalize-space()="Hammer"]')
    BTN_SAW = (By.XPATH, '//label[normalize-space()="Saw"]')
    BTN_TOOL_BELTS = (By.XPATH, '//label[normalize-space()="Tool Belts"]')
    PRODUCT_NAME = (By.CLASS_NAME, 'card-title')
    BTN_SORT_BY = (By.CLASS_NAME, 'form-select')
    BTN_PRICE_MIN = (By.XPATH, '//span[@aria-valuenow = "0"]')
    BTN_PRICE_MAX = (By.XPATH, '//span[@aria-valuenow = "100"]')
    PRODUCT_PRICE = (By.XPATH, '//span[@data-test="product-price"]')

    def navigate_to_home(self):
        self.url(self.URL_HOME)

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

    def check_if_prices_are_reordered(self):
        products_price_list = []
        for item in self.driver.find_elements(*self.PRODUCT_PRICE):
            product_price = float(item.text.replace('$', ''))
            products_price_list.append(product_price)
        ordered_products_price_list = sorted(products_price_list)
        assert products_price_list == ordered_products_price_list
