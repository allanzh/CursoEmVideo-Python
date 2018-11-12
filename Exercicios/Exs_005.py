# ==== Exercício 5: Leia um número inteiro e escreva na tela seu Antecessor e Sucessor

num = int(input('Digite um valor inteiro: ')) 
print('\nO Antecessor de {0} é: {1} \nO Sucessor de {0} é: {2}'.format(num, num-1, num+1))