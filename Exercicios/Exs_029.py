# ==== Exercício 29: Leia a velocidade de um carro. Se ele ultrapassar 80Km/h, informe que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.
velocidade = int(input('Informe a velocidade do veículo: '))
print('O veículo estava a {}km/h')
if velocidade > 80:
    diferenca = velocidade - 80
    multa = diferenca * 7
    print('Você será multado em R${},00 por ter passado a {}km/h, {}km/h a mais que a velocidade permitida da via.'.format(multa, velocidade, diferenca))
else:
    print('Parabéns, você é um motorista exemplar!')
