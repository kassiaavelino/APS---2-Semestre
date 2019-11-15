from time import sleep
import os
import sqlite3
import sys

#import getpass
#password = getpass.getpass('Senha: ')

conn = sqlite3.connect('cadastro.db')
cursor = conn.cursor()
def begin():
    def create_table():
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS cadastro (
            login TEXT NOT NULL,
            senha INTEGER
        );
    """)

    create_table()

    login1 = input('Login: ')
    senha1 = input('Senha: ')

    cursor.execute("""INSERT INTO cadastro (Login, Senha) 
    VALUES (?,?)""", (login1, senha1))
    print(' -------------------------')
    print('| Cadastrado com sucesso! |')
    print(' -------------------------')

    conn.commit()
    
def autenticacao():
    login = input('Login: ')
    senha = input('Senha: ')

    try:
        cursor1 = conn.execute('SELECT login FROM cadastro')

        for row in cursor1 :
            if login in row:
                print ('Usuário:', login)
                cursor1 = conn.execute('SELECT login FROM cadastro WHERE senha = %s' % (senha))
                print ('percorrendo a senha')
                if senha in cursor1:
                    print('Bem vindo ao sistema! %s' % login)
                    main()

                else:
                    print ('senha incorreta!')
                
                return
        print('Login incorreto" Se você ainda não se cadastrou, cadastre-se')
    except IOError:
        print('Select statement could not execute!')  




#lista contendo o alfabeto que será utilizado na cifragem
alfabeto = [' ','.',',','á','à','é','è','ã','ó','ò','õ',
'a','ô','ê','b','c','d','e','f','g','h','i','j','k','l',
'm','n','o','p','q','r','s','t','u','v','w','x','y','z',
'1','2','3','4','5','6','7','8','9','0','A','B','C','D',
'E','F','G','H','I','J','K','L','M','N','O','P','Q','R',
'S','T','U','V','W','X','Y','Z',
]

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

#essa função servirá para entrada de dados
def inputDados():
    msg = input('\nDigite a mensagem: \n')
    print("=-="*34)
    chave = int(input('Digite um numero inteiro de 1 à 25:\n'))
    print("=-="*34)
    return msg, chave

#essa chave servirá para apresentação dos dados
def outputDados(msg, chave):
    print('\nPara a chave: {}\nO resultado é: {}'.format( chave, msg))
    print('')
    print("=-="*34)

def m():
    while(True):
        sleep(1)
        menu_login = int(input("Selecione uma opção\n1.Cadastrar\n2.Login\n"))
        if(menu_login == 1):
            begin()
        elif(menu_login == 2):
           autenticacao() 

          
    
def fim():
    print("Retornando para o login")
# def fodase():
#     print('Vai a merda')
def main():
    #essa aqui é a estrutura de apresentação do menu
    while(True):
        sleep(1)        
        #diretorio = os.getcwd()
        #print("Voce esta nesse diretorio", diretorio)
        opcMenu = int (input("Selecione a opção desejada\n1. Cifrar\n2. Decifrar\n3. Sair\n"))
        if(opcMenu == 1):
            msg, chave = inputDados()
            result = cifrar(msg, chave)
            outputDados(result, chave) 
            msg_c = open('cifrada.txt','a')
            msg_c.write("\n"+ result)
            msg_c.close()  

        elif(opcMenu == 2):
            msg, chave = inputDados()
            result = decifrar(msg, chave)
            outputDados(result, chave) 
            msg_c = open('decifrada.txt','a')
            msg_c.write("\n" + result)
            msg_c.close()  

        elif(opcMenu == 3):
            print('Programa Finalizado!')
            sys.exit()

m()