# ==== Exercício 8: Leia um valor em metros e converta para centimetros e milimetros

metragem = float(input("Digite valor em metros: "))
print("{0}m é correspondente a {1}cm\n{0}m é correspondente a {2}mm".format(metragem, metragem * 100, metragem * 1000))