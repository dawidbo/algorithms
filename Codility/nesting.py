# https://app.codility.com/demo/results/trainingX735D8-33M/
# S = "(()(())())", the function should return 1 and given S = "())
def solution(S):
    lenS = len(S) 
    ans = 0
    for i in range(lenS):
        if S[i] == "(":
           ans += 1
        else:
            if ans == 0:
                return 0
            ans -= 1

    return 1 if ans == 0 else 0

# S = "(()(())())"
# S = "())"
S = "(()())"
print(solution(S))                   