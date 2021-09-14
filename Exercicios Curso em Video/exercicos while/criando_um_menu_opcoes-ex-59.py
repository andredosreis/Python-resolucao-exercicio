#Crie um programa que leia DOIS VALORES e mostre um MENU como o ao lado na tela:
#Seu programa deverá realizar opção solicitada em caso:
# 1 para soma - 2 - multiplicar- 3- maior e menor 4 - novos numeros- 5 - sair do programa.

from time import sleep

primeiro_valor = int(input('Primeiro valor'))
segundo_valor = int(input('Segundo valor'))


opcao = 0
while opcao != 5:
    print ('''    [1] Somar
    [2] Mutiplicar
    [3] Maior 
    [4] Novos numeros
    [5] Sair do programa''')
    opcao = int(input('Qual a sua opção? '))
    print('')
 
    if opcao == 1:
       soma = primeiro_valor + segundo_valor
       print(f'Soma entre o {primeiro_valor} e {segundo_valor} é {soma}')
       print('')
    
    elif opcao == 2:
        mult = primeiro_valor * segundo_valor
        print(f' A multiplicação do numero {primeiro_valor} com o {segundo_valor} é {mult}')
        print('')
    elif opcao == 3:
        if primeiro_valor > segundo_valor:
            print(f'O primeiro {primeiro_valor} é maior que segundo valor {segundo_valor} ')
        elif primeiro_valor < segundo_valor:
            print(f'o segundo valor {segundo_valor} é maior que o primeiro valor {primeiro_valor} ')
    elif opcao == 4:
        primeiro_valor = int(input('Primeiro valor'))
        segundo_valor = int(input('Segundo valor'))
    elif opcao == 5:
        print('Finalizando ')
    else:
        print('Opção invalida. tente novamente ')
    print('=-=' * 10)
    sleep(2)


print('fim do progrma volte sempre')


        
    
