from tkinter import *
from PIL import Image,ImageTk
import os
main=Tk()
main.title("PhoneBook")
# main.iconbitmap("Phonebook.ico")
main.geometry('600x700')
main.resizable(False,False)
my_image=ImageTk.PhotoImage(Image.open("main12.png"))
my_label=Label(image=my_image)
my_label.pack()
#main window button
my_image1=ImageTk.PhotoImage(Image.open("12.png"))
b1=Button(main,image=my_image1,borderwidth=0,bg="pink",relief="raised")
b1.place(relx=0.5,rely=0.55,anchor="center")
main.mainloop()