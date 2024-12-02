# Pyhton : révisions de base

# EXERCICE N°1
def test(n:int):
    return (n>=100)&(n<1000)

def sum_digits(n:int):
    a = n/100
    b = (n/10)%10
    c = n % 10
    return a+b+c

def product_digits(n:int):
    a = n / 100
    b = (n / 10) % 10
    c = n % 10
    return a * b * c

def absol(n:int):
    if n<0:
        return -n
    return n

def loop(n:int):
    n = absol(n)
    if sum_digits(n) == product_digits(n):
        return n
    return loop(n+1)

# EXERCICE N°2

def max3(x:int, y:int, z:int):
    if x>=y and x>=z:
        m = x
    elif y>z:
        m = y
    else: m = z
    return m




