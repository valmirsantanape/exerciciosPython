from tkinter import *
from tkinter import messagebox
import random

def no():
    messagebox.showinfo("", "Obrigado bro")
    quit()
def motionMause(event):
    btnYes.place(x=random.randint(0, 500), y=random.randint(0, 500))

root = Tk()
root.geometry("600x600")
root.title("suivey")
root.resizable(width=False, height=False)
root['bg'] = 'white'
label = Label(root, text="Oi linda. \nQuer namorar comigo? ", font="Arial 20 bold", bg='white').pack()
btnYes = Button(root, text='NO', font="Arial 20 bold")
btnYes.place(x=170, y=100)
btnYes.bind('<Enter>', motionMause)
btnNo  = Button(root, text="Yes", font="Arial 20 bold", command=no).place(x=350, y=100)
root.mainloop()
