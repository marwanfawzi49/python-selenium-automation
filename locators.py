from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

create_account = driver.find_element(By.CSS_SELECTOR, "h1.flex--item.fs-headline1.fw-bold.lh-xs.mb8.ws-nowrap")
terms_of_service = driver.find_element(By.CSS_SELECTOR,".flex--item.js-terms.fs-caption.fc-black-400.ta-left" )
email_field = driver.find_element(By.CSS_SELECTOR, "#email")
password_field = driver.find_element(By.CSS_SELECTOR, "#password")
password_icon = driver.find_elements(By.CSS_SELECTOR, '[class*="password"][class*="svg-icon"]')
sign_up = driver.find_element(By.XPATH, "//button[text()='Sign up']")
using_google_email = driver.find_element(By.CSS_SELECTOR, '[data-provider="google"]')
using_github = driver.find_element(By.CSS_SELECTOR, '[data-provider="github"]')
stack_overflow = driver.find_element(By.XPATH, "//a[text()='Get Stack Overflow for Teams free for up to 50 users']")
