# O(n^2) slower
def slow_solution(n):
    result = 0
    for i in range(n):
        for j in range(i + 1):
            result += 1
    return result
print(slow_solution(10))

# O(n) regular
for i in range(1, n+1):
    ans += i 
print(ans)

# proper soultion O(1)
def solution(X, Y, D):
    from math import ceil
    ans = 0
    if X == Y:
        return ans
    return ceil((Y-X)/D)
print(solution(X,Y,D))

# An = 1..n
n = 10
ans = 0