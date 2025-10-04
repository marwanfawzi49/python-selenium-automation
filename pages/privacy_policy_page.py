from pages.base_page import Page
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PrivacyPolicyPage(Page):

    def verify_pp_opened(self):
        self.wait_until_url_contains('target-privacy-policy')