#!/usr/bin/env python3

from tkinter import *
from gtts import gTTS
from playsound import playsound
import os
import PyPDF2


root = Tk()
root.geometry('350x300')
root.resizable()
root.config(bg='salmon')
root.title('Text to Speech')


Label(root, text='Text to Speech', font='Calibri 20 bold', bg='salmon').pack()
Label(root, text='Enter Text:', font='arial 13 bold', bg='salmon').place(x=22, y=70)
Msg = StringVar()


entry_field = Entry(root, textvariable=Msg, width=50)
entry_field.place(x=25, y=100)


def text_to_speech():
  Message = entry_field.get()
  speech = gTTS(text=Message)
  speech.save('Text.mp3')
  playsound('Text.mp3')

def close():
  root.destroy()
  delete()

def reset():
  Msg.set("")
  delete()

def again():
  playsound('Text.mp3')

def audiobook():
  pdfreader = PyPDF2.PdfFileReader(open('Book.pdf', 'rb'))
  for page_num in range(pdfreader.numPages):
    line = pdfreader.getPage(page_num).extractText()
    speaker = gTTS(line)
    speaker.save('Audiobook.mp3')
  playsound('Audiobook.mp3')


def delete():
  if os.path.exists('Text.mp3') and os.path.exists('Audiobook.mp3'):
   os.remove('Text.mp3')
   os.remove('Audiobook.mp3')
  elif os.path.exists('Text.mp3') or os.path.exists('Audiobook.mp3'):
   if os.path.exists('Text.mp3'):
     os.remove('Text.mp3')
   else:
     os.remove('Audiobook.mp3')
  else:
    print('No files found')


Button(root, text="Play", font='Calibri 15 bold', command=text_to_speech,width=4).place(x=55, y=140)
Button(root, text='Again', font='Calibri 15 bold', command=again).place(x=138,y=140)
Button(root, text='Close', font='Calibri 15 bold', command=close, bg='Red').place(x=138, y=190)
Button(root, text='Reset', font='Calibri 15 bold', command=reset).place(x=230,y=140)
Button(root, text='Book', font='Calibri 15 bold', command=audiobook).place(x=230, y=190)

root.mainloop()
