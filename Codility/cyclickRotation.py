# from binaryGap.binaryGap import *
# shif array of one place by right - CyclicRotation
# A = [3, 8, 9, 7, 6] is [6, 3, 8, 9, 7]
def reverse(A):
    N = len(A)
    for i in range(N//2):
        k = N - i - 1
        A[i], A[k] = A[k], A[i]
    return A

# a = [1,2,3,4,5]
# print(reverse(a))
def solution(A, K):
    N = len(A)
    j = 0
    while j<K:
        for i in range(N):
            A[i],A[N-1]=A[N-1],A[i]
        j+=1
    return A

print(solution([3, 8, 9, 7, 6], 3))
print(solution([0, 0, 0], 1))
print(solution([1, 2, 3, 4], 4))