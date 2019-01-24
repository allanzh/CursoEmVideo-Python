# ==== Exercício 22: Analise de um nome completo
nome = str(input('Digite seu nome completo: ')).strip() # Strip utilizado para remover 
print('Analisando o nome digitado...')
print('Seu nome em MAIUSCULAS é {}'.format(nome.upper()))
print('Seu nome em minusculas é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format( len(nome) - nome.count(' ') ))
splitted = nome.split() #splitted vira uma lista com os nomes separados em index
print('Seu primeiro nome é {} e tem {} letras'.format(splitted[0], len(splitted[0])))