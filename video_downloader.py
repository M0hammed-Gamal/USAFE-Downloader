import os
import subprocess
import yt_dlp
import requests

def download_file(url, output_path, filename):
    # Construct the full file path
    full_path = os.path.join(output_path, filename)
    response = requests.get(url, allow_redirects=True)

    # Save the file
    with open(full_path, 'wb') as file:
        file.write(response.content)
    print(f"Downloaded: {full_path}")

def download_video(url, output_path, filename):
    ydl_opts = {
        'outtmpl': os.path.join(output_path, filename + '.%(ext)s'),
        'progress_hooks': [hook],
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

def hook(d):
    if d['status'] == 'downloading':
        print(f"\rDownloading: {d['_percent_str']} | ETA: {d['eta']} seconds", end='')

def main():
    url = input("Enter the URL of the file (video, audio, pdf, etc.): ")
    output_path = input("Enter the path where you want to save the file (leave blank for current directory): ")
    filename = input("Enter the desired filename (without extension): ")

    if not output_path:
        output_path = os.getcwd()

    # Ensure the output path exists
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    # Check the file type based on the URL extension
    if url.lower().endswith(('.pdf', '.mp3', '.mp4', '.avi', '.mkv', '.flv', '.mov')):
        if url.lower().endswith('.pdf'):
            print("Detected PDF file.")
            download_file(url, output_path, filename + '.pdf')
        elif url.lower().endswith(('.mp3', '.mp4', '.avi', '.mkv', '.flv', '.mov')):
            print("Detected video or audio file.")
            download_video(url, output_path, filename)
        else:
            print("Downloading other file type.")
            download_file(url, output_path, filename)
    else:
        print("Detected video URL.")
        download_video(url, output_path, filename)

if __name__ == "__main__":
    main()
