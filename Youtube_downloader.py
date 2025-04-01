import yt_dlp
import os
from datetime import datetime
import re

def get_valid_resolution(is_shorts):
    if is_shorts:
        valid_resolutions = {
                "best": "bv*[vcodec~='^((he|a)vc|h26[45])']+ba[ext=m4a]/best",  
                "1080" : "bv[width=1080][vcodec~='^((he|a)vc|h26[45])']+ba[ext=m4a]",
                "720": "bv[width=720][vcodec~='^((he|a)vc|h26[45])']+ba[ext=m4a]",
                "480": "bv[width=480][vcodec~='^((he|a)vc|h26[45])']+ba[ext=m4a]",
                "360": "bv[width=360][vcodec~='^((he|a)vc|h26[45])']+ba[ext=m4a]",
            }
    else:
        valid_resolutions = {
                "best": "bv*[vcodec!~='^av01']+ba[ext=m4a]/best",  
                "1080" : "bv[height=1080][vcodec~='^((he|a)vc|h26[45])']+ba[ext=m4a]",
                "720": "bv[height=720][vcodec~='^((he|a)vc|h26[45])']+ba[ext=m4a]",
                "480": "bv[height=480][vcodec~='^((he|a)vc|h26[45])']+ba[ext=m4a]",
                "360": "bv[height=360][vcodec~='^((he|a)vc|h26[45])']+ba[ext=m4a]",
            }
    while True:
        resolution = input("Enter desired resolution (360, 480, 720, 1080): ").strip()
        if resolution in valid_resolutions:
            resolution = valid_resolutions[resolution]
            return resolution
        print(f"Error: Invalid resolution. Please choose from {', '.join(valid_resolutions)}")

def download_youtube(url):
    os.makedirs("Downloads", exist_ok=True)
    downloads_folder = os.path.join(os.getcwd(), "Downloads")
    timestamp = datetime.now().strftime("%y%m%d_%H%M%S")
    raw_video_path = os.path.join(downloads_folder, f"download_{timestamp}")

    is_shorts = bool(re.search(r"/shorts/", url))
    resolution = get_valid_resolution(is_shorts)

    ydl_opts = {
        'format': resolution,
        'outtmpl': raw_video_path,
        'noplaylist': True,
        'quiet': False,
        # 'ffmpeg_location': resource_path('ffmpeg.exe'),
        #  commented ==> find on it's own
        'merge_output_format' : 'mp4',
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("\nDownload completed successfully!")
        
    except Exception as e:
        print(f"\nError: {str(e)}")

def main():
    while True:
        url = input("Enter the YouTube URL (or 'quit' to exit): ")
        if url.lower() == 'quit':
            break
        if url:
            download_youtube(url)
        input("\nPress Enter to continue downloading or close the window...")

if __name__ == "__main__":
    main()