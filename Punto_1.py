frase = (input("ingrese El tecto a contabilizar: "))

frase.lower()
texto = frase.split()

cantpal=[]

for palabra in texto:
    cantpal.append(texto.count(palabra))

print("Pares\n" + str(list(zip(texto, cantpal))))
 




