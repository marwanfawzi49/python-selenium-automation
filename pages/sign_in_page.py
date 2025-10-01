from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class SignInPage(Page):
    FORM_UNIQUE = (By.CSS_SELECTOR, "h1.styles_ndsHeading__HcGpD")


    def verify_sign_in_form_opened(self):
        el = self.wait.until(EC.visibility_of_element_located(self.FORM_UNIQUE))
        assert el is not None, "Sign In form did not open"
