def keres(feladvany, lista):
    eredmeny=[]
    for helyseg in lista:
        if len(feladvany) == len(helyseg) and helyseg[0] == feladvany[0] and helyseg[-1] == feladvany[-1]:
            eredmeny.append(helyseg)
    return eredmeny

def betutipp(feladvany:str, helyseg):
    index = feladvany.index('.')
    return helyseg[index]

def ellenor(eredeti, uj, betu):
    if len(eredeti) != len(uj):
        return False
    for i in range(len(eredeti)):
        if eredeti[i] != uj[i]:
            if eredeti[i] != '.':
                return False
            else:
                if uj[i] != betu:
                    return False  
    return True

def kizar(lista, betu):
    eredmeny=[]
    for helyseg in lista:         
        if not betu in helyseg[1:-1]:
            eredmeny.append(helyseg)
    return eredmeny