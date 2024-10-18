# USAFE Downloading Script Using yt-dlp

This guide provides instructions for setting up and using a Python script to download videos, audio files, PDFs, and other file types from various platforms using `yt-dlp`.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
  - [Option 1: Manual Installation](#option-1-manual-installation)
    - [Install Python](#install-python)
    - [Install yt-dlp](#install-yt-dlp)
    - [Install Requests](#install-requests)
  - [Option 2: Install via PowerShell](#option-2-install-via-powershell)
- [Script Usage](#script-usage)
- [Example](#example)
- [Supported File Types](#supported-file-types)
- [Notes](#notes)

## Prerequisites

1. **Python Installed**: Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

## Installation

You can install the necessary tools either manually or through an automated PowerShell script.

### Option 1: Manual Installation

#### Install Python

1. Download the latest version of Python from [python.org](https://www.python.org/downloads/).
2. Run the installer and **ensure you check the option "Add Python to PATH"**.

#### Install yt-dlp

1. Open Command Prompt (cmd).
2. Run the following command:

   ```bash
   pip install yt-dlp
   ```

#### Install Requests

1. Open Command Prompt (cmd).
2. Run the following command:

   ```bash
   pip install requests
   ```

### Option 2: Install via PowerShell

You can automate the installation process using PowerShell. Open PowerShell and run the following script:

```powershell
# Install Python
$pythonInstaller = "https://www.python.org/ftp/python/3.10.12/python-3.10.12-amd64.exe"
$pythonInstallerPath = "$env:TEMP\python-installer.exe"
Invoke-WebRequest -Uri $pythonInstaller -OutFile $pythonInstallerPath
Start-Process -FilePath $pythonInstallerPath -ArgumentList "/quiet InstallAllUsers=1 PrependPath=1" -Wait
Remove-Item $pythonInstallerPath

# Install yt-dlp
python -m pip install --upgrade pip
python -m pip install yt-dlp
python -m pip install requests
```

## Script Usage

1. **Download the Script**: Ensure you have the `video_downloader.py` script saved in your desired directory.

2. **Run the Script**: Navigate to the directory where the script is located and run:

   ```bash
   python video_downloader.py
   ```

3. **Input Details**:
   - **URL**: Enter the URL of the file (video, audio, PDF, etc.) you want to download.
   - **Output Path**: Specify the path where you want to save the file (leave blank for the current directory).
   - **Filename**: Provide a desired filename (without the extension) for the downloaded file.

## Example

```plaintext
C:\Users\Mohammedgam\Desktop>python video_downloader.py
Enter the URL of the file (video, audio, pdf, etc.): https://example.com/sample.mp3
Enter the path where you want to save the file (leave blank for current directory): C:\Users\Mohammedgam\Desktop\audio
Enter the desired filename (without extension): my_audio
Detected audio file.
Downloading: 100% | ETA: 0 seconds
Downloaded: C:\Users\Mohammedgam\Desktop\audio\my_audio.mp3
```

## Supported File Types

The script supports downloading the following file types:

- **Video Formats**: `.mp4`, `.avi`, `.mkv`, `.flv`, `.mov`
- **Audio Formats**: `.mp3`
- **Document Formats**: `.pdf`

## Notes

- Ensure that the URL you provide points to a direct file download. If the URL does not point directly to a downloadable file, the script may return an error.
- If you encounter issues, please check your internet connection and ensure the URL is valid.
