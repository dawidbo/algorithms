def solution(A):
    B = {}
    for elt in A:
        if elt in B:
            B[elt] += 1
        else:
            B[elt] = 1

    for k,v in B.items():
        if v%2 == 1:
            return k
    return None        

print(solution([9, 3, 9, 3, 9, 7, 9 ]))# 7
print(solution([]))
print(solution([1,3,3,1,5]))