def randomizeList(start,end,numElement):
    from random import randint
    ranList = []
    for elt in range(numElement):
        ranList.append(randint(start,end))
    return ranList

counter = 0
isNotFound = True
arr = randomizeList(1,10,6)

while isNotFound:
    counter += 1
    try:
        findNum = int( input( "Guess a number: " ) )
    except ValueError:
        print( "It's not a number !!! Try again." )
    else:
        for i in arr:
            if i == findNum:
                isNotFound = False
                break
                
print( "You found number: " + str( findNum ) + " in " + str( counter ) + " test/s !!!" )