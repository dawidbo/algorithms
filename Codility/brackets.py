#https://app.codility.com/demo/results/trainingRAXRQ7-TM7/
def brackets(S):
    lenS = len(S)
    bufforList = []
    dicTags = { "}":"{", "]":"[",")":"(" }
    sum = 0
    for i in range(lenS):
        if S[i] == "{" or S[i] == "[" or S[i] == "(":
            bufforList.append(S[i])
            sum += 1    
        else:
            if len(bufforList) == 0:
                return 0
            if dicTags[S[i]] == bufforList[-1]:
                bufforList.pop()
                sum -= 1
            else:
                return 0
    return 1 if sum == 0 else 0     
        
S = "{[([{()()}])()]}"  
# S = "([)()]"
# S = '))(('
# S= '{{{{'
# print(brackets(S))