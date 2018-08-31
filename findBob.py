def findBob_1(s):
    """ Find bob and count number of occurrences
        Ver: 1
        Args: 
            s [string]
        Returns:
            ans [string]          
    """
    bob = 0
    numLetters = len(s)-1
    for num in range( numLetters ):
        if s[num] == 'b':
            if numLetters >= num + 2:
                if s[num + 1] == 'o':
                    if s[num + 2] == 'b':
                        bob += 1
    return "Number of times bob occurs is: "+str(bob)

def findBob_2(s):
    """ Find bob and count number of occurrences. Use slice method.
        Ver: 2
        Args: 
            s [string]
        Returns:
            ans [string]          
    """
    lenS=len(s)
    bob=0
    for i in range(lenS):
        if s[i:i+3] == "bob":
            bob+=1
    return "Number of times bob occurs is: "+str(bob)

#s = 'adobdybobobtbobobbobbzbobbsoboborkobobo'
#print(findBob_1(s))
#print(findBob_2(s))