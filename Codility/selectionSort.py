# selection sort
# szukanie najmniejszego elementu i zmienianie z perwszym, drugim itd 
# O(n^2)
def selectionSortList(lista):
    sortedList = []
    lenL = len(lista)
    for i in range(lenL):
        min = i # zamiana indexow
        for j in range(i+1, lenL):
            if lista[i] > lista[j]:
                min = j # zamiana indexow
        lista[i], lista[min] = lista[min], lista[i]
            
    return lista



usortedList = [9,7,2,1]
print(usortedList)
print(selectionSortList(usortedList))