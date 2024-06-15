import random
import string
#
#
#
#
# # printez o litera random
# l = random.choice(string.ascii_letters)
# print(l)
#
# # generez o parola random
# password = ''
# for i in range(2):
#     character = random.choice(string.ascii_letters)
#     password += character
#     print(password)
#
#
# # explicit wait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
#
# # WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.ID, 'locator'))
#
#
# my_list = [1, 'list_elem', False, 1]
# print(my_list, type(my_list))
# #OUTPUT: [1, 'list_elem', False, 1] <class 'list'>
#
#
# my_set = {1, 'set_elem', False, 1}
# print(my_set, type(my_set))
# #OUTPUT: {False, 1, 'set_elem'} <class 'set'>
#
#
# my_tuple = (1, 'tuple_elem', False, 1)
# print(my_tuple, type(my_tuple))
# #OUTPUT: (1, 'tuple_elem', False, 1) <class 'tuple'>
#
#
# my_dict = {1: 'dict_elem_1', 2: 'dict_elem_2'}
# print(my_dict, type(my_dict))
# #OUTPUT: {1: 'dict_elem_1', 2: 'dict_elem_2'} <class 'dict'>
#
#
# class PaymentProcessor:
#     def process_payment(self, amount, payment_method):
#         if payment_method == "credit_card":
#             return self.process_credit_card(amount)
#         elif payment_method == "paypal":
#             return self.process_paypal(amount)
#         elif payment_method == "apple_pay":
#             return self.process_apple_pay(amount)
#         elif payment_method == "google_pay":
#             return self.process_google_pay(amount)
#         elif payment_method == "cryptocurrency":
#             return self.process_crypto(amount)
#         else:
#             return "Invalid payment method"
#
#     def process_credit_card(self, amount):
#         # Logic for processing credit card payment
#         return f"Processed credit card payment of ${amount}"
#
#     def process_paypal(self, amount):
#         # Logic for processing PayPal payment
#         return f"Processed PayPal payment of ${amount}"
#
#     def process_apple_pay(self, amount):
#         # Logic for processing Apple Pay payment
#         return f"Processed Apple Pay payment of ${amount}"
#
#     def process_google_pay(self, amount):
#         # Logic for processing Google Pay payment
#         return f"Processed Google Pay payment of ${amount}"
#
#     def process_crypto(self, amount):
#         # Logic for processing cryptocurrency payment
#         return f"Processed cryptocurrency payment of ${amount}"
#
# # Test different payment methods
# payment_processor = PaymentProcessor()
# amount = 100
#
# print(payment_processor.process_payment(amount, "credit_card"))
# print(payment_processor.process_payment(amount, "paypal"))
# print(payment_processor.process_payment(amount, "apple_pay"))
# print(payment_processor.process_payment(amount, "google_pay"))
# print(payment_processor.process_payment(amount, "cryptocurrency"))
# print(payment_processor.process_payment(amount, "invalid_method"))
#
#
# # functie pentru introdus toate datele:
#
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#
# def fill_form(url):
#     # Initialize the WebDriver (make sure chromedriver is in your PATH)
#     driver = webdriver.Chrome()
#     form_data = {
#         "username": "my_username",
#         "password": "my_password",
#         "email": "my_email@email.com"
#     }
#     try:
#         # Open the webpage
#         driver.get(url)
#
#         # Wait for the page to load
#         WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
#
#         # Loop through the form data dictionary and fill in the form
#         for field_name, value in form_data.items():
#             try:
#                 # Find the input field by name attribute and fill it
#                 input_element = WebDriverWait(driver, 10).until(
#                     EC.presence_of_element_located((By.NAME, field_name))
#                 )
#                 input_element.clear()  # Clear any pre-filled data
#                 input_element.send_keys(value)
#             except Exception as e:
#                 print(f"Could not fill in the field {field_name}: {e}")
#
#         # Optionally, submit the form if there's a submit button
#         try:
#             submit_button = WebDriverWait(driver, 10).until(
#                 EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))
#             )
#             submit_button.click()
#         except Exception as e:
#             print(f"Could not click the submit button: {e}")
#
#     finally:
#         # Close the browser after a delay to see the result (remove sleep in production)
#         import time
#         time.sleep(5)
#         driver.quit()
#
# # Example usage
# url = "http://example.com/form-page"
# form_data = {
#     "username": "your_username",
#     "password": "your_password",
#     "email": "your_email@example.com"
    # Add more fields as necessary
# }

# set1 = {'aa', 'bb', 'cc'}
# set2 = ['bb', 'cc', 'aa']
# assert set1 == set2


from seleniumbase import Driver
from selenium.webdriver.support.ui import Select

driver = Driver()
driver.get('https://practicesoftwaretesting.com/#/')
PRODUCT_PRICE = (By.XPATH, '//span[@data-test="product-price"]')
BTN_SORT_BY = (By.CLASS_NAME, 'form-select')
def sort_products_by_price(self):
    sort = Select(self.identify_elem(self.BTN_SORT_BY))
    sort.select_by_visible_text('Price (High - Low)')
def check_if_prices_are_reordered(self):
    products_price_list = []
    product_price = float(self.read_txt(self.PRODUCT_PRICE)[1:])
    products_price_list.append(product_price)
    ordered_products_price_list = sorted(products_price_list)
    assert products_price_list == ordered_products_price_list
    print(products_price_list, ordered_products_price_list)

    pass