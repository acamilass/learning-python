print("CÁLCULO DO IMC\n")

# FUNÇÕES

def imc(peso_user, altura_user):
    calc = peso_user / (altura_user * altura_user)
    return calc

def type_imc(gen_user, peso_user, altura_user):
    if gen_user == "f":
        if imc(peso_user, altura_user) < 19.1:
            return "Você está abaixo do peso"
        elif imc(peso_user, altura_user) >= 19.1 and imc(peso_user, altura_user) <= 25.8:
            return "Você está no peso ideal"
        elif imc(peso_user, altura_user) >= 25.9 and imc(peso_user, altura_user) <= 27.3:
            return "Você está acima do peso"
        elif imc(peso_user, altura_user) >= 27.4 and imc(peso_user, altura_user) <= 32.3:
            return "Você tem obesidade 1"
        else:
            return "Você tem obesidade 2"
    else:
        if imc(peso_user, altura_user) < 20.7:
            return "Você está abaixo do peso"
        elif imc(peso_user, altura_user) >= 20.7 and imc(peso_user, altura_user) <= 26.4:
            return "Você está no peso ideal"
        elif imc(peso_user, altura_user) >= 26.5 and imc(peso_user, altura_user) <= 27.8:
            return "Você está acima do peso"
        elif imc(peso_user, altura_user) >= 27.9 and imc(peso_user, altura_user) <= 31.1:
            return "Você tem obesidade 1"
        else:
            return "Você tem obesidade 2"

# END

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

print("O seu imc é: ", imc(peso, altura))
print(type_imc(genero, peso, altura))






    