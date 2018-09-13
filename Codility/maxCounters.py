'''
    You are given N counters, initially set to 0, and you have two possible operations on them:
    increase(X) ? counter X is increased by 1,
    max counter ? all counters are set to the maximum value of any counter.
    A non-empty array A of M integers is given. This array represents consecutive operations:

    if A[K] = X, such that 1 ? X ? N, then operation K is increase(X),
    if A[K] = N + 1 then operation K is max counter.
    For example, given integer N = 5 and array A such that:

        A[0] = 3
        A[1] = 4
        A[2] = 4
        A[3] = 6
        A[4] = 1
        A[5] = 4
        A[6] = 4
    the values of the counters after each consecutive operation will be:

        (0, 0, 1, 0, 0)
        (0, 0, 1, 1, 0)
        (0, 0, 1, 2, 0)
        (2, 2, 2, 2, 2)
        (3, 2, 2, 2, 2)
        (3, 2, 2, 3, 2)
        (3, 2, 2, 4, 2)
    
    https://app.codility.com/demo/results/trainingBQGKND-C77/
'''
def solution(N, A):
    aLen = len(A)
    ansList = [0] * (N + 1)
    ansLen = len(ansList)
    maxValue = 0
    offset = 0
    for i in range(aLen):
        if A[i] == (N + 1):
            offset = maxValue
    
        if A[i] >= 1 and A[i] <= N:
            # offset byl wywyolany ansList[A[i]] += 1
            ansList[A[i]] = max( offset+1,  ansList[A[i]]+1 )
            if maxValue < ansList[A[i]]:
                maxValue = ansList[A[i]]
       
    for i in range(1,ansLen):
        if ansList[i] < offset:
            ansList[i] = offset
    
    return ansList[1:]
         

A = [3,4,4,6,1,4,4]
N = 5
print(solution(N, A))