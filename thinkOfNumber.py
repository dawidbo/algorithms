# zgadywanie liczby z okreslonego przedzialu MIT
a = 0
b = 100 
print("Please think of a number between 0 and 100!")
while True:
    x=(a+b)//2    
    print("Is your secret number "+ str(x) + "?")
    letter = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    if letter=="h":
        b=x
    elif letter=="l":
        a=x
    elif letter=="c":
        break 
    else:
        print("Sorry, I did not understand your input.")                
print("Game over. Your secret number was: ",x)