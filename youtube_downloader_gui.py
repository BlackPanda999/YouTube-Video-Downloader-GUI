# youtube_downloader_gui.py

import os
from tkinter import Tk, Label, Entry, Button, filedialog, messagebox
from pytube import YouTube

def download_video():
    url = url_entry.get()
    if not url:
        messagebox.showwarning("Input Error", "Please paste a YouTube link.")
        return

    try:
        yt = YouTube(url)
        stream = yt.streams.filter(progressive=True, file_extension='mp4')                            .order_by('resolution').desc().first()

        save_path = filedialog.askdirectory()
        if not save_path:
            return

        status_label.config(text="📥 Downloading...")
        stream.download(output_path=save_path)
        status_label.config(text="✅ Download complete!")
        messagebox.showinfo("Success", f"Downloaded: {yt.title}")
    except Exception as e:
        status_label.config(text="❌ Failed to download.")
        messagebox.showerror("Error", str(e))

# GUI setup
root = Tk()
root.title("YouTube Video Downloader")
root.geometry("500x200")

Label(root, text="🎥 Paste YouTube Link:", font=("Arial", 12)).pack(pady=10)

url_entry = Entry(root, width=60)
url_entry.pack()

Button(root, text="Download Video", command=download_video, bg="green", fg="white").pack(pady=10)

status_label = Label(root, text="", font=("Arial", 10))
status_label.pack()

root.mainloop()
