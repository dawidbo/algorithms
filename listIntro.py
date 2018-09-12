# List 
# order sequence
# square brackets []
# homogeneus(all int) - (not common is mixed type)
# mutable

# initialize
lista = []

def sumList(newList):
    sum = 0
    for i in newList:
        sum += i
    return sum
print(sumList([1,2,3,4,5]))

#Add
lista.append([1,2]) #[1, 2, 3, [1, 2]]
lista.extend([1,2]) #[1, 2, 3, [4, 5], 1, 2]
# del(list[index])  - delete specific index
# L.pop() - end of list delete last element
# L.remove(2) - delete by first value occure

#string to list
s = "abcdef"
print( list(s) ) #['a', 'b', 'c', 'd', 'e', 'f']
print( s.split() ) #['abcdef']
print( s.split("c") ) #['ab', 'def']

#list to string
print( ''.join( ['a', 'b', 'c', 'd', 'e', 'f'] ) )#abcdef
print( '_'.join( ['a', 'b', 'c', 'd', 'e', 'f'] ) )#a_b_c_d_e_f


#sorting by built in list
L = [1,2,3,423,24,22] 
sorted(s) # not mutable nie zminia listy
L.sort()# mutable asc [1, 2, 3, 22, 24, 423]
L.reverse()# mutable desc [423, 24, 22, 3, 2, 1]

# RANGE special procedure is something like tuples
# for var in range(5) is same as for var in (0,1,2,3,4)
a = range(5)
for i in a:
    print("i:", i)