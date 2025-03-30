import yt_dlp
import sys
import os

def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

def download_youtube(url):
    raw_video_path = "downloaded_video.mp4"  # Keep original format

    ydl_opts = {
        'format': 'best[height<=720][ext=mp4]',
        'outtmpl': raw_video_path,   # Save in original format
        'noplaylist': True,          # Ignore playlists
        'quiet': False,              # Show progress
        'merge_output_format': 'mp4',  # 출력 형식을 mp4로 강제
        'ffmpeg_location': resource_path('ffmpeg.exe'),
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("Download completed successfully!")
    
    except Exception as e:
        print(f"Error: {str(e)}")
        input("Press Enter to exit...")

if __name__ == "__main__":
    url = input("Enter the YouTube Shorts URL: ")
    download_youtube(url)