# ALIASES
# case immutable valriable
a=5
b=a
print(id(a)==id(b)) # True
b=7
print(id(a)==id(b)) # False

# case mutable variable
L1 = [1,2,3]
L2 = L1 # same object in memory
L2.append(4)
print(id(L1)==id(L2)) # True

L3 = list(L1)
print(id(L1)==id(L3)) # False

L4 = L1[:] #slice technique
print(id(L1)==id(L4)) # False

# case tuples immutables
t = (1,2,3)
tt = tuple(t)
print(id(t)==id(tt)) # True

ttt = t[:]
print(id(t)==id(ttt)) # True


# mutation ISSUE - on the same list - after remove index change from 1 to 0 
def remove_dups(L1,L2):
    for e in L1:
        if e in L2:
            L1.remove(e)

L1 = [1,2,3,4]
L2 = [1,2,5,6]
remove_dups(L1,L2)
print(L1) # [2, 3, 4]


def remove_dups1(L1,L2):
    copyL1 = L1[:]
    for e in copyL1:
        if e in L2:
            L1.remove(e)

L1 = [1,2,3,4]
L2 = [1,2,5,6]
remove_dups1(L1,L2)
print(L1) # [3, 4]