#Abrindo arquivos
#Para abrir um arquivo de texto com Python é necessário utilizar a função open. A sintaxe padrão da função é open(nome, modo, buffering), sendo “nome” o arquivo que será aberto, “modo” a forma de abertura do arquivo e “buffering” é quantidade de bytes reservados na memória para a abertura do arquivo (opcional). Essa função também pode ser utilizada para criar novos arquivos, sendo o que diferencia abertura de criação é o valor inserido no campo “modo” durante a chamada da função.

#Os valores mais comumente utilizados para “modo” são:

#r

#somente leitura

#w

#escrita (caso o arquivo já exista, ele será apagado e um novo arquivo vazio será criado)

#a

#leitura e escrita (adiciona o novo conteúdo ao fim do arquivo)

#r+

#leitura e escrita

#w+

#escrita (o modo w+, assim como o w, também apaga o conteúdo anterior do arquivo)

#a+

#leitura e escrita (abre o arquivo para atualização)

#Observe que os valores de modo e buffering são opcionais, logo, se esses campos não forem informados, o sistema adotará valores padrões: para modo r (leitura); e para buffering o valor definido pelo sistema operacional.

#Crie um script chamado arquivos.py com o seguinte conteúdo:

arq = open("meu_arquivo.txt") 
#No exemplo acima, o script tentará abrir um arquivo chamado meu_arquivo.txt (sugerimos que crie um arquivo com esse nome com em seu editor de textos e insira qualquer conteúdo), e esse deve estar no mesmo diretório do script arquivos.py. Uma vez aberto, podemos realizar a leitura do arquivo usando as funções: read(n), readline( ) ou readlines( ).

#A função read(n) lê até n bytes. Caso o valor não seja informado, a função lê o arquivo inteiro. A função readline( ) retorna uma string contendo a primeira linha do arquivo. Por fim, a função readlines( ) retorna uma lista de strings, sendo cada elemento uma linha do arquivo.

#Veja um exemplo de leitura e impressão de todas as linhas de um arquivo de exemplo chamado meu_arquivo.txt:

arq = open("meu_arquivo.txt")
linhas = arq.readlines()
for linha in linhas:
    print(linha)
#Nesse exemplo, o arquivo foi aberto e registrado na variável arq, entretanto seu conteúdo só pode ser lido e armazenado em uma lista através da função readlines( ). Por fim, um laço for foi utilizado para imprimir cada linha do arquivo armazenada na lista linhas.

#Gravando texto em arquivo
#A gravação de uma linha em uma arquivo é feita de maneira simples com o uso da função write(“texto”). É possível escrever diversas linhas em um arquivo com o auxílio de um laço de repetição.

arq = open("meu_arquivo2.txt","w+")
 
linhasParaOArquivo = ["linha 1","linha 2","linha 3", \
"linha 4","linha 5"]
 
for lnh in linhasParaOArquivo:
    arq.write(lnh)
    arq.write("\n")
#Observe a seguinte linha no código acima: “arq.write(‘\n’)”. Essa linha foi adiciona para que houvesse uma separação entre linhas com uma quebra de linha. Sem ela, todo o conteúdo da lista “linhasParaOArquivo” seria escrito em sequência sem espaçamento. Podemos ainda utilizar “\t” para inserir uma tabulação ao invés de uma quebra de linha.

#Fechando arquivos
#Todo arquivo aberto fica armazenado na memória RAM do computador, até que seja fechado.

#Para fechar um arquivo, basta chamar a função close( ).

arq = open("meu_arquivo2.txt","w+")
linhasParaOArquivo = ["linha 1","linha 2","linha 3", \
"linha 4","linha 5"]
for lnh in linhasParaOArquivo:
    arq.write(lnh)
    arq.write("\n")
 
arq.close()
#Recebendo atributos na chamada do script (parâmetros)
#Uma funcionalidade importante que pode dar poder ao programa desenvolvido é a capacidade de receber, na chamada do programa, parâmetros. Esses podem ser desde dados utilizados durante a execução do programa até mesmo nomes de arquivos que serão processados ou criados. Como por exemplo, executar o programa da seguinte maneira:

#python arquivo.py meu_arquivo.txt 
#Nesse exemplo, o script arquivo.py deve conter a importação do módulo sys, o qual permite receber valores passados na chamada de um programa em Python.

import sys
 
for argumento in sys.argv:
    print(argumento)
#Para a chamada de programa do quadro anterior, a saída seria:

#arquivo.py    meu_arquivo.txt 
#Observe que o primeiro argumento é sempre o nome do programa que foi chamado, seguido dos demais argumentos passados como parâmetro.

#Abrindo um arquivo enviado como parâmetro
#Para abrir um arquivo enviado como parâmetro, aplique o parâmetro a uma variável e depois utilize a função open( ).

import sys
 
nome_arquivo = sys.argv[1]
arquivo = open(nome_arquivo)
linhas = arquivo.readlines()
for linha in linhas:
	print(linha)
#Observe que obtivemos o conteúdo armazenado na posição 1 de sys.argv. Durante a chamada do script, o primeiro nome após o script é armazenado em sys.argv[1], o segundo em sys.argv[2] e assim sucessivamente.

#Criando mensagens de ajuda (helpers)
#Você pode aperfeiçoar o seu programa inserindo mensagens que ajudem o usuário a executá-lo. Para isso, precisaremos usar dois conceitos ainda não citados. O primeiro é a variável sys.argc: ela conta quantos elementos foram enviados como parâmetro. A segunda é a função sys.exit( ), que interrompe a execução do programa. Veja:

import sys
 
if sys.argc > 1:
	arquivo = sys.argv[1]
else:
	print("Sintaxe 'python meu_programa.py [arquivo]’")
	sys.exit()
 
if arquivo == "-h" or arquivo == '--help':
	print("Sintaxe 'python meu_programa.py [arquivo]’")
	sys.exit()
#No exemplo, verificamos quantos argumentos o programa recebeu (o próprio nome do programa conta como um argumento, assim se houver mais de um, a variável arquivo recebe o conteúdo do primeiro argumento). Se a condição não for cumprida, o usuário recebe um aviso explicando como executar o programa corretamente, e em seguida a execução do código é interrompida. Caso o usuário insira os valores -h ou –help (valores comumente usados em scripts para que o programa liste suas funções), o programa exibe uma mensagem com sua correta sintaxe e também interrompe a execução.
