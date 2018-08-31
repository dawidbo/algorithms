def perfectCube_1(x):
    """ Is number x is a number for perfect cube
        Ver: 1
        Args: 
            x [int]
        Returns:
            ans [string]  
    """
    num = 0
    ans = "Not perfect cube"
    while num**3 < abs(x):
        num += 1 
    if num**3 == x:
        ans = "Perfect " + str(num)
    return ans

def perfectCube_2(x):
    """ Is number x is a number for perfect cube
        Ver: 2
        Args: 
            x [int]
        Returns:
            ans [string]  
    """
    ans = "Not perfect cube"
    for num in range(abs(x) + 1):
        if num**3 == abs(x):
            break
    if num**3 == abs(x):
        if x < 0:
            x = abs(x)
        ans = "Perfect "+str(num)
    return ans

#x=27
#print(perfectCube_1(x))
#print(perfectCube_2(x))