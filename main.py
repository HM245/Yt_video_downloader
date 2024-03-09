import tkinter
import customtkinter
from pytube import YouTube
#path="/home/hardik/Desktop"

def startDownload():
    try:
        ytlink=link.get()
        ytObject=YouTube(ytlink, on_progress_callback=on_progress)
        video=ytObject.streams.get_highest_resolution()
        title.configure(text=ytObject._title, text_color="Blue")
        finishLabel.configure(text="")
        if video:
            video.download()
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
customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("blue")

#our app frame
app = customtkinter.CTk()
app.geometry("720x480")
app.title("Youtube Video Downloader")

#Adding UI Elements
title=customtkinter.CTkLabel(app, text="Insert a youtube video link here")
title.pack(padx=50,pady=50) #paddiing

#Link input
url_var=tkinter.StringVar()
link=customtkinter.CTkEntry(app, width=350,height=40, textvariable=url_var)
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

#Download Button
download=customtkinter.CTkButton(app, text="Download", command=startDownload)
download.pack(padx=50,pady=50)#padding

#Run app
app.mainloop()
