'''
Uma companhia de teatro deseja dar uma série de espetáculos. O custo total desse 
espetáculo é de R$ 200,00. A direção calcula que a R$ 5,00 o ingresso seriam vendidos 
120. Eles também calcularam que a cada R$ 0,50 diminuído no preço do ingresso espera-se que as vendas de ingresso aumentem em 26 unidades. Com isso, faça um algoritmo que 
escreva uma tabela de valores de lucros esperados em função do preço do ingresso, 
fazendo-o variar de R$ 5,00 até R$ 1,00 com intervalos de R$ 0,50. Escreva ainda o lucro 
máximo esperado, o preço do ingresso e a quantidade de ingressos vendidos para a 
obtenção desse lucro
'''

valorIngresso = 5
qtdVendas = 120
valorShow = 200
lucro = valorIngresso * qtdVendas - valorShow
lucroMaximo = lucro
Preço = valorIngresso
Quantidade = qtdVendas

while valorIngresso > 1:
    print(f'preço ingresso = {valorIngresso:.2f}, quantidade = {qtdVendas}, lucro = {lucro:.2f}')
    valorIngresso -= 0.5
    qtdVendas += 26
    lucro = valorIngresso * qtdVendas - valorShow

    if lucro > lucroMaximo:
        lucroMaximo = lucro
        Preço = valorIngresso
        Quantidade = qtdVendas
print('\n')
print(f'Lucro máximo = {lucroMaximo:.2f}')
print(f'Preço do ingresso = {Preço:.2f}')
print(f'Quantidade vendida = {Quantidade}')
