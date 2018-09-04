# sumowanie elementow tablicy
# Python 3.5
p = ""
arr = []
sum = 0
print("Enter a number for summary. ")
while p != "e":
    x = 0
    try:
        x = int(input("Enter a number: "))
    except ValueError:
        print("Its not a number !!! Try again.")
    else:
        arr.append(x)
    p = input("Press 'enter' for next number or 'e' for end.")
for i in arr:
    sum += i
print("Sum: ",str(sum))