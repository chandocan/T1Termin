lista = ["png", "jpg", "jpeg", "tiff", "bmp"]
n = input('nome:')
for i in lista:
    n = input('nome:')
    if n == i:
        print('esta na lista',n)
        break
    else:
        print('não esta na lista')

