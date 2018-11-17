# ==== Exercício 16: Leia um numero real e retorne apenas o numero inteiro relativo a ele
import math

num = float(input("Digite um número: "))
# função trunc vai arredondar o numero real para o numero inteiro mais proximo de zero possível então "trunc(6.999) => 6"
print("O número {} tem a parte inteira {}".format(num, math.trunc(num)))