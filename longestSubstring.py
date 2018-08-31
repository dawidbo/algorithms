def longestSubstring(alfaString):
    """ Find longest substring in alphabetical string
        Ver: 1
        Args: 
           alfaString [string]
        Returns:
            string with longest chain
        TIP: Assume that string is in correct order  
    """
    lenStr = len(alfaString) 
    index = 0
    longestStr = ""
    strTemp = ""
    for i in range(lenStr):
        if i < lenStr - 1:
            if alfaString[i] > alfaString[i+1]: 
                strTemp = ""    
                while index <= i:
                    strTemp += alfaString[index]
                    index += 1              
        elif i == lenStr - 1:
            strTemp = ""
            while index <= i:
                strTemp += alfaString[index]
                print(strTemp)
                index += 1  
        if len(longestStr) < len(strTemp):
            longestStr = strTemp
    return "Longest substring in alphabetical order is: " + str(longestStr)
 
#s = 'abcdefghijklmnopqrstuvwxyz'
#s = 'azcbobobegghakl'
#s = 'abcebcd'
#s = 'abccccc'
#s = 'abcdefghijklmnopqrstuvwxyz'
#print(longestSubstring(s))