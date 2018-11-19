import time

def cont_tempo():
    inicio = time.clock()
    input("Digite o seu nome: ")
    fim = time.clock()
    tempo = fim - inicio
    return tempo

print("Você levou "+ str(cont_tempo()) +" segundos para digitar o seu nome")
