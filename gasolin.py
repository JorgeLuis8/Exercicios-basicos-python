'''
- Um posto está vendendo combustíveis com a seguinte tabela de descontos:
Álcool:
- até 20 litros, desconto de 3% por litro
- acima de 20 litros, desconto de 5% por litro
Gasolina:
- até 20 litros, desconto de 4% por litro
- acima de 20 litros, desconto de 6% por litro
Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível (A para álcool e G para gasolina),
calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 4,53 o preço do litro
do álcool é R$ 3,45.
'''

qtd_litro=int(input("Informe a quantidade de litros que deseja: "))
tipo_combustivel=input("Informe o tipo de combustivel que deseja: G/A ").upper().strip()

if tipo_combustivel	 == 'A':
    if qtd_litro<=20:
        desconto=(3.45*0.03)*qtd_litro
        print(f'O preço a ser pago deve ser : R${(qtd_litro*3.45)-desconto:.2f}')
    else:
        desconto=(3.45*0.05)*qtd_litro
        print(f'O preço a ser pago deve ser : R${(qtd_litro*3.45)-desconto:.2f}')
elif tipo_combustivel == 'G':
    if qtd_litro<=20:
       desconto=(4.53*0.04)*qtd_litro
       print(f'O preço a ser pago deve ser : R${(qtd_litro*4.53)-desconto:.2f}') 
    else:
        desconto=(4.53*0.06)*qtd_litro
        print(f'O preço a ser pago deve ser : R${(qtd_litro*4.53)-desconto:.2f}') 