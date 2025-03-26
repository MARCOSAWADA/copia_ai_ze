import mysql.connector

from tkinter import *
from tkinter import ttk, messagebox

conexao = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "cliente_tk"
)

cursor = conexao.cursor()

janela = Tk()
janela.title("WELCOME TO THE OUTWORLD MORTAL KOMBAT")
janela.geometry("600x600")

# Label e imputs de entrada
Label(janela, text="ID: ").grid(row=0, column=0, padx=5, pady=5)
# Entry = input
# "state=DISABLED" = deixa um campo que não pode ser editado
id = Entry(janela, state=DISABLED, width=5)
id.grid(row=0, column=1, padx=5, pady=5)

Label(janela, text="NOME DO LUTADOR: ").grid(row=1, column=0, padx=5, pady=5)
nome = Entry(janela, width=30)
nome.grid(row=1, column=1, padx=5, pady=5)

Label(janela, text="EMAIL: ").grid(row=2, column=0, padx=5, pady=5)
email = Entry(janela, width=30)
email.grid(row=2, column=1, padx=5, pady=5)

Label(janela, text="TELEFONE: ").grid(row=3, column=0, padx=5, pady=5)
telefone = Entry(janela, width=30)
telefone.grid(row=3, column=1, padx=5, pady=5)

# ________________________2ºSEGUNDO______________________________

# Definindo a fonte personalizada
import tkinter.font as tkFont  # Importando o módulo font
fonte_personalizada = tkFont.nametofont("TkDefaultFont")  # Pega a fonte padrão do sistema
fonte_personalizada.actual()  # Asegura que as configurações sejam aplicadas
fonte_personalizada.configure(size=12)  # Ajuste o tamanho da fonte conforme necessário


# Listar Clientes

tabela = ttk.Treeview(janela, columns=("ID" , "Nome" , "Email" , "Telefone"), show="headings")
tabela.heading("ID" , text="ID")
tabela.heading("Nome" , text="Nome do Lutador")
tabela.heading("Email" , text="Email")
tabela.heading("Telefone" , text="Telefone")

tabela.column("ID" , width=30)
tabela.column("Nome" , width=150)
tabela.column("Email" , width=150)
tabela.column("Telefone" , width=150)

# Aplicando a fonte personalizada na tabela
tabela.tag_configure("fonte_tabela", font=fonte_personalizada)

tabela.grid(row=5, column=0, columnspan=4, padx=40, pady=80)

cursor.execute("SELECT * FROM cliente")
for row in cursor.fetchall():
    tabela.insert("", END, values=row)




# ________________________1ºPRIMEIRO______________________________
# FUNÇÕES:
# "a função get estará na variável da linha do Entry"

def cadastrar():
    nome_bd = nome.get()
    email_bd = email.get()
    telefone_bd = telefone.get()

    if nome and email and telefone:
        cursor.execute("INSERT INTO cliente (nome_cliente, email, telefone) VALUES (%s, %s, %s)", (nome_bd, email_bd, telefone_bd))
        conexao.commit()

        nome.delete(0, END)
        email.delete(0, END)
        telefone.delete(0, END)
        
        tabela.insert("" , END, values=(cursor.lastrowid, nome_bd, email_bd, telefone_bd))

    else:
        messagebox.showwarning("Atenção", "Preencha todos os campos.")


btn_cadastrar = Button(janela, text="Cadastrar", command=cadastrar)
btn_cadastrar.grid(row=4, column=0, padx=5, pady=5)


janela.mainloop()