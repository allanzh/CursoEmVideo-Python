# ==== Exercício 24: Identificar a palavra Santo no primeiro nome da cidade
splitCidade = input('Digite o nome da cidade: ').strip().upper().split()
print(splitCidade[0] == 'SANTO')