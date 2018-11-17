# ==== Exercício 13: Leia um salário e mostre o novo salário com aumento de 15%

salario = float(input("Qual o salário atual? "))
salario = salario + ((salario * 15) / 100)
print("Seu novo salário será: R${:.2f}".format(salario))