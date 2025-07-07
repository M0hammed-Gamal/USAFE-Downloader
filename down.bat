@echo off
setlocal

:: Prompt user for URL and download path
set /p URL="Enter the URL of the video: "
set /p SAVE_PATH="Enter the path where you want to save the video (leave blank for current directory): "

:: Set default path if not provided
if "%SAVE_PATH%"=="" set SAVE_PATH=.

:: Print status
echo Downloading video from %URL%...
echo Saving to %SAVE_PATH%...

:: Run yt-dlp to download the video
yt-dlp.exe -o "%SAVE_PATH%\%(title)s.%(ext)s" %URL%

:: Check for errors
if %ERRORLEVEL% neq 0 (
    echo An error occurred during the download.
) else (
    echo Download completed successfully!
)

endlocal
pause
