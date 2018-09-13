# MissingInteger
# ?e, bior?c pod uwag? tablic? A z liczb ca?kowitych N, zwraca najmniejsz? dodatni? liczb? ca?kowit? (wi?ksz? ni? 0), kt�ra nie wyst?puje w A.
# Na przyk?ad, bior?c pod uwag? A = [1, 3, 6, 4, 1, 2], funkcja powinna powr�ci? 5.
# Bior?c pod uwag? A = [1, 2, 3], funkcja powinna wr�ci? 4.
# Bior?c pod uwag? A = [-1, -3], funkcja powinna zwr�ci? 1.

def solution(A):
    aLen = len(A)
    B = [0] * (aLen + 2)
    bLen = len(B)
    for i in range(aLen):
        if A[i] > 0 and A[i] < bLen and B[A[i]] == 0:
            B[A[i]] = A[i]
    for i in range(1, bLen):
        if B[i] == 0:
            return i
    return 1
     

#A = [1, 2, 3]
#A = [-1, -3]
A = [1,1,2,3,4,5,99]
print(solution(A))