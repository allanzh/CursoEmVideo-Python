# ==== Exercício 7: Leia duas notas de um determinado aluno e mostre na tela a média

# lendo as duas notas:
n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))

# Calculando a média:
media = (n1 + n2) / 2

# Mostrando na tela
print("A média do aluno foi: {}".format(media))