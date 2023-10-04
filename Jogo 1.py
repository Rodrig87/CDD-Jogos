contador1 = 0
contador2 = 0

while contador1 < 2 and contador2 < 2:
    jogador1 = input("Digite: Pedra, Papel ou Tesoura - ")
    jogador2 = input("Digite: Pedra, Papel ou Tesoura - ")

    while jogador1 == jogador2:
        jogador1 = input("Digite: 'Pedra', Papel ou Tesoura - ")
        jogador2 = input("Digite: Pedra, Papel ou Tesoura - ")

    if jogador1 == 'Pedra':
        if jogador2 == 'Tesoura':
            print("Vitória do Jogador 1")
            contador1 = contador1 + 1
        else:
            print("Vitória do Jogador 2")
            contador2 = contador2 + 1
    if jogador1 == 'Tesoura':
         if jogador2 == 'Pedra':
             print("Vitória do Jogador 2")
             contador2 = contador2 + 1
         else:
             print("Vitória do Jogador 1")
             contador1 = contador1 + 1
    if jogador1 == 'Papel':
        if jogador2 == 'Tesoura':
            print("Vitória do Jogador 2")
            contador2 = contador2 + 1
        else:
            print("Vitória do Jogador 1")
            contador1 = contador1 + 1
if contador1 == 2:
    print("Jogador 1 ganhou!!")
else:
    print("Jogador 2 ganhou!!")
