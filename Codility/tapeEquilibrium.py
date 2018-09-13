#A[0] = 3
#A[1] = 1
#A[2] = 2
#A[3] = 4
#A[4] = 3

# | (A[0] + A[1] + ... + A[P ? 1]) ? (A[P] + A[P + 1] + ... + A[N ? 1]) |

# p = 1, 2, 3, 4   0 < P < N ( liczba elt tablicy )

# p = 1 => ( 3 ) - ( 1 + 2 + 4 + 3 ) = | 3 - 10 | = 7
# p = 2 => ( 3 + 1 ) - ( 2 + 4 + 3 ) = | 4 - 9  | = 5 
# p = 3 => ( 3 + 1 + 2 ) - ( 4 + 3 ) = | 6 - 7  | = 1 return Minimum 
# p = 4 => ( 3 + 1 + 2 + 4 ) - ( 3 ) = | 10 - 3 | = 7

# return 1
# oblicz tylko jedna strone druga wylicz ;)

def solution(A):
    """ Tape Equilibrium - get minimum value from list
        mathematical formula: | (A[0] + A[1] + ... + A[P ? 1]) ? (A[P] + A[P + 1] + ... + A[N ? 1]) |
        where 0 < P < N and N is list length
        A - list with intigers
        return int
    """
    N = len(A)
    sum = 0
    tempLeft = 0
    leftSide = 0
    for elt in A:
        sum += elt
    l = 0
    min = 0
    for i in range(N-1):
        tempLeft += A[i]
        leftSide = abs((sum - 2 * tempLeft))
        if i == 0:
            min = leftSide
        else:
            if min > leftSide:
                min = leftSide
    return min

A = [3, 1, 2, 4, 3, 1]
print(solution(A))