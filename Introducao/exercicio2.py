'''
    Faça um programa que receba 4 notas de um aluno e exiba se ele foi aprovado ou reprovado
    Se o estudante tiver uma media maior ou igual a 10, ele deve ser aprovado
    Se tiver nota maior ou iguar a 7 e menor que 10 ele tera que fazer a recuperação
    Se a media estiver abaixo de 7, o estudante deve ser dado como reprovado
'''

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nora: "))
nota3 = float(input("Digite a terceira nota: "))
nota4 = float(input("Digite a quarta nota: "))

media = (nota1 + nota2 + nota3 + nota4) / 4

print(f"A sua media é: {media}")
if media >= 10:
    print("Estudante aprovado")
elif media < 7:
    print("Estudante reprovado")
else:
    print("Fazer recuperação")