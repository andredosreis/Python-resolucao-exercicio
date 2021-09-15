#crie um programa que leia vários numeros inteiros pelo teclado.
#O progrma só vai para quando o usuario digitar o valor 999, que é a 
# condição de parada. No final, mostre quantos numeros foram digitados e qual foi a soma entre esle (desconsiderando o flag)
num = cont = soma = 0
num = int(input('Digite um nume [para parar digite 999]'))

while num != 999:
    soma += num
    cont += 1
    num = int(input('Digite um nume [para parar digite 999]'))

print(f'Voce digitou {cont} e sua soma é {soma}')
