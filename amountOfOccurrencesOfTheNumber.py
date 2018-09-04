p = ""
arr = []
amount = 0
print( "Add numbers to list." )
while p != "e":
    try:
        x = int( input ("Enter a number: "))
    except ValueError:
        print("Its not a number !!! Try again.")
    else:
        arr.append(x)
        p = input("Press enter to add next value or 'e' for finish ")
while True:
    try:
        x = int(input("Choose the number you are looking for: "))
    except ValueError:
        print("Its not a number !!! Try again.")
    else:
        break
for i in arr:
    if i==x:
        amount += 1 
print("Amount of occurrences of the number: "+str(x)+" is: "+str(amount))