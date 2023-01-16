#Pograma para enviar
import random

def menu():
    print('*',' '*16,'Jogo da Forca',' '*16,'*')
    print('*'*51)
    print('*',' '*20,'Menu',' '*21,'*')
    print('*'*51)
    print('* 1 - Jogar',' '*37,'*')
    print('* 2 - Sair',' '*38,'*')
    print('*'*51)
    n1=int(input('* Resposta:'))
    return n1


while True:
    m=menu()
    print(m)
    k=0
    t=1
    while True:
        if m==1:
            s=('girafa','camelo','tigre','gato',)
            print('Vamos jogar')
            print('Tens 10 tentativas para acertar a palavra')
            print('A palavra é um animal')
            f=(random.randrange(0,4))
            f=s[f]
            n='_'*len(f)
            print('A palavra tem',len(f),' letras')
            print(n)
            
            while k<len(f)*2 and f!=n:
                h=str(input('Insira a sua resposta: '))
                k+=1
                if h in f:
                    for i in range(0,len(f)):
                        if h==f[i]:
                            n=n[:i]+h+n[i+1:]
                            print(n)
                else:
                    print('Letra Errada')
            if f==n:
                print('Parabéns acertast-te com',k,'tentativas')
                print('-'*50)
                break
                break
                
    
                    
                    
            
        elif m==2:
            break
        else:
            print('ERRO')
            m=menu()
            print(m)
