from tkinter import *
from tkinter import ttk
import base64
from time import sleep
from typing import List
from Persistencia import Persistencia
from util import util
import _thread as th

class Tela_Principal:

    def __init__(self) -> None:

        self.font_menu = 'Calibri 14 bold'
        self.font_titulo = 'Calibri 24 bold'
        self.font_msg = 'Calibri 12 bold'
        self.font_default = 'Calibri 14'
        self.font_default_labels = 'Calibri 14 bold'

        self.color_theme = 'Black'
        self.color_contrast = 'White'
        self.dict_color_msg = {"info": "Green", "warning": "DarkOrange", "error": "Red", "wait": "Navy"}
        self.color_ask = 'SlateBlue'
        
        self.height_window = 532

        #CARREGA AS IMAGENS PARA O SISTEMA
        self.setImagensBase64()

        self.current_frame = None
        self.frame_msg = None

        self.current_setor = None
        self.new_setor = None

        self.window()
    
    def window(self):
        self.windowMain = Tk()
        self.windowMain.geometry(util().toCenterScreen(850, 532))
        self.windowMain['bg'] = 'Yellow'
        self.windowMain.title("IGTEC - SERVICE SYSTEM")
        self.windowMain.resizable(False, False)
        
        #ABRIR MENU LATERAL
        self.menu()

        #ABRIR HOME
        self.home()

        self.windowMain.mainloop()

    def menu(self):
        
        #FRAME DO MENU
        self.frameMenu = Frame(self.windowMain, width=100, height=self.height_window, bg=self.color_theme)
        self.frameMenu.pack(side=LEFT)

        imagem_inicio_white = PhotoImage(data=base64.b64decode(self.imagem_inicio_white))
        self.btInicio = Button(self.frameMenu, text='Home', font=self.font_menu, image=imagem_inicio_white, width=96, height=80, compound=TOP, bd=0, bg=self.color_theme, fg=self.color_contrast, command=self.home)
        self.btInicio.imagem = imagem_inicio_white
        self.btInicio.place(x=0, y=0)

        imagem_cliente_white = PhotoImage(data=base64.b64decode(self.imagem_cliente_white))
        self.btCliente = Button(self.frameMenu, text='Cliente', font=self.font_menu, image=imagem_cliente_white, width=96, height=80, compound=TOP, bd=0, bg=self.color_theme, fg=self.color_contrast, command='')
        self.btCliente.imagem = imagem_cliente_white
        self.btCliente.place(x=0, y=90)
        
        imagem_novo_white = PhotoImage(data=base64.b64decode(self.imagem_novo_white))
        self.btNovo = Button(self.frameMenu, text='Novo', font=self.font_menu, image=imagem_novo_white, width=96, height=80, compound=TOP, bd=0, bg=self.color_theme, fg=self.color_contrast, command=lambda: th.start_new_thread(self.TelaNovo, ()))
        self.btNovo.imagem = imagem_novo_white
        self.btNovo.place(x=0, y=180)

        imagem_servicos_white = PhotoImage(data=base64.b64decode(self.imagem_servicos_white))
        self.btServico = Button(self.frameMenu, text='Serviços', font=self.font_menu, image=imagem_servicos_white, width=96, height=80, compound=TOP, bd=0, bg=self.color_theme, fg=self.color_contrast, command=self.servicos)
        self.btServico.imagem = imagem_servicos_white
        self.btServico.place(x=0, y=270)

        imagem_despesas_white = PhotoImage(data=base64.b64decode(self.imagem_despesas_white))
        self.btDespesas = Button(self.frameMenu, text='Despesas', font=self.font_menu, image=imagem_despesas_white, width=96, height=80, compound=TOP, bd=0, bg=self.color_theme, fg=self.color_contrast, command=self.despesas)
        self.btDespesas.imagem = imagem_despesas_white
        self.btDespesas.place(x=0, y=360)
        
        imagem_ajustes_white = PhotoImage(data=base64.b64decode(self.imagem_ajustes_white))
        self.btAjustes = Button(self.frameMenu, text='Ajustes', font=self.font_menu, image=imagem_ajustes_white, width=96, height=80, compound=TOP, bd=0, bg=self.color_theme, fg=self.color_contrast, command=self.ajustes)
        self.btAjustes.imagem = imagem_ajustes_white
        self.btAjustes.place(x=0, y=450)

    def home(self):
        
        #DESTROI O FRAME ATUAL
        self.destruirFrameOnly()

        #DESMACA O SETOR ATUAL
        self.desmarcarSetor()

        self.btInicio['bg'] = 'White'
        self.btInicio['fg'] = 'Black'
        imagem_inicio_black = PhotoImage(data=base64.b64decode(self.imagem_inicio_black))
        self.btInicio['image'] = imagem_inicio_black
        self.btInicio.image = imagem_inicio_black
        self.current_setor = self.btInicio

        #FRAME DE EXIBIÇÃO HOME
        self.frameHome = Frame(self.windowMain, width=750, height=self.height_window, bg=self.color_contrast)
        self.frameHome.pack(side=RIGHT)

        #LOGO
        logo = PhotoImage(data=base64.b64decode(self.imagem_logo))
        w = Label(self.frameHome, image=logo, bd=0)
        w.imagem = logo
        w.place(x=-5, y=-40)
        
        #ATRIBUI AO FRAME ATUAL
        self.current_frame = self.frameHome

    def servicos(self):
        #DESTROI O FRAME ATUAL
        self.destruirFrameOnly()

        #DESMACA O SETOR ATUAL
        self.desmarcarSetor()

        self.btServico['bg'] = 'White'
        self.btServico['fg'] = 'Black'
        imagem_servicos_black = PhotoImage(data=base64.b64decode(self.imagem_servicos_black))
        self.btServico['image'] = imagem_servicos_black
        self.btServico.image = imagem_servicos_black
        self.current_setor = self.btServico

        #FRAME DE EXIBIÇÃO SERVIÇOS
        self.frameServicos = Frame(self.windowMain, width=750, height=self.height_window, bg=self.color_contrast)
        self.frameServicos.pack(side=RIGHT)

        lblTitulo = Label(self.frameServicos, text='SERVIÇOS', font=self.font_titulo, bg=self.color_contrast, width=44)
        lblTitulo.place(x=0, y=10)
        
        #ATRIBUI AO FRAME ATUAL
        self.current_frame = self.frameServicos

    def despesas(self):
        #DESTROI O FRAME ATUAL
        self.destruirFrameOnly()

        #DESMACA O SETOR ATUAL
        self.desmarcarSetor()

        self.btDespesas['bg'] = 'White'
        self.btDespesas['fg'] = 'Black'
        imagem_despesas_black = PhotoImage(data=base64.b64decode(self.imagem_despesas_black))
        self.btDespesas['image'] = imagem_despesas_black
        self.btDespesas.image = imagem_despesas_black
        self.current_setor = self.btDespesas

        #FRAME DE EXIBIÇÃO AJUSTES
        self.frameDespesas = Frame(self.windowMain, width=750, height=self.height_window, bg=self.color_contrast)
        self.frameDespesas.pack(side=RIGHT)
        
        lblTitulo = Label(self.frameDespesas, text='DESPESAS', font=self.font_titulo, bg=self.color_contrast, width=44)
        lblTitulo.place(x=0, y=10)

        #ATRIBUI AO FRAME ATUAL
        self.current_frame = self.frameDespesas
    
    def ajustes(self):
        #DESTROI O FRAME ATUAL
        self.destruirFrameOnly()

        #DESMACA O SETOR ATUAL
        self.desmarcarSetor()

        self.btAjustes['bg'] = 'White'
        self.btAjustes['fg'] = 'Black'
        imagem_ajustes_black = PhotoImage(data=base64.b64decode(self.imagem_ajustes_black))
        self.btAjustes['image'] = imagem_ajustes_black
        self.btAjustes.image = imagem_ajustes_black
        self.current_setor = self.btAjustes

        #FRAME DE EXIBIÇÃO AJUSTES
        self.frameAjustes = Frame(self.windowMain, width=750, height=self.height_window, bg=self.color_contrast)
        self.frameAjustes.pack(side=RIGHT)
        
        lblTitulo = Label(self.frameAjustes, text='AJUSTES', font=self.font_titulo, bg=self.color_contrast, width=44)
        lblTitulo.place(x=0, y=10)

        #ATRIBUI AO FRAME ATUAL
        self.current_frame = self.frameAjustes

    def destruirFrameOnly(self):
        #DESTROI A TELA ATUAL CASO EXISTA
        if self.current_frame:
            self.current_frame.destroy()

    def TelaNovo(self):
        
        self.destruirFrameOnly()
        
        #DESMACA O SETOR ATUAL
        self.desmarcarSetor()

        self.btNovo['bg'] = 'White'
        self.btNovo['fg'] = 'Black'
        imagem_novo_black = PhotoImage(data=base64.b64decode(self.imagem_novo_black))
        self.btNovo['image'] = imagem_novo_black
        self.btNovo.image = imagem_novo_black
        self.current_setor = self.btNovo

        #FRAME DE EXIBIÇÃO AJUSTES
        self.frameNovo = Frame(self.windowMain, width=750, height=self.height_window, bg=self.color_contrast)
        self.frameNovo.pack(side=RIGHT)

        #ATRIBUI AO FRAME ATUAL
        self.current_frame = self.frameNovo

        def definirSubcategorias():

            if comboCategoria.get() != '':
                #MENSAGEM DE AGUARDE
                th.start_new_thread(self.msg, ("wait", "CARREGANDO SUBCATEGORIAS ..."))

                #LIMPA OS COMBO
                comboSubcategoria1['values'] = tuple([])
                comboSubcategoria2['values'] = tuple([])

                #TODAS AS SUBCATEGORIAS
                subcategorias = Persistencia().getSubcategorias(comboCategoria.get())

                #VALORES DOS COMBOBOX
                comboSubcategoria1['values'] = tuple(
                    subcategorias
                )

                #VALORES DOS COMBOBOX
                comboSubcategoria2['values'] = tuple(
                    subcategorias
                )

                #CASO EXISTA UMA SUBCATEGORIAS
                if len(subcategorias) > 0:
                    #EXIBIR A PRIMEIRA
                    comboSubcategoria1.current(0)
                    comboSubcategoria2.current(0)

                #DESTROI A MSG DE AGUARDE
                self.destroyMsg(None)

        lblTitulo = Label(self.current_frame, text='NOVO SERVIÇO', font=self.font_titulo, bg=self.color_contrast, width=44)
        lblTitulo.place(x=0, y=10)

        #NOME DO CLIENTE
        lblNomeCliente = Label(self.current_frame, text='Nome Cliente:', font=self.font_default_labels, bg=self.color_contrast)
        lblNomeCliente.place(x=50, y=70)

        etNomeCliente = Entry(self.current_frame, font=self.font_default, width=20)
        etNomeCliente.place(x=50, y=100)

        #ENDEREÇO
        lblEndereco = Label(self.current_frame, text='Endereço:', font=self.font_default_labels, bg=self.color_contrast)
        lblEndereco.place(x=270, y=70)

        etEndereco = Entry(self.current_frame, font=self.font_default, width=20)
        etEndereco.place(x=270, y=100)

        #CONTATO
        lblContato = Label(self.current_frame, text='Contato:', font=self.font_default_labels, bg=self.color_contrast)
        lblContato.place(x=490, y=70)

        etContato = Entry(self.current_frame, font=self.font_default, width=20)
        etContato.place(x=490, y=100)

        #DATA
        lblData = Label(self.current_frame, text='Data:', font=self.font_default_labels, bg=self.color_contrast)
        lblData.place(x=50, y=140)

        etData = Entry(self.current_frame, font=self.font_default, width=20)
        etData.insert(0, util().getData())
        etData.place(x=50, y=170)

        #HORA
        lblHora = Label(self.current_frame, text='Hora:', font=self.font_default_labels, bg=self.color_contrast)
        lblHora.place(x=270, y=140)
        
        etHora = Entry(self.current_frame, font=self.font_default, width=20)
        etHora.place(x=270, y=170)

        #SERVIÇO
        lblCategoria = Label(self.current_frame, text='Categoria:', font=self.font_default_labels, bg=self.color_contrast)
        lblCategoria.place(x=50, y=210)

        comboCategoria = ttk.Combobox(self.current_frame, font=self.font_default, width=13, state="readonly")
        comboCategoria.place(x=50, y=240)
        comboCategoria.bind("<Return>", lambda: th.start_new_thread(definirSubcategorias, (None)))
        
        imagem_buscar_sub = PhotoImage(data=base64.b64decode(self.imagem_buscar_sub))
        btBuscarSub = Button(self.current_frame, image=imagem_buscar_sub, font=self.font_menu, bd=0, bg=self.color_contrast, width=50, command= lambda: th.start_new_thread(definirSubcategorias, ()))
        btBuscarSub.image = imagem_buscar_sub
        btBuscarSub.place(x=210, y=230)

        #SUBCATEGORIA 1
        lblSubcategoria1 = Label(self.current_frame, text='Subcategoria 1:', font=self.font_default_labels, bg=self.color_contrast)
        lblSubcategoria1.place(x=270, y=210)

        comboSubcategoria1 = ttk.Combobox(self.current_frame, font=self.font_default, width=18, state="readonly")
        comboSubcategoria1.place(x=270, y=240)

        #SUBCATEGORIA 2
        lblSubcategoria2 = Label(self.current_frame, text='Subcategoria 2:', font=self.font_default_labels, bg=self.color_contrast)
        lblSubcategoria2.place(x=490, y=210)

        comboSubcategoria2 = ttk.Combobox(self.current_frame, font=self.font_default, width=18, state="readonly")
        comboSubcategoria2.place(x=490, y=240)

        #VALOR DO SERVIÇO
        lblValorServico = Label(self.current_frame, text='Valor do Serviço:', font=self.font_default_labels, bg=self.color_contrast)
        lblValorServico.place(x=50, y=280)

        etValorServico = Entry(self.current_frame, font=self.font_default, width=20)
        etValorServico.insert(0, "0,00")
        etValorServico.place(x=50, y=310)

        #VALOR DE MATERIAL
        lblValorMaterial = Label(self.current_frame, text='Valor de Materiais:', font=self.font_default_labels, bg=self.color_contrast)
        lblValorMaterial.place(x=270, y=280)

        etValorMaterial = Entry(self.current_frame, font=self.font_default, width=20)
        etValorMaterial.insert(0, "0,00")
        etValorMaterial.place(x=270, y=310)

        #DESCONTO
        lblDesconto = Label(self.current_frame, text='Desconto:', font=self.font_default_labels, bg=self.color_contrast)
        lblDesconto.place(x=490, y=280)

        etDesconto = Entry(self.current_frame, font=self.font_default, width=20)
        etDesconto.insert(0, "0,00")
        etDesconto.place(x=490, y=310)

        #PAGAMENTO
        lblPagamento = Label(self.current_frame, text='Forma de pagamento:', font=self.font_default_labels, bg=self.color_contrast)
        lblPagamento.place(x=50, y=350)

        comboPagamento = ttk.Combobox(self.current_frame, font=self.font_default, width=18, state="readonly")
        
        comboPagamento['values'] = tuple(
            ['DINHEIRO', 'CARTÃO', 'PIX', 'OUTRO'])
        comboPagamento.current(0)
        comboPagamento.place(x=50, y=380)

        #OBSERVAÇÃO
        lblObs = Label(self.current_frame, text='Observações:', font=self.font_default_labels, bg=self.color_contrast)
        lblObs.place(x=270, y=350)

        etObs = Entry(self.current_frame, font=self.font_default, width=42)
        etObs.place(x=270, y=380)

        def salvar():

            try:
                #INSERE O SERVIÇO NO BANCO DE DADOS
                Persistencia().insertServico(
                    etNomeCliente.get(),
                    etEndereco.get(),
                    etContato.get(),
                    etData.get(),
                    etHora.get(),
                    comboCategoria.get(),
                    comboSubcategoria1.get(),
                    comboSubcategoria2.get(),
                    float(etValorServico.get().replace(",", ".")),
                    float(etValorMaterial.get().replace(",", ".")),
                    float(etDesconto.get().replace(",", ".")),
                    comboPagamento.get(),
                    etObs.get()
                )
                
                #LIMPAR CAMPOS
                limpar()

                #SUCESSO
                th.start_new_thread(self.msg, ("info", f"SERVIÇO CADASTRADO !", ))
            except:
                th.start_new_thread(self.msg, ("error", "VERIFIQUE OS CAMPOS E TENTE NOVAMENTE !", ))
                
        def limpar():
            #LIMPAR TODOS OS CAMPOS
            etNomeCliente.delete(0, END)
            etEndereco.delete(0, END)
            etContato.delete(0, END)

            etData.delete(0, END)
            etData.insert(0, util().getData())

            etHora.delete(0, END)

            etValorServico.delete(0, END)
            etValorServico.insert(0, "0,00")

            etValorMaterial.delete(0, END)
            etValorMaterial.insert(0, "0,00")

            etDesconto.delete(0, END)
            etDesconto.insert(0, "0,00")

            comboPagamento.current(0)

            etObs.delete(0, END)

        #BPTÃO DE SALVAR
        btSalvar = Button(self.current_frame, text='Salvar', font=self.font_menu, bd=0, bg='Green', fg=self.color_contrast, width=10, command= lambda: self.ask("wait", "CADASTRAR SERVIÇO ?", salvar))
        btSalvar.place(x=50, y=450)
        
        btCancelar = Button(self.current_frame, text='Cancelar', font=self.font_menu, bd=0, bg='Red', fg=self.color_contrast, width=10, command= lambda: self.ask(None, "CANCELAR CADASTRO ?", limpar))
        btCancelar.place(x=160, y=450)

        
        #FOCAR NO CAMPO DE NOME
        etNomeCliente.focus_force()

        #MENSAGEM DE AGUARDE
        th.start_new_thread(self.msg, ("wait", "CARREGANDO TIPOS DE SERVIÇOS ..."))

        #VALORES DOS COMBOBOX
        comboCategoria['values'] = tuple(
            Persistencia().getTipoServicos()
        )

        #DESTROI A MSG DE AGUARDE
        self.destroyMsg(None)

    def msg(self, type, msg):
        
        #CASO JÁ EXISTA UMA MENSAGEM
        if self.frame_msg:
            #APAGA A ATUAL
            self.frame_msg.destroy()

        #FRAMA QUE ARMAZENA OS COMPONENTES DA MENSAGEM
        self.frame_msg = Frame(self.current_frame, width=750, height=35, bg=self.dict_color_msg[type])
        self.frame_msg.place(x=0, y=498)

        #FOCAR APENAS NA MENSAGEM
        self.frame_msg.grab_set()

        #EXIBE A MENSAGEM
        lblMsg = Label(self.frame_msg, text=msg, font=self.font_msg, bg=self.dict_color_msg[type], fg=self.color_contrast)
        lblMsg.place(x=0, y=5)

        if type != 'wait':
            btOk = Button(self.frame_msg, text="OK", font=self.font_msg, fg=self.dict_color_msg[type], bg=self.color_contrast, bd=0, width=10, height=0, command=lambda: self.destroyMsg(None))
            btOk.place(x=660, y=3)

            #FOCA NO BOTÃO
            btOk.focus_force()
        
            #PROCURA O APERTA DO ENTER
            btOk.bind("<Return>", self.destroyMsg)

    def ask(self, type, msg, command):
        
        #CASO JÁ EXISTA UMA MENSAGEM
        if self.frame_msg:
            #APAGA A ATUAL
            self.frame_msg.destroy()

        #FRAMA QUE ARMAZENA OS COMPONENTES DA MENSAGEM
        self.frame_msg = Frame(self.current_frame, width=750, height=35, bg=self.color_ask)
        self.frame_msg.place(x=0, y=498)

        #FOCAR APENAS NA MENSAGEM
        self.frame_msg.grab_set()

        def yes(event):

            if type == 'wait':
                #SUCESSO
                th.start_new_thread(self.msg, ("wait", "AGUARDE ...", ))

                #EXECUTA A FUNÇÃO RECEBIDA DO BOTÃO
                th.start_new_thread(command, ())
            
            else:
                #EXECUTA O COMANDO EM SERIE
                command()

            #DESTROI O FRAME
            self.frame_msg.destroy()

        #EXIBE A MENSAGEM
        lblMsg = Label(self.frame_msg, text=msg, font=self.font_msg, bg=self.color_ask, fg=self.color_contrast)
        lblMsg.place(x=0, y=5)

        btYes = Button(self.frame_msg, text="Sim", font=self.font_msg, fg=self.color_ask, bg=self.color_contrast, bd=0, width=10, height=0, command=lambda: yes(None))
        btYes.place(x=560, y=3)

        btNo = Button(self.frame_msg, text="Não", font=self.font_msg, fg=self.color_ask, bg=self.color_contrast, bd=0, width=10, height=0, command=lambda: self.destroyMsg(None))
        btNo.place(x=660, y=3)

        #FOCA NO BOTÃO
        btYes.focus_force()
        
        #PROCURA O APERTA DO ENTER
        btYes.bind("<Return>", yes)

    def destroyMsg(self, event):
        #APAGA A MENSAGEM
        self.frame_msg.destroy()

    def desmarcarSetor(self):
        
        if self.current_setor:
            #DESMARCA BOTÃO
            self.current_setor['bg'] = 'Black'
            self.current_setor['fg'] = 'White'
            
            if self.current_setor['text'] == 'Home':
                #RETORNA AO PADRÃO
                imagem_inicio_white = PhotoImage(data=base64.b64decode(self.imagem_inicio_white))
                self.current_setor['image'] = imagem_inicio_white
                self.current_setor.image = imagem_inicio_white

            elif self.current_setor['text'] == 'Novo':
                #RETORNA AO PADRÃO
                imagem_novo_white = PhotoImage(data=base64.b64decode(self.imagem_novo_white))
                self.current_setor['image'] = imagem_novo_white
                self.current_setor.image = imagem_novo_white

            elif self.current_setor['text'] == 'Serviços':
                #RETORNA AO PADRÃO
                imagem_servicos_white = PhotoImage(data=base64.b64decode(self.imagem_servicos_white))
                self.current_setor['image'] = imagem_servicos_white
                self.current_setor.image = imagem_servicos_white

            elif self.current_setor['text'] == 'Despesas':
                #RETORNA AO PADRÃO
                imagem_despesas_white = PhotoImage(data=base64.b64decode(self.imagem_despesas_white))
                self.current_setor['image'] = imagem_despesas_white
                self.current_setor.image = imagem_despesas_white

            elif self.current_setor['text'] == 'Ajustes':
                #RETORNA AO PADRÃO
                imagem_ajustes_white = PhotoImage(data=base64.b64decode(self.imagem_ajustes_white))
                self.current_setor['image'] = imagem_ajustes_white
                self.current_setor.image = imagem_ajustes_white

    def setImagensBase64(self):
        
        self.imagem_inicio_white = 'iVBORw0KGgoAAAANSUhEUgAAADAAAAAwCAYAAABXAvmHAAAABmJLR0QA/wD/AP+gvaeTAAABOklEQVRoge3XLU6DQRSG0fsRAiRNMIgmOAwbwKDrWEMdG0BikVgWgUODAVaAwmHQCAwJhhB6UCNI/79OOxDmLKB5bibtm0ZUVbU06KNfuqMVnOALA5yV7pkZGpwbdoG10n0TYQOXI+KTK2yV7hwJHdxMiE/usF269wd08TBDfPKI3dLdERGBPTzNEZ88Y790/AFeWsQnrzgsFd/D2wLxyTuOVh3fx0eG+OQTx6uKTwOV23IHz/iByi3/4Jk+ULldYTNXfAfXK4xPFh888w9Ubu0HT/uBym3+wbP4QOU2dvCGvu3oRcR9RHRbPd1y7ETErWmDJ/9A5TZ+8CxvoHIb4DR1N9PeDuZ87qyappnY+Lv/4s2gHlBaPaC09dwfOO1XI/ev2p9/gXpAafWA0uoBpdUDSqsHVFVV/W/f06ytkPSmv/YAAAAASUVORK5CYII='
        self.imagem_inicio_black = 'iVBORw0KGgoAAAANSUhEUgAAADAAAAAwCAYAAABXAvmHAAAABmJLR0QA/wD/AP+gvaeTAAABOElEQVRoge2XoW7CUBSGPwghS0iwS+ZmeIEZNI5XgIeYnJ2c3UPMoTfFG6BwGDQCQzJTsRbTmzRdL72lpz00nC/5XXvz/Wlu/hQMw2iSZZpO8gr8ATHwruxSiR7wASS5fAJ9Ra8ghsAX/+VdVsCDml0JI+AHv7zLGhgXvJ9/rlUegU2BhC9b4Cl3hlqBZ2BXIFCWPTDJnKNS4AU4VBTP5ghMtQrMgFMNeZdfYN52gSUQCci7FJ3VGG6gpOR9Ecc3UJ0oUDZQTWQoJT8CvluWT/APXiWqDpR0NqnDVVw7UNLJD14QdQdKOofUKQipgZKOG7yLSA+UdCJg4ZNva6DqJgbenHTP1yZDEvBMk1x0vPlfvDKsgDYDwbNC7lMWkbvV+S9gBbSxAtpYAW2sgDZWQBsrYBiGcd+cAeC40B/rJq6jAAAAAElFTkSuQmCC'
        
        self.imagem_cliente_white = 'iVBORw0KGgoAAAANSUhEUgAAADAAAAAwCAYAAABXAvmHAAAABmJLR0QA/wD/AP+gvaeTAAAB0ElEQVRoge3Yz28NURTA8XNbaiNqw6YrllppiPgLWIutHysWYk9Y8B8QTYWdPeEfUOwtumoTe3akC540EfU+Fp02bfPe1Ht3ah653+Suzpx7vidzMnNnIgqFQuG/Aicxh2V8r9YyHmGmbb++4ACe4Jf+rOExJtr23UYl/65GfCdvR6oJPB1AfoP5tr0jYnPm68amH2uYzq0/1kAP14fcZzwiruUWb6KBcxm553OLp9wN0ImIg0Omd1JKh3LqN3EHtJQbEc008Ckj92Nu8SYaWMjIfd1A/TwwUz0Sh3mMnmjbPyIirB8PBmWube9NMIE3A8gvYH/b3tuomphXP05r1k+qoyW/FUzjIZbQqdYSHhiVmS8UCoXRAWOYGiJvCk2cxQYHk7iCV1jBT1wYIP9ilbOCl7iMyb103ih8Gs+w2uMt+wN3MF6Tvw93q2t3slrtfWovxI/jBbp1B5yKD7iFWRyu1ixuV7Hd6OI5jjUlfxXf/qBw03zFpVz5my2Ib6WLG3WOfT/qcSYi3kczX205dCPibEppsVewTu7+LvG/xVhE3OsXrLsDnyPiyF4YDcGXlNLRXoG6BrJ/eTRJSqmn6yiMSBalgbb55xsoFAqFdvkNO6T52MfWNtwAAAAASUVORK5CYII='
        self.imagem_cliente_black = 'iVBORw0KGgoAAAANSUhEUgAAADAAAAAwCAYAAABXAvmHAAAABmJLR0QA/wD/AP+gvaeTAAABpUlEQVRoge3Yv08UQRjG8Y+gRwk9lZYCIYr/h7H1R6WFscfoH6GRSLSz12hiLEX9J8DYa0dCgRASI3AWu5eY43bhZuYyq5lv8lR777zPs/tmZ+coFAqF/40lrGEL+7W28AyLGX2dygxe4Aj9Bh1iHb1MHhuZwRfNxof1WcdCvHR28wM9z+J0BEvax6ZtnBZim0/FLoB7getM426C/tF8Nf7dH2gzg98T7AkP8DO2eYoR6meqRZoAPyJqv8c2TxFgI6L2Y4L+0SyqXokhr9HLGfyOZN34AdayOG2gh0/Obn4DF7I4baGn+jxoG6dD1Z3vnPm/WcBT1Sa1V2sTT3Ro5guFQqE7TGE+oG5emm+xIGZxG++wg9+4Pkb9jbpmB29xq15z4lzFKxw4ucv+wiPVUbGJ83hc/3a4/qBe+8okjF/CGxyPaDysb1jFMuZqLeNhfe20+mO8xsVU5u+ojn6hx8ZQ7eJmrPkHGYwPP437oeavCfu/J7WOsBIS4EMHzA/0PiTAdgeMD7TdZPJcS4D+uIknzEiv2XbCVJQAufnnAxQKhUJe/gCyKGTbBPfqzgAAAABJRU5ErkJggg=='
        
        self.imagem_novo_white = 'iVBORw0KGgoAAAANSUhEUgAAADAAAAAwCAYAAABXAvmHAAAABmJLR0QA/wD/AP+gvaeTAAABJklEQVRoge2ZMU7EMBBF3yBahES/9Zbbcko4CLAnoKamRbTUK2EO8CmgADYekk28g9G8dpzJfH2P7TiQxGJTH5CkbwnMJudYMt/JnJf/BVJANK4ASStJt5KKPhkYMwsnX5G0lbT2aqw2jKQV8AhceAmOwA7YmNnLUNBz4Jr44uGjhqta0HOgAGctKjqAYmbnQwFPwN78jKS2P/zvVagHUkA03Qs4HTtw7qlzKmNXwe4dSAHRpIBoRq9CU1n627lG9w6kgGgW64Hfds5WPdG9AykgmsV64Oeczn1gJCkgmmZnoWN9wXXvQAqIxuuBN75c7gbflb7WAp4D9w0KOZRqLd7t9Bp4IP4fwQ64NLPnoWDVATN7AjbADVDa1OZSgDuc4pMkSeJ5B44npH8aQA6SAAAAAElFTkSuQmCC'
        self.imagem_novo_black = 'iVBORw0KGgoAAAANSUhEUgAAADAAAAAwCAYAAABXAvmHAAAABmJLR0QA/wD/AP+gvaeTAAABAUlEQVRoge2ZTQ6CMBBGn8at8QK6NNydEE/glVxQD6CLxkRJKXRoGWrmJd1QKN+Xmf6DoctO8M0rQxvZ2tsv/Lk6ZkCbKQMXoAMcPleH+crXc2kZa88BN6BJMTQU/8ggcGl5AGeJgW4D4j+lHRMZG7IccEw0XQoHnEIVMQOh/NQkqPXvR6HNYwa0qd7AIeHdpavOVGaNgtVHwAxoYwa0SRmFUsm9dw5SfQTMgDY5+8DUzFmkT1QfATOgTc4+MMxpmwfmYAa0KbkWWmUHV30EzIA2sT7w5PdwV/OstB+riEXgXkCIFJGWhu1ccFwlBsDfjLT4EK4tvMdfsojFG4ZhlOcNWtmss+bYuskAAAAASUVORK5CYII='

        self.imagem_servicos_white = 'iVBORw0KGgoAAAANSUhEUgAAADAAAAAwCAYAAABXAvmHAAAABmJLR0QA/wD/AP+gvaeTAAABDUlEQVRoge2YsU7DQAyGPyNWKgRrVzq2I29Z3gPoE5SZnbXq2rVS7wX+Di0DImc1Dakb5G+LfHH8yZdLZEhisbY3SNKPBGatc/xlvpsuD78GUiAaV0DSWNKbpKIjDWs64eQrkhaSnrwaqy+MpDHwBTx4CS7AFpia2aYp6HXghfji4VDDvBb0OlCAuz4qOoOdmd03BTyBX/szktr34X+fQkMgBaIZvMDtqQu7/nW25dRTcPAdSIFoUiCaFIgmBaJJgWhSIJoUiCYFokmBaFIgGm8qUYDR90XwrHRXC3gd+OihkHNZ1gLedHoCfAKPfVTUgi3wbGbrpmC1A2a2AmbAK4ftdGkK8I5TfJIkSTx7iziUbBghU0EAAAAASUVORK5CYII='
        self.imagem_servicos_black = 'iVBORw0KGgoAAAANSUhEUgAAADAAAAAwCAYAAABXAvmHAAAABmJLR0QA/wD/AP+gvaeTAAAA+ElEQVRoge2ZQQ6CMBAAR+NV412P6t8J8QX6JDnQD+ihMSEEit1SlpqdpAcoLTvZ0gIFQ5eNoM17hj5m62+beHN1TECbKYEzUAMOP1b745XOeWkZ688Bd+AaI9QPvpkhwNTSACeJQL2C4L+lGgsyNGU5YB8pnYsWOA5VhASGxqcmg7H+/Sy0ekxAm+IFdhHXpr51xvLTLFh8BkxAGxPQxgS0MQFtYlbiVKZWVtFKX3wGTEAbE9DGBLRZch3I8kVXfAZMQJvQM+CAQ+dY819pO1YRysAzQyBSHpJGN+CF/t5AA1wkAuB3Rip8CpcOvMVvsoiDNwzDyM8HGuapnv76NFMAAAAASUVORK5CYII='

        self.imagem_despesas_white = 'iVBORw0KGgoAAAANSUhEUgAAADAAAAAwCAYAAABXAvmHAAAABmJLR0QA/wD/AP+gvaeTAAACgElEQVRoge2ZO2tUQRiG38+kiBLjFW0SRRBEhCxiESLYWIlapLRIJYKFnWAhaOEf0D9gq403BAURy3gBm0QtYrGgohAUFJZoRNY8FntOmIznnL1wdmcW9qlmvvlm5v3mfjjSgAEDBkQLMAHcBWr0nhpwHzhQpNGKxEual7S97IFpk++SKmb2OatwQ0HFGwovXmpouJ5XWDQDNUmbu6GoA2pmtiWroCgAuqenfcwsU2vREuoLhstqKG+E8ihrhvt+BgYBhKa0PRDq1Or7GYgpgMeSxi2HvEoxXWQTee+dIqIJoN17JCWmJdQRpZ1C3QCYlbRJ0m0zW263cq+oA1dzNHxJfPbk6Qw9A38lzZjZo04bCL0HrmSJB3YD5yWNJaYZYMz3K6QHS6cK/DeAwAXgZ4b/N+BETAFczOjzbJM6K8DhWAI44vU3DCx5PreAOc/2NJYAtnn9TXvl95zAqo69DuxI6wXbxGb2wzONe/lXiV9djXdSypCkQ2km9DHq4j9dRp30C0kHnfxqmgj2FvLfPsCkpAXH9FXSlJl9KGon9D3g8lbSopPfJWkOON1Ra93ewTl9HiP7DngC7I8+gKTfo6w/dVJ+AWeiDyDpewS4ROP2dakDJ6MPwNGwE3joVV0Emn/80OV/Ai2NotZm451Xfe1ILTqFnrXaSRkAy47A+dRuZr8lPfDc96WJogAuq/FzoVcsOem9rH+pjni+f9JEbgBm9l5SRdIdSbUyFDbhpZPeKmlWkoCNkk55vtUe6GkP4Li3zleB58Anz/46tNZcgJtN9v4KMBVaZy7AEHDN29ApC8B0aI0tAYwC5xLhH4FKaE1tA0wmAbwp8ovpNdoR/wDcvofSsO8f3AAAAABJRU5ErkJggg=='
        self.imagem_despesas_black = 'iVBORw0KGgoAAAANSUhEUgAAADAAAAAwCAYAAABXAvmHAAAABmJLR0QA/wD/AP+gvaeTAAACeUlEQVRoge3YS4hOYRgH8B/jtnBJxrVMDMWCJCkWmlATFrISKVGW1uwVzWLKghIpQtjIAjsLyUKKhbIQmdzvDOUyaYzFe4bX5/vmO9+Z76rvX2+953ne83+e/znvnSaaaKKJWmJEEf8YrMZGLEM7Jia+j3iBO7iGy/iUMu5YrEVnwjsXkzEavejBLVxJuL+n5P2N6ehOyAZSlq84gtYheCfgAN6XwNuLriSnVNgufMm0AXLLY8zIw9uK+8Pg/YhdaQRkDRCXE3l4j5WB92e1BLzOw/uqTNx/Id8g/qdRRuRy/ywQb1i8I8tAmClwAX/JAqspoCKoBwFXsSZ6noN9wrScCeUYaPnGUb423Qp3m+X4loK3ZgKeCyv9IDqwGy2RraueBZyOfC34nNh3RvalxXhrOQZ6o/r4pMDKyP4wC3G1/sDFHP+FjLw1E/AFbZF/LPYqvoGsGwEDuC5so2NMxVH0N4KAATzBDuEsEGMzfjSCgMHSg0057xyuZwEfotKX2PqxPnpnUT0LmBT5Tkb245F9fDHeWq4D86P61aj+IKpPKUYyqmzplI6tuJ3UzwjT6GQcitp0ZiGuVhfqw6oh8mjDyxS8NRMwIOw292OBP7vSWdiDN2l4q3mkLMY72D5tO9THgWZYqOUgzkWmP9/wf6DhBVSyC13C+aS+pVJBKjkLVQr//yz0FLNzbPeEw8cNPBJWyDfCB2gVbqMXYwW2YVyBeN9xFjdxV7gvfSdcO07DTMwTVugOLMyTW1GsEw4ZT4W7/FySYjit8Op8qkSuJTiIZ0lOG0p8PxPmCLfTucm/Fb5uQ6Ad54Qu8kroNnNrmlETTTTRREXwC+xgLwTTnFnuAAAAAElFTkSuQmCC'

        self.imagem_ajustes_white = 'iVBORw0KGgoAAAANSUhEUgAAADAAAAAwCAYAAABXAvmHAAAABmJLR0QA/wD/AP+gvaeTAAADCUlEQVRoge2Yz0tUURTHv7cMXahoIVYUZFEQjGsFhTKzFmEEZtuE/oJoUyu3LrKVtajIiLZCrWvpH6A4kkyokGgF7vqBkPlpMXfoebvvzZuZ9960mA/M4t17zrnf8+b+OPdJDRo0qBvAGLDHX/aAsUpiHEhLXEx6JZnAs5GUqyRA3RIATku67OkasX3/D4AB3gAzQA6YAnYJZ9fa5IDH1teUHym9BCYixMbldr3EtwKbCSTwBWh342exBu5JOh7Rvybpqf2tR9h1S7qboK54AIPAVshbfQG0BGxbgNkQ2y1gIPMErLBuYNsRtBoUH7BtAdYc222g2xc7k23UGPNVUrPT/M4Ys+Ox3ZH03mlutjH+IctzAOc5alt0+/YS1lIZaU6h1CmziGc9i/hliO1nYNCN35RBDsOSjoX0TUi6AJTm/IikUyG2RyVdkjRfsyLgJjGrSKAt4h+ohE2g1Y1f7SLOKWYVaYz5JulBleMEuW+M+e42VpvACU/byQj7V5LeSnqiYgk9Jel3hP2utemVNCNpTtLrqpQGoVhVDgEFz19cAIYqiNUDzHvizAM9tQrtwjm2gevAcoy5ugyMOr4DQJdnnEmP/2RN4m3gORtsAbgDPIoh3GXa+i7a5znPODVfKX3ih6oQG5crNYmLIf5g4I2lwTKQ6Nnj7kJnJJ1PcgCHs5JqW6DlAPqB9TJv8hPF+dtmfzeAlTI+60BfquIDSXQA+Qjxhz0+nbbPxxLQkYn4gCDfXg8RuwQwHuKzkqX2kpifIWLaInzaQ3x+pKUz6QtN5t9uohLYCGkfjvC5WmGsdKC4iJfC5jPQ6fE5AmyE+GS3iIE+4m2j43bOtwO3IsSXWAf6k9a7b84C5yTlJR1KeiDLL0k5Y0whqYDuGliV9CGp4B4KKn6JSw/SLeZGUhUfSKJUTi9SLImnqxD70Pou2Od/yuk0E/BdaEaBjzGE54Frjq/3QpM5QBPFm5kvkQJwsd4aYwE89yTwrB5aqi0lfCdrtqetpdoE8tr/sRZJy7XLadCgQaX8ATbXAAP+yrwrAAAAAElFTkSuQmCC'
        self.imagem_ajustes_black = 'iVBORw0KGgoAAAANSUhEUgAAADAAAAAwCAYAAABXAvmHAAAABmJLR0QA/wD/AP+gvaeTAAADd0lEQVRoge2ZTUtVQRjHf/meLjIViwgC29kuUhECLbhKRVlrLblCLi59Az9BBpGVQbkPe6FatgyCCCKKFrqrrBa+La4iZPa6mDnc45xnzpkzt2sJ9w8D9848L/9nzsx5njkDZZRRRinQAMwCv3Wb1X3bBr0UyAetpxSOKjz1WoEpYBXICuPtQt8hoS8LrGhbrZ5cUqMTyFOY2Q3UjIcxSfQJTBoyPVo3GM8DHSVjHcKIQG4JNesZYByYF2Tm9VhGyy4JMtLT/OtoAtYF58W2b0DLVgQA8LAEATzwIeK7iR976sXhSQls0gVcBJpDfW3AHPIsfgauAWeEsQFgAvhi0Z3TtgM0a99dvuRbKbxt1lHLZshC/hNwAagO6ZsyAWqAYR2sFMSQ9hXsszyer9gpwYHU7gKNgr4tgACNwLSjjymfAFYcDF8Hdlj0kwJA695w8JP3CWCEzYnGbNMx5F0DCIKIexIbFJEfepETzkdgV4KuawCglpO0t5aIZvnUaBcMn4+Rr0TO1lk9ZsOwoCPVVKmRITr7VRbZFuC1QCRor1CZXEK1th2WzySRc0lkppFHwA8LgafA4RhbR7SMNAHfiSbIxAAk1APHgBxwi2hhdsKiJy0bWxu22DhpyM1rDjnNqd4lgPBJSmptFr3nKQJ4ZrFxMEFvxiWAJOe2o+FyigAWLTYaHHQ3wbeYk1CbQrbO0p+aj6Qwm6Cz1/jfCFwFdqbwW691zBJkT4Ke0xJK2sSntFwlMIpaDq5LR1pKoxTyw2lj3GsTmxg3jE6gzrNviiAubc5+onXRZR/CJsxE9jWGyAfgXcz4W+B9zLhp2ysPmJBKCbOtAWOozVkLXAJe6v414AVqGdRomTHdn2S36FLiKLAQ4+AXcB844GF7H3Ab+Bljfxk47ks+qZxeBbp9jYfQrW3Z/HiX0y4HmjsUl0sqcDv5eR1oXI+U08BuD/tNwD1HH15HyjSH+gXUod5WZodRhSrmpL31Vw/1kP6zyiJwE/VO3496I9Xp3/2o76O2xGf7rNLpSz4OgxYSxbRBHyK+G/Ccp14czpbApoj/6uOuzxMYIFo6L6MuMPqAK6gNamJBj/Vp2WVjvAZVzJUcHUQvOMzrI5cLjl7+0QUHFK6Y8shZMkc0gJwgl9U2tvSKyQVbdslXKjSgavyA/Azb7Jq1jDK2C/4AAnR7lZrA8aQAAAAASUVORK5CYII='
        
        self.imagem_buscar_sub = 'iVBORw0KGgoAAAANSUhEUgAAADAAAAAwCAYAAABXAvmHAAAABmJLR0QA/wD/AP+gvaeTAAACDUlEQVRoge2Zy0rzQBiGHw9YkIpbUX8QFetevBTBwy2oG3/F+1FBY6VrF249rHTlVahg66b++sfFTKB+5jTTJhNhXvgWk3wzeZ9OZvKlAS8vL68q6w/QBNpAWHK0gRbQ6Mf8swPjMl60F2M1K2A+iiDJ5FAKQBuYMIQuSm1gMu5EGkBYjBdrxXodLtvFoDUogHfgDNgEloG6jmV9LNA5pSrvAmsC8znGWwAuDMaVMXCAD2DPYty/wGcVAGzMRzpwDdCMya8Bu8At8KbjFtjR56RargC6/LznZ4CHlD73OqdXi3qs0gFORV4tw3wvhJyJwAXAhsjbNTCxLfpuuQBYEnl3BiZuRN+GC4C6yOsYmOiIvvV+AcouJf6LttUv2ysbgGnRfjToK3OnLK7/TTYAK6J9bND3RLRXLa6fW0n34pnIq6G2yDzb6Jjo62Qb7aIKs17NZEDEPcjmcPQgC1FVpdQYap+/Qe02HeBaH5O/PMChgfmBA4SoqrIfjQBHOa5TGMAnsN8PATCKKk2cAETRQhVmWZpD3TajlhCFAYSo18UAVdtEr5TjqKp1XZ+LFuypJUShAKZxHgORtSYqBZA0E2nVaeUA5EysAf9+G0A0E1sZ5hMB/D9zrpUGIF8+XOo16UQawFUBRmx1adOpgfq4UNZiToonYNYGANSXkQA1hWUbf0W9e1ib9/Ly8ipeX7gnvAJ++c/9AAAAAElFTkSuQmCC'

        self.imagem_logo = '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YvrpXYRhcC244ILFiy++mKYAAKYSLKZqq6Pw//znP6kGgycCKwAAjTm9DwAAZBMsAACAbIIFAACQTbAAAACyCRYAAEA2wQIAAMgmWAAAANkECwAAIFtb3Xl7woQJxVxzzZWmYHDMN998xSuvvJKmaGSBBRYoZphhhuLll18u3n777TR3dFh44YWLVVZZpVh00UWLRRZZpPz//e9/fzH77LMXs802W/n/zDPPXN7Ic+LEicWbb75ZvPrqq8Vjjz1WPPHEE2V54IEHirvvvrv8eTt573vfW7z77rtpavSZfvrpi9dff71444030pyRMdNMMxXzzDNPMd1006U5rSt+h8mTJ5fbmnYT24mPfOQj5fHOBz7wgXJbEiX+drPOOmu5LYny3//+t/xMxfYititPPfVU5/Yk/r/nnnuKp59+Oq2VoeTO2zUiWLSKBx98MEJQj6UaLNIjYfDMO++8dT9vytTyjW98I71bU73wwguV6gF13ce3Q9lhhx0qF1xwQeWZZ55Jv/HgqgaMyg9+8INKNazUff5WKBdeeGH6bQjVcFWphs2679VQlb322qvy0ksvpVfQnrbYYou6v3urlDXXXLNy/PHHV+666670Gw2u5557rnLOOedUttpqq7rPr+SXarConHvuuekdH90EC+iFYNG4fOADH0jvVHdPPfVU3WVascw555yVb3/725Xnn38+/XbD69prr61svfXWdV9bM5YDDjggvXJqTZw4se77NRTlrLPOSs/a/maaaaa670Gzlm222aZy4403plc/vGK7/M1vfrMyxxxz1H1tSv+LYDGVPhZAlve9732p1t2CCy6Yaq1r1113LZsWvPbaa8X3v//9EfudNthgg+Kiiy6Kk0HFFVdcUay22mrpJ80pmnDQXTRlGQ7R/OqLX/ximmp/0VSo2a2xxhrFZZddVn6Hf/3rXxdrr712+snwim32kUceWTbPe/LJJ4svf/nL6SeQT7AAsrzzzjup1l20gW5Vp556ankAcMYZZzTdQfKmm25a/OUvfyn7aTTrwWP0eWPkjNRB60iJPpjNaueddy4mTZpU3HrrrcXmm2+e5jaH6Ad2+umnl9u6+B9y6byd6R//+EeqTRUHU9F5c+zYsWlO+4gDmXif4/+33nqrPKgcM2ZM2WF3zjnnLOaff/70yPah83Zj0cnw9ttvT1NdxeckOi63ktNOO63Yfffd09TAxfbqueeeK1566aXyzGCU6GwZ35sQ24fo8Lf44osXyy23XPa263Of+1zxy1/+Mk01h/vuu68YN25cmiKsv/76xZ///Oc0NXQ+/vGPF1deeWWaal+xD1pvvfWK8ePHpznNY7vtthuU7+Tzzz9fXjV98cUXy/1vxwAQsS2JQTJi2xHbkhgk4YMf/GDDq8h9ceaZZxa77bZbmqIvdN6uEcGiVTRjH4t6ryPKCSeckB7RWp5++unKJZdcUjnssMMqn/70pyvVA55KNTTU/R17K9VwVanuRCv77rtv2da3GsLSs7QWfSwal2qwSO9Ud8PZnjy3VHcI6VX3T3XHXnbijuWrO/S66+5rqYbYslN49WAkrb1/oiP5ggsuWHfdyugqm2yySfpU1FdvGWVwyvzzz18OXjEQN9xwQzkYxoc//OG66+5P2WijjSrHHHPMgAeY2HnnneuuV+le9LGYSrDINGbMmLqv5fTTT0+PaG6333575Tvf+U5lhRVWqPt7DEWJje4uu+xSufjii9OraG6CRePSDsHioYceSq+4byKAH3zwweXOpN76BqssvPDCZch/8cUX0zP3zYEHHlh3fcroKYLFyJSjjjoqvcN9d8YZZ1RWXXXVuusbzPK5z32uMn78+PSsfXPnnXfWXZfStQgWUwkWmVoxWPz617+ubLjhhnVf90iUuLLxP//zP5Vnn302vcLmIlg0Lq0cLOKz1x8//elPy6sK9dY11GWBBRYoD0D66qabbqq7HmV0FMFi+Mt9992X3t3e3XHHHZV111237nqGo+y9996VN998M72a3sWoePXWo0wpgsVUgkWmVgkW119/fbmjqfdam6nEwdNxxx2XXnVzECwal1YNFksssUR6lb2Ls5D11jFS5Xvf+156ZY09+uijdZcfDWX77bdP70JXX//61+s+vt2KYDG8pa/DUEegaKbmivE5ee2119KrayyGFq+3DkWwqKXzdqa4Q2ZHZ8xaMbpCMwzhFsNjHnrooWlq4KKDafVArLy7cHTSjrt+dnTajt8/OqzHXYSjc1l0WI07CP/73/9OSw/MJz/5ybIzVDz3SNJ5u7FW7Lwdn+EYPrY3t9xyS7HWWmulqeZz8cUXF1tuuWWaqi/uvrvSSiulqdGj0a4ttl/R+bWdVQ8Yi6uuuipNddcOd99uFjGIS3Sa7s3qq69ejubWjGJ0ubPOOitN9Sy2ndF5nK6qwULn7Q4RLFqFKxZ9t+eee9Z9Xb2VcePGVfbff/+yA/cTTzyR1jZw1cBRufnmmyvHHntsZbPNNqtMP/30dZ+3UalusCvVjXFa4/BzxaJxacUrFn2x7bbb1l222crGG2+cXnHPLrroorrLtmupHjSn37y+xRZbrO5y7VRcsRie0pd9/eWXX1532WYsr776anrVPau33GgvrlhMJVhkarZgcdBBB9V9PT2VeeaZp7LffvsN64F7/J1OO+20yhprrFH3NfVUYoSqxx9/PK1l+AgWjUurBYvLLrssvbqeLbnkknWXbdYSnbx7E02D6i3brqWR6FtTb5l2KoLF0JfYh/Xm6KOPrrtsM5f7778/vfr67r333rrLjeYiWEwlWGRqlmDxm9/8pu7r6KnEELBxW/9mcOaZZ5bt3eu9znolhsEdToJF49JKwWLNNddMr6xnrRYqOsriiy+efoOezTTTTHWXbcfSiGAhWAxG6c3Pfvazusu1QultJLoDDjig7nKjtQgWU7nzdhtYYYUViq233jpN9SxuwnXdddfF1rA48cQTs2+iM1h22WWX4uGHHy5vJLbtttumuT373e9+V7YP/u1vf5vmQN/ceOONqVbfNttsU34WW9Gjjz5a3iSvkZtvvjnVgBzHH398qtX3t7/9rdhzzz3TVOtZYIEFUq2+Y489NtWgK8GihV100UXlAXa9u3/XWmONNYqnn366+Oc//1ne9bVZRSfpX/3qV2Xw6cudjz/72c8W66yzTpqCxuIzNeOMM6ap7q655priN7/5TZpqTXGX38svvzxNdbfaaqsVH/3oR9MUMFD7779/qtW38sorp1rrWnvttVOtvt///vepBlMJFi0qrlD0dnZ/kUUWKcPErbfeWo7m1EpOO+20MmD0NuLNTTfdVIarZ599Ns2B+uIz1cjGG2+caq1t8803T7X6zjzzzFQDBuKkk05Ktfp23nnnVGtt48ePL66//vo01d0WW2yRajCVYNGCognT//3f/6Wp+n79618Xjz/+eNn8qZXFcJqPPfZYMXbs2DSnvghOjc7UMrptsMEGqVbf4YcfnmrtYd9990217saNG1cstNBCaQror3322SfVuothrM8999w01fp623aecMIJqQZTCBYtZvrppy+eeeaZNNVdNHuKM/3RVrxdLLroouV9JI466qg0p744U/ujH/0oTcFUBx98cKrV993vfjfV2kOMp97IgQcemGpAf/R2ZTP6DLab6NfYk0YnMRidBIsWEk1+IjT05Cc/+UnZ7KldHXLIIcULL7zQsJ38N77xjeKggw5KUzDFpptummrd9eWmUK3opz/9aap1t+uuu6Ya0B+93fi2t9YEreiAAw5Ite7iuCSaXUMHwaJFxJe3kfvvv7/Ya6+90lT7ipEq3n777YaXZ2O0iuisDqG3O+L2diWsVcWJhp7EXWLjDrpA/3z6059Ote5OP/30VGsvMeLcf//73zTVXbv0KWFwCBYtYN555021+iZPnlwsu+yyaWp0uPbaa4vvfOc7aWqq1Vdfvbyq0yxD6TLyNtlkk1Sr78EHH0y19nLfffelWn0f+9jHUg3oixlmmKGYaaaZ0lR3F1xwQaq1n/POOy/VurMtoZZg0eTWW2+94tVXX01T3cVBdGzsRqPvfe97XTbk559/fnHbbbelKZhizTXXTLXurr766lRrTzGqS0/WXXfdVAP6IoZrbuSGG25ItfZz5ZVXplp3ggW1BIsmdsoppzTcUDXqbzFa7LDDDuW9ByJ87bjjjmkuTLX88sunWnd33HFHqrWnRsEp7hsD9F2jbcmkSZNSrT01GnVxjjnmSDUQLJpWHCg3GtLuqaeeSjXiRnnzzDNPmoKuGnUsbPdg0WgY3RgMAei70bwteeONN3q8amFkKGoJFk1qpZVWSrXuYug3fQigb6Kjck+eeOKJVGtfMfBD3G37i1/8YjkUZgyXGfMaNbEEultwwQVTrbvRsC3ZbLPNisUXX7zYfvvti9122634zGc+U57U6214a0YXwaIJXXjhhcWTTz6ZprracMMNi6222ipNATniZlajQQxDfc4555RD615zzTVpLtAfs846a6p1N1q2JXHD2l/96lflHfzjJOeECRPST2AKwaIJRb+BnjgogMHz+uuvpxpAY43uoTRaggX0RrBoMo1uanXRRRelGjAYDIAADAbbEphCsGgyX/va11Ktq7iXxdZbb52mAACguQgWTSTaQcfN7uo5++yzUw0AAJqPYNFEjj766FTrbosttkg1AABoPoJFE7nkkktSrau999471QAAoDkJFk3ikUceSbXudt9991QDAIDmJFg0icsuuyzVultxxRVTDQCGztixY8s7LMcNFEeqxL0RHn/88eKAAw5IrwpoFYJFk7j99ttTravlllsu1QBgaL3yyivFxz/+8fKOyiNV5pprrmKRRRYpjj322OJHP/pRemVAKxAsmsQ999yTal195CMfSTUAGDrLLLNMqjWPzTbbLNWAViBYNIm47FvP0ksvnWoAMHTeeOONVGseb731VqoBrUCwaBLRprSe97znPakGtIuVVlqpuP/++8u79Q5Hefvtt4vHHnusOP/884vFFlssvQro6umnny4eeuihNNUcDjrooFQDWsF01Z1Oy9yHPjZ4jc7gx8F5tM0cTjPPPHPdMyqnn3568eUvfzlN9W666aZLta7OOeec4gtf+EKaYiTMN998Zbtj6ovmej31EXrzzTeL2WabLU2NjEabuIUXXrh49tln09TwmHPOOYvXXnstTY2Mo446qvjWt76VptpTo7/7oosuWjzxxBNpqj1tsskmxVVXXZWmuutpnxOWXXbZsn/fO++8k+YMr3ht8dx//OMf05zmcN555xWf//zn01RXxxxzTHHIIYekKUabueeeuzj55JOLnXbaKc0ZxSJYtIoHH3ww9hQ9lmqwSI8cPmPGjKn7WqrBIj2ib+qtI0p/18Pgm3feeev+bZQppRos0jvV3cSJE+suM5ylkYUWWqjuMkNZNt544/TsIyv+bvVeX7uURhZZZJG6y7RTqQaL9NvWV28ZpXGpBov07nV39NFH111GGR2lGiwq5557bvo0jG6aQjWJWWedNdW6eumll1INaAevv/56qo2s/fffP9UAYHBoCpVpsJpCjRs3rmxzPa1YR6xrJEUzlxi1aqaZZkpzmtu7775bjBkzpthxxx3TnDyaQjWmKVT/xWANMZzmSLrtttuKNddcM021n0Z/d02hGjeFoj5NoeiJplBTCRaZBitYfPazny1++9vfpqmpPvzhDxd//etf09TI2G233YozzzwzTbWOwfpoCxaNCRYDs8QSS5RlqA7wJk2aVB5cHnrooWlOV7FdWWWVVdJU+xEsBIvBJljQE8GiRgSLVtHOfSyOOuqouuuJMtL23Xffuq+rmcucc86ZXn0+fSwaF30smrdsscUW6Tft7s4776y7TLuURvSxKFOX0s+ij4XSU9HHYip9LJpEo5sAxTCRI2ny5MmpBrSSuKIKAMNFsGgS0eSpJ7/4xS9SbWTEuPfRBC1eY7OV1VdfPb1KAABGVLpy0RLauSlUWGeddequa+aZZ06PoJ5675mmUMNXNIVq3rL11lun37Q7TaHqL9cuRVOowS+aQik9FU2hpnLFool8/etfT7Wu/vvf/5YjuACDSwdWoK+qx0yp1t1o2ZastdZaxRFHHFEce+yxRTVMuYEv3QgWTWSrrbZKte6MNACDL0byAOiLRv0Nx44dm2rt6zvf+U4xfvz4cqS5Aw44oDj44IOLc845p3j00UfTI0CwaDo9DVf34IMPFjfffHOaAvoqhrztSbsHi3nmmSfVuosroUDf/ec//0m17hp919rFPvvsk2pdRT9M6CBYNJmjjjoq1bpbZ511Ug3oq9deey3Vuov7GbSzRgc7jd4XoLvnnnsu1bpbfPHFU619jYbwRD7BoglF+8V64o7SX/ziF9MU0BcPPPBAqnUXN/drZ40Odp555plUA/qi0bZktdVWS7X2NWbMmFSDngkWTSjaL84444xpqqtoz3j33XenKaA3d9xxR6p11+7DFa+55pqp1t2//vWvVAP6Iu5W38j00zukAt+CJnXPPfekWndx/wbto6Fv7rrrrlTrrt2bF66yyiqp1l2j9wXo7uGHH061+rbbbrtUG12eeOKJVAPBommNGzeuHHWhJ7POOmuqAY1ceumlqVZfo4PvVrbMMsukWn033nhjqgF91ag51O67755q7afRdvL2229PNRAsmlqME73UUkulqa5iPO155503TQE9+fe//11MnDgxTXV32GGHpVp72W233VKtuxgpa9KkSWkK6KsLLrgg1bpbf/31U639NGpWefXVV6caCBZNL4aZ7cmrr75azDHHHGlqdIpmYfW89dZbqQZFce6556Zad1tuuWWqtZeDDjoo1bo7//zzUw3oj+OPPz7V6vvJT36Sau1ll112SbXuLrroolQDwaIlvP3226nW3RtvvFHe8XM0Dh35vve9r8eO7CuttFKqwZQBERr5+c9/nmrtYccdd0y1+n74wx+mGtAfcS+L+++/P011t9dee6Vae1l11VVTrau4IvzKK6+kKRAsWkKMEPX666+nqfriRl9XXHFFmmpvTz/9dBmmehouMy7Z3nbbbWkKiuKll15qOJpaNBtqp5vlNboiEQcBDz30UJoC+uvLX/5yqtXXaCS6VvTNb34z1br7wQ9+kGowhWDRIqLJU2/h4hOf+ESxww47pKn2FP1O3v/+96ep7j7/+c8X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l330ox8tR0FptuGZ47sUN/GL93e//fZreHae7lr5c9lXcWZ7tIiz9XHlr5ldffXV5f40zmyfeOKJaW5zmDRpUvH973+//F7E/a5ilCsYKE2hMv3tb38r/6/dUcVdrhdffPFyaLl2FE08Opp1RCez2KhHs47o1N2O4+VrCtXYaqutVvzlL39JU13F5yPuCt0u4sZREZRjYIHhdt1115UBPQq9a7Rri0Eonn322TTVvkZT4IzhW6PZYSuJu1vvsccexc477zzsxwv33HNPefPcGIAiTiiSR1OoqQQL6IVg0bvoS1HvPg+77bZb2Z+nHcUZ0q222qpsy77RRhsVs846a/pJvjhAGj9+fPGnP/2pvMttb/d4obt4/9Zaa600NdXDDz/cp3sOtIM42B4NZ5/vvvvu8p5MrS5aCXz84x8vtylxcnIwRZ/K6HMT25O77rorzWWwCBZTCRbQC8Gib/bee+9ipZVWKjshR+fCGMBgqIdibTbzzz9/eRZyySWXLG/+GIMRxNDMUaKTZcfVm7jCGe9RfK4iRERH4ti+/fWvf22ZZpStIJqLrb/++mXn1ujoe+utt7Zt0G0kmresvvrq5WABcWW5XcTf9Nprry1++ctfpjntJbYXccwTd/aOkBgdshdccMHyIHaeeeYpWwvEIVxsT6KlRAz9HjfAjTAZHb2jyeRoahI3kgSLqQQL6IVgAQD0RLCYSudtAAAgm2ABAABkEywAAIBsggUAAJBNsAAAALIJFgAAQDbBAgAAyCZYAAAA2QQLAAAgm2ABAABka6tgUalUUg0AABhObRUs5p577lSDwTPDDDOkGgAAPZmu0kKn+R966KFi6aWXTlPdbbnllsWYMWOKd999N82BPDPPPHNx0UUXFW+//XaaAwAwVZzYPvnkk4uddtopzRm92ipYAADAcBIsptJ5GwAAyCZYAAAA2VoqWGjnDgBAM5kwYUIxadKkNDW6tVQfi7feequ44447yg61MJxiQIAXXnih3HBMN9105bz46sRgATPNNJOhjgFgFIr9fxwHLL/88sXCCy+c5o5eLRUsAACA5qSPBQAAkE2wAAAAsgkWAABANsECAADIJlgAAADZBAsAACCbYAEAAGQTLAAAgGyCBT166qmnUg2AdjR58uTixRdfTFMj45133in+9re/pan2Evcg/uc//1ncd999xWOPPZbmQvsSLPpp4sSJxbvvvpum2td0001XfOADHyj/B6D9/PGPfyxmmmmmYsEFFyx22mmnNHd43XDDDcWMM85YrLzyyuX+5j//+U/6Ses78MADi+mnn7744Ac/WCy//PLF4osvXv6ODz30UHoEtB/BooFLLrmk2HzzzYs555yz3BhEmX322YsZZpihc3rJJZcsvvrVrxZ//etf01LtJ85oMXRix3rYYYcV++yzT3HkkUcW999/f/pJfZdddlnxqU99qth6662LCRMmpLk0u1133bVzuzEUZd55503PBH3z5JNPptrIXKH+9a9/Xay33nppqiiWWGKJYo455khTre+nP/1p+f8iiyxSfO1rXyvr4fjjj081aD+CRR3nnXdeuaPeaqutissvv7zhGZRHHnmk3HisssoqxSyzzFJcdNFF6SftI864MPiee+658nMWO9bvfe97xSmnnFJ8+9vfLsaNG1fMOuusZYCo59hjjy3+8Ic/FP/3f/9XnH/++WkuzS7ODg+lV199NdWgb+IkWYe4ajCcTj755GK77bZLU0Wx1lprFQ8//HCaag/RxCsstthixZe+9KWyHkZDqwdGr+kq0QCQThtssEFx/fXXp6kptthii2LjjTcull566WL++ecvNxYvvfRS8Y9//KM8+LvxxhvTI6eIA8NoT9nK4oC3Q/y+wsXgq32PF1544eKTn/xkMX78+C6fndgh3X777cUCCyyQ5hRlgP3vf/9b1m+++ebiox/9aFmn+f35z38um1PW/u2nNfPMM5fblzvuuKNYbrnlyquisUwjcYC49tprl4EU+uqMM84ovvzlL5f12Mf96U9/KutD7Tvf+U7xgx/8IE0VxTbbbFNevWg39Y4nQpwU+sxnPpOmoL0IFjV23nnn4txzz01TRfHNb36zbJrSF9/97neLww8/PE0VZVvKuJrRqgSLoRVXJ6LpU9hkk02Kq666qqyHRx99tLwC9u9//zvNKYpNN920PHCMA4HHH388zZ3SMZD2U/v9i1AhMDAURiJY7LbbbsWZZ56Zpqb0Q/jRj36UptrPb3/72/Jk0dtvv13MM888xUYbbVR86EMfSj+F9iNYJK+99lox99xzp6mi+NnPflbsscceaapv7r333mLFFVdMUwNbR7MQLIZW7c41ztTFGbtpRRO76L/Tk+eff77sdEl7eeutt8qrFh3uvPPOMmjCYBvu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/GU5Lv4mm2xSLL/88mnulPssRMAAoHXEjTg7nHTSSanWu0cffTTV8u+lAaONPhbQQFwqj3a4IW5KVHvDJQCa14033tjlRn19PdzZaKONimuvvbasf+ELXyjOOeecsg70zhULaGDLLbdMtaL4z3/+k2oANLt11lkn1aZYddVVU61np556ameoCP25Kz0gWEApRn+KETWm9cILL6Ta1NGiAGgN0ZS1w1133VVux7/1rW8Vt912WzFhwoRy9LPHH3+8OP/884tlllmm2GuvvdKji+KQQw4pm8cCfacpFKPexIkTO0cG2XfffYtNN920bAJ1wQUXFD/5yU/K+cFXBaD1RHCIZqwRIvoq+mTss88+aQroK8GCUe+EE04o9t9//zRV3+WXX15sttlmaQqAVhMjQ/34xz8ubrjhhjSnq/e9733FLrvsUhxxxBFpDtBfggUkMbzsVVddVfz9738vr2LEeNhbbbVVceyxx5Zj+gPQPl555ZVyaNl55513xO8bBO1CsAAAALLpvA0AAGQTLAAAgGyCBQAAkE2wAAAAsgkWAABANsECAADIJlgAAADZBAsAACCbYAEAAGQTLAAAgGyCBQAAkE2wAAAAsgkWAABANsECAADIJlgAAADZBAsAACCbYAEAAGQTLAAAgGyCBQAAkE2wAAAAsgkWAABANsECAADIJlgAAADZBAsAACCbYAEAAGQTLAAAgGyCBQAAkE2wAAAAsgkWAABANsECAADIJlgAAADZBAsAACCbYAEAAGQTLAAAgGyCBQAAkE2wAAAAsgkWAABANsECAADIJlgAAADZBAsAACCbYAEAAGQTLAAAgGyCBQAAkE2wAAAAsgkWAABANsECAADIJlgAAADZBAsAACCbYAEAAGQTLAAAgGyCBQAAkE2wAAAAsgkWAABANsECAADIJlgAAADZBAsAACCbYAEAAGQTLAAAgGyCBQAAkE2wAAAAsgkWAABANsECAADIJlgAAADZBAsAACCbYAEAAGQTLAAAgGyCBQAAkE2wAAAAsgkWAABANsECAADIJlgAAADZBAsAACCbYAEAAGQTLAAAgGyCBQAAkE2wAAAAsgkWAABANsECAADIJlgAAADZBAsAACCbYAEAAGQTLAAAgGyCBQAAkE2wAAAAsgkWAABANsECAADIJlgAAADZBAsAACCbYAEAAGQTLAAAgGyCBQAAkE2wAAAAsgkWAABANsECAADIJlgAAADZBAsAACCbYAEAAGQTLAAAgGyCBQAAkE2wAAAAsgkWAABANsECAADIJlgAAADZBAsAACCbYAEAAGQTLAAAgGyCBQAAkE2wAAAAsgkWAABANsECAADIJlgAAADZBAsAACCbYAEAAGQTLAAAgGyCBQAAkE2wAAAAsgkWAABANsECAADIJlgAAADZBAsAACCbYAEAAGQTLAAAgGyCBQAAkE2wAAAAsgkWAABANsECAADIJlgAAADZBAsAACCbYAEAAGQTLAAAgGyCBQAAkE2wAAAAsgkWAABANsECAADIJlgAAADZBAsAACCbYAEAAGQTLAAAgGyCBQAAkE2wAAAAsgkWAABANsECAADIJlgAAADZBAsAACCbYAEAAGQTLAAAgGyCBQAAkE2wAAAAsgkWAABANsECAADIJlgAAADZBAsAACCbYAEAAGQTLAAAgGyCBQAAkE2wAAAAsgkWAABANsECAADIJlgAAADZBAsAACCbYAEAAGQTLAAAgGyCBQAAkE2wAAAAsgkWAABANsECAADIJlgAAADZBAsAACCbYAEAAGQTLAAAgGyCBQAAkE2wAAAAsgkWAABANsECAADIJlgAAADZBAsAACCbYAEAAGQTLAAAgGyCBQAAkE2wAAAAsgkWAABANsECAADIJlgAAADZBAsAACCbYAEAAGQqiv8PPUNyKIf8ztIAAAAASUVORK5CYII='

Tela_Principal()