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