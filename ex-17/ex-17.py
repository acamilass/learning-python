nome_aluno = input("Digite o nome do aluno: ")
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
qtd_faltas = int(input("Digite a quantidade de faltas: "))

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
print("Media:",media)
print("Percentual de presença:",str(100 * perc_pres) +"%")
print("Resultado:",res)