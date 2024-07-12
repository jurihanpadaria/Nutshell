from customtkinter import *
from tools import Powershell

class MachineInterface:
    def __init__(self, master=None):
        pass

        self.computador = CTkEntry(master, placeholder_text='Computador', width=400)
        self.computador.grid(row=2, column=0, padx=(10, 5), pady=0, sticky='w', columnspan=2)
        
        self.grupo = CTkEntry(master, placeholder_text='Grupo', width=400)
        self.grupo.grid(row=3, column=0, padx=5, pady=5, sticky='w', columnspan=2)

        self.remover_computador = CTkButton(master, text='Remover do AD', fg_color='#DC143C',command=self.remover)
        self.remover_computador.grid(row=3, column=1, padx=5, pady=5, sticky='e')

        self.adicionar_computador = CTkButton(master, text='Adicionar', command=self.adicionar)
        self.adicionar_computador.grid(row=4, column=0, padx=5, pady=5, sticky='e')

        

    def adicionar(self):
        Powershell.add_computer_to_group()

    def remover(self):
        Powershell.remove_computer_from_AD()
    