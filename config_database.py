import sqlite3

# funções
def inserir(eng, pt):
    banco = sqlite3.connect('database_palavras.db')
    cursor = banco.cursor()
    cursor.execute(f"INSERT INTO pessoas VALUES('{eng}', '{pt}')")
    banco.commit()
    banco.close()

def deletar(eng=0, pt=0):
    banco = sqlite3.connect('database_palavras.db')
    cursor = banco.cursor()
    if eng !=0:
        cursor.execute(f"DELETE FROM pessoas WHERE eng = '{eng}'")
        banco.commit()
        banco.close()
        return 
    elif pt != 0:
        cursor.execute(f"DELETE FROM pessoas WHERE port = '{pt}'")
        banco.commit()
        banco.close()
        return
    else:
        banco.close()
        return

