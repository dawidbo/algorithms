# wyszukiwanie binarne, liczba rzeczywista
# 0---1---2---3---4---5--->
def randomizeList(start,end,numElement):
    from random import randint
    ranList = []
    for elt in range(1, numElement):
        ranList.append(randint(start,end))
    return ranList

randList = randomizeList(1,6,50)
randList.sort()
a = 0
b = len(randList)-1
c = 0
isBingo = False
number = 35
while a<=b:
    c=(a+b)//2
    if randList[c]==number:
        isBingo = True
        break
    if randList[c]<number:
        a=c+1
    else:
        b=c-1
if isBingo:
    print("Bingo!","Number: ",number," is in index:",c)    
else:
    print("Nope!")