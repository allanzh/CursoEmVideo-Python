# ==== Exercício 6: Leia um número e exiba na tela o Dobro, Triplo e Raiz Quadrada desse número.

# importando lib math para usar função sqrt
# No python é possivel importar a lib inteira ou apenas algumas funções específicas:

# \/ Lib inteira
#import math # <-- Importando desse jeito é preciso chamar as funções usando "math."  ex: math.sqrt(2)

# \/ Funções de uma determinada Lib 
from math import sqrt, pow, acos #... <-- Importando desse jeito não é preciso chamar as funções usando "math."  ex: sqrt(2)


num = int(input("Digite um numero: "))
print("\nO numero escolhido foi {0} \n   O dobro é {1} \n   O Triplo é {2}\n   A Raiz Quadrada é {3}".format(num, num * 2, num * 3, int(sqrt(num))))
