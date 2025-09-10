from itertools import product
from behave import given, when, then
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

driver_path = ChromeDriverManager().install()

service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

@given("open Target homepage")
def open_target_homepage(context):
    context.driver.get("https://www.target.com")

#locator:
search_bar = (By.CSS_SELECTOR, "[aria-label='What can we help you find? suggestions appear below']")
search_btn = (By.CSS_SELECTOR, "[data-test='@web/Search/SearchButton']")
search_result_text = (By.CSS_SELECTOR, "span.h-text-bs.h-display-flex.h-flex-align-center.h-text-grayDark")


@when("search for {product}")
def search_product(context, product):
    context.driver.find_element(*search_bar).send_keys(product)
    context.driver.find_element(*search_btn).click()

@then("see result for {product}")
def search_result(context, product):
    result_text = context.driver.find_element(*search_result_text).text
    assert product in result_text, f" Expected {product} in result text, but got {result_text}"





driver.quit()








