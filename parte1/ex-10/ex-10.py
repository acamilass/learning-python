meses = ("janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", 
        "outubro", "novembro", "dezembro")

data_nasc = input("Digite a sua data de nascimento (DD/MM/AAAA): ")

mes = int(data_nasc[3:5]) - 1
print("Você nasceu no mês de:",meses[mes])