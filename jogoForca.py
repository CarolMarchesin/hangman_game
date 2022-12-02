import os 
import os.path
from random import randint

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(len(erros) == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(len(erros) == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(len(erros) == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(len(erros) == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(len(erros) == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(len(erros) == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (len(erros) == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")


def desencriptarPalavra():
    if(os.path.isfile('BancoDePalavras.txt')):
        arq = open('BancoDePalavras.txt', 'r')
        arquivoTXT = arq.readlines()

        numero_palavras = len(arquivoTXT)
        
        numero_aleatorio = randint(0,numero_palavras)

        palavra_secreta = arquivoTXT[numero_aleatorio-1].replace('\n', '')

        palavra_descriptografada = ''
        for i in palavra_secreta:
            palavra_descriptografada = palavra_descriptografada + chr(ord(i) - 5)

        arq.close()
        return palavra_descriptografada
    
    else:
        print('\n')
        print('É necessário configurar o jogo antes!')
        print('\n')
        configurarJogo()

    
def encriptarPalavra(palavra):

    palavra_criptografada = ''
    for i in palavra:
        palavra_criptografada = palavra_criptografada + chr(ord(i) + 5)
    return palavra_criptografada


def adicionarPalavra():
    os.system("cls")
    nova_palavra = input('Digite uma palavra: ').strip().upper()

    nova_palavra = encriptarPalavra(nova_palavra)

    # Gravar palavra no arquivo
    arq = open('BancoDePalavras.txt', 'a')
    arq.write(nova_palavra+'\n')
    arq.close()
    
    os.system("cls")
    menuPrincipal()


# Configurar Jogo
def configurarJogo():
    os.system("cls")
    while(True):
        print('* JOGO DA FORCA*')

        print('>>>   CONFIGURAÇÃO DO JOGO:')
        print('Escolha uma opção:')
        print('A)	Adicionar nova palavra ao jogo.')
        print('B)	Concluir configuração.')

        opcao = input('Opção escolhida: ')

        if (opcao == 'A' or opcao == 'a'):
            adicionarPalavra()
        elif (opcao == 'B' or opcao == 'b'):
            os.system('cls')
            menuPrincipal()
        else:
            print('Opção inválida! Tente novamente...')

os.system('cls')

# Jogar
def jogar():
    os.system('cls')

    palavra_escolhida = desencriptarPalavra()

    qtd_traços= len(palavra_escolhida)
    print('>>> A palavra secreta tem este tamanho: ')
    print()
    print(qtd_traços * '_ ')
    
    chances = 7
    digitadasErradas = []
    totalDigitadas = []

    while True:
        print()
        letra = str(input('Digite a letra que deseja tentar advinhar: ')).strip().upper()
        print('\n')

        if len(letra) > 1:
                print('Digite 1 letra por vez!')
                continue
        
        if letra not in palavra_escolhida:
            if letra not in digitadasErradas: 
                digitadasErradas.append(letra)
                chances -= 1
                print('>>> Lista de Letras já selecionadas:')
                print(digitadasErradas)

            print('\n')
            print('>>> Enforcado:')
            desenha_forca(digitadasErradas)
            print('\n')

            if chances == 0 :
                print('Você perdeu... :(')
                print('\n')
                break

        if letra not in totalDigitadas:    
            totalDigitadas.append(letra)
        
        secreto_temporario = ''
        for letra_secreta in palavra_escolhida:
            if letra_secreta in totalDigitadas:
                secreto_temporario += letra_secreta
            else:
                secreto_temporario += '_ '

        if secreto_temporario == palavra_escolhida:
            print(secreto_temporario)
            print('Parabéns, você ganhou!!!')
            print('\n')
            break
            
        else:
            print(secreto_temporario)
            
        

# Menu Principal
def menuPrincipal():
    while(True):
        print('* JOGO DA FORCA*')
        print('>>>   MENU:')
        print('1)	Configuração do Jogo')
        print('2)	Jogar')
        print('3)	Sair')

        opcao = int(input('Digite a opção que deseja escolher:'))
        print('\n')

        if (opcao == 1):
            configurarJogo()
        elif (opcao == 2):
            jogar()
        elif (opcao == 3):
            exit(0)
        else:
            print('Opção inválida! Tente novamente...')
    
    
    
# Início do Programa
menuPrincipal()