# ==== Exercício 26: ler uma frase e mostre quantas vezes aparece a letra "A", em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.
frase = input('Escreva uma frase: ').strip().upper()
qtdA = frase.count('A')
first = frase.find('A') + 1
last = frase.rfind('A') + 1
print('A frase contém {} ocorrências da letra A'.format(qtdA))
print('          a primeira ocorrência é na posição {}\n          a ultima ocorrência é na posição {}'.format(first, last))