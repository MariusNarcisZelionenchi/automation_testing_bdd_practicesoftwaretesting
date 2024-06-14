from behave import *


@given('I am on the <<Home>> page')
def step_impl(context):
    context.home_page_obj.navigate_to_home()


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
