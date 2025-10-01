from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support import expected_conditions as EC


from pages.base_page import Page


class Header(Page):
    SEARCH_FIELD = (By.ID, 'search')
    SEARCH_BTN = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")
    CART_ICON = (By.CSS_SELECTOR, '[data-test="@web/CartLink"]')
    ACCOUNT_ICON = (By.XPATH, "//span[text()='Account']")

    def search_product(self, search_word):
        self.input_text(search_word, *self.SEARCH_FIELD)
        self.click(*self.SEARCH_BTN)
        sleep(9)

    def click_cart(self):
        self.wait_until_clickable_click(*self.CART_ICON)

    def click_sign_in(self):
        self.click(*self.ACCOUNT_ICON)

    def click_account(self):
        # wait for the Account icon to be clickable, then click
        self.wait.until(EC.element_to_be_clickable(self.ACCOUNT_ICON)).click()