frase =(input("digite la frase"))

carcdic= []

for caracter in frase:
    carcdic.append(frase.count(caracter))

    print("Caracteres\n" + str(list(zip(frase, carcdic))))