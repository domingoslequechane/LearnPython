'''Usando o laço For, faça uma tabuada comple que imprima a tabuada dos numeros 1 e 12'''

for i in range(1, 13):
    print(f"\n====[TABUADA {i}]8====")
    for j in range(1, 13):
        print(f"{i} x {j} = {i * j}")