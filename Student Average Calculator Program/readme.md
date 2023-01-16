This program calculates the average grade of a student

print('Programa para calcular a média de um aluno')
print("-"*50)
The user inputs the student's name

nome = input('Insira o nome do aluno: ')
The user inputs the student's first grade

nota1 = float(input("Insira a primeira nota: "))
The user inputs the student's second grade

nota2 = float(input("insira a segunda nota: "))
The program calculates the average grade by adding the first and second grade and dividing by 2

media = (nota1 + nota2)/2
The program displays the student's name and average grade

print('{0} teve média igual a: {1:4.2f}'.format(nome, media))