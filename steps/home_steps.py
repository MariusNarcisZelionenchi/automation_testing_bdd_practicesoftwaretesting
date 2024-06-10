from behave import *


@given('I am on the <<Home>> page')
def step_impl(context):
    context.home_page_obj.navigate_to_home()


@when('I click on the <<Sign In>> button')
def step_impl(context):
    context.home_page_obj.click_sign_in()


@then('The <<Sign In>> page loads')
def step_impl(context):
    context.home_page_obj.check_url_sign_in()
