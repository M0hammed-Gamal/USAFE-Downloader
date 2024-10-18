import yt_dlp
import os
import sys

def download_video(url, output_path):
    # Prepare download options
    ydl_opts = {
        'format': 'bestvideo+bestaudio',
        'merge_output_format': 'mp4',
        'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),
        'ffmpeg_location': 'C:/ProgramData/chocolatey/bin/ffmpeg.exe',  # Update this to your actual ffmpeg path
        'progress_hooks': [progress_hook],  # Hook for download progress
    }

    # Run yt-dlp with the provided options
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
    except Exception as e:
        print(f"Error: {e}")

def progress_hook(d):
    if d['status'] == 'downloading':
        percent = d['_percent_str'].strip()  # Get the percentage completed
        speed = d['_speed_str']  # Download speed
        eta = d['_eta_str']  # Estimated time left
        
        # Update the status in one line
        sys.stdout.write(f"\rDownloading: {percent} | Speed: {speed} | ETA: {eta}")
        sys.stdout.flush()

    elif d['status'] == 'finished':
        print(f"\nDownload complete. File saved to: {d['filename']}")

    elif d['status'] == 'error':
        print("An error occurred during the download.")

def main():
    # Ask the user for inputs
    url = input("Enter the URL of the video: ")
    output_path = input("Enter the path where you want to save the video (leave blank for current directory): ")
    if not output_path:
        output_path = os.getcwd()

    # Start download
    download_video(url, output_path)

if __name__ == '__main__':
    main()
