from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep





@then("Verify 'Your cart is empty' message is shown")
def verify_empty_cart_msg(context):
     context.app.cart_page.verify_cart_empty_msg()