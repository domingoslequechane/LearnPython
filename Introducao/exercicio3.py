'''
    Faça um programa que receba 3 números inteiros e imprima o maior dentre eles
'''

numero1 = int(input("Digite o primeiro numero: "))
numero2 = int(input("Digite o segundo numero: "))
numero3 = int(input("Digite o terceiro numero: "))

if numero1 > numero2 and numero1 > numero3:
    print(f"O maior numero é: {numero1}")
elif numero2 > numero1 and numero2 > numero3:
    print(f"O maior numero é: {numero2}")
else:
    print(f"O maior numero é: {numero3}")