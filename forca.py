import random

def jogar():
    
    menu_de_jogo()

    palavra_secreta = carrega_palavras()

    letras_certas = inicializa_letras_certas(palavra_secreta)

    enforcou = False
    acertou = False
    erros = 0

    print(letras_certas)

    while(not enforcou and not acertou):
        chute = input("Qual a letra? ")
        chute = chute.strip().upper()

        if(chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if(chute.upper() == letra.upper()):
                    letras_certas[index] = letra
                index += 1
        else:
            erros += 1
            print("Ops, você errou! Faltam {} tentativas.".format(6-erros))

        enforcou = erros == 6
        acertou = '_' not in letras_certas 
        print(letras_certas)

    if(acertou):
        print("Voce ganhou!!")
    else:
        print("Voce perdeu!!")
    
    print("Fim de jogo")

def inicializa_letras_certas(palavra):
    return ['_' for letras in palavra]

def menu_de_jogo():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

def carrega_palavras():
    palavras = []
    with open("palavras.txt") as arquivo:
        for linha in arquivo:
            linha = linha.strip()
            palavras.append(linha)

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta

if(__name__ == "__main__"):
    jogar()