# ==== Exercício 14: Conversor de temperatura que lê C° e mostra F°

temp = float(input("Digite a temperatura em C°: "))
print("{}°C é equivalente a {}°F".format(temp, ( ( (9 * temp) / 5) + 32) ))