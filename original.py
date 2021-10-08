# opencv - biblioteca para reconhecimento de imagem
# pytesseract IA emcanismo de reconhecer caracteres
# baixar o executavel que faz o reconhecimento de caracteres e fazer a IA aponta para ele

# primeiro ler a imagem depois reconhecer acaractere


#import cv2
import pytesseract
from PIL import Image

# carregando a imagem
#img = cv2.imread('/home/alfredo/python_projetosAlfredo/transformar imagem em texto/meu_nome.png')


#aponta a onde está o execultavel do pytesseract se fosse no windows tem que criar uma pasta só para ele 

#image_file = 'meu_nome.png'
img = Image.open('meu_nome.png')
# colocou a img numa varial é transformal de imagem para string 
resultado = pytesseract.image_to_string(img)
#config = r'--oem 3 --psm 6'
#resultado = pytesseract.image_to_string(img, config=config)
print('='*70)
print(resultado)

'''
da para munda a engine é paginação do tesseract com esse comando abaxio
config = r'--oem 3 --psm 6'
resultado = pytesseract.image_to_string(img, config=config)

isso no caso se ele não recolherce a imagem tenta fazer assim para poder ver se ele entende melhor a image é 
traduz ela de forma mais direta.
'''
# escrevendo o arquivo em formato de texto
#var = "Some text to be written to the file."
var = resultado

with open("Output.txt", "w") as txtfile:
    print("String Variable: {}".format(var), file=txtfile)

