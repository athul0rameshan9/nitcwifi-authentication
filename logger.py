from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd

# Initialize the Chrome WebDriver
driver = webdriver.Chrome()

# Open the login page
driver.get('http://172.16.16.1:1000/login?5723b4f0c234a97f')

# Locate the username and password fields
username_field = driver.find_element(By.NAME, "username")
password_field = driver.find_element(By.NAME, "password")

#the loop starts here
name = "athl_b**0**0**"#place your username here
password = "******"#place your password here





# Enter your login credentials
username_field.send_keys(name)
password_field.send_keys(password)

# Submit the form
password_field.send_keys(Keys.RETURN)

# Wait for the login process to complete
time.sleep(2)

while True:
    time.sleep(1)



#code to logout
"""
try:
    time.sleep(2) 
    logout_link = driver.find_element(By.LINK_TEXT, "logout")
    logout_link.click()
    time.sleep(2)  # Wait for the logout process to complete
    print("Logout successful!")
except Exception as e:
    print("Logout failed:", e)
    driver.back()
"""

# Close the browser

