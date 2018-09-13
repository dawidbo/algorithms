# int('1100100',2)
# binarna liczba 1100100 = 100
def getDecToBin(n):
    """ decimal number convert to string
        return - string - binary number
    """
    binList = []
    while n != 0:
       binList.append(str(n%2))
       n //= 2
    binList.reverse()
    return ''.join(binList)

# binary to decimal  1*2^6 + 1*2^5 + 0*2^4 + 0*2^3 + 1*2^2 + 0*2^1 + 0*2^0 
def getDecFromBin(n):
    binList = []
    for elt in str(n):    
        binList.append(int(elt))
    i = len(binList) - 1
    result = 0
    binList.reverse()
    while i >= 0:
        result += binList[i] * pow(2,i)
        i -= 1
    return result

"""
al = getDecToBin(100)
print(al)
al1 = getDecFromBin(1100100)
print(al1)
"""
# find zeros gap 000001 10000 00010001000
def countZerosGap(n):
    """ Counting zeros betwen 2 one
        n - string - binary number
        return - int - num of zeros the bigger gap """
    onesList = []
    for i in range(len(n)):
        if int(n[i]) == 1:        
            onesList.append(i)
    max = 0
    if len(onesList) > 1:
        for i in range(len(onesList)):
            try:
                next = onesList[i+1] - onesList[i]
                if max < next:
                    max = next
            except IndexError:
                return max - 1
    return max


# testList = ['0000','11111','00001','10000','001100','00100100','1100100100000001']   
# for elt in testList:
# print(countZerosGap(elt))

def solution(N):
    return countZerosGap(getDecToBin(N))

N = 1041
print(solution(N))