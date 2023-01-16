n1=int(input("Insira o 1º comprimento do lado do triângulo "))
n2=int(input("Insira o 2º comprimento do lado do triângulo "))
n3=int(input("Insira o 3º comprimento do lado do triângulo "))
if n1==n2 and n1==n3 and n2==n3:
    print("O triângulo é equilátero")
elif n1==n2 or n2==n3 or n3==n2:
    print("O triângulo é isósceles")
else: print("O triângulo é escaleno")
