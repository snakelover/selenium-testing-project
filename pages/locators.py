from selenium.webdriver.common.by import By


class MainPageLocators(object):
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators(object):
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators(object):
    ADD_TO_THE_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    NAME_IN_MESSAGE_OF_SUCCESFUL_ADDITION = (By.CSS_SELECTOR, "#messages .alert:nth-child(1) > .alertinner strong")
    PRICE_OF_THE_CART = (By.CSS_SELECTOR, "#messages .alert:nth-last-child(1) .alertinner strong")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main p")
