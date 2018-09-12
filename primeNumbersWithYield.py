def genPrimes():
    li=[]
    li.append(2)
    next = li[0]
    yield next
    num = li[0] + 1
    while True:
        isInList = False
        for elt in li:
            if num % elt == 0:
                isInList = True
        if not isInList:
            li.append(num)
            next = li[-1]
            yield next
        num += 2 

#a = genPrimes()
#a.__next__()

'''
def genFib1():
    fib1 = 1 # n - 1
    fib2 = 0 # n - 2
    while True:
        # fib(n) = fib(1) + fib(2)
        next = fib1 + fib2
        yield next
        fib2 = fib1
        fib1 = next
''' 