from tkinter import *

root = Tk()
root.geometry("500x300")
root.title("FlashCards")

# funções -printa o entry
def confirme():
    #novo = e.get()
    print(e.get().split())

def nova_janela():
    top = Toplevel()
    top.title("DATABASE")
    top.geometry("400x200")
    et = Entry(top).pack()
    


# label configs
label = Label(root, text="\n\nRYAN", font=("Times", 22))
label.pack()

# botões, SÓ PODE USAR O PLACE 
botao1 = Button(root, text="ANTERIOR", font=("Times", 16), bd=4)
botao2 = Button(root, text="PRÓXIMA", font=("Times", 16), bd=4)
confirmar = Button(root, text="CONFIRMAR", font=("Times", 7), activebackground="green", command=confirme)
confg_data = Button(root, text="DATABASE", font=('Times', 16), bd=4, command=nova_janela)


botao1.place(x=0, y=255)
botao2.place(x=385, y=255)
confirmar.place(x=340, y=180)
confg_data.place(x=0, y=0)
# entrada
e = Entry(root, bd=3)
e.place(x=190, y=180)

root.mainloop()