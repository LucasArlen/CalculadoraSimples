from enum import auto
from tkinter import * # Import tkinter
from tkinter import ttk

import sv_ttk

class Calculadora:

    # Faz o calculo
    def calcular(self):
        try:
            self.resultado.set(eval(self.operacao.get()))
        except:
            self.resultado.set("Operação Inválida!")

    # Limpa a tela
    def limpar(self):
        self.operacao.set("")
        self.resultado.set("")

    # Adiciona o valor ao display
    def adicionar(self, valor):
        self.operacao.set(self.operacao.get() + valor)
        
    # Inicializa a calculadora
    def __init__(self, master):

        self.master = master
        master.title("Calculadora")

        style = ttk.Style()
        style.theme_use("clam")
        sv_ttk.set_theme("dark")


        # Variaveis
        self.operacao = StringVar()
        self.resultado = StringVar()

        # window size
        master.geometry("300x300")

        # Display
        display = ttk.Entry(master, textvariable=self.operacao, font=("Arial", 20), justify="left")
        display.grid(row=0, column=0, columnspan=4, sticky="nsew")

        # Blank Resultado
        ttk.Label(master, textvariable=self.resultado, font=("Arial", 20), justify="left").grid(row=1, column=0, columnspan=4, sticky="nsew")


        # Configuração do tamanho das colunas
        master.columnconfigure(0, weight=1)
        master.columnconfigure(1, weight=1)
        master.columnconfigure(2, weight=1)
        master.columnconfigure(3, weight=1)

        # Configuração do tamanho das linhas
        master.rowconfigure(0, weight=1)
        master.rowconfigure(1, weight=1)
        master.rowconfigure(2, weight=1)
        master.rowconfigure(3, weight=1)
        master.rowconfigure(4, weight=1)
        master.rowconfigure(5, weight=1)
        master.rowconfigure(6, weight=1)

        # Botões
        ttk.Button(master, text="7", command=lambda: self.adicionar("7")).grid(row=2, column=0, sticky="nsew")
        ttk.Button(master, text="8", command=lambda: self.adicionar("8")).grid(row=2, column=1, sticky="nsew")
        ttk.Button(master, text="9", command=lambda: self.adicionar("9")).grid(row=2, column=2, sticky="nsew")
        ttk.Button(master, text="+", command=lambda: self.adicionar("+")).grid(row=2, column=3, sticky="nsew")
        ttk.Button(master, text="4", command=lambda: self.adicionar("4")).grid(row=3, column=0, sticky="nsew")
        ttk.Button(master, text="5", command=lambda: self.adicionar("5")).grid(row=3, column=1, sticky="nsew")
        ttk.Button(master, text="6", command=lambda: self.adicionar("6")).grid(row=3, column=2, sticky="nsew")
        ttk.Button(master, text="-", command=lambda: self.adicionar("-")).grid(row=3, column=3, sticky="nsew")
        ttk.Button(master, text="1", command=lambda: self.adicionar("1")).grid(row=4, column=0, sticky="nsew")
        ttk.Button(master, text="2", command=lambda: self.adicionar("2")).grid(row=4, column=1, sticky="nsew")
        ttk.Button(master, text="3", command=lambda: self.adicionar("3")).grid(row=4, column=2, sticky="nsew")
        ttk.Button(master, text="*", command=lambda: self.adicionar("*")).grid(row=4, column=3, sticky="nsew")
        ttk.Button(master, text="0", command=lambda: self.adicionar("0")).grid(row=5, column=0, sticky="nsew")
        ttk.Button(master, text=".", command=lambda: self.adicionar(".")).grid(row=5, column=1, sticky="nsew")
        ttk.Button(master, text="=", command=self.calcular).grid(row=5, column=2, sticky="nsew")
        ttk.Button(master, text="/", command=lambda: self.adicionar("/")).grid(row=5, column=3, sticky="nsew")
        ttk.Button(master, text="C", command=self.limpar).grid(row=6, column=0, columnspan=4, sticky="nsew")

        # Enter for calculate
        master.bind("<Return>", lambda event: self.calcular())
        master.bind("<KP_Enter>", lambda event: self.calcular())


# Inicia a aplicação
if __name__ == "__main__":
    root = Tk()
    my_gui = Calculadora(root)
    root.mainloop()
