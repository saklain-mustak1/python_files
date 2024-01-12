import pygame
import tkinter as tkr
#from tkinter import *
from tkinter.filedialog import askdirectory
import os

music_player = tkr.Tk()
music_player.title("saklain music player")
music_player.geometry('700x600')

directory = askdirectory()
os.chdir(directory)
song_list = os.listdir(directory)

play_list = tkr.Listbox(music_player, font='Helvetica 12 bold', bg='yellow', selectmode=tkr.SINGLE)
for item in song_list:
    if item.endswith('.mp3'):
        song_list.append(item)

    pos = 0
    play_list.insert(pos, item)
    pos += 1


pygame.init()
pygame.mixer.init()


def play():
    pygame.mixer.music.load(play_list.get(tkr.ACTIVE))
    from numpy.ma import var
    var.set(play_list.get(tkr.ACTIVE))
    pygame.mixer.music.play()


def stop():
    pygame.mixer.music.stop()


def pause():
    pygame.mixer.music.pause()


def unpause():
    pygame.mixer.music.unpause()

play()
stop()
pause()
unpause()

music_player.mainloop()
