# Tablica T[8][8] zawiera liczby naturalne. Proszę napisać funkcję, która sprawdza czy można
# wybrać z tablicy niepusty podzbiór o zadanej sumie. Warunkiem dodatkowym jest aby żadne dwa wybrane elementy nie leżały w tej samej kolumnie ani wierszu. 
# Do funkcji należy przekazać wyłącznie tablicę oraz wartość sumy, funkcja powinna zwrócić wartość typu bool.
#sprawdzic czy dziala

def solve(T, s):
    def recur(T, s, curr_sum=0, i=0, rows=[], cols=[]):
        
        if i == 8:
            if curr_sum == s:
                return True
            return False
        if curr_sum == s:
            return True
        
        for i in range(len(T)):
            for j in range(len(T)):
                #biorę element do podzbioru
                if i not in rows and j not in cols:
                    recur(T, s, curr_sum + T[i][j], i + 1, rows + [i], cols + [j])
                #nie biorę elementu do podzbioru
                recur(T, s, curr_sum, i + 1, rows, cols)
        
