while True:
    n1=int(input("insira um número do mes "))
    if n1>12:
        print("ERRO")
    elif n1==1:
        print("Janeiro")
    elif n1==2:
        print ("Fevereiro")
    elif n1==3:
        print ("Março")
    elif n1==4:
        print ("Março")
    elif n1==5:
        print ("Maio")
    elif n1==6:
        print ("Junho")
    elif n1==7:
        print ("Julho")
    elif n1==8:
        print ("Agosto")
    elif n1==9:
        print ("Setembro")
    elif n1==10:
        print ("Outubro")
    elif n1==11:
        print ("Novenbro")
    elif n1==12:
        print ("Dezembro")
    if n1<=0:
      print("ERRO")
    if n1>12:
        print("ERRO")
    if n1==1 or n1==3 or n1==5 or n1==7 or n1==8 or n1==10 or n1==12:
        print("31 dias")
    elif n1==4 or n1==6 or n1==9 or n1==11:
        print("30 dias")
    else:
        print("28 dias")
    n2=str(input("queres parar? "))
    if n2==("sim"): 
        break
    
    
    
    
    
 
 
