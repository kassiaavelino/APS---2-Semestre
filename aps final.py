from time import sleep
import os
import sys
import getpass

#lista contendo o alfabeto que será utilizado na cifragem
alfabeto = [' ','.',',','á','à','é','è','ã','ó','ò','õ',
'a','ô','ê','b','c','d','e','f','g','h','i','j','k','l',
'm','n','o','p','q','r','s','t','u','v','w','x','y','z',
'1','2','3','4','5','6','7','8','9','0','A','B','C','D',
'E','F','G','H','I','J','K','L','M','N','O','P','Q','R',
'S','T','U','V','W','X','Y','Z',
]

#def de decoração
def deco():
    print('='*80)

#essa função servirá para entrada de dados 
def inputCifrar():
    deco()
    msg = input('Digite uma mensagem\n\nMensagem: ')
    deco()
    chave = int(input('Digite um número inteiro de 1 à 12:\n\nNúmero da chave: '))
    deco()
    while(True):
        if (chave >= 1 and chave <=12):
            return msg, chave
        else:
            print('Numero Inválido!\nFaça Novamente')
            print('')
            deco()
            main()

#essa função servirá para entrada de dados 
def inputDescifrar():
    deco()
    msg = input('Digite a mensagem cifrada\n\nMensagem: ')
    deco()
    chave = int(input('Digite o numero da chave\n\nNumero da chave: '))
    deco()
    while(True):
        if (chave >= 1 and chave <=12):
            return msg, chave
        else:
            print('Numero Invalido\nFaça Novamente')
            print('')
            deco()
            main()

#essa chave servirá para apresentação dos dados descifrada
def inputDados(msg, chave):
    print(' \nA mensagem decifrada é: {}'.format(msg))
    print('')
    deco()

#essa chave servirá para apresentação dos dados cifrada
def outputDados(msg, chave):
    print('\nA mensagem cifrada é: {}'.format(msg))
    print('')
    deco()

#variável chave será o número utilizado para cifrar e decifrar a mensagem    
def cifrar (msg, chave):
    #armazenará o resultado da cifragem
    msgCifrada = ''
    #Esse loop percorrerá cada caractere da mensagem que virá a ser cifrada
    for caracter in msg:    
#        esse contador será utilzado para verificar em qual indice o caractere da volta está no vetor alfabeto
        for i in range(len(alfabeto)):
            if (alfabeto[i] == caracter):
                if ((i+chave) > len(alfabeto)):
                    msgCifrada = msgCifrada + alfabeto[i + chave]
                else:    
                    msgCifrada = msgCifrada + alfabeto[i + chave]
    return msgCifrada

#def de decifrar a mensagem
def decifrar (msg, chave):
    #armazenará o resultado da cifragem
    msgDecifrada = ''
    #Esse loop percorrerá cada caractere da mensagem que virá a ser cifrada
    for caracter in msg:
#        esse contador será utilzado para verificar em qual indice o caractere da volta está no vetor alfabeto
        for i in range(len(alfabeto)):
            
            if (alfabeto[i] == caracter):
                msgDecifrada = msgDecifrada + alfabeto[i - chave]          
    return msgDecifrada            

def main():    
    #essa aqui é a estrutura de apresentação do menu
    sleep(1)
    while(True):
        deco()
        opcMenu = int (input("Selecione a opção desejada\n\n1. Cifrar\n2. Decifrar\n3. Sair\n\nOpção: "))
        deco
        if(opcMenu == 1):
            msg, chave = inputCifrar()
            result = cifrar(msg, chave)
            outputDados(result, chave) 
            msg_c = open('cifrada.txt','a')
            msg_c.write("\n"+ result)
            msg_c.close() 
            cadastro() 

        elif(opcMenu == 2):
            msg, chave = inputDescifrar()
            result = decifrar(msg, chave)
            inputDados(result, chave) 
            msg_c = open('decifrada.txt','a')
            msg_c.write("\n" + result)
            msg_c.close() 
            cadastro() 
                
        elif(opcMenu == 3):
            print("Encerrando a aplicação...")
            sys.exit()
            break
            
        elif(opcMenu >= 4):
            print('Opção Inválida!!!\nInsira novamente')

            
            
# cadastro de login               
def cadastro():
        deco()
        print('    Faça seu login\n')   
        login = str(input('Login: '))
        senha = int(getpass.getpass('Senha: '))
        
        deco()
        if (login == 'adm') and (senha == 123):
            main()

        else:
            deco()
            print('Login ou Senha Inválida')
            print('Tente Novamente')
            deco()
            cadastro()
cadastro() 
