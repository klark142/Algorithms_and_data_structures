COUNT_POSSIBILITIES = 0

def hetmany():
  def rek(i, K):
    if i == 8:
      print(K)
      global COUNT_POSSIBILITIES
      COUNT_POSSIBILITIES += 1
    else:
      for x in range(8): # sprawdzamy kazda mozliwa kolumne na ustawienie i-tego hetmana
        j = 0
        while j < i:
          if K[j] == x or abs(K[j] - x) == i - j:
            break
          j += 1
        else:
          K[i] = x
          rek(i+1, K)

  rek(0, [0] * 8)

hetmany()
print(COUNT_POSSIBILITIES)