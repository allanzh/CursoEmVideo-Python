# ==== Exercício 15: Programa que lê Km rodado e dias de uso de um carro e calcula preço do aluguel
# Considere:
#       1 dia = R$60,00
#       1 km = R$0,15

dias = int(input("Você utilizou o carro por quantos dias? "))
km = float(input("Quantos km rodados? "))

resultado = (60 * dias) + (0.15 * km)

print("Você pagará: R${:.2f}".format(resultado))