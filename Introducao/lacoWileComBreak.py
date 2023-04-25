'''O comando Break serve para interromper uma intrução white;'''

i = 0

while i < 5:
    print(i)
    if i % 2 == 0:
        i += 2
        continue
    i += 1