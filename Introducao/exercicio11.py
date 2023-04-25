'''Usando o laço for, faça um programa que receba um número e imprima a tabuada desse mesmo número'''

numero = int(input("Digite um numero: "))
print(f"Tabuada da casa {numero}")
for i in range(1, 13):
    print(f"{numero} x {i} = {numero*i}")