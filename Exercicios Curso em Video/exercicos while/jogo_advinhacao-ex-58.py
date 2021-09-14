#faça um programa que o computador vai pensar em um numero entre 0 e 10. 
#so que o jogador vai tentar advinhar ate acertar, mostrando no final quantos palpites foram nescessário para vencer

from random import randint
computador = randint(0,10)
print('Sou seu computador... acabei de pensar em um numero entre 0 e 10. ')
print('Será que você consegue adivinhar qual foi? ')

acretou = False
palpites = 0
while not acretou:
    jogador = int(input('Qual o seu palplite ?'))
    palpites += 1
    #o palpite fica nessa posição pq depois da pergunta ele vai contando 
    if jogador == computador:
        acretou = True
    else:
        if jogador < computador:
            print('Mais .. Tente mais uma vez ')
        elif jogador > computador:
            print('Menos... Tente mais uma vez ')
        
  # O moral do pragrama é se eu esciolher um numero que for maior ou menor que o computador escolheu, ele vai entrar 
  # no if e else nos dando a opção se preciso mais ou menos numeros ate chegar o certo
print (f'Você acertou com {palpites} tentativas. Parabens')


