from seleniumbase import Driver


class Browser:
    driver = Driver()
    # service = Service(GeckoDriverManager().install())
    # driver = webdriver.Firefox(service=service)
    driver.maximize_window()
    driver.implicitly_wait(1)

    def close_browser(self):
        self.driver.quit()
