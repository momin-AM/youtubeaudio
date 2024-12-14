import yt_dlp
from tkinter import *
import tkinter.messagebox as msg

# pyinstaller --onefile --windowed --icon=C:\\Users\sk454\Downloads\\icons8-youtube-50.ico youtube_audio.py

def mainc():
    global video_url,file_path
    video_url0=url_var.get()
    file_path0=path_var.get()
    if 'youtube.com' in video_url0:
        video_url=video_url0
    else:
        video_url='https://www.youtube.com/'+video_url0
    if '/' in file_path0 or '\\' in file_path0:
        file_path = r"{}".format(file_path0)
    else:
        file_path=f'C:\\Users\\sk454\\Music\\youtube\\{file_path0}.%(ext)s' 
    try:
        download_status.config(text='downloading...',bg='skyblue')
        root.update_idletasks()
        download()
        download_status.config(text='downloaded successfully',bg='yellow')       
        msg.showinfo('success',f'song downloaded {file_path0} successfully')
    except:
        download_status.config(text='something went wrong',bg='red')   
        msg.showerror('Error','sorry! error in downloading')

def download():
    global video_url,file_path
    url_var.set('')  
    path_var.set('')
    ydl_opts = {
        'format': 'bestaudio/best',  
        'extractaudio': True,  
        'audioformat': 'mp3', 
        'outtmpl': file_path 
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])
def nullfunc():
    msg.showinfo('null','for future improvements')

def info():
    msg.showinfo('Info','an under development project\ncreated by momin')

file_icon=r"C:\\Users\sk454\Downloads\\icons8-youtube-50.ico"

root=Tk()
root.iconbitmap(file_icon)
root.title('audio downloader')
root.geometry('666x444')
main_menu=Menu(root)
menu0=Menu(main_menu,tearoff=0)
menu0.add_command(label='null',command=nullfunc)
menu0.add_command(label='null',command=nullfunc)
menu0.add_separator()
menu0.add_command(label='info',command=info)
main_menu.add_cascade(label='options',menu=menu0)
root.config(menu=main_menu)
Label(root,text='url here : ').grid(row=1,column=0)
url_var=StringVar()
path_var=StringVar()
url_widget=Entry(root,textvariable=url_var,borderwidth=2)
url_widget.grid(row=1,column=1)
Label(root,text='song name : ').grid(row=2,column=0)
path_widget=Entry(root,textvariable=path_var,borderwidth=2)
path_widget.grid(row=2,column=1)
Button(root,text='download',bg='grey',command=mainc).grid(row=3,column=2)
Label(root,text='').grid(row=4,column=2)
download_status=Label(root,text='')
download_status.grid(row=5,column=2)

root.mainloop()
