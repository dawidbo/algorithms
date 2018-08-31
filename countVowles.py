
def countVowles_1(s):
    """ Count volwes in string. Volwes = 'a,e,i,o,u'
        Ver: 1
        Args: 
            s [string]
        Returns:
            ans [string]          
    """
    ans=0    
    for letter in s:
        if letter=="a" or letter=="e" or letter=="i" or letter=="o" or letter=="u":
            ans+=1
    return "Number of vowels: "+str(ans)


def countVowles_2(s):
    """ Count volwes in string. Volwes = 'a,e,i,o,u'
        Ver: 2
        Args: 
            s [string]
        Returns:
            ans [string]          
    """
    ans=0    
    volwes = ["a","e","i","o","u"]
    for letter in s:
       if letter in volwes:
            ans+=1
    return "Number of vowels: "+str(ans)

#s = 'adcffoooaaaaaaaaaaaaaaaaaaa'        
#print(countVowles_1(s))
#print(countVowles_2(s))