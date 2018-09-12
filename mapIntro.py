# functions
def applyToEach(L, f):
    lenL = len(L)
    for i in range(lenL):
        L[i] = f(L[i])

L = [1, -2, 3.4]
applyToEach(L, abs)
print(L)

applyToEach(L, int)
print(L)

def increment(num):
    return num+1

def applyFuns(L, x):
    for f in L:
        print(f(x))

L = [abs, int, str, increment]
applyFuns(L, 4.5)


# python provides a general purpose HOP, map
# map( abs, [1,-2,3,-4] ) apply function to all value

def applyMap(f, L):
    for elt in map(f, L):
        print(elt)
applyMap(abs, [1,-2,3,-4])


L1 = [1,28,36,50]
L2 = [2,57,9,51]
for elt in map(max, L1, L2):
    print(elt)
# 2, 57, 36, 51 

#convert the map into a list, for readability:
x = map(max, L1, L2)
print(list(x))