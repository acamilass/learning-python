print("CÁLCULO DO IMC\n")

# FUNÇÕES

def imc(peso_user, altura_user):
    calc = peso_user / (altura_user * altura_user)
    return calc

def validar_peso(peso_user):
    valid_peso = False
    while valid_peso == False:
        try:
            peso_user = float(peso_user)
            if peso_user <= 0:
                print("Informe um peso maior que zero")
            else:
                valid_peso = True
        except:
            print("Informe um peso válido, separando as casas decimais por '.' ")
        valid_peso = True
        peso_user = input("oioioioioiInforme o seu peso: ")

    return peso_user

# valid_peso = False
valid_alt = False


peso = validar_peso(input("Informe o seu peso: "))

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




    