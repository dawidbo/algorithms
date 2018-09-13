'''
that, given three integers A, B and K, returns the number of integers within the range [A..B] 
that are divisible by K, i.e.:
{ i : A ? i ? B, i mod K = 0 }
For example, for A = 6, B = 11 and K = 2, your function should return 3, 
because there are three numbers divisible by 2 within the range [6..11], namely 6, 8 and 10.
https://app.codility.com/demo/results/trainingC5G9VX-JES/       
''' 
def solution(A,B,K):
    if A%K==0:  
        return (B-A)//K+1
    else:           
        return (B-(A-A%K))//K

A=7
B=11
K=11
print(solution(A,B,K))