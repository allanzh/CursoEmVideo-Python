# ==== Exercício 23: Ler um numero e mostrar digitos separadamente
num = int(input('Digite um número: '))
strnum = str(num)
print('Separando o numero digitado...')
print('Unidade: {}'.format(strnum[3]))
print('Dezena: {}'.format(strnum[2]))
print('Centena: {}'.format(strnum[1]))
print('Milhar: {}'.format(strnum[0]))