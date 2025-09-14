from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# Set up the driver
driver_path = ChromeDriverManager().install()
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# Locator
target_circle = (By.XPATH,"[class='cell-item-content']")





# Use driver directly inside the function
def open_target_homepage(driver):
    driver.get("https://www.target.com")
    driver.find_element(*target_circle).click()



#verify:
assert driver.find_elements(*target_circle), "Heading not found"


sleep(10)  # Pause to see the result
driver.quit()
