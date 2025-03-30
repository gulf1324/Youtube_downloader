# YouTube Downloader

A simple Python script to download YouTube videos.

## Features
- Built with `yt_dlp` for reliable video downloading

## Prerequisites

### 1. Install Python
- **Download and install Python 3.9 or later** from [python.org](https://www.python.org/downloads/).
  - Ensure you check "Add Python to PATH" during installation.
- Verify installation: `python --version`


### 2. Install FFmpeg
- **Download FFmpeg** from [ffmpeg.org](https://ffmpeg.org/download.html) or use a pre-built binary:
- Windows: Get it from [gyan.dev](https://www.gyan.dev/ffmpeg/builds/) (e.g., `ffmpeg-release-essentials.zip`).
- Extract and place `ffmpeg.exe` in the same folder as `Youtube_downloader.py`, or add it to your system PATH.
- Verify installation: `ffmpeg -version`

### 3. Install Required Python Packages
- Open a terminal and install `yt_dlp`: `pip install yt_dlp`

---
## Usage
### 1. *Running the Script*
1. Clone or download this repository.
2. Ensure `ffmpeg.exe` is in the same directory as `Youtube_downloader.py` (or in your PATH).
3. Open a terminal in the project folder and run: `python Youtube_downloader.py`
4. Follow the prompt.

### 2. *Building the Executable*
To create a standalone `.exe` file (Windows):
1. Install Nuitka: `pip install nuitka`
2. Run the build command in the project folder: 
  ```
  nuitka --standalone --onefile ^
  --enable-plugin=data-files ^
  --include-data-file="python39.dll=python39.dll" ^
  --include-data-file="ffmpeg.exe=ffmpeg.exe" ^
  --windows-console-mode=force ^
  Youtube_downloader.py
  ```
3. Find the executable in the `dist/` folder.
4. Run the `.exe` file and follow the same prompts as above.
---


## Troubleshooting
- **FFmpeg not found**: Ensure `ffmpeg.exe` is in the correct location or PATH.
- **Download errors**: Check your internet connection and URL validity.
- **Module not found**: Verify `yt_dlp` is installed.

## License
This project is open-source and available under the [MIT License](LICENSE).

## Acknowledgments
- Built with [yt_dlp](https://github.com/yt-dlp/yt-dlp)
- FFmpeg by [ffmpeg.org](https://ffmpeg.org/)
- Enhanced by Grok 3 (xAI)