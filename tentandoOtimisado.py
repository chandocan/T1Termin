import os
from re import S
from PySimpleGUI.PySimpleGUI import Exit
import pytesseract
from PIL import Image
import PySimpleGUI as sg
import pathlib
import pyttsx3
from os import system, name
import glob
from pyttsx3 import engine
from gtts import gTTS, lang #langs ler arquivo
import speech_recognition as sr #speech recognition biblioteca de voz para texto
from playsound import playsound #Musica
import darkdetect #detectar modo escuro
import docx2txt # para arquivo docx
import PyPDF2   # para pdf
from inspect import Traceback
from time import sleep
import os
import pyglet

file = None
#filepath = 'pequeno.txt'
class ConversorTexto:
    def __init__(self):
        file_types = [("Todos arquivos", "*.*")] # busca qualquer tipo de arquivo no FileBrowse
        fonte = 20 # tamanho da fonte
      

        layout = [
       
            [sg.Text('VOCÊ DEVE ESCOLHER APENAS UMA AÇÃO É MARCA COM A LETRA "S" ESSE CONVERSO É PARA ARQUIVOS C/EXTEÇÃO PNG ',font=fonte)],
            [sg.Text('VOCÊ TEM QUE DEIXA AS OUTRA OPÇÕES EM BRANCO MARQUE APENAS UMA OPÇÃO COM "S" aguarde um poco se existir muitos caracteres na imagem.')],
            [sg.Text('dependendo do processamento de seu PC é do tamanho do arquivo de imagem pode demora um pouco. se você quer só o arquivo de txt deixe todas as perguntas em branco depois de crialo')],
            [sg.Text('se você quer ficar com o arquivo renomei ele obs: pode ser que tenha algusn erros pois depende de como esta a imagem ')],
            [sg.Text('deseja criar um arquivo de Texto.txt sera salvo no seu PC com nome arquivotxt2.txt ',font=fonte,size=(75,1)),sg.Input(key='sim_não',font=fonte,size=(3,1))],
            [sg.Text('deseja ABRI o arquivo já existente em modo texto sem salva? só usa esse função se tiver o arquivotxt2.txt', font=fonte,size=(85,1)),sg.Input(key='sim_não2',font=fonte,size=(3,1))],
            [sg.Text('deseja remover o arquivo ao sair se sim isso remove o arquivo arquivotxt2 ', font=fonte,size=(65,1)),sg.Input(key='sim_não3',font=fonte,size=(3,1))],
            [sg.Button('ok',key= 'teste',font=fonte),sg.Button('Ler Arquivo',key='-3-',font=fonte),sg.Button('Stop',key= 'Enter1')],
            [sg.Output(size=(100,5)),sg.Button('Busca Arquivo',key='-1-',font=fonte),sg.Text('Busque seu arquivotxt2 p/ser exibido',font=9),sg.Button('salva',key='-2-')],
            [sg.Text('> New file <', font=('Consolas', 10), size=(40, 1), key='_INFO_')], # salvar arquivo e updte de valores e 40 linha horizontal da barra do pequeno menu
            [sg.Multiline(font=('Consolas', 12), size=(65, 10), key='_BODY_')], # 65 horizontal da janela inferior e 10 vertical Janelinha Multiline: Caixa de texto grande: listagem de caixa de texto 
            #[sg.Button('Limpar Terminal', key='-4-'),sg.Input(size=(25, 1), key='-6-'),sg.Button('ler arquivo2',key='-5-'),sg.FileBrowse(file_types=file_types, key= 'file_browse')],   # para buscara arquivo  sg.FileBrowse    precisou de um Input antes   
            [sg.Text('Selecione um arquivo para começar!')],
            [sg.Text(size=(23,1), key='arquivo_selecionado')],
            [sg.Button('Ditar texto', key='ditar_texto'), sg.Input(size=(25, 1), key='-FILE-'),sg.FileBrowse(file_types=file_types, key= 'file_browse'), sg.Button('Ler arquivo', key='ler_arquivo')]
            
            ]



        # contrução da janela 
        #self.janela = sg.Window('Converso de Imagem para Texto de Alfredo ', layout=layout, margins=(0, 0), resizable=True, return_keyboard_events=True, finalize=True)
        self.janela = sg.Window('My new window', layout,resizable=True,return_keyboard_events=True)
    
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
    
    
    def entroducao(self):
        engine.say('Bem vindo alfredo a programação com python')
        # esperando o texto termina para poder roda o restante do codigo
        engine.runAndWait()

    def limpar_terminal(self):
        if name == 'nt':
            system('cls')
        else:
            system('clear') 
    
    def linguagem(self):  # use para trocar a linguagem no futuro 
        
        # procura uma forma de deixa o texto em portuguễs por padrão
        engine = pyttsx3.init()
        engine.setProperty('rate', 80) #90
        engine.setProperty('voice', 'brazil-mbrola-1') 

    def speak(text):
        tts = gTTS(text = text, lang = 'pt-br', slow= False)
        filename = 'audio.mp3'
        tts.save(filename)
        playsound(filename)
        os.remove(filename)    
    
    
    
    def faladorOffLine(self):
        # usou uma compressão de lista buscando arquivos
        lista_arquivo = [f for f in glob.glob("*.txt")]
        while True:
            engine = pyttsx3.init()
            engine.setProperty('rate', 80) #90
            engine.setProperty('voice', 'brazil-mbrola-1') 
            print(lista_arquivo)

            self.linguagem()

            arquivo_selecao = 'arquivotxt2.txt'

            with open((arquivo_selecao), 'r') as arquivo:
                # variavel texto recebe o arquivo aqui
                texto = arquivo.read()
                print(texto)
                self.linguagem()
                engine.say(texto)
                engine.runAndWait()
                self.limpar_terminal()
             
          
                print('Você pode muda o nome desse arquivo clicando com o botão direito do mouse nele para salva em seu PC de outro nome a ele não esquesa de colocar no final a extenção "txt", O Narrador\ so vai ler o arquivo que tenha o nome arquivotxt2.txt se você quer reler um arquivo basta renomealo para arquivotext2.txt lembrando que tem que ser um aquivo de texto' )
        
            break
    def falador_Online(self):
            arq = open("arquivotxt2.txt") # nome do arqui
            linha = arq.read()  # carregamento do arquivo em uma variavel

            filename = linha
            tts = gTTS(filename, lang='pt-BR')
            filename = '/tmp/temp.mp3'
            tts.save(filename)
            

            music = pyglet.media.load(filename, streaming=False)
            music.play()

            sleep(music.duration) #prevent from killing para não remover durante a duraçõa da naração
            os.remove(filename) #remove temperory file     
             


    
    def inicial(self):
        
        while True:
      
           # extraindo dados
            #self.button, self.values = self.janela.Read()
            self.event, self.values = self.janela.Read()
            if self.event is None:
                break
            if self.event == '\r':
                elem = self.janela.FindElementWithFocus()
                if elem is not None:
                    elem.Click()

            if self.janela and self.values == sg.WINDOW_CLOSED:
                break

            elif self.event == '-1-':
                self.open_file()

            elif self.event == '-2-':
                self.save_file_as()
            # processo offline
            elif self.event == '-3-':
                self.faladorOffLine() 
            elif self.event == '-4-':
                self.limpar_terminal()
            elif self.event == 'ler_arquivo':
               
                self.falador_Online()

            if self.janela == self.janela and self.event == 'teste':
                filepath = self.values['-FILE-']
                nome_arquivo = os.path.basename(filepath)
                #abri o arquivo é 'como' text_to_read txt recebe text_to_read leitura vai abri o que esta dentro do arquivo
                with open(nome_arquivo) as text_to_read:
                    txt = text_to_read.read()
                filename = txt
                tts = gTTS(filename, lang='pt-BR')
                filename = '/tmp/temp.mp3'
                tts.save(filename)
                

                music = pyglet.media.load(filename, streaming=False)
                music.play()

                sleep(music.duration) #prevent from killing para não remover durante a duraçõa da naração
                os.remove(filename) #remove temperory file     
                



                
            deseja = str(self.values['sim_não']).lower() #criando
            deseja2 = str(self.values['sim_não2']).lower()#abrindo s/salvar
            remocao =  str(self.values['sim_não3']).lower()#removendo


            # criando arquivo de texto
            if deseja == 's':
                # carregamento da imagem
                img = Image.open('paraler.png')

                # colocou a img numa varial é transformal de imagem para string 
                texto = pytesseract.image_to_string(img)
                with open("arquivotxt2.txt", "w") as txtfile:
                    print("String Variable: {}".format(texto), file=txtfile)
                print('arquivo criado com exito! com o nome arquivotxt2.txt você pode busca ele para se exibido abaixo,\n deixe tudo embranco ao sair')
            # vendo sem salva o arquivo
            elif deseja2 == 's':            

                # carregamento da imagem
                img = Image.open('paraler.png')

                # colocou a img numa varial é transformal de imagem para string 
                texto = pytesseract.image_to_string(img)
                print(texto)

            #removendo o arquivo     
            elif remocao == 's':
                os.remove("arquivotxt2.txt") 
                print('O arquivotxt2 foi EXECLUIDO só posso LER se você pedir para cria ele em: \n DESEJA CRIAR UM ARQUIVO DE TEXTO.TXT SALVO NO SEU PC COM NOME arquivotxt2.txt')
               


tela =  ConversorTexto()
tela.inicial()
