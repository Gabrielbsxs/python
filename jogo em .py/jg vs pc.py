
from random import  randint
from time import sleep
print('vou pensar em um número entre 0 e 5, tente adivinhar ...') #computador adivinha
jogador=int(input('Que número pensei ?')) #jogador tenta adivinhar
print('Processando ...')
sleep(4) #como se estivesse pensando e demora para responder
computador=randint(0,5)
if computador==jogador:
    print('Parabéns, você acertou')
else:
    print(f'Você errou,pensei no número {computador} e não no numero {jogador}')
