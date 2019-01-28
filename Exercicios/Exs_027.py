# ==== Exercício 27: leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente
nome = input('Escreva seu nome completo: ').strip().upper().split()
lastindex = len(nome) - 1 #pegar a ultima posição do split
print('Seu primeiro nome é {} e seu último nome é {}'.format(nome[0], nome[lastindex]))