
def probabilidade2():
    print('O seu filho tem 75% de chance de ter olhos castanhos e 25% de chance de ter olhos azuis')
    

def probabilidade1():
    print('O seu filho tem 50% de chance de ter olhos castanhos e 50% de chance de ter olhos azuis')

def castanho():
    print('O seu filho vai ter olhos castanhos')

def azul():
    print('O seu filho vai ter olhos azuis')
    
    
def paiazul():
    global corepai
    global genepai
    print('Dados sobre o pai')
    print('Qual a core dos olhos do pai?')
    corepai=str(input())
    corepai=corepai.upper()
    if corepai==('AZUL'):
        azul()
    elif corepai==('CASTANHO'):
        print('Um dos seus genes é castanho ou outro ou é castanho ou azul')
        print('O seu segundo gene é castanho ou azul?')
        genepai=str(input())
        genepai=genepai.upper()
        if genepai==('CASTANHO'):
            castanho()
        elif genepai==('AZUL'):
            probabilidade1()
        
        
def paicastanho():
    global corepai
    global genepai
    print('Dados sobre o pai')
    print('Qual a core dos olhos do pai?')
    corepai=str(input())
    corepai=corepai.upper()
    if corepai==('AZUL'):
        probabilidade1()
    elif corepai==('CASTANHO'):
        print('Um dos seus genes é castanho ou outro ou é castanho ou azul')
        print('O seu segundo gene é castanho ou azul?')
        genepai=str(input())
        genepai=genepai.upper()
        castanho()
        
def mae():
    global coremae
    global genemae
    print('Dados sobre a mãe')
    print('Qual a core dos olhos da mãe?')
    coremae=str(input())
    coremae=coremae.upper()       
    if coremae==('AZUL'):
        paiazul()
    elif coremae==('CASTANHO'):
        print('Um dos seus genes é castanho ou outro ou é castanho ou azul')
        print('O seu segundo gene é casatnho ou azul?')
        genemae=str(input())
        genemae=genemae.upper()
        if genemae==('CASTANHO'):
            castanho()
        elif genemae==('AZUL'):
            paiazul()
            


mae()




















      
