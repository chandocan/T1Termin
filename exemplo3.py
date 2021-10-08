
# melhor exemplo de  event values que ja vi
import PySimpleGUI as sg
#from matplotlib.pyplot import show
from PIL import Image
import glob, os
import sys
'''
layout = [  [sg.Text('Button Test')],
            [sg.Button('Button 1', key='_1_')],
            [sg.Button('Button 2', key='_2_')],
            [sg.Button('Button 3', key='_3_')],  ]

window = sg.Window('My new window', layout,
                   return_keyboard_events=True)
while True:             # Event Loop
    event, values = window.Read()
    if event is None:
        break
    if event == '\r':
        elem = window.FindElementWithFocus()
        if elem is not None:
            elem.Click()
    elif event == '_1_':
        print('Button 1 clicked')
    elif event == '_2_':
        print('Button 2 clicked')
    elif event == '_3_':
        print('Button 3 clicked')
'''
# criação de arquivo de texto
'''
    if window == janela2 and event =='txt_button':
        window['texto_informativo'].update('Arquivo criado com sucesso!', text_color = 'green')
        with open('arquivo.txt', 'w', encoding='utf-8') as text_file:
            said = get_audio()
            text_file.write(said)
'''

#cookbook
#receitas https://pysimplegui.readthedocs.io/en/latest/cookbook/
#https://pysimplegui.readthedocs.io/en/latest/cookbook/

file_types = [("Todos arquivos", "*.*")]
layout = [  [sg.Text('Button Test')],
            [sg.Button('Button 1', key='_1_'),sg.Button('button 4', key='_4_'),sg.Button('button 7',key='_7_')],
            [sg.Button('Button 2', key='_2_'),sg.Button('button 5', key="_5_"),sg.Button('button 8',key='_8_')],
            [sg.Button('Button 3', key='_3_'),sg.Button('button 6', key='_6_'),sg.Button('button 9',key='_9_')],
            [sg.Input(size=(25, 1), key="-FILE-"),sg.FileBrowse(file_types=file_types, key= 'file_browse')],
            [sg.Output(size=(100,5))]
              ]

window = sg.Window('Titulo aqui', layout,
                   return_keyboard_events=True)
while True:             # Event Loop
    event, values = window.Read()
    
    if event is None:
        break

    # visualizando
    elif event == '_1_':

        #salvando imagem com PIL
        from PIL import Image 
        img_PIL = Image.open ('/home/alfredo/python_projetosAlfredo/ImagemParaTesteAqui/dog2.png')
        print(img_PIL.size) # ver o tamanho da imagem
        img_PIL.show()      # visualizando a imagem
    
    # salando como jpg
    elif event == '_2_':
        
        img_PIL = Image.open('/home/alfredo/python_projetosAlfredo/ImagemParaTesteAqui/dog2.png')
        img_PIL.save ('dog_JPG.jpg')
    
    # criando miniaturas
    elif event == '_3_':

        #with Image.open('/home/alfredo/python_projetosAlfredo/ImagemParaTesteAqui/dog2.png') as im:
        #    im.rotate(45).show() # visualizando a imagem
        

        # buca as imagens que tenham extenção jpg no seu diretorio atual é cria miniaturas 
        size = 50, 50 # tamanho da imagem da para deimencionar 
        for infile in glob.glob("*.jpg"): #  busca os jpg
            file, ext = os.path.splitext(infile)
            with Image.open(infile) as im:
                im.thumbnail(size)
                im.save(file + ".thumbnail", "JPEG")
    # rederizando imagem isso serve para fazer a rederização de personagem de desenhos de games
    # quanto maior a rederização maior o zoom nessa image da para se aproxima dela
    elif event == '_4_':

        im = Image.open('dog2.png')
        im.resize(
            (1280,720) # x, y
        )
        im.save('dog_maior.jpg')

    
    # rotação de imagem
    elif event == '_5_':
        print('teste2123')
        folder = sg.popup_get_folder('Where are your images?')
        file_list = os.listdir(folder)
        fnames = [f for f in file_list if os.path.isfile(
        os.path.join(folder, f)) and f.lower().endswith((".png", ".jpg", "jpeg", ".tiff", ".bmp", ".gif", ".ico"))]
        print(fnames)
        num_files = len(fnames)
        print('quantidade de arquivos',num_files)
        print('digite o nome do aquivo')
        arquivo_selecao = input('digite o nome do arquivo:')
        with Image.open((arquivo_selecao), 'r') as arquivo:
            arquivo.show()

    elif event == '_6_':
  
        folder = sg.popup_get_folder('Where are your images?')
        if not folder:
            exit(0)
        file_list = os.listdir(folder)
        fnames = [f for f in file_list if os.path.isfile(
        os.path.join(folder, f)) and f.lower().endswith((".png", ".jpg", "jpeg", ".tiff", ".bmp", ".gif", ".ico"))]
        num_files = len(fnames)
        file_list = os.listdir(folder)
        print(file_list)
        if event == 'cria2':
                
            img_PIL = Image.open(file_list)
            img_PIL.save(file_list[0]-1)
    # rotacionado
    elif event == '_7_':
        # invertendo imagem com Flip
        #im =  Image.open('dog22.png')
        #im.transpose(Image.FLIP_LEFT_RIGHT).show()
        #im.transpose(Image.FLIP_TOP_BOTTOM).show() # virando imagem
        #im.transpose(Image.ROTATE_180).show() # virando imagem

        
        #rotação
        im = Image.open('dog22.png')
        #im.rotate(45, expand=True).show() # em graus posso tira o expand=True não vai espandir 
        #print(array(im))
    elif event == '_8_':
        im = Image.open('dog22.png')
        copied_image = Image.copy()
        #plt.imsshow(copied_image) # deve esta desatualizado deve sr uma forma de exibir a imagem
        copied_image.show()
    # evento para pesquisa
    elif event == '_9_':# tendo escreve arquivo de forma diferente
        print('v')
        
        def myfunc(outfile=None): # Isso significa que você não pode usar o with open(outfile, 'w') as out:padrão, mas às vezes vale a pena.
            if outfile is None:
                out = sys.stdout
            else:
                out = open(outfile, 'w')
            try:
                # do some stuff
                out.write('mytext' + '\n') # original out.write(mytext + '\n') vriavel que representa o texto 
                # ...
            finally:
                if outfile is not None:
                    out.close()





'''
import os, PySimpleGUI as sg

document_ext = ['.SVG', '.txt', '.XML']

layout = [
           [
            sg.Text("This program can be used to search for a particular \nterm in all files under the folder location provided.") 
           ],
           [
            sg.Listbox(document_ext, size=(10,5), key="-File_Ext-")
           ],
          [
            sg.Text('What would you like to search for?')
           ],
           [
            sg.InputText(size=(30,5), key="-Search_Term-")
           ],
           [
            sg.Text("Choose Folder to Search:")
            ],
           [
            sg.In(size=(30,5), key="-FOLDER-"),
            sg.FolderBrowse()
           ],
           [
            sg.Text("Where Should Report Be Saved?")
            ],
           [
            sg.In(size=(30,5), key="-FOLDER2-"),
            sg.FolderBrowse()
           ],
           [
            sg.Button(button_text="Search")    
           ],
           [
            sg.Multiline(key="-Output-", size=(30,5))    
           ]
        ]

window = sg.Window("File Contents Searcher", layout)#, margins=(200,200))

def main(svalue, location, ext):
    number_found = 0
    search_results = ""
    location = (values["-FOLDER-"]) # Set values to window.read() values
    svalue= (values["-Search_Term-"]) # Ditto for this
    ext = str(values["-File_Ext-"][0].lower()) # Needs this to choose value and make it case insensitive

    #os.chdir(location) # Don't need
    for dpath, dname, fname in os.walk(location): #Hardcoded to value above
        for name in fname:
            pat = os.path.join(dpath,name)
            if name.endswith(ext):
                with open(pat) as f:
                    if svalue in f.read():
                        number_found += 1
                        search_results += "--- \nFilename: {} \nFilepath: {} \n".format(name, pat)
    search_results_head = "\"{}\" was found in {} files. \n \n".format(svalue, number_found)
    output = "RESULTS \n \n" + search_results_head + search_results
    return output, search_results_head

def create_log(sl, s_res):
     s1 = (values["-FOLDER2-"])  # Hardcoded again
     print(os.getcwd())
     with open("FileSearchResults.txt", "w") as f:
         f.write(s_res)
     return "Report Saved"

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == "Search":
        m = main("-Search_Term-", "-FOLDER-", "-File_Ext-")
        print(m)
        c = create_log(r"-FOLDER2-", m[0])
        window["-Output-"].update(m[1] + " " + c)
window.close() 
'''

'''
/usr/bin/env python
import PySimpleGUI as sg
from PIL import Image
import PIL
import io
import base64
import os
from typing import Union, Tuple

"""
    Demo Image Album.... displays images on Graph Element and transitions
    by sliding them across.  Click on right side of image to navigate down through filenames, left side for up.
    
    Contains a couple of handy PIL-based image functions that resize an image while maintaining correct proportion.
    One you pass a filename, the other a BASE64 string.
    
    Copyright 2020 PySimpleGUI.org
"""

G_SIZE = (800,600)


def convert_to_bytes(file_or_bytes, resize=None):
    

    Will convert into bytes and optionally resize an image that is a file or a base64 bytes object.
    :param file_or_bytes: either a string filename or a bytes base64 image object
    :type file_or_bytes:  (Union[str, bytes])
    :param resize:  optional new size
    :type resize: (Tuple[int, int] or None)
    :return: (bytes) a byte-string object
    :rtype: (bytes)
    
    
    if isinstance(file_or_bytes, str):
        img = PIL.Image.open(file_or_bytes)
    else:
        img = PIL.Image.open(io.BytesIO(base64.b64decode(file_or_bytes)))

    cur_width, cur_height = img.size
    if resize:
        new_width, new_height = resize
        scale = min(new_height/cur_height, new_width/cur_width)
        img = img.resize((int(cur_width*scale), int(cur_height*scale)), PIL.Image.ANTIALIAS)
    bio = io.BytesIO()
    img.save(bio, format="PNG")
    del img
    return bio.getvalue()

folder = sg.popup_get_folder('Where are your images?')
if not folder:
    exit(0)

file_list = os.listdir(folder)
fnames = [f for f in file_list if os.path.isfile(
    os.path.join(folder, f)) and f.lower().endswith((".png", ".jpg", "jpeg", ".tiff", ".bmp", ".gif", ".ico"))]
num_files = len(fnames)

graph = sg.Graph(canvas_size=G_SIZE, graph_bottom_left=(0, 0), graph_top_right=G_SIZE, enable_events=True, key='-GRAPH-')
layout = [[graph]]

window = sg.Window('Scrolling Image Viewer', layout, margins=(0,0), element_padding=(0,0), use_default_focus=False, finalize=True)

window.read()
offset, move_amount, direction  = 0, 5, 'left'
while True:
    file_to_display = os.path.join(folder, fnames[offset])
    img_data = convert_to_bytes(file_to_display, resize=G_SIZE)
    id = graph.draw_image(data=img_data, location=(0, G_SIZE[1]))

    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

    if event in ('<', '>'):
        direction = 'left' if event == '<' else 'right'
    elif event == '-GRAPH-':
        direction = 'left' if values['-GRAPH-'][0] < (G_SIZE[0] // 2) else 'right'

    for i in range(G_SIZE[0]//move_amount):
        graph.move_figure(id, -move_amount if direction == 'left' else move_amount, 0)
        window.read(timeout=0)
    graph.delete_figure(id)

    if direction == 'left':
        offset = (offset + (num_files - 1)) % num_files     # Decrement - roll over to MAX from 0
    else:
        offset = (offset + 1) % num_files                   # Increment to MAX then roll over to 0

window.close()
'''