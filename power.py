def iterPower(base, exp):
    if (type(base)==int or type(base)==float) and (type(exp)==int and exp >= 0):
        prod = 1
        for i in range(1,exp + 1):
            prod*=base   
        return prod    

def recurPower(base, exp):
    if exp == 1:
        return base
    else:
        return base*recurPower(base, exp - 1)

print(iterPower(2,3))
print(recurPower(2,3))