#Desemvolva um programa que leia NOME, IDADE, a SEO DA PESSOA. No Final do programa.
# faça um progama que leia o nome de 4 pessoas, idade e o sexo de cada pessoa. No final do programa mostre
# A media da idade do grupo
# qual é o nome do homem mais velho.
# quantidade mulhers tem menos de 20 anos 

somaidade = 0
mediaidade = 0
maioridadadehomem = 0
nomevelho = ''
totmulher20 = 0


for p in range (1,5):
    print(f'----- {p}ª PESSOA ---------')
    nome = input('Nome ').strip()
    idade = int(input(' Idade '))
    sexo = str(input(' Sexo ')).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mn':
        maioridadadehomem = idade
        nomevelho = nome
    if sexo in 'Mn' and idade > maioridadadehomem:
        maioridadadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:  # ('Mn') caso o usuario usar qualquer um maiusculo ou minusculo 
        totmulher20 += 1
mediaidade = somaidade /4
print(f'A media de idade do grupo é de  {mediaidade} anos')
print(f'O home mais velho tem {maioridadadehomem} anos e se chama {nomevelho} ')
print(f' Ao todos são {totmulher20} com menos de 20 anos ')

