# WITHOUT TKINTER

#import pyshorteners
#
# def short_url(url):
#     short_url = pyshorteners.Shortener().tinyurl.short(url)
#     print(f'your short URL is: {short_url}')
#
#
# short_url()
# -----------------------------------------
# -----------------------------------------
# -----------------------------------------
# -----------------------------------------
# -----------------------------------------'


# WITH TKINTER
from tkinter import *
import pyshorteners
root = Tk()
root.geometry("400x400")
root.title("URL shortner")
# my structure
title = Label(root,text="URL SHORTNER",font=('montserrat',20))
label = Label(root,text="Please input a URL", font=('montserrat',12),pady= 20)
URLentry = Entry(root, width="50")
button = Button(root,text="Run",padx= 20,pady= 5,bg='royalblue',font=('montserrat',12),bd="0")
resultTitle = Label(root, text="RESULT",font=('montserrat',12),pady= 20)
result = Label(root,text="",pady= 20)
# packing my structure
title.pack()
label.pack()
URLentry.pack()
button.pack()
resultTitle.pack()
result.pack()


# function
def short_url():
    URL = URLentry.get()
    short_url = pyshorteners.Shortener().tinyurl.short(URL)
    print(f'your short URL is: {short_url}')
    resultTitle.config(text=f'short URL: {short_url}')

button.config(command=short_url)



root.mainloop()