'''
    Yes, sorting the array and taking the last three elements (largest positive elements) will give you a candidate for the maximum product of three, 
    however take in mind that each int may be as low as -1000. 
    Therefore multiplying the two most negative values by the largest positive value is also a candidate. 
    The largest most positive candidate is the answer.
    https://app.codility.com/demo/results/training34RRDF-PG5/
'''
def solution(A):
    lenA = len(A)
    A.sort()
    return A[0]*A[1]*A[lenA -1] if A[0]*A[1]*A[lenA -1] > A[lenA -3]*A[lenA -2]*A[lenA -1] else A[lenA -3]*A[lenA -2]*A[lenA -1]
 
A = [-10, -2, -4]
A = [-5, 5, -5, 4] 
print(solution(A))