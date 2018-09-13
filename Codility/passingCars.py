 '''
    For example, consider array A such that:
      A[0] = 0
      A[1] = 1
      A[2] = 0
      A[3] = 1
      A[4] = 1 
  
    We have five pairs of passing cars: (0, 1), (0, 3), (0, 4), (2, 3), (2, 4)
    https://app.codility.com/demo/results/trainingCKK74F-TDX/
'''
def solution(A):
    eps = 1000000000
    aLen = len(A)
    passO = 0
    ans = 0
    for i in range(aLen):
        if A[i] == 0:
            passO += 1
        else:
            ans += passO
            if ans > eps:
                ans = -1
                break
    return ans 
    
A = [0, 1, 0, 1, 1, 0 , 1]
print(solution(A))