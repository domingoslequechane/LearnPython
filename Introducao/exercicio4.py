'''
    Faça um programa que receba um (1) numero e exiba se ele é positivo ou negativo
'''

numero = int(input("Digite um numero: "))

if numero > 0:
    print("Numero positivo")
elif numero < 0:
    print("Numero negativo")
else:
    print("Numero neutro")