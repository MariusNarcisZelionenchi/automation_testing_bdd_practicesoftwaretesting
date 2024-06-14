
from selenium.webdriver.common.by import By
from base_page import BasePage
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select


class HomePage(BasePage):

    BTN_HAMMER = (By.XPATH, '//label[normalize-space()="Hammer"]')
    BTN_SAW = (By.XPATH, '//label[normalize-space()="Saw"]')
    BTN_TOOL_BELTS = (By.XPATH, '//label[normalize-space()="Tool Belts"]')
    PRODUCT_NAME = (By.CLASS_NAME, 'card-title')
    BTN_SORT_BY = (By.CLASS_NAME, 'form-select')
    BTN_PRICE_MIN = (By.XPATH, '//span[contains(@class,"slider-pointer-min")]')
    BTN_PRICE_MAX = (By.XPATH, '//span[contains(@class,"slider-pointer-max")]')
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
        product_price = float(self.read_txt(self.PRODUCT_PRICE)[1:])
        products_price_list.append(product_price)
        ordered_products_price_list = sorted(products_price_list)
        assert products_price_list == ordered_products_price_list

    def modify_max_price(self):
        action = ActionChains(self.driver).drag_and_drop_by_offset(self.identify_elem(self.BTN_PRICE_MAX), -116, 0)
        action.perform()

    def check_if_prices_are_lower_than_max_price(self):
        products_price_list = []
        product_price = float(self.read_txt(self.PRODUCT_PRICE)[1:])
        products_price_list.append(product_price)
        max_price_value = float(self.identify_elem(self.BTN_PRICE_MAX).get_attribute("aria-valuenow"))
        for item in products_price_list:
            assert item <= max_price_value
