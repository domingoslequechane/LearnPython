'''Assim como peradores relacionais ele retorna Verdade ou falso,
mas diferentemente, ele faz uma comparação entre os Verdadeiros e Falsos'''

'''Operadores:
    and -> && / e
    or -> | / ou
    not -> não
'''

# And - so retorna True se as duas condicoes forem verdadeiras
operador = True & True
# ou
operador = True and True
print(operador)

# Or - so retorna True se apenas uma das duas condicoes forem verdadeiras
operador = True | False
#  ou
operador = True or False
print(operador)

# not - retorna o valor contrario, de True para False (vice-versa)
operador = not False
print(operador)
#  ou
operador = not True
print(operador)