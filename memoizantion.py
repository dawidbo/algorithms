# fibonnaci  with memoizantion
# global variables brakes scope side effect, global acces outside of scope
def fib(n):
    global numFibCalls 
    numFibCalls += 1
    if n==1:
        return 1
    elif n==2:
        return 2
    else:
        return fib(n-1)+fib(n-2)
x=5
numFibCalls=0  
print (fib(x)) #8
print("normal:", numFibCalls) #9


def  fib_efficient(n,d):
    global numFibCalls 
    numFibCalls+=1
    if n in d:
        return d[n]
    else:
        ans=fib_efficient(n - 1, d) + fib_efficient(n - 2, d)
        d[n]=ans
        return ans

d = {1:1, 2:2}
numFibCalls=0  
x=5
print(fib_efficient(x, d)) #8
print("eff:",numFibCalls) #7