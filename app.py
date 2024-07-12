from customtkinter import *
from user_interface import UserInterface
from machine_interface import MachineInterface
    
class Nutshell:
    def __init__(self, master=None):
        root.resizable(False, False)
        root.geometry('450x600')
        root.title('Nutshell')
        set_appearance_mode('dark')

        root.grid_columnconfigure(0, weight=1)

        self.titulo = CTkLabel(master, text='Nutshell - An Active Directory Manager')
        self.titulo.grid(row=0, column=0, padx=20, pady=20, columnspan=3)

        self.combobox = CTkComboBox(master, values=['Usuário', 'Máquina'], width=250, command=self.opcao)
        self.combobox.set('Selecione uma das opções')
        self.combobox.grid(row=1, column=0, padx=20, pady=(0, 5), columnspan=3)
        
        

    def opcao(self, escolha):
        print(f'Você escolheu a opção {escolha}')

        if escolha == 'Usuário':
            UserInterface()

        elif escolha == 'Máquina':
            MachineInterface()


root = CTk()
Nutshell(root)
root.mainloop()
