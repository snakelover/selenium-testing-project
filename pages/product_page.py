from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_the_basket(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_THE_BASKET_BUTTON)
        button.click()
