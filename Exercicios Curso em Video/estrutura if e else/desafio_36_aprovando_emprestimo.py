# escreva um programa para aprovar o emprestimo bacario para a comra de uma casa. Pergute 
# o VALOR DA CASA, o SALARIO, do comprador e em QUANTOS ANOS ele vai pagar
#a prestação mensal, não pode excerder 30% do salario ou então o emprestimo é negado

v_casa = float(input('Qual o valor da Casa?'))
v_salario = float(input('Qual o seu salario?'))
q_anos = int(input('Em quantos anos voce pretende pagar?'))

porcetagem_salario = v_salario * 30 / 100
valor_parcelas = v_casa / (q_anos * 12)



if valor_parcelas <= porcetagem_salario:
    print('valor Aprovado')
    print(f'o valor da parcela é: R$ {valor_parcelas:.2f}' )
    print (porcetagem_salario)

elif valor_parcelas > porcetagem_salario:
    print('valor reprovado')
    print(f'valor da parcela é: R$ {valor_parcelas:.2f}')
