from tkinter import *
from config_database import inserir, deletar

root = Tk()
root.geometry("500x300")
root.title("FlashCards")

# funções -printa o entry
def confirme():
    #novo = e.get()
    print(e.get().split())


def nova_janela():
    # funções
    def validar():
        if vat.get() == "inserir" and et.get() and et1.get():
            inserir(et.get(), et1.get())
            print("INSERIDO COM SUCESSO")

    top = Toplevel()
    top.title("DATABASE")
    top.geometry("400x150")
    et = Entry(top, width=30) # english
    et.pack()
    et1 = Entry(top, width=30) # portuguese
    et1.place(x=108, y=40)

    # variável
    vat = StringVar()
    vat.set("inserir")

    # dropmenu
    dpm = OptionMenu(top, vat, "inserir", "remover")
    dpm.place(x=0, y=0)

    # inglês ou português labels
    ing = Label(top, text="English").place(x=300, y=0)
    portu = Label(top, text="Portuguese").place(x=300, y=40)

    # botão
    botao = Button(top, text="CONFIRMAR", command=validar).place(x=160, y=70)


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