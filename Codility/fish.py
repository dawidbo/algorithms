# https://app.codility.com/demo/results/trainingMDA4QM-5PZ/
def solution(A, B):
    up = 0
    s1 = []
    for i in range(0, len(A)):
        if B[i] == 0:
            if not s1:
                up += 1
            else:
                while s1 and A[i] > s1[-1]:
                    s1.pop()
                if not s1:
                    up += 1
        else:
            s1.append(A[i])
    return up + len(s1)
'''
A = [4,7]
B = [1,0]
A = [4,7]
B = [0,0]
A = [4,7]
B = [1,1]
A = [4,3,2,1,5]
B = [0,0,0,0,0]
A = [4,3,2,1,5]
B = [1,1,1,1,1]
'''
A = [4,3,2,1,5]
B = [0,1,0,0,0]

print(solution(A,B))
