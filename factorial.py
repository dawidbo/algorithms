def factorial_recurs(n):
    if n == 1:
        return 1
    else:
        return n*factorial_recurs(n-1)

def factorial_iteraction(n):
    prod = 1
    for i in range(1, n + 1):
        prod *= i
    return prod
       
print(factorial_recurs(3))
print(factorial_iteraction(3))