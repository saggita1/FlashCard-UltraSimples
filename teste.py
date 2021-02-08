from tkinter import *

root = Tk()

def teste():
    if e.get():
        print('TEEM')

e = Entry(root)
e.pack()
butao = Button(root, text="clique", command=teste).pack()

root.mainloop()