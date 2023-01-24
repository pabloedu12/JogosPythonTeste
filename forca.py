def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    enforcou = False
    acertou = False

    palavra_secreta = "banana"
    letras_certas = ['_', '_', '_', '_', '_', '_',]

    while(not enforcou and not acertou):
        chute = input("Qual a letra? ")
        chute = chute.strip()

        index = 0
        for letra in palavra_secreta:
            if(chute.upper() == letra.upper()):
                letras_certas[index] = letra
            index = index + 1
        
        print(letras_certas)