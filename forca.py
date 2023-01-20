def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    enforcou = False
    acertou = False

    palavra_secreta = "banana"

    while(not enforcou and not acertou):
        chute = input("Qual a letra? ")

        index =0
        for letra in palavra_secreta:
            if(chute == letra):
                print("Encontrei a letra {} na posição {}".format(letra, index))
            index = index + 1
        print("Jogando...")

    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar()
