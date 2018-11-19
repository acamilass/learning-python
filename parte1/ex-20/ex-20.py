res = ""
compras = []
total = 0
valid_valor = False

while res != "n":
    prod = input("Digite o nome do produto: ").capitalize()
    # qtd = int(input("Quantidade do produto: "))
    
    while valid_valor == False:
        valor = input("Digite o valor do produto: ")
        try:
            valor = float(valor)
            if valor <= 0:
                print("O valor precisa ser maior que zero")
            else:
                valid_valor = True
        except:
            print("Formato de preço inválido. Use apenas números e separe com ponto '.'\n")

    # total_prod = qtd * valor
    compras.append([prod, valor])
    total += valor
    valid_valor = False

    res = input("Deseja comprar mais algo? S/N ").lower()

print("\nItens comprados:")
for i in compras:
    print(i[0],"- R$"+ str(i[1]))

print("Total: R$"+ str(round(total, 2)))


