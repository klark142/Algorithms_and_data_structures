def zlicz_samogloski(s):
  cnt = 0
  samogloski = ['a', 'e', 'i', 'o', 'u', 'y']
  for z in s:
    if z in samogloski:
      cnt += 1
  return cnt

def oblicz_wage_ASCII(s):
  _sum = 0
  for z in s:
    _sum += ord(z)
  
  return _sum


# s - wyraz, do ktorego chcemy znalezc wyraz o tej samej wadze
# T - zbior znakow z ktorego chcemy zbudowac wyraz
def zad16(s1, T):
  W = oblicz_wage_ASCII(s1)
  samogloski = zlicz_samogloski(s1)

  def rek(s2):
    print(s2)
    if zlicz_samogloski(s2) > samogloski or oblicz_wage_ASCII(s2) > W:
      return False
    
    if zlicz_samogloski(s2) == samogloski and oblicz_wage_ASCII(s2) == W:
      print("----DZIALANIE ZAKONCZONE----")
      print(s2)
      return True
    
    for z in T:
      if rek(s2 + z):
        return True
    
    return False
  
  return rek("")


zad16("ula", "exe")

