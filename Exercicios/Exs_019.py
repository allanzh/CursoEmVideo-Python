# ==== Exercício 19: Sortear um entre 4 alunos para apagar o quadro lendo o nome deles e escrevendo o nome do escolhido.
import random

# Capturando nomes: 
aluno1 = input("Digite o nome do aluno: ")
aluno2 = input("Digite o nome do aluno: ")
aluno3 = input("Digite o nome do aluno: ")
aluno4 = input("Digite o nome do aluno: ")

# Dois métodos de resolver a partir daqui:

# ===============================
# Método 1 - Utilizando if/else
# ===============================
'''
Utilizei esse método antecipando o assunto "estruturas de controle de fluxo" que não tinha sido ensinado ainda. 
'''

# sorteio guarda um numero aleatorio entre 1 e 4 gerado pelo computador.
sorteio = random.randint(1,4)

# Se o sorteio for 1, guarda-se o valor do nome do aluno 1 como sorteado
if (sorteio == 1):
    alunoSorteado = aluno1
# Se o sorteio for 2, guarda-se o valor do nome do aluno 2 como sorteado
if (sorteio == 2):
    alunoSorteado = aluno2
# Se o sorteio for 3, guarda-se o valor do nome do aluno 3 como sorteado
if (sorteio == 3):
    alunoSorteado = aluno3
# Se o sorteio for 4, guarda-se o valor do nome do aluno 4 como sorteado
if (sorteio == 4):
    alunoSorteado = aluno4

# Imprime o aluno sorteado:
print("O aluno sorteado foi: ", alunoSorteado)

# ===============================
# Método 2 - Utilizando Lista
# ===============================
'''
Eu não sabia utilizar lista antes de ver a resolução desse exercicio, 
foi uma falha do professor que esqueceu de passar o conteudo suficiente para a resolução dessa questão,
segue o metodo utilizado por ele para resolver
'''

# Gera-se uma lista para guardar os nomes e sortea-los:
lista = [aluno1, aluno2, aluno3, aluno4]

# Sorteia um aluno e guarda seu nome:
alunoSorteado = random.choice(lista)

# Imprime o aluno sorteado:
print("O aluno sorteado foi: ", alunoSorteado)

'''
Note que, ao rodar o programa assim, o programa irá gerar dois sorteados, e eles não necessariamente serão os mesmos,
basta então comentar uma das duas formas para sortear apenas uma vez.
'''