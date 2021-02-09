from tkinter import *
import sqlite3
from config_database import inserir, deletar
from PIL import ImageTk, Image

root = Tk()
root.geometry("500x300")
root.title("FlashCards")
root.iconbitmap("laptop_computer_files_archive_documents_pc_icon_179700.ico")
# variáveis globais
tu_at = 0 # Tupla Atual

# funções
def carregar_palavras():
    global lista_palavras
    global tu_at

    # sqlite config
    banco = sqlite3.connect('database_palavras.db')
    cursor = banco.cursor()
    
    cursor.execute("SELECT * FROM pessoas")
    lista_palavras = cursor.fetchall()
    banco.close()

    # resetando a tupla atual e os botões
    tu_at = 0
    confirmar["state"] = NORMAL
    botao1["state"] = DISABLED
    botao2["state"] = NORMAL

    if not lista_palavras: # caso a lista esteja vazia
        lista_palavras = [("", "")]
        botao1["state"] = DISABLED
        botao2["state"] = DISABLED
        confirmar["state"] =DISABLED
    elif len(lista_palavras) == 1:
        botao1["state"] = DISABLED
        botao2["state"] = DISABLED

def confirme():
    global corr_erra
    if e.get() == lista_palavras[tu_at][1]:
        corr_erra.config(text="CORRETA", bg="green", font=("Times", 20))
     
    else:
        corr_erra.config(text="ERRADA", bg="red", font=("Times", 20))

def nova_janela():
    # funções
    def validar():
        if vat.get() == "inserir" and et.get() and et1.get():
            inserir(et.get(), et1.get())
            et.delete(0, END)
            et1.delete(0, END)
            return
        elif vat.get() == "remover" and (et.get() or et1.get()):
            if et.get():
                deletar(eng=et.get())
                et.delete(0, END) 
                et1.delete(0, END)
                return 
            if et1.get():
                deletar(pt=et1.get())
                et.delete(0, END)
                et1.delete(0, END)
                return 
        else:
            et.delete(0, END)
            et1.delete(0, END)
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

def proxima():
    global tu_at
    global e
    global corr_erra

    # correta e errada
    corr_erra.config(text="", bg="white")

    # PRINCIPAL
    tu_at += 1
    label.configure(text=f"\n\n{lista_palavras[tu_at][0]}")

    # ESTADO DO BOTÃO
    if tu_at == len(lista_palavras) - 1:
        botao2["state"] = DISABLED # desabilitando o botão pra não dar erro
    botao1["state"] = NORMAL # Ativando botão ANTERIOR

    e.delete(0, END) # limpando a Entry

def anterior():
    global tu_at
    global e
    global corr_erra

    # Correta e errada
    corr_erra.config(text="", bg="white")

    # PRINCIPAL
    tu_at -= 1
    label.configure(text=f"\n\n{lista_palavras[tu_at][0]}")

    # ESTADO DO BOTÃO
    if tu_at == 0:
        botao1["state"] = DISABLED # desabilitando 
    botao2["state"] = NORMAL # Ativando botão PRÓXIMO

    e.delete(0, END) # limpando a entry

def iniciar():
    global lista_palavras
    # sqlite config
    banco = sqlite3.connect('database_palavras.db')
    cursor = banco.cursor()
    
    cursor.execute("SELECT * FROM pessoas")
    lista_palavras = cursor.fetchall()
    banco.close()

    if not lista_palavras: # caso a lista esteja vazia
        lista_palavras = [("", "")]
        botao1["state"] = DISABLED
        botao2["state"] = DISABLED
        confirmar["state"] =DISABLED
    elif len(lista_palavras) == 1:
        botao1["state"] = DISABLED
        botao2["state"] = DISABLED

def recarregar():
    global label
    carregar_palavras()
    label.config(text=f"\n\n{lista_palavras[tu_at][0]}")
    # Correta e errada
    corr_erra.config(text="", bg="white")


# imagem
my_img = ImageTk.PhotoImage(Image.open("img_botao.png"))

# botões, SÓ PODE USAR O PLACE 
botao1 = Button(root, text="ANTERIOR", font=("Times", 16), bd=4, command=anterior)
botao1["state"] = DISABLED
botao2 = Button(root, text="PRÓXIMA", font=("Times", 16), bd=4, command=proxima)
confirmar = Button(root, text="CONFIRMAR", font=("Times", 7), activebackground="green", command=confirme)
confg_data = Button(root, text="DATABASE", font=('Times', 16), bd=4, command=nova_janela)
reload_database = Button(root, image=my_img, command=recarregar).place(x=140, y=6)

# label configs
# carregando as palavras
iniciar()
label = Label(root, text=f"\n\n{lista_palavras[tu_at][0]}", font=("Times", 26))
label.pack()

# correta e errada
corr_erra = Label(root, text="", bg="white")
corr_erra.place(x=190, y=220)

# colocar na tela
botao1.place(x=0, y=255)
botao2.place(x=385, y=255)
confirmar.place(x=340, y=180)
confg_data.place(x=0, y=0)
# entrada
e = Entry(root, bd=3)
e.place(x=190, y=180)

root.mainloop()
