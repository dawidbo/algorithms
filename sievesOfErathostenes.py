# sito Eratostenesa
def sito(n):
    """ Sieves of Erathostenes - find prime number [0,n] 
    Assume: n is int 
    Return: list of prime numbers """
    from math import sqrt
    primeList = []
    allNum = {}
    # boundry of calculate
    sqrtN = int(sqrt(n)) + 1
    # initialization of range numbers
    for i in range(n):
        allNum[i] = True
    # sito Erastotenesa
    for i in range(2, sqrtN):
        if allNum[i]:
            j = 2*i
            while j <= n:
                allNum[j] = False
                j += i
    # get True from dictionary 
    for elt in allNum.keys():
        if allNum[elt]:
            primeList.append(elt)      
    return primeList
# execute
lista = sito(100)
for elt in lista:
    print(elt)