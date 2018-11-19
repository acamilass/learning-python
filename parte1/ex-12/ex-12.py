print("DICIONÁRIO PORTUGUÊS-INGLÊS")

colors = {
    "amarelo": "yellow",
    "azul": "blue",
    "vermelho": "red",
    "verde": "green",
    "rosa": "pink",
    "laranja": "orange",
    "roxo": "purple"
}

traduz = input("Digite uma cor para ser traduzida: ")

print(colors.get(traduz, "Esta cor não está no dicionário"))