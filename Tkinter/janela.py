import tkinter as tk

#criando janela principal
janela = tk.Tk()
janela.title("Voucher Turma 140")
janela.geometry("600x400")

def mudar_texto():
    frase.config(text="OLÁ MUNDO")

frase = tk.Label(janela, text="Clique no botão abaixo")
frase.pack(pady=30)

botao = tk.Button(janela, text="Clique Aqui" , command=mudar_texto)
botao.pack(pady=50)


#manter a janela aberta
janela.mainloop()