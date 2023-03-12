from math import sqrt

def agm(a, b, prec):
    for i in range(prec):
        a, b = sqrt(a * b), (a + b) / 2.0
    print(a)
    
a, b = map(int, input('Two numbers for AGM: ').split())
prec = int(input('Precision: '))

agm(a, b, prec)