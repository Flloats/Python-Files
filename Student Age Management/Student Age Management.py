ages = []

for i in range(5):
    age = int(input('Enter the age of student {}: '.format(i+1)))
    ages.append(age)

print('-'*15+'Menu'+'-'*15)
print('1- Print the list')
print('2- Show youngest student age')
print('3- Show oldest student age')
print('4- Sum of elements in the list')
print('5- Sort the list')
print('6- Print age of a specific position')
print('7- Exit')
print('-'*34)

option = int(input('Option: '))

if option == 1:
    print(ages)
elif option == 2:
    print('Youngest student age:', min(ages))
elif option == 3:
    print('Oldest student age:', max(ages))
elif option == 4:
    print('Sum of ages:', sum(ages))
elif option == 5:
    ages.sort()
    print(ages)
elif option == 6:
    pos = int(input('Enter the position: '))
    print('Age at position {}: {}'.format(pos, ages[pos-1]))