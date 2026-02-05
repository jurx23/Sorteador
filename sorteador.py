import random

print("Bem vindo ao sorteador de números!\n\n" \
"Você deverá escolher um intervalo e um número será sorteado.\n")

inicio_intervalo = int(input("Digite o primeiro número do intervalo: "))
fim_intervalo = int(input("Digite o último número do intervalo: "))

numero_sorteado = random.randint(inicio_intervalo,fim_intervalo)

print(f"O número sorteado foi: {numero_sorteado}")