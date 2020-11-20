def imc(estatura, peso):
    return peso/estatura ** 2


peso= float(input("Por favor Digite su Peso: "))
estatura = float(input("Por favor Digite Su estatura en metros: "))

resultado = imc(estatura,peso)

if resultado < 18.5:
    print (f"Su IMC es: {resultado} categorizado en peso insuficiente")
else:
    if resultado >=18.5 and resultado < 24.9:
        print(f"Su IMC es: {resultado} categorizado en peso Normal")
    else:
        if resultado >=25 and resultado < 26.9:
            print(f"Su IMC es: {resultado} categorizado en peso SobrePeso Grado 1")
        else:
            if resultado >=27 and resultado < 29.9:
                print(f"Su IMC es: {resultado} categorizado en peso SobrePeso Grado II")
            else:
                if resultado >=29 and resultado < 34.9:
                    print(f"Su IMC es: {resultado} categorizado en peso SobrePeso Grado II")
                else:
                    print(f"Su IMC es: {resultado} Usted Esta Muy Gordito")
            

