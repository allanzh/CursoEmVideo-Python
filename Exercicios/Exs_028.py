# ==== Exercício 28: Faça o computador "pensar" em um número inteiro entre 0 e 5, peça para o usuário descobrir qual foi o número. Escreva se o usuário venceu ou perdeu.
from random import randint
numEscolhido = randint(0,5)
numUsuario = int(input('Tente adivinhar o número que pensei entre 0 a 5: '))
if numEscolhido == numUsuario:
    print('Parabéns, você adivinhou o número')
else:
    print('Você errou, o número que pensei foi {}'.format(numEscolhido))