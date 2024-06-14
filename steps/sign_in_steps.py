from behave import *


@given('I am on the <<Home>> page and I navigate to <<Sign In>> page')
def step_impl(context):
    context.sign_in_page_obj.navigate_to_sign_in_from_home()


@given('I am on the <<Sign In>> page')
def step_impl(context):
    context.sign_in_page_obj.navigate_to_sign_in()


@then('The <<Sign In>> page loads')
def step_impl(context):
    context.sign_in_page_obj.check_url_sign_in()


@when('I insert "{email}" in the email field')
def step_impl(context, email):
    context.sign_in_page_obj.insert_invalid_credentials(email)


@when('I insert "{password}" in the password field')
def step_impl(context, password):
    context.sign_in_page_obj.insert_password(password)


@when('I insert "{email}" as username and "{password}" as password')
def step_impl(context, email, password):
    context.sign_in_page_obj.insert_invalid_credentials(email)
    context.sign_in_page_obj.insert_password(password)


@then('I cannot login with the "{email}" and "{password}" into the account and i receive "{email_err}" error')
def step_impl(context, email, password, email_err):
    context.sign_in_page_obj.insert_invalid_credentials(email, password, email_err)


@when('I click the <<Login>> button')
def step_impl(context):
    context.sign_in_page_obj.click_login()


@then('The email error message is displayed. The email error message is "{email_err}"')
def step_impl(context, email_err):
    context.sign_in_page_obj.check_email_err_msg(email_err)


@then('The credentials error message appears. The credentials error message is "{credentials_err}"')
def step_impl(context, credentials_err):
    context.sign_in_page_obj.check_credentials_err(credentials_err)


@when('I insert "{email}" in the email field and a 1 or 2 characters password in the password field')
def step_impl(context, email):
    context.sign_in_page_obj.insert_too_short_password(email)


@then('The password error message appears. The password error message is "{password_err}"')
def step_impl(context, password_err):
    context.sign_in_page_obj.check_password_err_msg(password_err)


@then('Clear input')
def step_impl(context):
    context.sign_in_page_obj.clear_fields()


@then('The <<Account>> page loads')
def step_impl(context):
    context.sign_in_page_obj.check_url_account()


@when('I click on the <<Register Your Account>> button')
def step_impl(context):
    context.sign_in_page_obj.click_register_new_account_btn()


@then('The <<Register>> page loads')
def step_impl(context):
    context.sign_in_page_obj.check_url_register()


@when('I input "{prenume}" as <<First Name>>')
def step_impl(context, prenume):
    context.sign_in_page_obj.input_first_name(prenume)


@when('I input "{nume}" as <<Last Name>>')
def step_impl(context, nume):
    context.sign_in_page_obj.input_last_name(nume)


@when('I input "{data_nasterii}" as <<DateOfBirth>>')
def step_impl(context, data_nasterii):
    context.sign_in_page_obj.input_dob(data_nasterii)


@when('I input "{adresa}" as <<Address>>')
def step_impl(context, adresa):
    context.sign_in_page_obj.input_address(adresa)


@when('I input "{cod_postal}" as <<Postal Code>>')
def step_impl(context, cod_postal):
    context.sign_in_page_obj.input_post_code(cod_postal)


@when('I input "{oras}" as <<City>>')
def step_impl(context, oras):
    context.sign_in_page_obj.input_city(oras)


@when('I input "{judet}" as <<State>>')
def step_impl(context, judet):
    context.sign_in_page_obj.input_state(judet)


@when('I input "{tara}" as <<Country>>')
def step_impl(context, tara):
    context.sign_in_page_obj.input_country(tara)


@when('I input "{telefon}" as <<Phone>>')
def step_impl(context, telefon):
    context.sign_in_page_obj.input_phone(telefon)


@when('I input the <<Email Address>>')
def step_impl(context):
    context.sign_in_page_obj.input_random_email()


@when('I input the <<Password>>')
def step_impl(context):
    context.sign_in_page_obj.input_random_password()


@when('I input a fake <<First Name>>')
def step_impl(context):
    context.sign_in_page_obj.input_fake_first_name()


@when('I input a fake <<Last Name>>')
def step_impl(context):
    context.sign_in_page_obj.input_fake_last_name()


@when('I input a fake <<Address>>')
def step_impl(context):
    context.sign_in_page_obj.input_fake_address()


@when('I input a fake <<Postal Code>>')
def step_impl(context):
    context.sign_in_page_obj.input_fake_postal_code()


@when('I input a fake <<City>>')
def step_impl(context):
    context.sign_in_page_obj.input_fake_city()


@when('I input a fake <<State>>')
def step_impl(context):
    context.sign_in_page_obj.input_fake_state()


@when('I input a fake <<Phone>>')
def step_impl(context):
    context.sign_in_page_obj.input_fake_phone()


@when('I input a fake <<Email Address>>')
def step_impl(context):
    context.sign_in_page_obj.input_fake_email()


@when('I input a fake <<Password>>')
def step_impl(context):
    context.sign_in_page_obj.input_fake_password()


@when('I fill in the required info')
def step_impl(context):
    context.sign_in_page_obj.fill_form()


@when('I click on the <<Register>> button')
def step_impl(context):
    context.sign_in_page_obj.click_register_btn()


@when('I insert the registered email and the registered password')
def step_impl(context):
    context.sign_in_page_obj.insert_registered_email_and_password()


@when('I insert the fake registered email and the fake registered password')
def step_impl(context):
    context.sign_in_page_obj.insert_registered_fake_email_and_password()


@when('I sign out')
def step_impl(context):
    context.sign_in_page_obj.sign_out()


@then('The <<Home>> page loads')
def step_impl(context):
    context.sign_in_page_obj.navigate_to_home()
