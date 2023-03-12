def funkcja(a, b):
    result = ''
    tablica_reszt = [] * b
    reszta = a % b
    while reszta != 0 and tablica_reszt[reszta] == None:
        tablica_reszt[reszta] - len(result)
        reszta = reszta * 10
        iloraz = reszta / b
        result += str(iloraz)
        reszta = reszta % b
    if reszta == 0:
        return a / b
    else:
        return str((a / b)) + '.' + str(result[:tablica_reszt[reszta]]) + '(' + str(result[tablica_reszt[reszta]:]) + ')'
