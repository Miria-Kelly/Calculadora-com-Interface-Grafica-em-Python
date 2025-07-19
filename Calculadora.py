import tkinter as tk

def clicar(num):
    entrada_var.set(entrada_var.get() + str(num))

def apagar():
    novo = entrada_var.get()
    entrada_var.set(novo[:-1])

def calcular():
    try:
        resultado = eval(entrada_var.get())
        entrada_var.set(str(resultado))

    except:
        entrada_var.set("erro")


def pressionar_tecla(event):
    tecla = event.char

    if tecla.isdigit() or tecla in "-*+/":
         clicar(tecla)
    elif tecla == "\r":

        calcular()
    elif tecla == "\x08":
        apagar()

janela = tk.Tk()
janela.title("Calculadora")
janela.geometry("310x230")

entrada_var = tk.StringVar()
entrada = tk.Entry(janela, textvariable=entrada_var, bd=5, width=15, font=("Arial", 18))
entrada.grid(row=0, column=0, columnspan=3)


janela.bind("<KeyPress>", pressionar_tecla)

botaoApagar = tk.Button(janela, text="<-", width=3, height=2, command=apagar)
botaoApagar.grid(row=0, column=3)
botaoApagar = tk.Button(janela, text="=", width=3, height=2, command=calcular)
botaoApagar.grid(row=0, column=4)

#lambda pra nao chamar a função assim q iniciar de iniciar

botao1 = tk.Button(janela, text="1", width=7, height=3, command=lambda: clicar(1))
botao1.grid(row=1, column=0, padx=2, pady=3)


botao2 = tk.Button(janela, text="2", width=7, height=3, command=lambda: clicar(2))
botao2.grid(row=1, column=1, padx=2, pady=3)

botao3 = tk.Button(janela, text="3", width=7, height=3, command=lambda: clicar(3))
botao3.grid(row=1, column=2, padx=2, pady=3)


botao4 = tk.Button(janela, text="4", width=7, height=3, command=lambda: clicar(4))
botao4.grid(row=2, column=0, padx=2, pady=3)

botao5 = tk.Button(janela, text="5", width=7, height=3, command=lambda: clicar(5))
botao5.grid(row=2, column=1, padx=2, pady=3)

botao6 = tk.Button(janela, text="6", width=7, height=3, command=lambda: clicar(6))
botao6.grid(row=2, column=2, padx=2, pady=3)

botao7 = tk.Button(janela, text="7", width =7, height=3, command=lambda: clicar(7))
botao7.grid(row=3, column=0, padx=2, pady=3)

botao8 = tk.Button(janela, text="8", width=7, height=3, command=lambda: clicar(8))
botao8.grid(row=3, column=1, padx=2, pady=3)

botao9 = tk.Button(janela, text="9", width=7, height=3, command=lambda: clicar(9))
botao9.grid(row=3, column=2, padx=2, pady=3)

botao0 = tk.Button(janela, text="0", width = 7, height=3, command=lambda: clicar(0))
botao0.grid(row=3, column=3, padx=2, pady=3)

botao_soma = tk.Button(janela, text="+", width=3, height=2, command=lambda: clicar("+"))
botao_soma.grid(row=2, column=3)
botao_mult = tk.Button(janela, text="*", width=3, height=2, command=lambda: clicar("*"))
botao_mult.grid(row=2, column=4)
botao_div = tk.Button(janela, text="/", width=3, height=2, command=lambda: clicar("/"))
botao_div.grid(row= 1, column=3)
botao_sub = tk.Button(janela, text="-", width=3, height=2, command=lambda: clicar("-"))
botao_sub.grid(row=1, column=4)

janela.mainloop()