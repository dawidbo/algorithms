def createRadomizeList(start, end):
    """ Generate random list
        ver. 1
        Args:
            start int
            end int
        Return:
            list - usortedList
    """
    from random import randint
    ranList = []
    for i in range(end):
        ranList.append(randint(start,end))
    return ranList

def minAndMax(unsortedList):
    """ Get min and max value from list
        ver. 1
        Args:
            unsortedList obj list
        Return:
            string
    """
    min = usortedList[0]
    max = usortedList[0]
    for elt in unsortedList:
        if elt > max:
            max = elt
        elif elt < min:
            min = elt
            
    return "minimum: "+str(min)+", maximum: "+str(max)  

#print(minAndMax(createRadomizeList(1,10001)))