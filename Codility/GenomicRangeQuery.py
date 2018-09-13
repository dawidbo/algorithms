# GenomicRangeQuery
# Find the minimal nucleotide from a range of sequence DNA.
# prefix sum oznacz sume wszytkich elementow przed tym na ktorym stoisz
# 62%
# https://app.codility.com/demo/results/trainingR67JZC-XNB/

def solution(S, P, Q):
    pLen = len(P)
    qLen = len(Q)
    nucloList = []
    ans = []
    for i in range(pLen):
        min = "Z"
        if P[i] <= Q[i]: 
            for j in range(P[i],Q[i]+1):
                if S[j] < min:
                    min = S[j]
        nucloList.append(min)   
    i = 0
    for elt in nucloList:
        nucloList[i] = impactDict[elt]
        i+=1
    return nucloList 
                            
impactDict = {"A":1, "C":2, "G":3, "T":4}
S = "CAGCCTA"
P = [2,5,0]    
Q = [4,5,6]
print(solution(S, P, Q))