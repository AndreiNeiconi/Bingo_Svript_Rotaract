import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
import random
import pandas as pd
import os
from yt_dlp import YoutubeDL


# Bingo Game Class
class BingoGame:
    # Initialize the program
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Bingo Game")
        self.window.geometry("400x300")
        self.UI()
    
    # Create User Interface
    
    def UI(self):
        self.Button = tk.Button(self.window, text = "Incarca Fiser excel",)
        self.Button.bind("<Button-1>", lambda event: self.load_excel())
        self.Button.pack(pady=20)
        self.show_List = tk.Button(self.window, text = "Arata lista de meloy",command=self.show_list).pack(pady=20)
        self.download_Button = tk.Button(self.window, text = "Descarca meloy",command=self.download_link).pack(pady=20)
    # Load Excel File

    def load_excel(self):
        file_path = tk.filedialog.askopenfilename()
        if file_path:
            try:
                self.df = pd.read_excel(file_path,sheet_name='Sheet1')            
                messagebox.showinfo("Success", "Excel file loaded successfully!")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to load Excel file: {e}") 
# Get Data from DataFrame
    def get_data(self):
        self.id = self.df.iloc[:, 0].tolist()
        self.Names = self.df.iloc[:, 1].tolist()
        self.crop_time = self.df.iloc[:, 2].tolist()
        self.link = self.df.iloc[:, 3].tolist()
# Show List
    def show_list(self):
        self.tk = tk.Toplevel(self.window)
        self.tk.title("Lista de meloy")
        self.tk.geometry("600x400")
        self.get_data()
        text_area = tk.Text(self.tk, wrap='word')
        text_area.pack(expand=True, fill='both')
        for i in range(len(self.id)):
            entry = f"ID: {self.id[i]}, Name: {self.Names[i]}, Crop Time: {self.crop_time[i]}, Link: {self.link[i]}\n"
            text_area.insert(tk.END, entry) 
# Download Links
    def download_link(self):
        try:
            for index, item in enumerate(self.link):
                timestamp = self.crop_time[index] if index < len(self.crop_time) else None

                ydl_opts = {
                    'format': 'bestaudio/best',
                    'noplaylist': True,  # download only this video
                    'postprocessors': [{
                        'key': 'FFmpegExtractAudio',
                        'preferredcodec': 'mp3',
                        'preferredquality': '192',
                    }],
                    'outtmpl': os.path.join('downloads', '%(title)s.%(ext)s'),
                }

                # Add timestamp only if it exists
                if timestamp and timestamp.strip():
                    ydl_opts['download_sections'] = [f'*{timestamp}']
                    print(timestamp)

                with YoutubeDL(ydl_opts) as ydl:
                    ydl.download([item])

            self.download_complete()

        except Exception as e:
            messagebox.showerror("Error", f"Failed to download files: {e}")

    # Download Complete Notification
    def download_complete(self):
        messagebox.showinfo("Download Complete", "All files have been downloaded successfully!")

        





        
    



game = BingoGame()
game.window.mainloop()  