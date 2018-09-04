def squarePrecision(num,epsilon=0.01,guess=0.0,step=0.1):
	""" Get square from number 
        Ver: 1
        Args:
        	num int
        	epsilon - float - precision
        	guess - float - start step for counting
        	step - float
        Returns:
        	string
	""" 
	ans = "failed"       
	while guess <= num:
	    if abs(guess**2 -num) < epsilon:
	        break
	    else:
	        guess += step
	if abs(guess**2 - num) < epsilon:
	    ans = "succeeded: "+str(guess)
	return ans
#print(squarePrecision(25))    