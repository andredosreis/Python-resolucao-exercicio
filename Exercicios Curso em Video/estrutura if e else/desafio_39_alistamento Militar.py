#esreva um programa que leia o ano de nascimento de um jovem e informe de acordo com a sua idade, se ele AINDA VAI SE ALISTAR ao serviço militar
#se é a HORA DE SE ALISTAR ou se já  PASSOIU DO TEMPO do alustamento. Seu programa tambem devera mostrar o tempo que falta ou passou do prazo.

from datetime import date

atual = date.today().year
nasc = int(input('Ano de nascimento'))
idade = atual - nasc

print(f'Quem nasceu em {nasc} tem {idade} em {atual}.')


if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE')
elif idade < 18:
    saldo = 18 - idade
    print(f'Ainda faltam {saldo} anos para o alistamento. ')
    ano = atual - saldo
elif idade > 18:
    saldo = idade - 18
    print(f'Voce ja deveria ter se alisatado há {saldo} anos')
    ano = atual - saldo
    print(f'seu alismento foi em {ano}')
elif  nasc >= atual:
    print('Por favor entre com o ano correto.')

