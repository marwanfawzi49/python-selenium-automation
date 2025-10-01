from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class RightMenu(Page):
    SIGN_IN_PRIMARY_BTN = (By.XPATH, "//button[contains(., 'Sign in or create account')]")
    DRAWER_HEADING = (By.CSS_SELECTOR, "[data-test='modal-drawer-heading']")

    def verify_sign_in_heading(self):
        el = self.wait.until(EC.visibility_of_element_located(self.DRAWER_HEADING))
        assert "sign in" in el.text.lower(), f'Expected heading "Sign in", but got: {el.text}'

    def click_sign_in_from_menu(self):
        self.wait.until(EC.element_to_be_clickable(self.SIGN_IN_PRIMARY_BTN)).click()