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

class UserInterface:
    def __init__(self, master=None):
        pass
        self.user_creation = TopLevel()

        self.usuario = CTkEntry(master, placeholder_text='Usuário', width=400)
        self.usuario.grid(row=2, column=0, padx=(10, 5), pady=0, sticky='w', columnspan=2)

        self.criar_user = CTkButton(master, text='Criar usuário', fg_color='#65B307', command=self.criar)
        self.criar_user.grid(row=2, column=2, padx=5, pady=10, sticky='e')

        self.habilitar_user = CTkButton(master, text='Habilitar', command=self.habilitar)
        self.habilitar_user.grid(row=3, column=0, padx=5, pady=5, sticky='e')

        self.desabilitar_user = CTkButton(master, text='Desabilitar', command=self.desabilitar)
        self.desabilitar_user.grid(row=3, column=1, padx=5, pady=5, sticky='e')

        self.desbloquear_user = CTkButton(master, text='Desbloquear', command=self.desbloquear)
        self.desbloquear_user.grid(row=3, column=2, padx=5, pady=5, sticky='e')

        self.grupolbl = CTkLabel(master, text='Opções para grupo')
        self.grupolbl.grid(row=4, column=0, padx=20, pady=10, columnspan=3)

        self.usuariogrupo = CTkEntry(master, placeholder_text='Usuário', width=200)
        self.usuariogrupo.grid(row=5, column=0, padx=5, pady=(10, 5), sticky='n', columnspan=3)

        self.grupo = CTkEntry(master, placeholder_text='Grupo do AD', width=200)
        self.grupo.grid(row=6, column=0, padx=5, pady=5, sticky='n', columnspan=3)

        self.adicionar = CTkButton(master, text='Adicionar para grupo', command=self.adicionar_para_grupo)
        self.adicionar.grid(row=7, column=0, padx=5, pady=10, sticky='e')

        self.remover = CTkButton(master, text='Remover do grupo', command=self.remover_do_grupo)
        self.remover.grid(row=7, column=1, padx=5, pady=10, sticky='e')

        self.mover = CTkButton(master, text='Mover para grupo')
        self.mover.grid(row=7, column=2, padx=5, pady=10, sticky='e')

        self.exportar = CTkButton(master, text='Exportar para CSV', command=self.exportarcsv)
        self.exportar.grid(row=8, column=0, padx=5, pady=5, sticky='e')

        self.importar = CTkButton(master, text='Importar para CSV', command=self.importarcsv)
        self.importar.grid(row=8, column=1, padx=5, pady=5, sticky='e')

        self.editar = CTkButton(master, text='Editar pelo CSV', command=self.editarcsv)
        self.editar.grid(row=8, column=2, padx=5, pady=5, sticky='e')


    def criar(self):
        self.user_creation.user_creation()

    def habilitar(self):
        Powershell.enable_ADUser(self.usuario.get())

    def desabilitar(self):
        Powershell.disable_ADUser(self.usuario.get())

    def desbloquear(self):
        Powershell.unlock_ADUser(self.usuario.get())

    def adicionar_para_grupo(self):
        Powershell.add_member_to_group(self.grupo.get(), self.usuariogrupo.get())

    def remover_do_grupo(self):
        Powershell.remove_user_from_group(self.grupo.get(), self.usuariogrupo.get())

    def exportarcsv(self):
        Powershell.export_userdata_from_ad_to_csv(r'C:\Users\thiago.farias\Desktop')

    def importarcsv(self):
        Powershell.import_userdata_from_csv_to_AD()
    
    def editarcsv(self):
        Powershell.edit_userdata_by_csv()
