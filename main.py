from pydoc import text
import string
from tkinter import *
from pytube import YouTube

root = Tk()
root.geometry('500x300')
root.resizable(0,0)
root.config(bg='black')
root.title('Youtube Downloader By: Veeti Bark')


Label(root, text='Youtube Video Downloader', font='arial 20 bold', fg='white', bg='black').pack()

link = StringVar()

Label(root, text='Enter link to the video:', font='Arial 10', fg='white', bg='black').place(x=175, y=50)
enter_link = Entry(root, width=40, textvariable=link).place(x=125, y=75)


def downloadMP4():
    try:
        url = YouTube(str(link.get()))
    except:
        Label(root, text='There was an error!', font='Arial 10', fg='white', bg='red').place(x=190, y=150)
    video = url.streams.first()
    try:
        video.download('./downloadedVideos')
        Label(root, text='Video downloaded succesfully!', font='Arial 10', fg='white', bg='green').place(x=160, y=150)
    except:
        Label(root, text='There was an error!', font='Arial 10', fg='white', bg='red').place(x=190, y=150)

Button(bg='white', fg='black', command=downloadMP4, text='Start download', activebackground="red").place(x=200, y=100)

root.mainloop()