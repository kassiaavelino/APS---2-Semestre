#Criando e escrevendo em arquivos de texto (modo 'w')

'''
arquivo = open('arq01.txt','w')
arquivo.write("Bóson Treinamentos\n")
arquivo.write("Criando um arquivo de texto em Python\n")
arquivo.write("Arquivo criado por Fábio dos Reis\n")
arquivo.write("É isso ai pessoal!\n")
arquivo.close()

#Lendo o arquivo criado:
arquivo = open('arq01.txt','r')
for linha in arquivo:
    linha = linha.rstrip()
    print(linha)
arquivo.close()
'''

'''
#Acrescentando texto ao arquivo criado, usando o modo 'a'
print("\n")
texto = input("Digite uma frase para acrescentar ao arquivo: ")
arquivo = open('arq01.txt','a')
arquivo.write(texto + "\n")
print("Operação concluída no arquivo "+ arquivo.name + " usando o modo de acesso" )
arquivo.close()

print ("\nTexto alterado:")
arquivo = open('arq01.txt','r')
for linha in arquivo:
    linha = linha.rstrip()
    print(linha)
arquivo.close()
'''
