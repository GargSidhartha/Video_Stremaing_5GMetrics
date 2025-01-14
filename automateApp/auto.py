from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import tkinter as tk
from tkinter import messagebox, ttk
import os
from appium.options.android import UiAutomator2Options

def get_device_info():
    root = tk.Tk()
    root.title("Video QoE Automation Setup")
    root.geometry("400x500")
    
    # Create and pack widgets
    tk.Label(root, text="Device Setup", font=('Arial', 14, 'bold')).pack(pady=10)
    
    # Device Name
    tk.Label(root, text="Device Name:").pack(pady=5)
    device_name = tk.Entry(root)
    device_name.insert(0, "OnePlus Nord")  # Default value
    device_name.pack()
    
    # ChromeDriver Path
    tk.Label(root, text="ChromeDriver Path:").pack(pady=5)
    chromedriver_path = tk.Entry(root)
    chromedriver_path.insert(0, r"C:\Users\Sidhartha Garg\Desktop\automateApp\chromedriver.exe")
    chromedriver_path.pack()
    
    # Website URL
    tk.Label(root, text="Website URL:").pack(pady=5)
    website_url = tk.Entry(root)
    website_url.insert(0, "http://34.131.13.37/")
    website_url.pack()
    
    # Playback Time
    tk.Label(root, text="Video Playback Time (seconds):").pack(pady=5)
    playback_time = tk.Entry(root)
    playback_time.insert(0, "30")
    playback_time.pack()
    
    # Store the values
    values = {}
    
    def on_submit():
        values.update({
            'device_name': device_name.get(),
            'chromedriver_path': chromedriver_path.get(),
            'website_url': website_url.get(),
            'playback_time': int(playback_time.get())
        })
        root.destroy()
    
    # Submit button
    tk.Button(root, text="Start Automation", command=on_submit).pack(pady=20)
    
    # Center the window
    root.eval('tk::PlaceWindow . center')
    
    root.mainloop()
    return values

def run_automation(config):
    # Desired Capabilities
    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.device_name = config['device_name']
    options.automation_name = "UiAutomator2"
    options.browser_name = "Chrome"

    # Add ChromeDriver path and version-specific options
    options.set_capability("appium:chromedriverExecutable", config['chromedriver_path'])
    options.set_capability("appium:chromeOptions", {
        "w3c": True,
        "args": [
            "--no-first-run",
            "--disable-popup-blocking",
            "--disable-notifications",
            "--start-maximized"
        ],
        "androidKeepAppDataDir": True,
        "androidPackage": "com.android.chrome"
    })

    # Add these capabilities to handle permissions
    options.set_capability("appium:noReset", True)
    options.set_capability("appium:fullReset", False)
    options.set_capability("appium:dontStopAppOnReset", True)
    options.set_capability("appium:newCommandTimeout", 120)
    options.set_capability("appium:ignoreHiddenApiPolicyError", True)
    options.set_capability("appium:autoGrantPermissions", True)
    options.set_capability("appium:skipDeviceInitialization", True)
    options.set_capability("appium:skipServerInstallation", True)
    options.set_capability("appium:enforceAppInstall", False)
    options.set_capability("appium:clearSystemFiles", False)
    options.set_capability("appium:clearDeviceLogsOnStart", False)

    try:
        # Initialize Appium Driver
        driver = webdriver.Remote('http://127.0.0.1:4723', options=options)
        
        # Open the Website
        driver.get(config['website_url'])
        
        # Wait for video element to be present
        video = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "video"))
        )
        
        # Click on video to start playback
        video.click()
        
        # Wait for video to complete
        sleep(config['playback_time'])

        # Find and Click the QoE Report Download Button
        download_button = driver.find_element(By.XPATH, "//button[text()='Download QoE Report (CSV)']")
        download_button.click()

        # Wait for the Download to Complete
        sleep(5)
        messagebox.showinfo("Success", "Video playback and QoE report download completed successfully!")

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")
    
    finally:
        # Close the Browser
        driver.quit()

if __name__ == "__main__":
    # Get configuration from user
    config = get_device_info()
    
    # Run the automation with the provided config
    if config:
        run_automation(config)
