intro='''
-------------------------------------
---------------> IMC <---------------
-------------------------------------
--------- 1 - CALCULAR IMC ----------
--------- 2 - VER TABELA ------------
--------- 3 - SAIR ------------------
-------------------------------------
'''
print(intro)
while True:
    print('-------------------------------------')
    n1=int(input('Opção - '))
    print('-------------------------------------')
    if n1==1:
        nome=str(input('Qual o nome do atleta'))
        idade=int(input('Qual a idade do atleta'))
        h1=int(input('Qual é o peso do atleta? '))
        h2=float(input('Qual é a altuta do atleta(cm)? '))
        if h1<=0 or h2<=0 or idade<=0:
            print('-------------------------------------')
            print('ERRO')
        else:
            print('-------------------------------------')
            a=(h1/(h2**2))
            if a<18.5:
                print("O IMC do atelta é",a,',está abaixo do peso normal ')
            elif a>=18.5 and a<=24.9:
                print("O IMC do atleta é",a,',está com o peso normal ')
            elif a>=25.0 and a<=29.9:
                print("O IMC do atleta é",a,',está com excesso de peso ')
            elif a>=30.0 and a<=34.9:
                print("O IMC do atleta é",a,',está com obesidade classe I ')
            elif a>=35.0 and a<=39.9:
                print("O IMC do atleta é",a,',está com obesidade classe II ')
            elif a>=40.0:
                print("O IMC do atleta é",a,',está com obesidade classe III ')
    elif n1==2:
        tabela='''
______________________________________________________
        IMC                     CLASIFICAÇÕES
   Menor do que 18.5        Abixo do peso normal
     18.5 - 24.9                Peso Normal
     25.0 - 29.9              Excesso de peso
     30.0 - 34.9            Obesidade classe I
     35.0 - 39.9            Obesidade classe II
 Maior ou igual a 40.0      Obesidade classe III
______________________________________________________
'''
        print(tabela)
    elif n1==3:
        break
    else:
        print('ERRO')
        
    
