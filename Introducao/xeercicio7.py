'''Escreva um programa que receba um numero do usuario e mostre a tabuada desse número'''

numero = int(input("Qual tabuada voce quer? digite um numero: "))
i = 1

while i <= 12:
    if i == 1 :
        print(f"Tabuada da casa {numero}")

    print(f"{numero} x {i} = {numero * i}")

    i += 1