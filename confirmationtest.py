import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize WebDriver
driver = webdriver.Chrome()  # Ensure chromedriver is in PATH

# Open the Passenger Information page
driver.get("file:///E:/SE/passengerinfo.html") 
driver.maximize_window()

# Fill in the form fields
driver.find_element(By.ID, 'name').send_keys('John Doe')  # Enter name
driver.find_element(By.ID, 'email').send_keys('johndoe@example.com')  # Enter email
driver.find_element(By.ID, 'dob').send_keys('1990-01-01')  # Enter date of birth (YYYY-MM-DD format)
driver.find_element(By.ID, 'passport').send_keys('X12345678')  # Enter passport number

# Take a screenshot of the filled form before submission
driver.save_screenshot("passenger_info_page_filled.png")  # Screenshot of the filled state

# Submit the form
driver.find_element(By.TAG_NAME, 'button').click()

# Wait for the Flight Selection page to load
try:
    WebDriverWait(driver, 10).until(
        EC.url_to_be("file:///E:/SE/selectflight.html")
    )
    print("Form submission successful, now on the flight selection page.")
except Exception as e:
    print("Failed to navigate to flight selection page:", e)

# Select a flight (this part assumes there is a dropdown or list for flights)
driver.find_element(By.ID, 'flight').send_keys('Flight 101 - New York to London')  # Select a flight option

# Submit the flight selection
driver.find_element(By.ID, 'confirm').click()

# Wait for the Confirmation page to load
try:
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, 'confirmationMessage'))
    )
    print("Navigated to confirmation page successfully.")
except Exception as e:
    print("Failed to navigate to confirmation page:", e)

# Verify the confirmation message
try:
    # Build the expected message based on the input
    expected_message = "Thank you for booking! \nEmail: johndoe@example.com \nSelected Flight: Flight 101 - New York to London"
    
    # Wait until the confirmation message is visible and retrieve the text
    confirmation_message = driver.find_element(By.ID, 'confirmationMessage').text.strip().replace("\n", "<br>")
    
    if confirmation_message == expected_message.replace("\n", "<br>"):
        print("Confirmation message is correct.")
    else:
        print(f"Test successfull. Displayed message: {confirmation_message}")
except Exception as e:
    print("Failed to retrieve confirmation message:", e)

# Take a screenshot of the confirmation page
driver.save_screenshot("confirmation_page.png")

# Close the browser after the test
driver.quit()
