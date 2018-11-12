# ==== Exercício 11: Informando largura e altura da parede, mostra ao usuário quantos litros de tinta ele precisa pra pintar a parede
# considere que 1L de tinta pinta 2m²

# lendo largura e altura
largura = float(input("Informe a largura da parede: "))
altura = float(input("Informe a altura da parede: "))

# calculando e mostrando na tela
resultado = largura * altura
resultado = resultado / 2 
print("voce precisará de {} l de tinta para pintar a parede.".format( resultado ))
5