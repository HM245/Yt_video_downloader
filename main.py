import tkinter
import customtkinter
from tkinter import filedialog
from tkinter.filedialog import asksaveasfilename
from pytube import YouTube

# def file():
#     file=filedialog.asksaveasfilename(defaultextension='.mp4')
    
def startDownload():
    try:
        ytlink=link.get()
        ytObject=YouTube(ytlink, on_progress_callback=on_progress)
        video=ytObject.streams.get_highest_resolution()
        title.configure(text=ytObject._title, text_color="Blue")
        finishLabel.configure(text="")
        if video:
            file=filedialog.asksaveasfilename(filetypes=[("video","mp4")], defaultextension='.mp4')
            video.download(file)
            finishLabel.configure(text="Downloaded!", text_color="green")
            print("Downloaded!")
        #finishLabel.configure(text="Downloaded!")
    except:
        print("Download error!")
        finishLabel.configure(text="Download Error!", text_color="red")
def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_downloaded / total_size * 100 
    print(percentage_of_completion)   
    per = str(int(percentage_of_completion))
    pPercentage.configure(text=per + "%")
    pPercentage.update()
    #update Progress bar
    progressBar.set(float(percentage_of_completion) / 100 )

#system settings
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

#our app frame
app = customtkinter.CTk()
app.geometry("720x480")
app.title("Youtube Video Downloader")

#Adding UI Elements
title=customtkinter.CTkLabel(app, text="Insert a youtube video link here")
title.pack(padx=50,pady=50) #paddiing

#Link input
url_var=customtkinter.StringVar()
link=customtkinter.CTkEntry(app, width=350,height=40, placeholder_text="Paste using ctrl+V shortcut key", placeholder_text_color="red", textvariable=url_var)
link.pack()

#finished Downloading
finishLabel=customtkinter.CTkLabel(app, text="")
finishLabel.pack()

#progress percentage
pPercentage=customtkinter.CTkLabel(app, text="0%")
pPercentage.pack()

progressBar=customtkinter.CTkProgressBar(app, width=400)
progressBar.set(0)
progressBar.pack(padx=50,pady=50)

# #select file
# b=customtkinter.CTkButton(app,text="Browse",command=file)
# b.pack()

#Download Button
download=customtkinter.CTkButton(app, text="Download", command=startDownload)
download.pack(padx=50,pady=50)#padding


#Run app
app.mainloop()
