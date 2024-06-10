from browser import Browser
from pages.account_page import AccountPage
from pages.home_page import HomePage
from pages.sign_in_page import SignInPage


def before_all(context):
    context.browser = Browser()
    context.home_page_obj = HomePage()
    context.sign_in_page_obj = SignInPage()
    context.account_page_obj = AccountPage()


def before_feature(context, feature):
    if "skip" in feature.tags:
        feature.skip("Marked with @skip")
        return


def before_scenario(context, scenario):
    if "skip" in scenario.effective_tags:
        scenario.skip("Marked with @skip")
        return


def after_all(context):
    context.browser.close_browser()
