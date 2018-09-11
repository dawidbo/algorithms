#greatest common divisor
def gcdIter(a,b):
    bigger=a
    if a<b:
        bigger=b
    while bigger >= 1:
        if a % bigger == 0 and b % bigger == 0:
            break    
        bigger -= 1
    return bigger
print(gcdIter(8, 16))  
    
def gcdRecurEuklides(a,b):
    """ Euklides
        Tip: is equal no then bigger minus smaller, is equal end
    """
    if a > b:
        a = a - b
    elif a < b:
        b = b - a
    else:
        return a
    return gcdRecurEuklides(a, b)     

print(gcdRecurEuklides(8, 16))

def gcdRecurMit(a,b):
    if b == 0: #Base case is when b = 0
        return a
    return gcdRecurMit(b,a%b)
print(gcdRecurMit(8,16))