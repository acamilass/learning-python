import func

print("CÁLCULO DO IMC\n")

valid_peso = False
valid_alt = False
valid_gen = False

while valid_gen == False:
    genero = input("Informe o seu genero (M/F): ").lower()
    if genero == "m" or genero == "f":
        valid_gen = True 
    else:   
        print("Informe um genero válido M ou F")     

while valid_peso == False:
    peso = input("Informe o seu peso: ")
    try:
        peso = float(peso)
        if peso <= 0:
            print("Informe um peso maior que zero")
        else:
            valid_peso = True
    except:
        print("Informe um peso válido, separando as casas decimais por '.' ")

while valid_alt == False:
    altura = input("Informe a sua altura: ")
    try: 
        altura = float(altura)
        if altura <= 0:
            print("Informe uma altura maior que zero")
        else:
            valid_alt = True
    except:
        print("Informe uma altura válida, separando as casas decimais por '.' ")

print("O seu imc é: ", func.imc(peso, altura))
print(func.type_imc(genero, peso, altura))
