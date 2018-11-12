# ==== Exercício 4: leia algo do teclado e mostre na tela o tipo primitivo e informações gerais

leitura = input("Digite: ")
print("O tipo desse valor é ", type(leitura))
print("É só espaço? ", leitura.isspace())
print("É numero? " , leitura.isnumeric())
print("É alfabetico? ", leitura.isalpha())
print("É alfanumérico? ", leitura.isalnum())
print("É maiusculo? ", leitura.isupper())
print("É minusculo? ", leitura.islower())
print("É titulo? ", leitura.istitle())