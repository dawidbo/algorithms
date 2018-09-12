def isIn(char, aStr):
    '''
        char: a single character
        aStr: an alphabetized string
        alfabet = "abcdefghijklmnopqrstuvwxyz"
        returns: True if char is in aStr; False otherwise
    '''
    a=0
    b=len(aStr)
    if b==0:
        return False
    if b==1:
        if char==aStr[0]:
            return True
        else:
            return False
    middle=b//2
    if char>=aStr[middle]:
        a=middle
    elif char<=aStr[middle]:
        b=middle
    return char==aStr[1] or isIn(char,aStr[a:b])

# s = "abdehikklmnprstvy"
# ch = "r"
# print(isIn(ch,s))