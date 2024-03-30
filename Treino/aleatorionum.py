import random

nummin = int(input("Digite o valor mínimo: "))
num_max = int(input("Digite o valor máximo: "))

numero_aleatorio = random.randint(nummin, num_max)

print("Número aleatório:", numero_aleatorio)