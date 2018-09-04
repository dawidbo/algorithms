# suma liczb calkowitych 
# dec: 19 = bin: 10011 = dec: 3 
def summarNumbers(x,s):
    """change int to number system e.g. 2,3,4,5,6 and sum result of this output number
        Args:
            x int
            s int - number system
        Return:
            int        
    """
    sum = 0
    while x>0:
        sum+=x%s
        x//= s
    return sum
sum = 0
while True:
    try:
        x = int(input("Write a number: "))
        s = int(input("Choose system: "))
    except ValueError:
        print("Write correct number!")
    else:
        sum=summarNumbers(x,s)         
        break
print("Total sum: ", sum)