'''
Faça um programa que o usuário informe a forma de um objeto (triângulo, quadrado ou 
círculo). Segundo a forma escolhida, leia as informações necessárias para calcular a área. 
O programa deverá repetir até o usuário escolher sair'''

while True:
    def circulo():
        raio = float(input('Informe o raio do circulo: '))
        area = 3.14*(raio*raio)
        print(f"A area do circulo é {area:.2f}")

    def triangulo():
        base = float(input('Informe a base do triangulo: '))
        altura = float(input('Informe a altura do trinagulo: '))
        resultado = (base*altura)/2
        print(f'A a area do triangulo é {resultado:.2f}')

    def quadrado():
        lado = float(input('Informe o lado do quadrado: '))
        resultado = lado**2
        print(f'A area do quadrado é {resultado}')

    print('-------Informe a forma do objeto desejado-------')
    print('--Para circulo [C]--')
    print('--Para triangulo [T]--')
    print('--Para quadrado [Q]--')
    print('--Para sair [S]')
    objt = input('-> ').upper()

    if objt == 'C':
        circulo()
    elif objt == 'T':
        triangulo()
    elif objt == 'Q':
        quadrado()
    elif objt == 'S':
        break
    else:
        print('Informe uma opção valida')
print('Fim do programa!')
