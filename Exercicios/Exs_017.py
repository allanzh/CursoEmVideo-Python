# ==== Exercício 17: ler o cateto oposto e cateto adjacente e calcular a hipotenusa.
# h² = Co² + Ca²
import math

cat_opo = float(input("Digite o cateto oposto: "))
cat_adj = float(input("Digite o cateto adjacente: "))

hip = math.pow(cat_opo , 2) + math.pow(cat_adj , 2) # esse calculo retorna o quadrado da hipotenusa
hip = math.sqrt(hip) # essa linha retorna a hipotenusa

print("A hipotenusa é: {:.2f}".format(hip))

# Tambem dá pra usar uma função da lib math
hipFromMath = math.hypot(cat_opo,cat_adj)

print("A hipotenusa é: {:.2f}".format(hipFromMath))