# triangle
# https://app.codility.com/demo/results/trainingRE75EW-BGY/
def sol(A):
    lenA = len(A)
    A.sort()
    for i in range(2,lenA):
        if A[i-2]+A[i-1] > A[i]:
            return 1
    return 0
            
#A = [10,2,5,1,8,20]
A = [1,5,10,50]
print(sol(A))