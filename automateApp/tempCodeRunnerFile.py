from appium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.chrome.options import Options

# Set up Chrome options
chrome_options = Options()
chrome_options.add_experimental_option('w3c', True)

# Desired Capabilities
desired_caps = {
    "appium:platformName": "Android",
    "appium:platformVersion": "12.0",  # e.g., "12.0"
    "appium:deviceName": "OnePlus Nord",         # e.g., "Pixel_5"
    "appium:automationName": "UiAutomator2",        # Use UiAutomator2 for Android
    "browserName": "Chrome",                 # Use Chrome browser for automation
    "appium:chromedriverExecutable": "C:\\Users\\Sidhartha Garg\\Desktop\\automateApp\\chromedriver.exe",  # Path to ChromeDriver
    "appium:noReset": True                          # Prevent resetting app state
}

# Connect to Appium Server
# Connect to Appium Server
desired_caps.update(chrome_options.to_capabilities())
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
# Open the Website
driver.get("http://34.131.13.37/")

# Wait for Playback Time (Adjust as needed)
sleep(30)

# Find and Click the QoE Report Download Button
download_button = driver.find_element(By.XPATH, "//button[text()='Download QoE Report (CSV)']")
download_button.click()

# Wait for the Download to Complete
sleep(5)

# Close the Browser
driver.quit()
