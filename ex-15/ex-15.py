idade = int(input("Digite a sua idade: "))
genero = input("Digite o seu gênero (M/F): ").lower()

if genero == "m":
    if idade >= 18:
        print("Você é um homem maior de idade")
    else:
        print("Você é um homem menor de idade")
elif genero == "f":
    if idade >= 18:
        print("Você é uma mulher maior de idade")
    else:
        print("Você é uma mulher menor de idade")
else:
    print("Erro na entrada de dados")