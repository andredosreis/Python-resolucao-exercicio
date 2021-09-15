#Crie um programa que leia o ANO DE NASCIMENTO de SETE PESSOAS.
#No final, mostre quantas pessoas ainda nao atigiram a maio idade 
# e quantas já são maiores 

from datetime import date
totalmaior = 0
totalmenor = 0
atual = date.today().year


for c in range (1, 8):
    nome = int(input(f'Em que ano a {c}ª pessoa nasceu? '))
    idade = atual - nome

    if idade < 18:
            
            totalmenor += 1 
        
    elif idade >= 18:
        
        totalmaior += 1
        
print(f'Ao todo tivemos {totalmaior} pessoas maiores de idade')
print(f'E também {totalmenor} pessoas menores de idade ')





        
        


    