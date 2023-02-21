def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    palavra_secreta = "maça".upper()
    letras_certas = ['_' for letras in palavra_secreta]

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
if(__name__ == "__main__"):
    jogar()