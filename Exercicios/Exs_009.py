# ==== Exercício 9: Exiba a tabuada de um numero escolhido.

# lendo numero 
numero = int(input("Digite um numero para ver sua tabuada: "))

# gerando tabuada dinamicamente com estrutura de repetição
i = 1
for i in range(1,11):
    print("{} X {} = {}".format(numero, i, numero * i))
    i = i + 1
