from behave import *


@given('I am on the <<Home>> page')
def step_impl(context):
    context.home_page_obj.navigate_to_home()


@when('I click the <<Contact>> button')
def step_impl(context):
    context.home_page_obj.click_contact_btn()


@when('I insert "{first_name}" as first name, "{last_name}" as last name and "{email}" as email')
def step_impl(context, first_name, last_name, email):
    context.home_page_obj.input_info(first_name, last_name, email)


@when('I select a subject')
def step_impl(context):
    context.home_page_obj.select_subject()


@when('I insert "{text}" as message')
def step_impl(context, text):
    context.home_page_obj.insert_msg(text)

@when('I choose a file to upload')
def step_impl(context):
    context.home_page_obj.choose_file_to_upload()


@when('I click <<Send>>')
def step_impl(context):
    context.home_page_obj.click_send(context)


@then('The "{msg}" message is displayed')
def step_impl(context, msg):
    context.home_page_obj.is_contact_msg_displayed(msg)


@when('I select "{product}" category')
def step_impl(context, product):
    context.home_page_obj.select_product(product)


@when('I click the <<Sort By>> arrow and I click the 3rd option')
def step_impl(context):
    context.home_page_obj.sort_products_by_price()


@then('The products are reordered')
def step_impl(context):
    context.home_page_obj.check_if_prices_are_reordered()


@when('I click on the max price and drag it to the left')
def step_impl(context):
    context.home_page_obj.modify_max_price()


@then('The page displays only products with a price lower than the new max price')
def step_impl(context):
    context.home_page_obj.check_if_prices_are_lower_than_max_price()
