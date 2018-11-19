print("\nDICIONÁRIO PORTUGUÊS-INGLÊS\n")

res = ""

colors = {
    "amarelo": "Yellow",
    "azul": "Blue",
    "vermelho": "Red",
    "verde": "Green",
    "rosa": "Pink",
    "laranja": "Orange",
    "roxo": "Purple"
}

while res != "n":
    traduz = input("Digite uma cor para ser traduzida: ").lower()

    print(colors.get(traduz, "Esta cor não está no dicionário"))

    res = input("Deseja consultar outra palavra? S/N ").lower()
