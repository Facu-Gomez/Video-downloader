from pytube import YouTube
from tkinter import *


root = Tk()
root.geometry('500x300')
root.resizable(0, 0)
root.title('Descarga tus videos de youtube aca papá')
root.configure(bg='#6e1818')

Label(root, text="Descarga tus videos",
      font='arial 20 bold', bg='#82a193').place(x=90, y=30)

link= StringVar()
Label(root, text='Pega el link aca:', font='arial 12',
      bg='#bd8bc7').place(x=190, y=90)
link_enter = Entry(root, width=70,
                   textvariable=link).place(x=32, y=120)

def Downloader():
    url = YouTube(str(link.get()))
    video = url.streams.get_highest_resolution()
    video.download()
    Label(root, text='DESCARGADO', font='arial 13 bold',
          bg='#8ba8c7', fg='#425f7d').place(x=180, y=240)
    
Button(root, text='DESCARGAR', font ='arial 13 bold italic',
       bg='#66162c', padx=2,
       command=Downloader).place(x=180, y=180)

root.mainloop()