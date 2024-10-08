# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time

# driver = webdriver.Chrome()

# driver.get('file:')

# # Successful Login
# driver.find_element(By.ID, "username").send_keys("valid_username")
# driver.find_element(By.ID, "password").send_keys("valid_password")
# driver.find_element(By.ID, "login_button").click()
# assert "Welcome, valid_username" in driver.page_source

# # Unsuccessful Login
# driver.find_element(By.ID, "username").send_keys("invalid_username")
# driver.find_element(By.ID, "password").send_keys("invalid_password")
# driver.find_element(By.ID, "login_button").click()
# assert "Invalid username or password" in driver.page_source

# driver.quit()

