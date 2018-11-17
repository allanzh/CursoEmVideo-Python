# ==== Exercício 18: ler um angulo e mostrar na tela seno, cosseno e tangente.
import math

angulo = float(input("Digite um angulo: "))

# Calculando ...
sen = math.sin(math.radians(angulo))
cos = math.cos(math.radians(angulo))
tgt = math.tan(math.radians(angulo))

print("O seno de {0} é: {1:.2f}\nO cosseno de {0} é {2:.2f}\nA tangente de {0} é {3:.2f}".format(angulo, sen, cos, tgt))