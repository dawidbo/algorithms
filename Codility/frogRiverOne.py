# frogRiverOne
# X = 5 - distance
# frog 1 2 3 4 5 ( x + 1) = 6 end 
# list A[0] = 1 means 1 st leaves fall down in 1 element
# when all distance full return second 0 idex or -1 when frok never jump to 
def solution(X, A):
    B = [0] * (X + 2)     
    sumTarget = X * ( X + 1 ) // 2
    aLen = len(A)
    bLen = len(B)
    sumCurrent = 0
    for i in range(aLen):
        if A[i]>0 and A[i]<bLen and B[A[i]]==0:
            B[A[i]]=A[i]
            sumCurrent+=A[i]
            if sumTarget==sumCurrent:
                return i
    return -1

X = 5
A = [1,3,1,4,2,3,4,5]
print(solution(X,A))