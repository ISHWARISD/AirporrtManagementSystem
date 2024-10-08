import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize WebDriver
driver = webdriver.Chrome()  # Ensure chromedriver is in PATH

# Open the Passenger Information page
driver.get("file:///E:/SE/passengerinfo.html") 
driver.save_screenshot("passenger_info_page_initial.png")  # Screenshot of the initial state

# Maximize the browser window
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

# Wait for the next page to load (Flight Selection page)
try:
    WebDriverWait(driver, 10).until(
        EC.url_to_be("file:///E:/SE/selectflight.html")  # Use the exact URL of your flight selection page
    )
    print("Form submission successful, now on the flight selection page.")
except Exception as e:
    print("Failed to navigate to flight selection page:", e)

# Now try to verify if the email is correctly displayed on the flight selection page
try:
    email_displayed = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, 'emailDisplay'))
    ).text

    if email_displayed == "johndoe@example.com":
        print("Email correctly displayed on flight selection page.")
    else:
        print(f"Test failed. Displayed email: {email_displayed}")
except Exception as e:
    print("Failed to retrieve displayed email:", e)

# Optionally, you can also verify specific elements on the new page
try:
    flight_selection = driver.find_element(By.ID, 'flight')
    print("Flight selection dropdown found. Test passed.")
except Exception as e:
    print("Test failed:", e)

# Add a delay to allow time for taking a screenshot of the flight selection page
time.sleep(5)  # Sleep for 5 seconds

# Take a screenshot of the flight selection page
driver.save_screenshot("flight_selection_page.png")

# Close the browser after the test
driver.quit()
