def LerDados():
   
    notaa=int(input('Nota do aluno: '))
    if notaa>20 or notaa<0:
        print('Erro - Nota errada')
        while True:
            
            notaa=int(input('Nota do aluno: '))
            if notaa<=20 or notaa>=0:
                break
    return(notaa)

def media(t,d):
    med=t/d
    return(med)

def perc(pop,d):
    yy=pop*100/d
    return(yy)
    
    
def calc():
    global mm
    global pp
    global pn
    global m
    global n
    z=0
    m=0
    n=21
    ne=0
    po=0
    for x in range(1,14,1):
        nota=LerDados()
        z=z+nota
        if nota>m:
            m=nota 
        elif nota<n:
            n=nota
        if nota<10:
            ne+=1
        elif nota>=10:
            po+=1
    mm=media(z,x)
    print(po,x)
    pp=perc(po,x)
    pn=perc(ne,x)
    
calc()
while True:
    print('''
***************** TURMA 10ºD ****************

*       ESTATÍSTICAS NOTAS MAEMÁTICAS       *

---------------------------------------------

* 1 - Média das notas                       *
* 2 - % de negativas e positivas            *
* 3 - Nota mais alta e nota mais baixa      *
* 4 - Sair                                  *

*********************************************
''')
    resp=int(input('Resposta: '))
    if resp==1:
        print('A média é',mm)
        print('-'*50)
    elif resp==2:
        print('A percentagem de negativas é',pn)
        print('A percentagem de positivas é',pp)
        print('-'*50)
    elif resp==3:
        print('A nota mais alta é',m)
        print('A nota mais baixa é',n)
        print('-'*50)
    elif resp!=1 or resp!=2 or resp!=3 or resp!=4:
        print('ERRO')
        print('-'*50)
    elif resp==4:
        break

    
    
