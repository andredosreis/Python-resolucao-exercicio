#Faça um programa que leia o SEXO de uma pessoa, mas só aceite os valores M ou F.
#caso esteje errado, peça a digitação novamente ater um valor correto

sexo = str(input('Digite o Sexo [M/F] ')).strip().upper()[0]


while sexo not in 'MmFf':
    sexo = str(input('Por favor digite a letra correta. ')).strip().upper()[0]

print(f'Você digitou {sexo}')
