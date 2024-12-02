# PARCOURIR UNE CHAINE

def print_string1(s):
    for c in s:
        print(c)


def print_string2(s):
    i = 0
    l = len(s)
    while i < l:
        print(s[i])
        i += 1


# EXERCICE 1.1
# Recherches

def occurences(s, x):
    occ = 0
    for c in s:
        if c == x:
            occ += 1
    return occ


def is_present(s, x):
    i = 0
    n = len(s)
    while i < n and s[i] != x:
        i += 1
    if i < n:
        return i
    else:
        return -1


# EXERCICE 1.2
# PALINDROME

def palindrome(s):
    end = len(s) - 1
    start = 0
    while start < end and s[start] == s[end]:
        start += 1
        end -= 1
        if s[start + 1] == ' ':
            start += 1
        if s[end - 1] == ' ':
            end -= 1
    return start >= end


def dec_to_bin(n, p):
    s = ""
    while n != 0:
        s = str(n % 2) + s
        n = n // 2
    while len(s) < p:
        s = '0' + s
    return s


def integer_to_comp_2(n, p):
    if n < 0:
        n = 2 ** p + n
    return dec_to_bin(n, p)


def bin_to_dec(s):
    n = 0
    for b in s:
        n = n * 2 + int(b)
    return n


def twocomp_to_integer(b, p):
    n = bin_to_dec(b)
    if b[0] == '1':
        n = n - 2 ** p
    return n


def freq(s):
    m, c = 0, " "
    for i in range(len(s)):
        cpt = 0
        for j in range(i, len(s)):
            cpt += s[i] == s[j]
        if cpt > m:
            m, c = (cpt, s[i])
    return m, c


# 3.2 Sous-chaîne alphabétique

def alpha(s):
    i = 0
    temp,temp2 = "",""
    for  j in s:
        if i <= ord(j):
            i = ord(j)
            temp += j
        else :
            if len(temp2) < len(temp):
                temp2 = temp
                temp = ""
    return temp2

# 3.3  Sous-Palindrome

def palindromic_sub(string):
    l, max = len(string), 0
    for i in range (0,l):
        j = 0
        while i-j >= 0 and i+j < l and string[i-j] == string[i+j]:
            j += 1
        z = j*2 -1
        if z > max:
            max = z
    return max
