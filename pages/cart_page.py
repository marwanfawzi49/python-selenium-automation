from selenium.webdriver.common.by import By

from pages.base_page import Page


class CartPage(Page):
    CART_EMPTY_MSG = (By.CSS_SELECTOR, '[data-test="boxEmptyMsg"]')

    def verify_cart_empty_msg(self):
        expected_text = 'Your cart is empty'
        self.verify_text('Your cart is empty', *CartPage.CART_EMPTY_MSG)