import random

def jogar():
    
    menu_de_jogo()
    palavra_secreta = carrega_palavras()

    letras_certas = inicializa_letras_certas(palavra_secreta)
    print(letras_certas)

    enforcou = False
    acertou = False
    erros = 0    

    while(not enforcou and not acertou):
        chute = pede_chute()

        if(chute in palavra_secreta):
            marca_chute_correto(chute, letras_certas, palavra_secreta)
        else:
            marca_chute_errado()

        enforcou = erros == 6
        acertou = '_' not in letras_certas 
        print(letras_certas)    
    if(acertou):
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor()        

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

def pede_chute():
    chute = input("Qual a letra? ")
    chute = chute.strip().upper()
    return chute

def marca_chute_correto(chute, letras_certas, palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if(chute.upper() == letra.upper()):
            letras_certas[index] = letra
        index += 1

def imprime_mensagem_vencedor():
    print("Voce ganhou!!")

def imprime_mensagem_perdedor():
    print("Voce perdeu!!")

def marca_chute_errado():
    erros += 1
    print("Ops, você errou! Faltam {} tentativas.".format(6-erros))

if(__name__ == "__main__"):
    jogar()