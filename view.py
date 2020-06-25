from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title('Desafio de programacion')

my_img = ImageTk.PhotoImage(Image.open("img/0.png"))
my_label = Label(image=my_img)
my_label.pack()

root.mainloop()