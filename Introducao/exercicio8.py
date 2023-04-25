'''
    Escreva um programa que receba notas de um aluno (0-10), caso
    Caso a nota digitada esteja fora desse intervalo, peça para o professor digitar novamente
'''

nota = 0

while nota <= 10:
    nota = float(input("Digite uma nota de 0 à 10: "))
    if nota > 10:
        print(f"Nota inválida. Voce digitou {nota}")
        nota = 0
        continue
    else:
        print("Nota valida e armazenada com sucesso!")
        break