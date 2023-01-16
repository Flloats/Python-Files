# Programa para calcular a média de um aluno
print('Programa para calcular a média de um aluno')
print("-"*50)
nome = input('Insira o nome do aluno: ')
nota1 = float(input("Insira a primeira nota: "))
nota2 = float(input("insira a segunda nota: "))
media = (nota1 + nota2)/2
print('{0} teve média igual a: {1:4.2f}'.format(nome, media))
