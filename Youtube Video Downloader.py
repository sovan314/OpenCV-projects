# tkinter allows to build gui applications
from tkinter import *
from tkinter import filedialog
from tkinter import ttk

# movie used for video editing processing and composting
from moviepy import *
from moviepy.editor import VideoFileClip

# pytube is used for downloading video from web
from pytube import YouTube

# used for automating process of copying and removal of files and directories
import shutil

#  Functions
def select_path():
    # allow user to select a path from the exploler
    path = filedialog.askdirectory()
    path_label.config(text=path)

def download_file_highest_resolution():
    # get user path
    get_link = link_field.get()
    # get selected path
    user_path = path_label.cget('text')
    screen.title("downloading....")
    # download viedo
    mp4_video = YouTube(get_link).streams.get_highest_resolution().download()
    video_clip = VideoFileClip(mp4_video)
    video_clip.close()
    # move file to slected directory using shutil module
    shutil.move(mp4_video, user_path)
    screen.title("downloading is done !try downloading another file.....")
def download_file_720p():
    # get user path
    get_link = link_field.get()
    # get selected path
    user_path = path_label.cget('text')
    screen.title("downloading....")
    # download video
    mp4_video = YouTube(get_link).streams.filter(res="720p").first().download()
    video_clip = VideoFileClip(mp4_video)
    video_clip.close()
    # move file to slected directory using shutil module
    shutil.move(mp4_video, user_path)
    screen.title("downloading is done !try downloading another file.....")

def download_file_240p():
    # get user path
    get_link = link_field.get()
    # get selected path
    user_path = path_label.cget('text')
    screen.title("downloading....")
    # download video
    mp4_video = YouTube(get_link).streams.filter(res="240p").first().download()
    video_clip = VideoFileClip(mp4_video)
    video_clip.close()
    # move file to slected directory using shutil module
    shutil.move(mp4_video, user_path)
    screen.title("downloading is done !try downloading another file.....")

def download_file_360p():
    # get user path
    get_link = link_field.get()
    # get selected path
    user_path = path_label.cget('text')
    screen.title("downloading....")
    # download video
    mp4_video = YouTube(get_link).streams.filter(res="360p").first().download()
    video_clip = VideoFileClip(mp4_video)
    video_clip.close()
    # move file to slected directory using shutil module
    shutil.move(mp4_video, user_path)
    screen.title("downloading is done !try downloading another file.....")

def download_file_480p():
    # get user path
    get_link = link_field.get()
    # get selected path
    user_path = path_label.cget('text')
    screen.title("downloading....")
    # download video
    mp4_video = YouTube(get_link).streams.filter(res="480p").first().download()
    video_clip = VideoFileClip(mp4_video)
    video_clip.close()
    # move file to selected directory using shutil module
    shutil.move(mp4_video, user_path)
    screen.title("downloading is done !try downloading another file.....")

def download_file_144p():
    # get user path
    get_link = link_field.get()
    # get selected path
    user_path = path_label.cget('text')
    screen.title("downloading....")
    # download video
    mp4_video = YouTube(get_link).streams.filter(res="144p").first().download()
    video_clip = VideoFileClip(mp4_video)
    video_clip.close()
    # move file to slected directory using shutil module
    shutil.move(mp4_video, user_path)
    screen.title("downloading is done !try downloading another file.....")

screen = Tk()
title = screen.title("My youtube downloader")

# canvas comes from tkinter
canvas = Canvas(screen, bg="white",width=500,height=1800)
canvas.pack()

# image logo
#imgg = PhotoImage(file='yt.png')

# resize
#imgg = imgg.subsample(2,2)
#canvas.create_image(250,80,image=imgg)

# link field
link_field = Entry(screen,width=40,bg='white',font=('Arial',15))
link_label = Label(screen,text="****Enter Your download link****",bg='yellow',font=('Imprint MT Shadow',20))

# select path for saving the file
path_label = Label(screen,text='Select Path For Downloading.....',bg='white',font=('Arial',15))
select_btn = Button(screen,text='select path',bg='pink',padx='35',pady='5',font=('Arial',15),command= select_path)

# add to window
canvas.create_window(250,280,window=path_label)
canvas.create_window(250,330,window=select_btn)

# add widgets to window
canvas.create_window(250,170, window=link_label)
canvas.create_window(250,220, window=link_field)

# download btns
dwnld_bttn_highest_resolution = Button(screen, text='Highest resolution',bg='green',padx='20',pady='3',command=download_file_highest_resolution)
dwnld_bttn_720p = Button(screen, text="720p resolution",bg='green',padx='20',pady='3',command=download_file_720p)
dwnld_bttn_480p = Button(screen, text="480p resolution",bg='green',padx='20',pady='3',command=download_file_480p)
dwnld_bttn_360p = Button(screen, text="360p resolution",bg='green',padx='20',pady='3',command=download_file_360p)
dwnld_bttn_240p = Button(screen, text="240p resolution",bg='green',padx='20',pady='3',command=download_file_240p)
dwnld_bttn_144p = Button(screen, text="144p resolution",bg='green',padx='20',pady='3',command=download_file_144p)

# add to canvas
canvas.create_window(250, 400,window=dwnld_bttn_highest_resolution)
canvas.create_window(250, 440, window=dwnld_bttn_720p)
canvas.create_window(250, 480, window=dwnld_bttn_480p)
canvas.create_window(250, 520, window=dwnld_bttn_360p)
canvas.create_window(250, 560, window=dwnld_bttn_240p)
canvas.create_window(250, 600, window=dwnld_bttn_144p)

screen.mainloop()
