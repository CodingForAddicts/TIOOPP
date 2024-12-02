# 12/11/24
from TD1 import absol


# PARTIE 1 ITERATION
# Exercice 1.1
# Somme des factorielles de 1 à n
def zorglug(n):
    j=1
    k=0
    i=1
    while i<=n:
        j = i*j
        k = j+k
        i = i+1
    return k

# Exercice 1.2
# Multiplication

#1 Multiplication dans N
def multiplication1(a,b):
    m=0
    for i in range(0,a):
        m += b
    return m

# Multiplication dans Z
def multiplication2(a,b):
    i = 0
    z = 0
    if b >= 0:
        while i<b: # Boucle 1 pour gérer les positifs
            z = z+a
            i = i+1
        return z
    while i<-b: # Boucle 2 pour gérer les négatifs
        z = z-a
        i=i+1
    return z

# Exercice 1.3
# Puissance

def puissance(x,n):
    if n<0:
        raise Exception("Not a Natural")
    else:
        if x == 0:
            if n == 0:
                return 1
            else:
                return 0
        elif x == 1:
            return 1
        elif x == -1:
            return 1+(n%2)*(-2)
        else:
            p=1
            while n>0:
                p = p*x
                n = n-1
            return p

def fibonacci(n):
    i = 0
    a = 1
    b = 0
    c = 0
    while i<n:
        c = a+b
        a = b
        b = c
        i+=1
    return c

# Exercice 1.5
# Suite

def u(n):
    n = n*2
    return n

def suite(n):
    m = 0
    while 0<n:
        m += u(n)
        n-=1
    return m

def suite2(n):
    i = 0
    x = 0
    while i<n:
        j = 0
        y = 0
        while j<i:
            y += u(j)
            j+=1
        x+=y
    return x

# Suite2(n) avec une seule boucle while
def suite3(n):
    sums, s, i = 0,0,1
    while i<=n:
        s+=u(i)
        sums+=s
        i+=1
    return sums


# PARTIE 2 REPETITIONS

# Exercice 2.1
# Euclide

def euclidean_pgcd(a,b):
    if a<=0 or b<=0 :
       raise Exception("Not a Euclidean")
    else:
        while b!=0:
            a,b=b,a%b
        return a

# Exercice 2.2
# Miroir

def mirror(n):
    if n<0: raise Exception("Not a Natural")
    else:
        processed = 0
        while n>0:
            processed = processed*10 + n%10
            n = n//10
    return processed

# Exercice 2.3
# Quotient
def quotient(a,b):
    if b>a:
        a,b = b,a
    if a < 0 or b < 0 :
        raise Exception("Not a Natural")
    else:
        resultat = 0
        while a>=b:
            a-=b
            resultat+=1
    return resultat,a

# Exercice 2.4
# Factorielle calculable

def factorial(limite):
    if limite <= 0:
        raise Exception("Not a Natural")
    un,n = 1,1
    while n < limite:
        n*=n+1
        un+=1
    un-=1
    if un%2!=0 :
        un-=1
    return un



# Exercice 2.5
# Détermine si un nombre est VRAIMENT premier

def premier(a):
    if a < 2:
        raise Exception("Not a Natural")
    if a%2 == 0:
        return a ==2
    n = 3
    while n*n <a and a% n!=0:
        n += 2
    return n*n > a



# EXO BONUS
# Multiplication egyptienne

def egypt(a,b):
    if b < 0:
        b = -b
        a = -a
    p = 0
    while b !=0:
        if b%2 == 1:
            p = p+a
            (a,b) = (a*2, b//2)
    return p
































