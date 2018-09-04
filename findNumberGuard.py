# Guard - insert guard to the end of array to prevent boundary error
def randomizeList(start,end,numElement):
    from random import randint
    ranList = []
    for elt in range(1, numElement):
        ranList.append(randint(start,end))
    return ranList
arr = randomizeList(1,6,50)
i = 0
while True:
    try:
        findNum = int(input("Guess a number: "))
    except ValueError:
        print("It's not a number !!! Try again.")
    else:
        arr.append(findNum)   
        while arr[i] != findNum:
            i += 1
        break
if i == len(arr)-1:
    print("Guard! Number not exist.")
else:
    print("Number has been founded: ", str(findNum), "on index", i)