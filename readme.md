Video Downloading Script Using yt-dlp
This guide will help you set up and use a Python script to download videos from various platforms using yt-dlp.

Prerequisites
1- Python Installed: Make sure you have Python installed on your system. You can download it from python.org.

2- Install Necessary Tools: You can either install the required tools manually or use PowerShell scripts for automatic installation.

* Option 1: Manual Installation
Install Python
1- Download the latest version of Python from python.org.
2- Run the installer and ensure you check the option "Add Python to PATH".
Install yt-dlp
1- Open Command Prompt (cmd).
2- Run the following command: pip install yt-dlp

  Install FFmpeg
1- Download FFmpeg from the FFmpeg website.
2- Extract the downloaded zip file.
3- Add the bin directory of the extracted folder to your system's PATH:
Right-click on "This PC" or "My Computer" > Properties > Advanced system settings > Environment Variables.
In the "System variables" section, find the "Path" variable and click Edit.
Add the path to the bin directory of FFmpeg (e.g., C:\ffmpeg\bin).



* Option 2: Automatic Installation Using PowerShell
If you prefer to automate the installation process, you can use the following PowerShell scripts. Open PowerShell as Administrator and run the commands below.

Install Python
# Download and install Chocolatey (package manager for Windows)
Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.SecurityProtocolType]::Tls12; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))

# Install Python
choco install -y python
Install yt-dlp

After Python is installed, you can install yt-dlp using pip. Run the following command in PowerShell:
# Ensure pip is updated
python -m pip install --upgrade pip

# Install yt-dlp
pip install yt-dlp

Install FFmpeg
FFmpeg can also be installed using Chocolatey. Run the following command in PowerShell:
# Install FFmpeg
choco install -y ffmpeg

Script Setup
Create a Python Script:

Open a text editor (like Notepad, VSCode, or PyCharm) and create a new file named video_downloader.py.
Copy the Script: Copy the following script into video_downloader.py

Save the Script: Save the file in a convenient location, such as your Desktop.

Running the Script
Open Command Prompt: Press Win + R, type cmd, and hit Enter.

Navigate to the Script Location: Use the cd command to navigate to the directory where you saved the script. For example, if it's on your Desktop:
cd C:\Users\Mohammedgam\Desktop

Run the Script: Execute the script by running:
python video_downloader.py

Follow Prompts: Enter the video URL and the location where you want to save the video when prompted.


Notes
Make sure to provide a valid URL for the video you want to download.
The script will download the video and audio separately and merge them into one MP4 file using FFmpeg.
Troubleshooting
If you encounter errors related to missing modules, ensure you have installed yt-dlp correctly.
For any issues related to FFmpeg, ensure its path is correctly set in the script and that it is installed properly.
you can contact me thru emil . 
