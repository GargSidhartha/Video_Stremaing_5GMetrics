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
