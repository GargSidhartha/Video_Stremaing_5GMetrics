# Video_Stremaing_5GMetrics
This project provides a web-based tool for monitoring and analyzing the Quality of Experience (QoE) in Dynamic Adaptive Streaming over HTTP (DASH) video playback, along with an automation script for streamlined testing and data collection [1].

## Project Overview

This project is divided into two main parts:

1.  **Enhanced DASH Streaming Webpage:** A self-contained web tool that allows real-time monitoring and analysis of DASH video playback [2].
2.  **Automation Script:** A script designed to automate testing and evaluation of the DASH streaming webpage [3].

## Part 1: Enhanced DASH Streaming Webpage

### Key Features

*   **Real-Time Metrics Monitoring:**
    *   Average Bitrate: Tracks the average bitrate of the video stream in Mbps [2].
    *   Total Stall Time: Measures the cumulative time the video is buffering [2].
    *   Buffer Health: Displays the current buffer length in seconds [2].
    *   Quality Switches: Counts the number of quality changes during playback [4].
*   **Interactive Charts:**
    *   Bitrate Chart: Visualizes the bitrate changes over time [4].
    *   Buffer Chart: Tracks the buffer length fluctuations during playback [4].
*   **User Controls:**
    *   ABR Strategy Selection: Allows users to switch between different ABR strategies (BOLA, Dynamic, Throughput) [4].
    *   Bitrate Limits: Enables setting minimum and maximum bitrate thresholds for the video stream [4].
    *   Reset Metrics: Clears all collected data and resets the visualizations [4].
*   **Data Logging and Export:**
    *   Metrics Log: Displays a real-time log of all significant events (e.g., quality changes, buffer states) [5].
    *   CSV Report: Allows users to download a detailed report of all metrics in CSV format for further analysis [5].
*   **Dynamic Adaptation:** The tool dynamically adapts to changes in network conditions and user settings, providing insights into how different ABR strategies perform under varying constraints [5].

### Technical Implementation

*   **Frontend:** Built using HTML, CSS, and JavaScript [6].
    *   Utilizes the `dash.js` library for DASH video playback and ABR logic [6].
    *   Uses `Chart.js` for real-time visualization of bitrate and buffer data [6].
*   **Backend:** The webpage is self-contained and does not require a backend server. All metrics are calculated and logged client-side [6].
*   **Key Functionality:**
    *   Event listeners track video playback events (e.g., buffer empty, buffer loaded, quality changes) [6].
    *   Metrics are updated in real-time and displayed on the webpage [6].
    *   Users can interact with the tool to test different ABR strategies and bitrate limits [6].

## Part 2: Automation Script

### Key Features

*   **User-Friendly Configuration:**
    *   A Tkinter-based GUI allows users to input device details, ChromeDriver path, website URL, and playback time [3].
    *   Default values are provided for quick setup [7].
*   **Automated Playback and Reporting:**
    *   Automates video playback on the specified DASH streaming webpage [7].
    *   Waits for the video to play for the specified duration [7].
    *   Downloads the QoE report in CSV format for further analysis [7].
*   **Cross-Platform Compatibility:**
    *   Supports Android devices using the Chrome browser [7].
    *   Handles permissions and browser settings automatically [7].
*   **Error Handling:**
    *   Includes robust error handling to manage exceptions during automation [8].
    *   Displays user-friendly error messages using Tkinter message boxes [8].

### Technical Implementation

*   **Appium:** Used for mobile browser automation on Android devices [8].
    *   Configures desired capabilities for Chrome browser and device settings [8].
*   **Selenium:** Interacts with the webpage elements (e.g., video player, download button) [8].
    *   Waits for elements to load and ensures smooth automation [8].
*   **Tkinter:** Provides a graphical interface for user input and configuration [8].
    *   Displays success and error messages during the automation process [8].
*   **Key Functionality:**
    *   Initializes the Chrome browser on the specified Android device [9].
    *   Navigates to the DASH streaming webpage and starts video playback [9].
    *   Waits for the specified playback time and downloads the QoE report [9].
    *   Closes the browser and notifies the user upon completion [9].

## Part 3: Combined Workflow

### Step-by-Step Process

1.  **Set Up the Webpage:** Deploy the Enhanced DASH Streaming webpage on a server or localhost. Ensure the webpage is accessible via the specified URL [9].
2.  **Configure the Automation Script:** Run the automation script and input device details, ChromeDriver path, website URL, and playback time using the Tkinter GUI [10].
3.  **Run the Automation:** The script will open the Chrome browser on the specified Android device, navigate to the webpage, and start video playback. After the specified playback time, it will download the QoE report and notify the user [10].
4.  **Analyze Results:** Use the downloaded CSV report to analyze QoE metrics and evaluate the performance of the DASH streaming system [10].

## Getting Started

*   To use the Enhanced DASH Streaming Webpage, simply open the `index.html` file in a web browser, or deploy it on a web server.
*   To run the Automation Script, you will need to:
    *   Install Appium and Selenium.
    *   Download the appropriate ChromeDriver for your Chrome browser version.
    *   Ensure you have Python 3.x installed.
    *   Run the automation script (`main.py` or similar) to launch the configuration GUI.

## Step-by-Step Instructions for Setting Up the Environment and Dependencies

1. **Install Python 3.x:**
   - Download and install Python 3.x from the official website: https://www.python.org/downloads/
   - Ensure that Python is added to your system's PATH.

2. **Install Appium:**
   - Install Appium using npm (Node Package Manager). First, install Node.js from https://nodejs.org/
   - Open a terminal or command prompt and run the following command:
     ```
     npm install -g appium
     ```

3. **Install Appium-Python-Client:**
   - Install the Appium-Python-Client using pip:
     ```
     pip install Appium-Python-Client
     ```

4. **Install Selenium:**
   - Install the Selenium package using pip:
     ```
     pip install selenium
     ```

5. **Download ChromeDriver:**
   - Download the appropriate ChromeDriver for your Chrome browser version from: https://sites.google.com/a/chromium.org/chromedriver/downloads
   - Place the ChromeDriver executable in a known location on your system.

6. **Set Up the Enhanced DASH Streaming Webpage:**
   - Deploy the `index.html` file on a web server or open it directly in a web browser.

## Detailed Instructions for Running the Project

1. **Run the Automation Script:**
   - Navigate to the directory containing the automation script (`automateApp/auto.py`).
   - Open a terminal or command prompt and run the script:
     ```
     python auto.py
     ```

2. **Configure the Automation Script:**
   - A Tkinter GUI will appear, prompting you to enter the following details:
     - Device Name: Enter the name of your Android device (e.g., "OnePlus Nord").
     - ChromeDriver Path: Enter the path to the ChromeDriver executable (e.g., `C:\path\to\chromedriver.exe`).
     - Website URL: Enter the URL of the Enhanced DASH Streaming webpage (e.g., `http://localhost/index.html`).
     - Video Playback Time: Enter the duration for video playback in seconds (e.g., "30").

3. **Start the Automation:**
   - Click the "Start Automation" button in the Tkinter GUI.
   - The script will open the Chrome browser on the specified Android device, navigate to the webpage, and start video playback.
   - After the specified playback time, the script will download the QoE report and notify you upon completion.

## Troubleshooting

### Common Errors and Solutions

1. **Error: "Appium server is not running"**
   - Solution: Ensure that the Appium server is running. You can start the Appium server by running the following command in a terminal or command prompt:
     ```
     appium
     ```

2. **Error: "ChromeDriver executable needs to be available in the path"**
   - Solution: Ensure that the ChromeDriver executable is in the specified path. Verify the path entered in the Tkinter GUI and make sure it points to the correct location of the ChromeDriver executable.

3. **Error: "Device not found"**
   - Solution: Ensure that your Android device is connected to your computer and that USB debugging is enabled. You can check if the device is recognized by running the following command:
     ```
     adb devices
     ```

4. **Error: "Element not found"**
   - Solution: Ensure that the Enhanced DASH Streaming webpage is accessible and that the specified URL is correct. Verify that the webpage elements (e.g., video player, download button) are present and correctly identified in the script.

5. **Error: "Playback time is too short"**
   - Solution: Increase the video playback time in the Tkinter GUI to ensure that the video plays for a sufficient duration before attempting to download the QoE report.

6. **General Troubleshooting Tips:**
   - Check the terminal or command prompt for detailed error messages and stack traces.
   - Ensure that all dependencies (Python, Appium, Selenium, ChromeDriver) are installed and up to date.
   - Verify that the Enhanced DASH Streaming webpage is functioning correctly by opening it directly in a web browser.
