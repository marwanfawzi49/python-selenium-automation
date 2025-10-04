
from pages.base_page import Page
from pages.cart_page import CartPage
from pages.header import Header
from pages.main_page import MainPage
from pages.right_menu import RightMenu
from pages.search_results_page import SearchResultsPage
from pages.sign_in_page import SignInPage
from pages.target_app_page import TargetAppPage
from pages.privacy_policy_page import PrivacyPolicyPage

class Application:

    def __init__(self,driver):
        self.driver = driver

        self.page = Page(driver)
        self.header = Header(driver)
        self.main_page = MainPage(driver)
        self.search_results_page = SearchResultsPage(driver)
        self.cart_page = CartPage(driver)
        self.right_menu = RightMenu(driver)
        self.sign_in_page = SignInPage(driver)
        self.privacy_policy_page = PrivacyPolicyPage(driver)
        self.target_app_page = TargetAppPage(driver)
        self.search_results_page = SearchResultsPage(driver)