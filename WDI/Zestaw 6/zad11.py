#Dana jest tablica T[N]. 
# Proszę napisać program zliczający liczbę “enek” o określonym iloczynie.
licznik = 0

def recursion(tab, product, n, p=0):
    global licznik 
    if n == 1:
        for i in range(p, len(tab)):
            if tab[i] == product:
                licznik += 1
    else:
        for i in range(p, len(tab)):
            if product % tab[i] == 0:
                recursion(tab, product / tab[i], n - 1, i + 1)
                