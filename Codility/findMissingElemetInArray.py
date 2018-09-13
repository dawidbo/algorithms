def solution(A):
    N = len(A)+1
    ans = N*(N + 1)//2
    for elt in A:
        ans -= elt
    return ans

A = [1,2,3,4,5,7]
print(solution(A))