from PIL import Image
from customtkinter import *
from random import choice
from user_creation import UserCreation
from tools import Powershell, UIFunctions
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo

funky = UIFunctions()

# Interface do Nutshell (Depois eu arrumo essa bagunça)
class UserInterface:
    def __init__(self, master=None):
        pass

        # Containeres
        # Container Inicial - Usuário e botões
        self.primeirocontainer = CTkFrame(master)
        self.primeirocontainer.grid(row=0, column=0, padx=20, pady=10, columnspan=3)

        self.containeruserinterface = CTkFrame(self.primeirocontainer)
        self.containeruserinterface.grid(row=1, column=0, padx=20, pady=(0, 5))

        self.containerbotoes = CTkFrame(self.primeirocontainer)
        self.containerbotoes.grid(row=2, column=0, padx=20, pady=(0, 10))

        # Segundo container - Opções
        self.segundocontainer = CTkFrame(master)
        self.segundocontainer.grid(row=3, column=0, padx=20, pady=10, sticky='w', columnspan=3)

        self.containergrupo = CTkFrame(self.segundocontainer)
        self.containergrupo.grid(row=0, column=0, padx=10, pady=10, sticky='nw')

        self.containerarquivos = CTkFrame(self.segundocontainer)
        self.containerarquivos.grid(row=0, column=1, padx=(0, 10), pady=10, sticky='nw')

        self.containermaquina = CTkFrame(self.segundocontainer)
        self.containermaquina.grid(row=0, column=2, padx=(0, 10), pady=10, sticky='nw')

        # Widgets
        self.titulo = CTkLabel(self.primeirocontainer, text='Welcome to Fulgore')
        self.titulo.grid(row=0, column=0, padx=20, pady=5)

        self.usuario = CTkEntry(self.containeruserinterface, placeholder_text='Usuário',
                                width=285)
        self.usuario.grid(row=1, column=0, padx=(10, 5), pady=0, sticky='w')

        self.criar_user = CTkButton(self.containeruserinterface, text='Criar usuário',
                                    fg_color='#02B126',
                                    hover_color='#01791A',
                                    command=self.criar)
        self.criar_user.grid(row=1, column=1, padx=5, pady=10, sticky='e')

        self.habilitar_user = CTkButton(self.containerbotoes, text='Habilitar', command=self.habilitar)
        self.habilitar_user.grid(row=0, column=0, padx=5, pady=5, sticky='e')

        self.desabilitar_user = CTkButton(self.containerbotoes, text='Desabilitar', command=self.desabilitar)
        self.desabilitar_user.grid(row=0, column=1, padx=5, pady=5, sticky='e')

        self.desbloquear_user = CTkButton(self.containerbotoes, text='Desbloquear', command=self.desbloquear)
        self.desbloquear_user.grid(row=0, column=2, padx=5, pady=5, sticky='e')

        # Checkbox e widgets de grupos
        self.grupocheck = CTkCheckBox(self.containergrupo, text='Opções para grupo', command=self.check_grupo)
        self.grupocheck.grid(row=0, column=0, padx=10, pady=10, sticky='w')

        self.usuario_no_grupo = CTkEntry(self.containergrupo, placeholder_text='Usuário do grupo', width=140)
        self.grupo_do_usuario = CTkEntry(self.containergrupo, placeholder_text='Grupo do usuário', width=140)
        self.add_para_grupo = CTkButton(self.containergrupo, text='Adicionar para grupo', fg_color='#02B126',
                                        hover_color='#01791A', command=self.adc)
        self.remover_do_grupo = CTkButton(self.containergrupo, text='Remover do grupo', fg_color='#FC0137',
                                          hover_color='#B20027', command=self.rmv)

        # Checkbox e widgets de arquivos
        self.arquivocheck = CTkCheckBox(self.containerarquivos, text='Opções para arquivos', command=self.check_arquivo)
        self.arquivocheck.grid(row=0, column=0, padx=10, pady=10, sticky='w')

        self.nomearquivo = CTkEntry(self.containerarquivos, placeholder_text='Nome do arquivo', width=140)
        self.patharquivo = CTkEntry(self.containerarquivos, placeholder_text='Lugar para salvar', width=140)
        self.exportarcsv = CTkButton(self.containerarquivos, text='Exportar para CSV', command=self.exportar)
        self.importarcsv = CTkButton(self.containerarquivos, text='Importar arquivo CSV', command=self.importar)

        # Checkbox e widgets de máquina
        self.maquinacheck = CTkCheckBox(self.containermaquina, text='Opções para máquinas', command=self.check_maquina)
        self.maquinacheck.grid(row=0, column=0, padx=10, pady=10, sticky='w')

        self.maquinasource = CTkEntry(self.containermaquina, placeholder_text='Computador', width=140)
        self.grupotarget = CTkEntry(self.containermaquina, placeholder_text='Grupo', width=140)
        self.mover = CTkButton(self.containermaquina, text='Adicionar', command=self.adicionar_maquina)
        self.remover = CTkButton(self.containermaquina, text='Remover', command=self.remover_maquina)

    # Funções para ativar as checkboxes
    def check_grupo(self):
        if self.grupocheck.get() == 1:
            self.usuario_no_grupo.grid(row=1, column=0, padx=5, pady=5, sticky='n')
            self.grupo_do_usuario.grid(row=2, column=0, padx=5, pady=(0, 5), sticky='n')
            self.add_para_grupo.grid(row=3, column=0, padx=5, pady=(10, 5), sticky='n')
            self.remover_do_grupo.grid(row=4, column=0, padx=5, pady=(0, 10), sticky='n')

        else:
            self.usuario_no_grupo.grid_remove()
            self.grupo_do_usuario.grid_remove()
            self.add_para_grupo.grid_remove()
            self.remover_do_grupo.grid_remove()

    def check_arquivo(self):
        if self.arquivocheck.get() == 1:
            self.nomearquivo.grid(row=1, column=0, padx=5, pady=5, sticky='n')
            self.patharquivo.grid(row=2, column=0, padx=5, pady=(0, 5), sticky='n')
            self.exportarcsv.grid(row=3, column=0, padx=5, pady=(10, 5), sticky='n')
            self.importarcsv.grid(row=4, column=0, padx=5, pady=(0, 10), sticky='n')
        else:
            self.nomearquivo.grid_remove()
            self.patharquivo.grid_remove()
            self.exportarcsv.grid_remove()
            self.importarcsv.grid_remove()

    def check_maquina(self):
        if self.maquinacheck.get() == 1:
            self.maquinasource.grid(row=1, column=0, padx=5, pady=5, sticky='n')
            self.grupotarget.grid(row=2, column=0, padx=5, pady=(0, 5), sticky='n')
            self.mover.grid(row=3, column=0, padx=5, pady=(10, 5), sticky='n')
            self.remover.grid(row=4, column=0, padx=5, pady=(0, 10), sticky='n')
        else:
            self.maquinasource.grid_remove()
            self.grupotarget.grid_remove()
            self.mover.grid_remove()
            self.remover.grid_remove()

    # Funções para todos os botões
    # Primeiro container
    def criar(self):
        creation_exec = UserCreation
        creation_exec()

    def habilitar(self):
        Powershell.enable_user(self.usuario.get())

    def desabilitar(self):
        Powershell.disable_user(self.usuario.get())

    def desbloquear(self):
        Powershell.unlock_user(self.usuario.get())

    # Segundo container
    # Grupos
    def adc(self):
        Powershell.add_member_to_group(ad_group=self.grupo_do_usuario.get(), ad_user=self.usuario_no_grupo.get())

    def rmv(self):
        Powershell.remove_user_from_group(ad_group=self.grupo_do_usuario.get(), ad_user=self.usuario_no_grupo.get())

    # Arquivos
    def exportar(self):
        Powershell.export_userdata_from_ad_to_csv(csv_path=self.patharquivo.get())

    def importar(self):
        filetypes = (('Text files', '*.txt'), ('All files', '*.*'))
        filename = fd.askopenfilename(title='Abra um arquivo', initialdir='/', filetypes=filetypes)
        showinfo(title='Arquivo selecionado', message=filename)
        

    # Máquinas
    def adicionar_maquina(self):
        Powershell.add_computer_to_group(ad_computer=self.maquinasource.get(), ad_group=self.grupotarget.get())

    def remover_maquina(self):
        Powershell.remove_computer_from_ad()


# Root
class Nutshell:
    def __init__(self, master=None):
        root.resizable(False, False)
        root.title('Fulgore')
        root.iconbitmap('./favicon.ico')
        set_appearance_mode('dark')

        quote = choice(['Não vá querer inventar moda de quebrar o programa, lazarento.',
                        'Não é bug, é feature!',
                        'Ó azidéia, mermão!',
                        'Java? Tô fora! Pego meu COBOL e vou embora!',
                        'Vamos deletar um usuário hoje, fera?',
                        'A maior injustiça foi terem tirado Chaves da televisão.',
                        'E lá vamos nós!'])

        nutshell_exec = UserInterface
        nutshell_exec()

        neko_arc = CTkImage(light_image=Image.open('./Neko-Arc.png'), dark_image=Image.open('./Neko-Arc.png'),
                            size=(100, 150))

        self.img = CTkLabel(master, image=neko_arc, text='')
        self.img.grid(row=12, column=0, padx=20, pady=10, columnspan=3)

        # CRIAR LOG DAS AÇÕES AQUI

        # FIM

        self.warning = CTkLabel(master, text=f'"{quote}"')
        self.warning.grid(row=13, column=0, padx=20, pady=10, columnspan=3)


root = CTk()
Nutshell(root)
root.mainloop()
