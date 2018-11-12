# ==== Exercício 12: Programa que le um preço e informa o novo preço com desconto de 5%

preco = float(input("Qual o preço do produto? "))
preco = preco - ((preco * 5) / 100)
print("O preco com desconto é: R${:.2f}".format(preco))