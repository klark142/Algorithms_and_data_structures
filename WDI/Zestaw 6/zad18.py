# W szachownicy o wymiarach 8x8 każdemu z pól przypisano liczbę naturalną. Na ruchy króla
# nałożono dwa ograniczenia: król może przesunąć się na jedno z 8 sąsiednich pól jeżeli ostatnia cyfra liczby na
# polu na którym stoi jest mniejsza od pierwszej cyfry liczby pola docelowego, oraz w drodze do obranego celu
# (np. narożnika) król nie może wykonać ruchu, który powoduje oddalenie go od celu. Dana jest globalna tablica
# T[8][8] wypełniona liczbami naturalnymi reprezentująca szachownicę. Lewy górny narożnik ma współrzędne
# w=0 i k=0. Proszę napisać funkcję sprawdzającą czy król może dostać się z pola w,k do prawego dolnego
# narożnika.

def is_valid(a, target):
  #first digit target
  b = target
  while b > 10:
    b //= 10
  
  return a % 10 < b

def solve(T):
  n = 8 
  def recur(T, w=0, k=0):
    if w == n - 1 and k == n - 1:
      return True
    
    moves = ((0, 1), (1, 1), (1, 0))
    for move in moves:
      new_w = w + move[0]
      new_k = k + move[1]
      if new_w < n and new_k < n and is_valid(T[w][k], T[new_w][new_k]):
        recur(T, new_w, new_k)
    
    return False
        