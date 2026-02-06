import random

print("Bem vindo ao sorteador de números!\n\n" \
"Você deverá escolher um intervalo e um número será sorteado.\n")

while True:
    try:
        inicio_intervalo = int(input("Digite o primeiro número do intervalo: "))
        break
    except ValueError:
        print("Digite apenas números!")

while True:
    try:
        fim_intervalo = int(input("Digite o último número do intervalo: "))
        if inicio_intervalo > fim_intervalo:
            print("O primeiro número do intervalo não pode ser maior que o último!")
            continue
        break
    except ValueError:
        print("Digite apenas números!")

numero_sorteado = random.randint(inicio_intervalo,fim_intervalo)

print(f"O número sorteado foi: {numero_sorteado}")