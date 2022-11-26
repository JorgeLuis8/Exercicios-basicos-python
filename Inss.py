'''''
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o
total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5%
para o sindicato, faça um programa que nos dê:
salário bruto.
quanto pagou ao INSS.
quanto pagou ao sindicato.
o salário líquido.
calcule os descontos e o salário líquido, conforme a tabela ao lado:
'''

hora_valor = float(input('Informe quanto você ganha por hora'))
hora_trabalhada = int(input("Quantas horas você trabalha por mês?"))
sal_burto = hora_valor * hora_trabalhada
Ir = sal_burto*0.11
inss = sal_burto*0.08
sindicato = sal_burto*0.05
sal_liquido = sal_burto-inss-sindicato
print(f"O seu salario bruto é {sal_burto:.2f}")
print(f"Voce deve pagar {Ir:.2f} de imposto de renda")
print(f"Voce deve pagar {inss:.2f} ao inss")
print(f"Voce deve pagar {sindicato:.2f} ao sindicato")
print(f"Seu salario liquido é {sal_liquido:.2f}")
