def counting(A, m):
    n = len(A)
    count = [0] * (m + 1) # [0]*3 = [0,0,0] zeros array
    for k in range(n):
        count[A[k]] += 1
    return count

A = [1,2,3,4,1,2,3,4]

print(counting(A,8))

# PermCheck
# permutation is when array all elements once  
# not permutatuion if miss number in sequence or duplicate

# A[0] = 4
# A[1] = 1
# A[2] = 3
# A[3] = 2

def solution1(A):    
    ans = 0
    n = len(A)
    if n <= 1:
        return 1
    count = [0] * (max(A) + 1)
    for i in range(n):
        count[A[i]] += 1
    for i in range(1, n+1):
        if count[i] != 1:
            return 0
    return 1


A = [1] 
print(solution1(A))

def slow_solution(A, B, m):
    n = len(A)
    sum_a = sum(A)
    sum_b = sum(B)
    print("sum a:",sum_a)
    print("sum b:",sum_b)
    for i in range(n):
        for j in range(n):
            change = B[j] - A[i]
            sum_a += change
            sum_b -= change
            if sum_a == sum_b:
                return True
            sum_a -= change
            sum_b += change
    return False

A = [1,2,3,4]
B = [2,2,3,4]
m = 4
print(slow_solution(A,B,m))


def solution(A):    
    Na = len(A)
    sumA = Na * (Na+1) / 2
    sumB = 0
    B = [0] * (Na + 1)
    Nb = len(B)
    for i in range(Na):
        if A[i] > 0 and A[i] <= Na and B[A[i]] == 0:
            B[A[i]] = 1
            sumB += A[i]
    return 1 if sumA == sumB else 0   
print(solution([1,2,3,4]))