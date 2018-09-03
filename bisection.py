# bisection
# szukanie pierwiastka
# ----a---------c-----------b------->
# epsilon - dokladnosc, precyzja
# (a+b)/2 = c, c**2 > b to b = c, c**2 < b to a = c, c**2 == n a=b=c
# 1. sprawdz czy jest co podzielic
# 2. podziel na 1/2 
def bisectionSquare(num,epislon=0.1):
    """ Use bisection method for find square
        Ver: 1
        Args:
            num float e.g. 2.0
            epsilon - float - precision
        Returns:
            string
    """ 
    a = 0.0
    b = num
    c = 0.0
    while abs(b-a)>epislon:
        c = ( a + b )/2 
        if c**2>num:
            b=c
        elif c**2<num:
            a=c
        else:
            a=b=c        
    print( "przedzial: < " +str(a)+ ", "+str(b)+ " > " )
    return c
#print(bisectionSquare(25))