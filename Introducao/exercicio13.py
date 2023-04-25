'''Faça um programa que imprima numeros pares entre 1 e 1000 usando for'''

for i in range(1, 1001):
    if i % 2 == 0:
        print(i)

'''Ou'''

for i in range(1, 1001, 2):
    print(i)