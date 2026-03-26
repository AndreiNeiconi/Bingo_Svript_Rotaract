----< Bingo Music Downloader >--------------
A Python-based desktop application built with Tkinter and yt-dlp designed to automate the process of
downloading and cropping audio tracks for Bingo games.
Simply upload an Excel sheet containing YouTube links and timestamps, and the app handles the rest.
----Features:
-Excel Integration: Batch import song data directly from .xlsx files.

-Smart Cropping: Automatically downloads only the specific segment of the audio (e.g., 01:00 to 01:30).

-Duplicate Prevention: Skips links that have already been processed in the current session.

-High Quality: Downloads and converts audio to 192kbps MP3 format.

-GUI Interface: Easy-to-use interface for non-technical users.

----Prerequisites---
Before running the application, ensure you have the following installed:

1.Python 3.8+

2.FFmpeg: This is required by yt-dlp for audio conversion and cropping.

-Windows: Download FFmpeg and add the /bin folder to your System PATH.

-Mac: brew install ffmpeg

-Linux: sudo apt install ffmpeg

---Installation---

git clone https://github.com/yourusername/bingo-downloader.git
cd bingo-downloader

Install dependencies:
pip install pandas openpyxl yt-dlp

Run the application:
python main.py

Excel File Format

Column A	 Column B	 Column C(Crop Time)	Column D(Link)
1	Song Name	01:20 -  01:50	 https://youtube.com/watch...
2	Song Name	00:10 - 00:40	   https://youtube.com/watch...

.---Note: The "Crop Time" must follow the MM:SS - MM:SS format.---.

----How to Use---

1.Launch the program.

2.Click "Incarca Fiser excel" to select your prepared spreadsheet.

3.(Optional) Click "Arata lista de meloy" to verify the data was read correctly.

4.Click "Descarca meloy".

5.The audio clips will be saved automatically in a folder named /downloads within the project directory.

Technologies Used
Language: Python

GUI: Tkinter

Engine: yt-dlp

Data Handling: Pandas & Openpyxl

Processing: FFmpeg
---License---

This project is for educational use only. Please ensure you have the right to download content from YouTube according to their Terms of Service.
