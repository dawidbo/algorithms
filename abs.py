def absoluteValue():
	""" Absolute value
        Ver: 1
        Returns:
            int
    """	
	while True:
	    try:    
	        x=int(input("Enter a number: "))
	    except ValueError:
	        print("Its not a number !!! Try again.")
	    else:
	        if x<0:
	            x=-x
	        break            
	return x
#print(absoluteValue())