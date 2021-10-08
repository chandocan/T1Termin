'''
def test_get_dell_smart_attributes(nvme0):
    import PySimpleGUI as sg
    
    smart = d.Buffer()
    nvme0.getlogpage(0xCA, smart, 512).waitdone()

    l = []
    l.append('Byte |  Value  | Attribute')
    l.append('   0 |  %5d  | Re-Assigned Sector Count' % smart.data(0))
    l.append('   1 |  %5d  | Program Fail Count (Worst Case Component)' % smart.data(1))
    l.append('   2 |  %5d  | Program Fail Count (SSD Total)' % smart.data(2))
    l.append('   3 |  %5d  | Erase Fail Count (Worst Case Component)' % smart.data(3))
    l.append('   4 |  %5d  | Erase Fail Count (SSD Total)' % smart.data(4))
    l.append('   5 |  %5d  | Wear Leveling Count' % smart.data(5))
    l.append('   6 |  %5d  | Used Reserved Block Count (Worst Case Component)' % smart.data(6))
    l.append('   7 |  %5d  | Used Reserved Block Count (SSD Total)' % smart.data(7))
    l.append('11:8 |  %5d  | Reserved Block Count (SSD Total)' % smart.data(11, 8))

    layout = [[sg.Listbox(l, size=(70, 10))]]
    sg.Window("Dell SMART Attributes",
              layout+[[sg.OK()]],
              font=('monospace', 16)).Read() 
'''

'''
import PySimpleGUI as sg

def autocomplete_popup_show(text_list ):
    autocomplete_popup_layout = [[sg.Listbox(values=text_list,
                                             size=(100,20*len(text_list)) if QT else (15, len(text_list)),
                                             change_submits=True,
                                             bind_return_key=True,
                                             auto_size_text=True,
                                             key='_FLOATING_LISTBOX_', enable_events=True)]]

    autocomplete_popup = sg.Window("Borderless Window",
                                   default_element_size=(12, 1),
                                   auto_size_text=False,
                                   auto_size_buttons=False,
                                   no_titlebar=True,
                                   grab_anywhere=True,
                                   return_keyboard_events=True,
                                   keep_on_top=True,
                                   background_color='black',
                                   location=(1320,622),
                                   default_button_element_size=(12, 1))

    window = autocomplete_popup.Layout(autocomplete_popup_layout).Finalize()
    return window 
'''
'''
import PySimpleGUI as sg
def PlayerChooseSongGUI(self):

        # ---------------------- DEFINION OF CHOOSE WHAT TO PLAY GUI ----------------------------

        layout = [[sg.Text('MIDI File Player', font=("Helvetica", 15), size=(20, 1), text_color='green')],
                  [sg.Text('File Selection', font=("Helvetica", 15), size=(20, 1))],
                  [sg.Text('Single File Playback', justification='right'), sg.InputText(size=(65, 1), key='midifile'), sg.FileBrowse(size=(10, 1), file_types=(("MIDI files", "*.mid"),))],
                  [sg.Text('Or Batch Play From This Folder', auto_size_text=False, justification='right'), sg.InputText(size=(65, 1), key='folder'), sg.FolderBrowse(size=(10, 1))],
                  [sg.Text('_' * 250, auto_size_text=False, size=(100, 1))],
                  [sg.Text('Choose MIDI Output Device', size=(22, 1)),
                   sg.Listbox(values=self.PortList, size=(30, len(self.PortList) + 1), key='device')],
                  [sg.Text('_' * 250, auto_size_text=False, size=(100, 1))],
                  [sg.SimpleButton('PLAY', size=(12, 2), button_color=('red', 'white'), font=("Helvetica", 15), bind_return_key=True), sg.Text(' ' * 2, size=(4, 1)), sg.Cancel(size=(8, 2), font=("Helvetica", 15))]]

        window = sg.Window('MIDI File Player', auto_size_text=False, default_element_size=(30, 1), font=("Helvetica", 12)).Layout(layout)
        self.Window = window
        return window.Read() 
'''
import os
from PySimpleGUI.PySimpleGUI import Button
import pytesseract
from PIL import Image
import PySimpleGUI as sg
import pathlib
import pygame as pg

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
            [sg.Button('ok'      ,font=fonte),sg.Button('Ler Arquivo',font=fonte)],
            [sg.Output(size=(100,5)),sg.Button('Busca Arquivo',font=fonte),sg.Text('Busque seu arquivotext2 p/ser exibido',font=9),sg.Button('salva')],
            [sg.Text('> New file <', font=('Consolas', 10), size=(40, 1), key='_INFO_')], # salvar arquivo e updte de valores e 40 linha horizontal da barra
            [sg.Multiline(font=('Consolas', 12), size=(65, 10), key='_BODY_')], # 65 horizontal da janela inferior e 10 vertical Janelinha
            [sg.Checkbox('teclado'),sg.Button('teclado2')]
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
            
    def Terminal(self): # TESTE
        print('Dores de parto TESTE')

     '''
    # pensando na boca
    def testePygame(self):
        # precisaria criar um layout e escla com "rect" junto com um update
        # em parte separada para pode chamar essa função
        # tem que fazer como evento unico para não atrapalhar o codico principal
        morrendo = pg.image.load('explode').convert_alpha()
        def __init__(self,x,y,scale):
            
      '''
        '''     
            pg.sprite.Sprite.__init__(self)
            self.images = []
            for num in range(1,6):
                # as imagens tem que esta com o mesmo nome de dentro da pasta 'exp'
                img = pg.image.load(f'explode/exp{num}.png').convert_alpha()
                img = pg.transform.scale(img,(int(img.get_width() * scale), int(img.get_height() * scale)))
                self.images.append(img)
        self.frame_index = 0 
        self.image = self.images[self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.counter = 0
        '''
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
            elif self.values in ('Open (Ctrl+O)', 'o:79'):
                self.open_file()
            elif self.values in('Exit', None):
                break
            elif self.button == 'teclado2':
                print('amor verdadeiro')
                #precisa de uma button para entra nesse novo loop
                while True:
                    # extraindo dados
                    self.button, self.event = self.janela.Read()

                    if self.janela and self.values == sg.WINDOW_CLOSED:
                        break

                    # teclado precionado
                    # keyboard presses
                    elif self.button == 'teclado2':
                        if sg.event.type == sg.KEYDOWN:
                            if sg.event.key == sg.K_a:
                                #Da para jogar uma variavel aqui para acionar algum evento
                                #moving_left = True
                                print('test A')
                            if sg.event.key == sg.K_d:
                                #Da para jogar uma variavel aqui para acionar algum evento
                                #moving_right = True
                                print('Teste D')
                            if sg.event.key == sg.K_SPACE:
                                #Da para jogar uma variavel aqui para acionar algum evento
                                #shoot = True
                                print('Teste espaço')
                            if sg.event.key == sg.K_q:
                                #Da para jogar uma variavel aqui para acionar algum evento
                                #grenade = True
                                print('Teste q')
                            if sg.event.key == sg.K_w and sg.alive:
                                #Da para jogar uma variavel aqui para acionar algum evento
                                #player.jump = True
                            #if sg.event.key == sg.K_ESCAPE:
                                #Da para jogar uma variavel aqui para acionar algum evento
                                #run = False
                                #print('teste escape')
                            #else:
                                #print('fim dos eventos')
                    
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
                print('você não fez ação nem uma com "S"!')  
            self.Terminal() # TESTE

tela =  ConversorTexto()
tela.inicial()

