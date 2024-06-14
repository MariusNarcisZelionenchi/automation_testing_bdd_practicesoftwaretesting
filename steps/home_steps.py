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