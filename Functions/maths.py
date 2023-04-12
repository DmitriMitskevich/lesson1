def summ(a,b):
    return a+b
def vych(a,b):
    return a-b
def proiz(a,b):
    return a*b
def raz(a,b):
    return a/b
def Ran_num():
    import random
    b = int(input("Nachalo diapozona: "))
    e = int(input("Konets diapozona: "))
    a = []
    for i in range(b, e):
        a.append(random.randint(b, e))
    return a
def S_circ(r):
    S_c = 3.14159265 * (r * r)
    return round(S_c)

def S_trian(a,b):
    return (a * b) / 2























def S_rect(a,b):
    return a*b

def min_max_chisla():
    n = int(input("Vvedite chislo: "))
    n = str(n)
    summ = 0
    for i in n[n.index(min(n)) + 1:n.index(max(n))] or n[n.index(max(n)) + 1:n.index(min(n))]:
        summ += int(i)
        print(i, end=" ")
    print()
    print(summ)
