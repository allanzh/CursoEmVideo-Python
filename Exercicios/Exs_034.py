# ==== Exercício 34: Pergunte o salário de um funcionário e calcule o valor do seu aumento.
#  Para salários superiores a R$1250,00, calcule um aumento de 10%.
#  Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input('digite seu salario: '))

if salario > 1250:
    aumento = (salario / 100)
    aumento *= 10
else:
    aumento = (salario / 100)
    aumento *= 15

print('O seu Salário será reajustado de R${:.2f} para R${:.2f}'.format(salario, salario + aumento))