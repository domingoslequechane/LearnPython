'''Faça um programa que defina o usuario e senha e depois verifique se o loin do usuario é válido'''

usuarioDB = 'leq'
senhaDB = '12345'

usuarioInput = str(input("Digite o seu nome de usuario: "))
senhaInput = str(input("Digite a sua senha: "))

if usuarioInput != usuarioDB and senhaInput != senhaDB:
    while usuarioInput != usuarioDB and senhaInput != senhaDB:
        print("Usuario ou senha Inválida")
        usuarioInput = str(input("Digite o seu nome de usuario: "))
        senhaInput = str(input("Digite a sua senha: "))
        if usuarioInput != usuarioDB and senhaInput != senhaDB:
            continue
        else:
            print("Usuario logado com sucesso!")
            break