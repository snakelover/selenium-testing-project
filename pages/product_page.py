from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_the_cart(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_THE_BASKET_BUTTON)
        button.click()

    def should_be_success_of_addition_message(self):
        name_from_message = self.browser.find_element(*ProductPageLocators.NAME_IN_MESSAGE_OF_SUCCESFUL_ADDITION).text
        # print("name_from_message= ", name_from_message)
        assert name_from_message == self.get_product_name(), "Name of product in the message is not the same as the actual product name"

    def should_be_the_right_price_of_the_cart(self):
        price_of_the_cart = self.browser.find_element(*ProductPageLocators.PRICE_OF_THE_CART).text
        assert price_of_the_cart == self.get_product_price(), "Price of product in the cart is not the same as the actual product price"

    def get_product_name(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        # print("product_name = ", product_name)
        return product_name

    def get_product_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        return product_price
