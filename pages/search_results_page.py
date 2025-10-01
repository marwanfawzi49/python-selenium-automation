from selenium.webdriver.common.by import By

from pages.base_page import Page

class SearchResultsPage(Page):
    SEARCH_RESULTS_TXT = (By.XPATH, "//div[@data-test='lp-resultsCount']")

    def verify_search_results(self, product):
        self.verify_partial_text(product,*self.SEARCH_RESULTS_TXT)

    def verify_product_url(self,product):
        #self.verify_url(f'https://www.target.com/s?searchTerm={product}')
        self.verify_partial_url(f'searchTerm={product}')