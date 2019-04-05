# ==== Exercício 31:  Pergunte a distância de uma viagem em Km e calcule o preço da passagem 
# até 200km: R$0,50 por Km 
# acima 200 km: R$0,45 por Km
dist = float(input('Qual a distancia em km da viagem? '))
if dist < 201:
    result = dist * 0.5
else:
    result = dist * 0.45
print('O preço da viagem é de R${:.2f}'.format(result))

# solução com if inline:
# result = dist * 0.5 if dist < 201 else dist * 0.45