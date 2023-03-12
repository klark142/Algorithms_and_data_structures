from math import sqrt 

def calculate_pi (prec = 10):
    a = sqrt(0.5) 
    mult = sqrt(0.5)

    for i in range(prec):
        a = sqrt(0.5 + 0.5 * a)
        mult *= a
    
    print(2 / mult)



calculate_pi()
