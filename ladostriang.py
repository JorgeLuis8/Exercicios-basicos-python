l1 = int(input("Informe um lado"))
l2 = int(input("Informe um lado"))
l3 = int(input("Informe um lado"))

if l1 < l2+l3 and l3 < l2+l1 and l2 < l1+l3:
    if l1 == l2 and l2 == l3:
        print("Esse triangulo é equilatero")

    elif l1 != l2 and l2 != l3:
        print("Esse triangulo é escaleno")
    else:
        print("Esse triangulo é isoceles")
else:
    print("Não é triangulo")
