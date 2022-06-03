import random
lista_frutas = ['manga', 'goiaba', 'acerola', 'melancia', 'uva', 'banana']
total_de_tentativas = 3
rodada = 1

while rodada <= total_de_tentativas:
    print('Total de tentativas {} de {}'.format(rodada, total_de_tentativas))
    chute = input('Digite o nome de uma fruta: ')
    print('Você digitou {}'.format(chute))

    acertou = chute == random.choice(lista_frutas)
    errou = chute != random.choice(lista_frutas)

    if acertou:
        print('Parabéns, você acertou!')
        break
    elif errou:
        print('Você errou!')

    rodada = rodada + 1

print('Total de tentativas encerradas...')
print('Fim de jogo!')