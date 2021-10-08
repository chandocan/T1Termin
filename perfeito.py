import os
import pytesseract
from PIL import Image
import PySimpleGUI as sg
import pathlib
import pyttsx3
from os import system, name
import glob
from pyttsx3 import engine


file = None
class ConversorTexto:
    def __init__(self):

        fonte = 20 # tamanho da fonte
      

        layout = [
       
            [sg.Text('VOCÊ DEVE ESCOLHER APENAS UMA AÇÃO É MARCA COM A LETRA "S" ESSE CONVERSO É PARA ARQUIVOS C/EXTEÇÃO PNG ',font=fonte)],
            [sg.Text('VOCÊ TEM QUE DEIXA AS OUTRA OPÇÕES EM BRANCO MARQUE APENAS UMA OPÇÃO COM "S" aguarde um poco se existir muitos caracteres na imagem.')],
            [sg.Text('dependendo do processamento de seu PC é do tamanho do arquivo de imagem pode demora um pouco. se você quer só o arquivo de txt deixe todas as perguntas em branco depois de crialo')],
            [sg.Text('se você quer ficar com o arquivo renomei ele obs: pode ser que tenha algusn erros pois depende de como esta a imagem ')],
            [sg.Text('deseja criar um arquivo de Texto.txt sera salvo no seu PC com nome arquivotext2 ',font=fonte,size=(67,1)),sg.Input(key='sim_não',font=fonte,size=(3,1))],
            [sg.Text('deseja ABRI o aquivo já existente em modo texto sem salva?', font=fonte,size=(65,1)),sg.Input(key='sim_não2',font=fonte,size=(3,1))],
            [sg.Text('deseja remover o arquivo ao sair se sim isso remove o arquivo arquivotext2 ', font=fonte,size=(65,1)),sg.Input(key='sim_não3',font=fonte,size=(3,1))],
            [sg.Button('ok'      ,font=fonte),sg.Button('Ler Arquivo',font=fonte),sg.Button('Enter')],
            [sg.Output(size=(100,5)),sg.Button('Busca Arquivo',font=fonte),sg.Text('Busque seu arquivotext2 p/ser exibido',font=9),sg.Button('salva')],
            [sg.Text('> New file <', font=('Consolas', 10), size=(40, 1), key='_INFO_')], # salvar arquivo e updte de valores e 40 linha horizontal da barra do pequeno menu
            [sg.Multiline(font=('Consolas', 12), size=(65, 10), key='_BODY_')], # 65 horizontal da janela inferior e 10 vertical Janelinha Multiline: Caixa de texto grande: listagem de caixa de texto 
            [sg.Text('ENTER2'),sg.Input(key='Nome')]
            ]



      
            


        # contrução da janela 
        self.janela = sg.Window('Converso de Imagem para Texto de Alfredo ', layout=layout, margins=(0, 0), resizable=True, return_keyboard_events=True, finalize=True)
    
    # para reseta arquivo 
    def new_file(self):
        '''Reset body and info bar, and clear filename variable'''
        self.janela['_BODY_'].update(value='')
        self.janela['_INFO_'].update(value='> New File <')
        file = None
        return file
    # As funções ficam abaixo da criação da janela
    # Função para abri arquivo    
    def open_file(self):
        '''Open file and update the infobar'''
        filename = sg.popup_get_file('Open', no_window=True)
        if filename:
            file = pathlib.Path(filename)
            self.janela['_BODY_'].update(value=file.read_text())
            self.janela['_INFO_'].update(value=file.absolute())
        return file
    # Função salvar arquivo
    def save_file_as(self):
        '''Save new file or save existing file with another name'''
        filename = sg.popup_get_file('Save As', save_as=True, no_window=True)
        if filename:
            file = pathlib.Path(filename)
            file.write_text(self.values.get('_BODY_'))
            self.janela['_INFO_'].update(value=file.absolute())
            return file
    def falador(self):
        
        def limpar_terminal():
            if name == 'nt':
                system('cls')
            else:
                system('clear')

        def apresentaMenu():
            print('escolha o arquivo digite o nome completo digite sair paran\
            encerra digite o nome completo do arquivo para pode ler')

        limpar_terminal()
        apresentaMenu()

        # procura uma forma de deixa o texto em portuguễs por padrão
        engine = pyttsx3.init()
        engine.setProperty('rate', 80) #90
        engine.setProperty('voice', 'brazil-mbrola-1') 

        
        #voices = engine.getProperty('voices')

        # vai pecorre uma liasta das vozes quando chega em  b'\x05pt-br' que é a brasileira vai para
        #for voice in voices:
        #    if voice.languages[0] == b'\x05pt-br':
        #        engine.setProperty('voice', voice.id)
        #        break


        #print(" - Languages: %s" % voice.languages)
        #print(voice)
        engine.say('Bem vindo alfredo a programação com python')
        # esperando o texto termina para poder roda o restante do codigo
        engine.runAndWait()
        #input('Pressione Enter para continuar')
        
        # esta estraindo a lista de arquivos presentes no diretorio atual
        # usou uma compressão de lista
        lista_arquivo = [f for f in glob.glob("*.txt")]
        while True:
            limpar_terminal()
            apresentaMenu()
            print(lista_arquivo)
            # vai perdi a entrada de dados do teclado
            arquivo_selecao = input('qual arquivo você quer ouvir  da lista use a exetenção do\n arquivo ou sair p/quit ?').lower()
            if arquivo_selecao == 'sair':
                limpar_terminal()
                exit()
            else:
                try:
                    with open((arquivo_selecao), 'r') as arquivo:
                        # variavel texto recebe o arquivo aqui
                        texto = arquivo.read()
                        print(texto)

                        # mudando a velocidade da fala
                        #rate = engine.getProperty('rate')
                        #engine.setProperty('rate', rate-55) # 55

                        engine.say(texto)
                        engine.runAndWait()
                        limpar_terminal()
                        apresentaMenu()
                except FileExistsError:
                    print('Digite um arquivo na lista apresentada use as extenções dos arquivos ou [sair] para finalizar o programa')
                    input('Enter para continuar')
  

    def inicial(self):
        while True:
            
           # extraindo dados
            self.button, self.values = self.janela.Read()

            if self.janela and self.values == sg.WINDOW_CLOSED:
                break

            elif self.button == 'Busca Arquivo':
                self.open_file()

            elif self.button == 'salva':
                self.save_file_as()

            elif self.button == 'Ler Arquivo':
                self.falador()
            #elif self.button == 'Enter':
            #     if sg.event.type == sg.KEYDOWN:
            #            if sg.event.key == sg.K_a:
                

            
            deseja = str(self.values['sim_não']).lower() #criando
            deseja2 = str(self.values['sim_não2']).lower()#abrindo s/salvar
            remocao =  str(self.values['sim_não3']).lower()#removendo
        
            # criando arquivo de texto
            if deseja == 's':
                # carregamento da imagem
                img = Image.open('meu_nome.png')

                # colocou a img numa varial é transformal de imagem para string 
                texto = pytesseract.image_to_string(img)
                with open("arquivotext2.txt", "w") as txtfile:
                    print("String Variable: {}".format(texto), file=txtfile)
                print('arquivo criado com exito!')
            # vendo sem salva o arquivo
            elif deseja2 == 's':            
           
                # carregamento da imagem
                img = Image.open('meu_nome.png')

                # colocou a img numa varial é transformal de imagem para string 
                texto = pytesseract.image_to_string(img)
                print(texto)

            #removendo o arquivo     
            elif remocao == 's':
                os.remove("arquivotext2.txt") 
            
   
            
            else:
                print('você não fez ação nem uma !')  
     

tela =  ConversorTexto()
tela.inicial()
