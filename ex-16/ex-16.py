nome_aluno = input("Digite o nome do aluno: ")
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
qtd_faltas = int(input("Digite a quantidade de faltas: "))

media = (nota1 + nota2)/2
perc_faltas = 5 * qtd_faltas

if media < 6: # logica errada
    res = "Reprovado por média"
elif perc_faltas >= 70 and media < 6:
    res = "Reprovado por faltas e média"
elif perc_faltas >= 70:
    res = "Reprovado por falta"
elif perc_faltas < 70 and media >= 6:
    res = "Aprovado por média"

print("\nInformações do aluno")
print("Nome do aluno:",nome_aluno)
print("Media:",media)
print("Percentual de presença:",str(100 - perc_faltas) +"%")
print("Resultado:",res)