from customtkinter import *
from tools import Powershell

class TopLevel:
    def __init__(self):
        pass

    def user_creation(self):
        janela = CTkToplevel()
        janela.geometry('350x550')
        janela.resizable(False, False)
        janela.title('Criar usuário')

        janela.grid_columnconfigure(0, weight=1)

        self.titulo = CTkLabel(janela, text='Criar usuário')
        self.titulo.grid(row=0, column=0, padx=20, pady=5, sticky='n')

        self.nomecompleto = CTkEntry(janela, placeholder_text='Nome completo', width=250)
        self.nomecompleto.grid(row=1, column=0, padx=20, pady=10, sticky='n')
        self.nome = CTkEntry(janela, placeholder_text='Nome', width=250)
        self.nome.grid(row=2, column=0, padx=20, pady=10, sticky='n')
        self.sobrenome = CTkEntry(janela, placeholder_text='Sobrenome', width=250)
        self.sobrenome.grid(row=3, column=0, padx=20, pady=10, sticky='n')
        self.nome_de_usuario = CTkEntry(janela, placeholder_text='Nome de usuário, ex: capivara.mestre', width=250)
        self.nome_de_usuario.grid(row=4, column=0, padx=20, pady=10, sticky='n')
        self.nomedominio = CTkEntry(janela, placeholder_text='capivara.mestre@pasaparanagua.com.br', width=250)
        self.nomedominio.grid(row=5, column=0, padx=20, pady=10, sticky='n')
        self.setor = CTkEntry(janela, placeholder_text='Setor', width=250)
        self.setor.grid(row=6, column=0, padx=20, pady=10, sticky='n')
        self.dominio = CTkEntry(janela, placeholder_text='Nome do domínio', width=250)
        self.dominio.grid(row=7, column=0, padx=20, pady=10, sticky='n')
        self.senha = CTkEntry(janela, placeholder_text='Senha', width=250)
        self.senha.grid(row=8, column=0, padx=20, pady=10, sticky='n')
        self.descricao = CTkEntry(janela, placeholder_text='Descrição', width=250)
        self.descricao.grid(row=9, column=0, padx=20, pady=10, sticky='n')

        self.criar = CTkButton(janela, text='Criar', fg_color='#65B307', command=self.criar_usuario)
        self.criar.grid(row=10, column=0, padx=20, pady=20, sticky='n')

    def criar_usuario(self):
        nomecompleto = self.nomecompleto.get()
        nome = self.nome.get()
        sobrenome = self.sobrenome.get()
        usuario = self.nome_de_usuario.get()
        nome_dominio = self.nomedominio.get()
        setor = self.setor.get()
        dominio = self.dominio.get()
        senha = self.senha.get()
        descricao = self.descricao.get()

        Powershell.create_ADUser(nomecompleto, nome, sobrenome, usuario, nome_dominio, setor, dominio, senha, descricao)
