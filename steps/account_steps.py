from behave import *


@given('I am on the <<Account>> page')
def step_impl(context):
    context.account_page_obj.navigate_to_account()


@when('I click on the <<Logo>>')
def step_impl(context):
    context.account_page_obj.click_logo()


@when('I click on the <<Search>> field, I type in "{item}" and I click the <<Search>> button')
def step_impl(context, item):
    context.account_page_obj.search(item)


@when('I click on the 2nd product')
def step_impl(context):
    context.account_page_obj.choose_item()


@when('I click on the <<Add to cart>> button')
def step_impl(context):
    context.account_page_obj.click_add_to_cart()


@then('<<The product being added to the shopping card>> message is displayed')
def step_impl(context):
    context.account_page_obj.is_item_added_msg_displayed()


@then('The number of products is displayed on the shopping cart')
def step_impl(context):
    context.account_page_obj.is_total_of_products_displayed()


@then('The number of products is correct')
def step_impl(context):
    context.account_page_obj.check_number_of_items()


@when('I click on the <<Shopping Cart>>')
def step_impl(context):
    context.account_page_obj.click_cart()


@when('I click on the quantity, delete the amount, increase the amount by 1 and hit enter')
def step_impl(context):
    context.account_page_obj.set_new_amount()


@then('New <<Total Unit Price>> is "{factor}" times the <<Unit Price>>')
def step_impl(context, factor):
    context.account_page_obj.check_total_unit_price(factor)


@when('I click on <<Proceed to checkout>> 1st button')
def step_impl(context):
    context.account_page_obj.click_proceed_1()


@then('The <<Proceed to checkout>> message is displayed')
def step_impl(context):
    assert context.account_page_obj.is_proceed_msg_displayed()


@when('I click on <<Proceed to checkout>> 2nd button')
def step_impl(context):
    context.account_page_obj.click_proceed_2()


@then('The address, city, state, country and postal code are displayed')
def step_impl(context):
    assert context.account_page_obj.is_info_displayed()


@when('I click on <<Proceed to checkout>> 3rd button')
def step_impl(context):
    context.account_page_obj.click_proceed_3()


@then('Payment method is requested')
def step_impl(context):
    context.account_page_obj.is_payment_msg_displayed()
