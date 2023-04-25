'''Receba a temperatura em farenheit e exiba em graus celsious'''
# C = 5 * f - 32 / 9

tempFarenheit = float(input("Digite a temperatira em farenheit: "))

tempCelsious = 5 * ((tempFarenheit - 32) / 9)

print(f"A temperatura em celsious é: {tempCelsious}")