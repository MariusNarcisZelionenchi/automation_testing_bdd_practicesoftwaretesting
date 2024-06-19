import time

from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select

from base_page import BasePage


class AccountPage(BasePage):

    BTN_SIGN_IN = (By.XPATH, '//a[@data-test="nav-sign-in"]')
    BTN_LOGO = (By.ID, 'Layer_1')
    FIELD_SEARCH = (By.ID, 'search-query')
    BTN_SEARCH = (By.XPATH, '//button[@class="btn btn-secondary"]')
    CHOSEN_ITEM = (By.XPATH, '//h5[normalize-space()="Belt Sander"]')
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
    BTN_PROCEED_TO_CHECKOUT_1 = (By.XPATH, '//div[@class="ng-star-inserted"]//button[@type="button"][normalize-space()="Proceed to checkout"]')
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
    BOX_BANK_NAME = (By.XPATH, '//input[@id="bank_name"]')
    BOX_ACCOUNT_NAME = (By.XPATH, '//input[@id="account_name"]')
    BOX_ACCOUNT_NUMBER = (By.XPATH, '//input[@id="account_number"]')
    BTN_CONFIRM = (By.XPATH, '//button[normalize-space()="Confirm"]')
    BOX_CREDIT_CARD_NUMBER = (By.XPATH, '//input[@id="credit_card_number"]')
    BOX_EXPIRATION_DATE = (By.XPATH, '//input[@id="expiration_date"]')
    BOX_CVV = (By.XPATH, '//input[@id="cvv"]')
    BOX_CARD_HOLDER_NAME = (By.XPATH, '//input[@id="card_holder-name"]')
    BTN_MONTHLY_INSTALLMENTS = (By.XPATH, '//select[@id="monthly_installments"]')
    BOX_GIFT_CARD_NUMBER = (By.XPATH, '//input[@id="gift_card_number"]')
    BOX_VALIDATION_CODE = (By.XPATH, '//input[@id="validation_code"]')
    PAYMENT_CONFIRMATION_MSG = (By.XPATH, '//div[@class="help-block"]')
    INVOICE_MSG = (By.XPATH, '//div[@id="order-confirmation"]')
    BTN_INVOICES = (By.XPATH, '//a[normalize-space()="My invoices"]')
    BTN_DETAILS = (By.XPATH, '//a[normalize-space()="Details"]')
    BTN_DOWNLOAD_PDF = (By.XPATH, '//button[@data-test="download-invoice"]')



    def navigate_to_account(self):
        self.url(self.URL_ACCOUNT)

    def click_logo(self):
        self.click_elem(self.BTN_LOGO)

    def search(self, item):
        self.click_elem(self.FIELD_SEARCH)
        self.write_txt(self.FIELD_SEARCH, item)
        self.click_elem(self.BTN_SEARCH)

    def choose_item(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.CHOSEN_ITEM))
        # time.sleep(2)
        self.click_elem(self.CHOSEN_ITEM)

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

    def click_proceed_2(self):
        self.click_elem(self.BTN_PROCEED_TO_CHECKOUT_2)

    # def is_info_displayed(self):
    #     assert self.is_elem_displayed(self.BOX_ADDRESS) and self.is_elem_displayed(self.BOX_CITY) and self.is_elem_displayed(self.BOX_STATE) and self.is_elem_displayed(self.BOX_COUNTRY) and self.is_elem_displayed(self.BOX_POSTCODE)

    def click_proceed_3(self):
        self.click_elem(self.BTN_PROCEED_TO_CHECKOUT_3)

    def is_payment_method_displayed(self):
        assert self.is_elem_displayed(self.BTN_PAYMENT_METHOD)

    def select_payment_method(self, payment_method):
        pay = Select(self.identify_elem(self.BTN_PAYMENT_METHOD))
        pay.select_by_visible_text(payment_method)

        if payment_method == 'Bank Transfer':
            self.write_txt(self.BOX_BANK_NAME, 'Iron Bank of Braavos')
            self.write_txt(self.BOX_ACCOUNT_NAME, 'Tycho Nestoris')
            self.write_txt(self.BOX_ACCOUNT_NUMBER, '010101010101010101')
            self.click_elem(self.BTN_CONFIRM)
        elif payment_method == 'Cash on Delivery':
            self.click_elem(self.BTN_CONFIRM)
        elif payment_method == 'Credit Card':
            self.write_txt(self.BOX_CREDIT_CARD_NUMBER, '1234-1234-1234-1234')
            self.write_txt(self.BOX_EXPIRATION_DATE, '03/2028')
            self.write_txt(self.BOX_CVV, '111')
            self.write_txt(self.BOX_CARD_HOLDER_NAME, 'Card Holder')
            self.click_elem(self.BTN_CONFIRM)
        elif payment_method == 'Buy Now Pay Later':
            installments = Select(self.identify_elem(self.BTN_MONTHLY_INSTALLMENTS))
            installments.select_by_visible_text('9 Monthly Installments')
            self.click_elem(self.BTN_CONFIRM)
        elif payment_method == 'Gift Card':
            self.write_txt(self.BOX_GIFT_CARD_NUMBER, 'mnz1234')
            self.write_txt(self.BOX_VALIDATION_CODE, '170379')
            self.click_elem(self.BTN_CONFIRM)

    def check_confirmation_msg(self, confirmation_msg):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.PAYMENT_CONFIRMATION_MSG))
        # time.sleep(2)
        assert self.is_elem_displayed(self.PAYMENT_CONFIRMATION_MSG) and self.read_txt(self.PAYMENT_CONFIRMATION_MSG) == confirmation_msg

    def click_confirm_btn(self):
        self.click_elem(self.BTN_CONFIRM)

    def check_invoice_msg(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.INVOICE_MSG))
        assert self.is_elem_displayed(self.INVOICE_MSG)

    def click_dropdown_menu(self):
        self.click_elem(self.BTN_USER_DROPDOWN)

    def click_my_invoices_btn(self):
        self.click_elem(self.BTN_INVOICES)

    def click_details_btn(self):
        self.click_elem(self.BTN_DETAILS)

    def click_download_btn(self):
        download_pdf = self.driver.find_element(*self.BTN_DOWNLOAD_PDF)
        action = ActionChains(self.driver)
        action.move_to_element(download_pdf)
        action.click().perform()

    def check_if_user_is_logged_in(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.BTN_USER_DROPDOWN))
        assert self.is_elem_displayed(self.BTN_USER_DROPDOWN)

    def sign_out(self):
        self.click_elem(self.BTN_USER_DROPDOWN)
        self.click_elem(self.BTN_SIGN_OUT)

    def is_sign_in_btn_displayed(self):
        assert self.is_elem_displayed(self.BTN_SIGN_IN)
