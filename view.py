from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title('Desafio de programacion')
root.iconbitmap("img/loco.ico")

my_img1 = ImageTk.PhotoImage(Image.open("img/0.png"))
my_img2 = ImageTk.PhotoImage(Image.open("img/1.png"))
my_img3 = ImageTk.PhotoImage(Image.open("img/2.png"))
my_img4 = ImageTk.PhotoImage(Image.open("img/3.png"))
my_img5 = ImageTk.PhotoImage(Image.open("img/4.png"))

image_list = [my_img1,my_img2,my_img3,my_img4,my_img5]


my_label = Label(image=my_img1)
my_label.grid(row= 0, column = 0, columnspan = 3)

def forward():
    return

def back():
  return


#Creacion de los botones#
button_back = Button(root, text="<<")
button_exit = Button(root, text="Exit Program", command = root.quit)
button_forward = Button(root, text=">>")

#Dando la posicion de los botones#
button_back.grid(row=1, column=0)
button_exit.grid(row=1,column=1)
button_forward.grid(row=1, column=2)

root.mainloop()