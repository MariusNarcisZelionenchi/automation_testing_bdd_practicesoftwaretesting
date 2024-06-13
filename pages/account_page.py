import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from base_page import BasePage


class AccountPage(BasePage):

    BTN_SIGN_IN = (By.XPATH, '//a[@data-test="nav-sign-in"]')
    BTN_LOGO = (By.ID, 'Layer_1')
    FIELD_SEARCH = (By.ID, 'search-query')
    BTN_SEARCH = (By.XPATH, '//button[@class="btn btn-secondary"]')
    SECOND_ITEM = (By.XPATH, '//a[@class="card"][2]')
    ITEM_PRICE = (By.XPATH, '//span[@aria-label="unit-price"]')
    BTN_INCREASE = (By.XPATH, '//i[@class="fa fa-plus"]')
    BTN_DECREASE = (By.XPATH, '//i[@class="fa fa-minus"]')
    BTN_ADD_TO_CART = (By.ID, 'btn-add-to-cart')
    MSG_PRODUCT_ADDED = (By.XPATH, '//div[@aria-label="Product added to shopping cart."]')
    BTN_NUMBER_OF_ITEMS_IN_CART = (By.ID, 'lblCartCount')
    BTN_CART = (By.XPATH, '//i[@class="fa fa-shopping-cart px-1"]')
    UNIT_PRICE = (By.XPATH, '/html/body/app-root/div/app-checkout/aw-wizard/div/aw-wizard-step[1]/app-cart/div/table/tbody/tr/td[3]/span')
    TOTAL_UNIT_PRICE = (By.XPATH, '/html/body/app-root/div/app-checkout/aw-wizard/div/aw-wizard-step[1]/app-cart/div/table/tbody/tr/td[4]/span')
    TOTAL_PRICE = (By.XPATH, '(//td[@class="col-md-2 text-end"])[4]')
    QUANTITY = (By.XPATH, '//input[@class="form-control quantity"]')
    BTN_PROCEED_TO_CHECKOUT_1 = (By.XPATH, '//button[@data-test="proceed-1"]')
    MSG_PROCEED_TO_CHECKOUT = (By.XPATH, '//p[@class="ng-star-inserted"]')
    BTN_PROCEED_TO_CHECKOUT_2 = (By.XPATH, '//button[@data-test="proceed-2"]')
    BOX_ADDRESS = (By.ID, 'address')
    BOX_CITY = (By.ID, 'city')
    BOX_STATE = (By.ID, 'state')
    BOX_COUNTRY = (By.ID, 'country')
    BOX_POSTCODE = (By.ID, 'postcode')
    BTN_PROCEED_TO_CHECKOUT_3 = (By.XPATH, '//button[@data-test="proceed-3"]')
    BTN_PAYMENT_METHOD = (By.ID, 'payment-method')
    BTN_USER_DROPDOWN = (By.ID, 'menu')
    BTN_SIGN_OUT = (By.XPATH, '//a[@data-test="nav-sign-out"]')

    def navigate_to_account(self):
        self.url(self.URL_ACCOUNT)

    def click_logo(self):
        self.click_elem(self.BTN_LOGO)

    def search(self, item):
        self.click_elem(self.FIELD_SEARCH)
        self.write_txt(self.FIELD_SEARCH, item)
        self.click_elem(self.BTN_SEARCH)

    def choose_item(self):
        # WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.SECOND_ITEM))
        time.sleep(2)
        self.click_elem(self.SECOND_ITEM)

    def click_increase(self):
        self.click_elem(self.BTN_INCREASE)
        self.click_elem(self.BTN_INCREASE)

    def click_add_to_cart(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.BTN_ADD_TO_CART))
        self.click_elem(self.BTN_ADD_TO_CART)

    def is_item_added_msg_displayed(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.MSG_PRODUCT_ADDED))
        assert self.is_elem_displayed(self.MSG_PRODUCT_ADDED)

    def is_total_of_products_displayed(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.BTN_NUMBER_OF_ITEMS_IN_CART))
        assert self.is_elem_displayed(self.BTN_NUMBER_OF_ITEMS_IN_CART)

    def check_number_of_items(self):
        products = int(self.read_txt(self.BTN_NUMBER_OF_ITEMS_IN_CART))
        assert products == 1

    def click_cart(self):
        self.click_elem(self.BTN_CART)

    def set_new_amount(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.QUANTITY))
        quantity = self.identify_elem(self.QUANTITY)
        quantity.send_keys(Keys.CONTROL, 'A')
        quantity.send_keys(Keys.DELETE)
        self.write_txt(self.QUANTITY, '2')
        quantity.send_keys(Keys.ENTER)
        time.sleep(2)

    def check_total_unit_price(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.TOTAL_UNIT_PRICE))
        unit_price = float(self.read_txt(self.UNIT_PRICE)[1:])
        total_unit_price = 2 * unit_price
        assert total_unit_price == float(self.read_txt(self.TOTAL_UNIT_PRICE)[1:])

    def click_proceed_1(self):
        self.click_elem(self.BTN_PROCEED_TO_CHECKOUT_1)

    def is_proceed_msg_displayed(self):
        return self.is_elem_displayed(self.MSG_PROCEED_TO_CHECKOUT)

    def click_proceed_2(self):
        self.click_elem(self.BTN_PROCEED_TO_CHECKOUT_2)

    def is_info_displayed(self):
        return self.is_elem_displayed(self.BOX_ADDRESS), self.is_elem_displayed(self.BOX_CITY), self.is_elem_displayed(self.BOX_STATE), self.is_elem_displayed(self.BOX_COUNTRY), self.is_elem_displayed(self.BOX_POSTCODE)

    def click_proceed_3(self):
        self.click_elem(self.BTN_PROCEED_TO_CHECKOUT_3)

    def is_payment_msg_displayed(self):
        return self.is_elem_displayed(self.BTN_PAYMENT_METHOD)

    def check_if_user_is_logged_in(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.BTN_USER_DROPDOWN))
        assert self.is_elem_displayed(self.BTN_USER_DROPDOWN)

    def sign_out(self):
        self.click_elem(self.BTN_USER_DROPDOWN)
        self.click_elem(self.BTN_SIGN_OUT)

    def is_sign_in_btn_displayed(self):
        assert self.is_elem_displayed(self.BTN_SIGN_IN)
