nome_aluno = input("Digite o nome do aluno: ")

valid_nota = False
while valid_nota == False:
    nota1 = input("Digite a primeira nota: ")
    try: 
        nota1 = float(nota1)
        if nota1 < 0 or nota1 > 10:
            print("Nota inválida, informe uma nota entre 0 e 10")
        else:
            valid_nota = True
    except:
        print("Informe uma nota separando os decimais por '.'")

valid_nota = False
while valid_nota == False:
    nota2 = input("Digite a segunda nota: ")
    try: 
        nota2 = float(nota2)
        if nota2 < 0 or nota2 > 10:
            print("Nota inválida, informe uma nota entre 0 e 10")
        else:
            valid_nota = True
    except: 
        print("Informe uma nota separando os decimais por '.'")

valid_faltas = False
while valid_faltas == False:
    qtd_faltas = input("Digite a quantidade de faltas: ")
    try:
        qtd_faltas = int(qtd_faltas)
        if qtd_faltas < 0 or qtd_faltas > 20:
            print("Quantidade inválida, informe um número entre 0 e 20")
        else:
            valid_faltas = True
    except:
        print("Informe um número inteiro para quantidade de faltas")

media = (nota1 + nota2)/2
perc_pres = (20 - qtd_faltas)/20

if media >= 6 and perc_pres >= 0.7:
    res = "Aprovado por média"
elif media < 6 and perc_pres < 0.7:
    res = "Reprovado por média e faltas"
elif media < 6:
    res = "Reprovado por média"
elif perc_pres < 0.7:
    res = "Reprovado por faltas"

print("\nInformações do aluno")
print("Nome do aluno:",nome_aluno)
print("Média:",media)
print("Percentual de presença:",str(100 * perc_pres) +"%")
print("Resultado:",res)