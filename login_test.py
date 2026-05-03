# Automated Login Test using Selenium

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Open browser
driver = webdriver.Chrome()

# Open demo login page
driver.get("https://the-internet.herokuapp.com/login")

# Maximize window
driver.maximize_window()

# -------------------------
# Test Case 1: Valid Login
# -------------------------
username = driver.find_element(By.ID, "username")
password = driver.find_element(By.ID, "password")

username.send_keys("tomsmith")
password.send_keys("SuperSecretPassword!")

driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
time.sleep(2)

print("Valid Login Test Executed")

driver.back()

# -------------------------
# Test Case 2: Invalid Login
# -------------------------
username = driver.find_element(By.ID, "username")
password = driver.find_element(By.ID, "password")

username.send_keys("wronguser")
password.send_keys("wrongpass")

driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
time.sleep(2)

print("Invalid Login Test Executed")

driver.back()

# -------------------------
# Test Case 3: Empty Fields
# -------------------------
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
time.sleep(2)

print("Empty Field Test Executed")

# Close browser
driver.quit()
