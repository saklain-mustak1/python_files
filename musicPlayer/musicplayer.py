import os
import pygame
from tkinter import *
from tkinter.filedialog import askdirectory

root = Tk()
root.geometry('500x400')
root.title('saklain play')

listofsong = []

index = 0


def nextsong(event):
    global index
    index += 1
    pygame.mixer.music.load(listofsong[index])
    pygame.mixer.music.play()

def prevsong(event):
    global index
    index -= 1
    pygame.mixer.music.load(listofsong[index])
    pygame.mixer.music.play()


def stopsong(evenyt):
    pygame.mixer.music.stop()


def folderchoce():
    folder = askdirectory()
    os.chdir(folder)

    for item in os.listdir(folder):
        if item.endswith(".mp3"):
            listofsong.append(item)

    pygame.mixer.init()
    pygame.mixer.music.load(listofsong[0])
    pygame.mixer.music.play()
folderchoce()


topic = Label(root, text='songs')
topic.pack()

sonslist = Listbox(root)
sonslist.pack()

for sons in listofsong:
    sonslist.insert(0, sons)

nextbotton = Button(root, text = 'NEXT')
nextbotton.pack()

previousbotton = Button(root, text = 'previous')
previousbotton.pack()

stopbutton = Button(root, text = 'Stop')
stopbutton.pack()

nextbotton.bind("<Button-1>", nextsong)
previousbotton.bind("<Button-1>", prevsong)
stopbutton.bind("<Button-1>", stopsong)




root.mainloop()
