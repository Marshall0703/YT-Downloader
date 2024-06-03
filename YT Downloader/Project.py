import tkinter as tk
from tkinter import *
from pytube import YouTube
from tkinter import messagebox, filedialog

def Widgets():
    head_label = Label(root, text="YT Downloader", padx=15, pady=15, bg="white", fg="black")
    link_label = Label(root, text="Link :", pady=5, padx=5, bg="white")
    destination_label = Label(root, text="File :", bg="white", pady=5, padx=9)
    root.linkText = Entry(root, width=40, textvariable=video_Link)
    root.destinationText = Entry(root, width=27, textvariable=download_Path)
    browse_B = Button(root, text="Browse", command=Browse, width=10, bg="green", relief=GROOVE)
    Download_B = Button(root, text="Download", command=Download, width=20, bg="green", pady=10, padx=15, relief=GROOVE)
    browse_B.grid(row=3, column=2, pady=1, padx=1)
    Download_B.grid(row=4, column=1, pady=20, padx=20)
    link_label.grid(row=2, column=0, pady=5, padx=5)
    head_label.grid(row=1, column=1, columnspan=3, pady=10, padx=5)
    root.destinationText.grid(row=3, column=1, pady=5, padx=5)
    root.linkText.grid(row=2, column=1, columnspan=2, pady=5, padx=5)
    destination_label.grid(row=3, column=0, pady=5, padx=5)

def Browse():
    download_Directory = filedialog.askdirectory(
        initialdir="Path Please", title="Save")
    download_Path.set(download_Directory)

def Download():
    Youtube_link = video_Link.get()
    download_Folder = download_Path.get()
    getVideo = YouTube(Youtube_link)
    videoStream = getVideo.streams.first()
    videoStream.download(download_Folder)
    messagebox.showinfo("DONE", "Download saved in\n" + download_Folder)

root = tk.Tk()
root.geometry("400x300")
root.title("YouTube Downloader")
root.config(bg = "black")
video_Link = StringVar()
download_Path = StringVar()
Widgets()


root.mainloop()
    
    
