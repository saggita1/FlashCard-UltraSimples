from tkinter import *
import sqlite3
from config_database import inserir, deletar

root = Tk()
root.geometry("500x300")
root.title("FlashCards")

# variáveis globais
tu_at = 0 # Tupla Atual
p_ing = 0 # palavra em inglês
p_pt = 0 # palavra em português

# funções
def carregar_palavras():
    global lista_palavras

    # sqlite config
    banco = sqlite3.connect('database_palavras.db')
    cursor = banco.cursor()
    
    cursor.execute("SELECT * FROM pessoas")
    lista_palavras = cursor.fetchall()
    banco.close()


def confirme():
    #novo = e.get()
    print(e.get().split())


def nova_janela():
    # funções
    def validar():
        if vat.get() == "inserir" and et.get() and et1.get():
            inserir(et.get(), et1.get())
            return
        elif vat.get() == "remover" and (et.get() or et1.get()):
            if et.get():
                deletar(eng=et.get())
                return
            if et1.get():
                deletar(pt=et1.get())
                return 
        else:
            print("ERRO")


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


# carregando as palavras
carregar_palavras()
# label configs
label = Label(root, text=f"\n\n{lista_palavras[tu_at][p_ing]}", font=("Times", 22))
label.pack()

# botões, SÓ PODE USAR O PLACE 
botao1 = Button(root, text="ANTERIOR", font=("Times", 16), bd=4)
botao2 = Button(root, text="PRÓXIMA", font=("Times", 16), bd=4)
confirmar = Button(root, text="CONFIRMAR", font=("Times", 7), activebackground="green", command=carregar_palavras)
confg_data = Button(root, text="DATABASE", font=('Times', 16), bd=4, command=nova_janela)


botao1.place(x=0, y=255)
botao2.place(x=385, y=255)
confirmar.place(x=340, y=180)
confg_data.place(x=0, y=0)
# entrada
e = Entry(root, bd=3)
e.place(x=190, y=180)

root.mainloop()