#Desenvolva uma logica que leia o peso e a alutar ade uam pessoa,
#calcula o IMC e moeste seu Status de acorco com a tabale abaixo_
# -Abaixo de 18.5: abaixo do Peso - 25 ate 30: Sobrepeso
# -Entre 18.5 a 25: Peso ideal  - 30 ate 40: Obesidade
# -Acima de 40: Obesidade mórbida:

peso = float(input('Qual o Seu Peso (KG)? '))

altura = float(input('Qual a sua altura (m)?'))

imc = peso / (altura **2)

print(f'O IMC dessa pessoa é de {imc:.1f}')

if imc < 18.5:
    print(f'Você esta ABAIXO DO PESO  ')
elif 18.5 <= imc <= 25:
    print(' Você esta no PESO IDEAL')
elif imc > 25 and imc <= 30:
    print('Você esta SOBREPESO')
elif imc > 30 and imc <= 40:
    print('Você esta OBESO')
else:
    print('Vece esta com OBESIDADE MÓRBIDA')