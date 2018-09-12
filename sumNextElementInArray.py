# [1,1 ,2,1 ,3,1 ,1,2 ] => [1,3 , 2,1 , 3,1]
def countNextElt(list):
    ansDic = {}
    for i in range(0,len(list),2):
        if list[i] in ansDic.keys():
            ansDic[list[i]] += list[i+1]
        else:
            ansDic[list[i]] = list[i+1]
    return ansDic
print(countNextElt([1,2 ,1,1 ,1,1 ,1,2 ]))