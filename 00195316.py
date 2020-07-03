from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title('Desafio de programacion')
#root.iconbitmap("icons/loco.ico")
root.resizable(width = 0, height = 0)
ox,oy = root.winfo_screenmmwidth()/2 , root.winfo_screenmmheight()/2

my_img1 = ImageTk.PhotoImage(Image.open("img/0.png"))
my_img2 = ImageTk.PhotoImage(Image.open("img/1.png"))
my_img3 = ImageTk.PhotoImage(Image.open("img/2.png"))
my_img4 = ImageTk.PhotoImage(Image.open("img/3.png"))
my_img5 = ImageTk.PhotoImage(Image.open("img/4.png"))
my_img6 = ImageTk.PhotoImage(Image.open("img/5.png"))
my_img7 = ImageTk.PhotoImage(Image.open("img/6.png"))
my_img8 = ImageTk.PhotoImage(Image.open("img/7.png"))
my_img9 = ImageTk.PhotoImage(Image.open("img/8.png"))
my_img10 = ImageTk.PhotoImage(Image.open("img/9.png"))
my_img11 = ImageTk.PhotoImage(Image.open("img/10.png"))
my_img12 = ImageTk.PhotoImage(Image.open("img/11.png"))
my_img13 = ImageTk.PhotoImage(Image.open("img/12.png"))
my_img14 = ImageTk.PhotoImage(Image.open("img/13.png"))
my_img15 = ImageTk.PhotoImage(Image.open("img/15.png"))
my_img16 = ImageTk.PhotoImage(Image.open("img/16.png"))
my_img17 = ImageTk.PhotoImage(Image.open("img/17.png"))
my_img18 = ImageTk.PhotoImage(Image.open("img/18.png"))
my_img19 = ImageTk.PhotoImage(Image.open("img/19.png"))
my_img20 = ImageTk.PhotoImage(Image.open("img/20.png"))
my_img21 = ImageTk.PhotoImage(Image.open("img/21.png"))
my_img22 = ImageTk.PhotoImage(Image.open("img/22.png"))
my_img23 = ImageTk.PhotoImage(Image.open("img/23.png"))
my_img24 = ImageTk.PhotoImage(Image.open("img/24.png"))
my_img25 = ImageTk.PhotoImage(Image.open("img/25.png"))
my_img26 = ImageTk.PhotoImage(Image.open("img/26.png"))
my_img27 = ImageTk.PhotoImage(Image.open("img/27.png"))


image_list = [my_img1,my_img2,my_img3,my_img4,my_img5,my_img6,my_img7,my_img8,my_img9,my_img10,my_img11,my_img12,my_img13,my_img14,my_img15,my_img16,my_img17,my_img18,my_img19,my_img20,my_img21,my_img22,my_img23,my_img24,my_img25,my_img26,my_img27]

status =  Label(root, text = " Image 1 of " + str(len(image_list)), bd = 1,relief = SUNKEN)

my_label = Label(image=my_img1)
my_label.grid(row= 0, column = 0, columnspan = 3)
my_label.grid_propagate(False)

#Agregando funcionalidad a los botones de adelante para atras#
def forward(image_number):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label = Label(image= image_list[image_number - 1])
    button_forward = Button(root, text=">>", command= lambda: forward(image_number +1))
    button_back = Button(root, text="<<", command = lambda : back(image_number - 1))
    
    if image_number == 27:
      button_forward = Button(root, text=">>", state = DISABLED)

    my_label.grid(row= 0, column = 0, columnspan = 3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)
    
    status =  Label(root, text = " Image "+  str(image_number) + " of " + str(len(image_list)), bd = 1,relief = SUNKEN)
    status.grid(row= 2, column = 0, columnspan = 3, pady= 5, sticky=W+E)


def back(image_number):
  global my_label
  global button_forward
  global button_back

  my_label.grid_forget()
  my_label = Label(image= image_list[image_number - 1])
  my_label.grid_propagate(False)
  button_forward = Button(root, text=">>", command= lambda: forward(image_number +1))
  button_back = Button(root, text="<<", command = lambda : back(image_number - 1))

  if image_number == 1:
    button_back = Button(root, text="<<", state = DISABLED)

  my_label.grid(row= 0, column = 0, columnspan = 3)
  button_back.grid(row=1, column=0)
  button_forward.grid(row=1, column=2)

  status =  Label(root, text = " Image "+  str(image_number) + " of" + str(len(image_list)), bd = 1,relief = SUNKEN)
  status.grid(row= 2, column = 0, columnspan = 3, pady= 5, sticky=W+E)


#Creacion de los botones#
button_back = Button(root, text="<<", command= lambda: back, state = DISABLED)
button_exit = Button(root, text="Exit Program", command = root.quit)
button_forward = Button(root, text=">>", command= lambda: forward(2))

#Dando la posicion de los botones#
button_back.grid(row=1, column=0)
button_back.grid_propagate(False)
button_exit.grid(row=1,column=1)
button_exit.grid_propagate(False)
button_forward.grid(row=1, column=2 , pady= 10)
button_forward.grid_propagate(False)
status.grid(row= 2, column = 0, columnspan = 3, pady= 5, sticky=W+E)

root.mainloop()