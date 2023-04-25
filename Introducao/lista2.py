lista = []
print("Adicione os nomes que pretende adicionar,\nDigite 'v' para ver a lista e 's' para sair da aplicação: ")
while True:
    entrada = str(input("Entrada: "))
    if entrada == '':
        print("A entrada não pode ser vasía")
        continue
    elif entrada == 'v':
        print(lista)
    elif entrada == 's':
        sair = str(input("Pretende realmente sair? (S-sim / N-nao): "))
        if sair == 'S':
            print("Obrigado pela prefencia!")
            break
        else:
            continue
    lista.append(entrada)