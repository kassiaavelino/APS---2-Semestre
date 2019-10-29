#testando os métodos read(), readline() e realines()
'''
manipulador = open('arquivo.txt', 'r')


print("\nMétodo read():\n")
print(manipulador.read())

manipulador.seek(0) #Volta para o início do arquivo

print("\nMétodo readline():\n")
print(manipulador.readline())
print(manipulador.readline())

manipulador.seek(0)

print("\nMétodo readlines():\n")
print(manipulador.readlines())

manipulador.seek(0)
'''

#01
'''
print("Teste de abertura de arquivos em Python")
print("Tentando abrir um arquivo de texto armazenado no PC:\n")

manipulador = open('arquivo.txt','r')

for linha in manipulador:
    linha = linha.rstrip()
    print(linha)
manipulador.close()
'''

#2
'''
print("\nContando as linhas do arquivo de texto: \n")
contador = 0
arq = open("arquivo.txt", "r")
for linha in arq:
    contador = contador + 1
print ("números de linhas no arquivo", contador)
arq.close()
'''
#3

print("\n Retornando somnete as linhas que possuem a palavra luis")
arq = open("arquivo.txt", "r")
contador = 0
for linha in arq:
    linha = linha.rstrip() #Retirar o espaço entre as linhas
    if "luis" in linha:
        contador = contador + 1
        print(linha)
print("\n Foram retornadas", contador, "linhas")
arq.close()

#4
'''
print("\n Retornando somente as linhas que possuem a palavra escolhida pelo usuário")
palavra = input("Digite a palavra q deseja procurar:")
arq = open("arquivo.txt", "r")
contador = 0
for linha in arq:
    linha = linha.rstrip() #Retirar o espaço entre as linhas
    if palavra in linha:
        contador = contador + 1
        print(linha)
print("\n Foram retornadas", contador, "linhas")
arq.close()
'''