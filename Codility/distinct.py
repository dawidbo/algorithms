# Compute number of distinct values in an array.
def solution(A):
    sum = 0
    lenA = len(A)    
    listA = [0]*lenA
    for i in range(lenA):
        if listA[A[i]] == 0:
            listA[A[i]] = 1
            sum += 1
    return sum
    
# https://app.codility.com/demo/results/trainingTTT9WA-CZM/
# https://app.codility.com/demo/results/trainingGS53QC-94K/
def distinct(A):
    n = len(A)
    if n == 0:
        return 0
    A.sort()
    result = 1
    for k in range(1, n):
        if A[k] != A[k - 1]:
            result += 1
    return result