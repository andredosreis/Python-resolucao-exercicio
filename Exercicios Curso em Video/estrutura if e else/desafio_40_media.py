#crie um porgrama que leia duas notas de um aluno e calcule sua media, 
#mostrando uma mensagem no final, de acordo com a media atingida:
# Média abaixo de 5.0: reprovado
# Média entre 5.0 e 6.9: Recuperação
# Média 7.0 ou superior: Aprovado

nota1 = float(input('Primeira nota '))
nota2 = float(input('Segunda Nota'))

media = (nota1 + nota2) / 2

if media < 5:
    print(f'Aluno REPROVADO sua media foi {media} ')
elif media > 5 and  media <= 7:
    print(f'Aluno RECUPERAÇÃO sua media foi {media} ')
else:
   
    print(f'Aluno APROVADO sua media foi {media}')
