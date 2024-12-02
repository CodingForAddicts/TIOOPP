# 1

def compte(x,l):
    cpt =  0
    longueur = len(l)
    for i in range(longueur):
        if x == l[i]:
            cpt += 1
    return cpt

# 2

def est_present(x,l):
    i = 0
    longueur = len(l)
    while i < longueur and x != l[i]:
        i+=1
    return i < longueur


def suppr(l,k):
    longueur = len(l)
    if k >= longueur or k< 0 :
        raise Exception()
    else :
        i = k+1
        while i < longueur:
            l[i-1] = l[i]
            i+= 1
        l.pop()
    print(l)

def abcd(n,val):
    l=[]
    for i in range(n):
        l.append(val)
    return l

