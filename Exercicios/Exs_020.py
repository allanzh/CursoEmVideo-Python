# ==== Exercício 20: Sortear a ordem de apresentação de trabalhos de 4 alunos e exibir em ordem de sorteio.
import random

# Capturando nomes e adicionando a uma list: 
aluno1 = input("Digite o nome do aluno: ")
aluno2 = input("Digite o nome do aluno: ")
aluno3 = input("Digite o nome do aluno: ")
aluno4 = input("Digite o nome do aluno: ")
alunos_list = [aluno1, aluno2, aluno3, aluno4]

# reposicionando os itens da lista com a função shuffle
random.shuffle(alunos_list)

print("A ordem de apresentação é: ", alunos_list)