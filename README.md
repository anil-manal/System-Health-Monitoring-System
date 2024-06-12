# System Health Monitoring System

## Overview

This project aims to develop a script that monitors the health of a Linux system. It checks various metrics such as CPU usage, memory usage, disk space, and running processes. If any of these metrics exceed predefined thresholds (e.g., CPU usage > 80%), the script sends an alert to the console or a log file.

## Features

- **CPU Usage Monitoring:** Monitors CPU usage and triggers alerts if it exceeds a predefined threshold.
- **Memory Usage Monitoring:** Monitors memory usage and triggers alerts if it exceeds a predefined threshold.
- **Disk Space Monitoring:** Monitors disk space usage and triggers alerts if it exceeds a predefined threshold.
- **Running Processes Monitoring:** Monitors running processes and triggers alerts if any process exceeds a predefined CPU usage threshold.

## Getting Started

To use this system health monitoring script locally, follow these steps:

1. Clone the repository to your local machine.
2. Install the required dependencies using `pip install Flask psutil`.
3. Run the Flask application using `python app.py`.
4. Open your web browser and navigate to [http://127.0.0.1:5000](http://127.0.0.1:5000) to access the system health monitoring dashboard.

## Deployment

This project is deployed on PythonAnywhere. You can access the live version of the system health monitoring application at the following URL:
[https://anilmanal001.pythonanywhere.com/](https://anilmanal001.pythonanywhere.com/)

## Project Structure

The project structure is organized as follows:

- **app.py:** Contains the Flask application code.
- **templates:** Directory containing HTML templates for the web interface.
  - **index.html:** Homepage template.
  - **system_health.html:** System health information template.
  - **running_processes.html:** Running processes information template.

## Usage

- **Homepage:** The homepage provides options to check system health and view running processes.
- **System Health Page:** Displays CPU usage, memory usage, and disk usage information with colored bars indicating the usage levels.
- **Running Processes Page:** Displays a table of running processes with details such as process name, memory usage, and CPU usage.
