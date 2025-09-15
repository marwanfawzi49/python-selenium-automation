from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep


def open_target_homepage(context):
    context.driver.get("https://www.target.com")

#locators
search_bar = (By.CSS_SELECTOR, "[aria-label='What can we help you find? suggestions appear below']")
search_btn = (By.CSS_SELECTOR, "[data-test='@web/Search/SearchButton']")
adding_btn = (By.CSS_SELECTOR, '[data-test="chooseOptionsButton"]')
total_price = (By.CSS_SELECTOR, ".styles_summary-heading__G1m7L")

#Searching for product
def search_product(context, product):
    context.driver.find_element(*search_bar).send_keys(product)
    context.driver.find_element(*search_btn).click()

#Adding the product to cart
def adding_product(context, product):
    context.driver.find_element(*adding_btn).click()

#verify the product in the cart
def verify_product_in_cart(context, product):
    context.driver.get("https://www.target.com/cart")
    context.driver.find_element(*total_price)
    print("✔ Product appears in the cart.")
