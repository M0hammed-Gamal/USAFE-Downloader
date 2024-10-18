Instructions:
1- Run the script.
2- Enter the video URL.
3- View the list of available formats.
4- Select the desired format code.
5- The video will be downloaded in that format.
6- make sure the yt-dlp.exe is in the same path with the script and downlaod path (important)

Important Notes :-
1- you need to dowonload yt-dlp.exe file 
https://github.com/yt-dlp/yt-dlp/releases
2- you need to dowonload 
* Chocolatey:
Open Command Prompt as an administrator (right-click Command Prompt and select "Run as administrator").
Run the following command to install Chocolatey
@powershell -NoProfile -ExecutionPolicy Bypass -Command "iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))" && SET "PATH=%PATH%;%ALLUSERSPROFILE%\chocolatey\bin"

*Install FFmpeg via Chocolatey:
In the same Command Prompt window, run
choco install ffmpeg

Test FFmpeg:
After installation, type ffmpeg in Command Prompt to verify that it is installed correctly.
