#This is a simple python program for calculating basic maths operations like addition , substraction, multiplication and division. 
#It provides an interactive interface and also provide usage statistics at the end of each use.

#Division Operation Function	
def division(a,b):
	c = a/b
	return c
	
	
	
#Multiplication Operation Function
def multiplication(a,b,):
	c = a*b
	return c
#	print(c)

#Substraction Operation Function
def substraction(a,b):
	c = a-b
	return c
#	print(c)

# Addition Operation function
def addition(a,b):
	c = a+b
	return c

	


#This is to initialize the counter to zero. The reason for this count is to enable the program count each time each of the functions are called.
count = 0

#This is the count for the addition function
countadd = 0

#This is the count for the substraction function
countsub = 0

#This is the count for the multiplication function
countmult = 0

#This is the count for the division function
countdiv = 0

#This is the conditional while statement used to call the calculator functions
while True:
	print("This is a simple calculator")
	print("Enter the number 1 to Add")
	print("Enter the number 2 to Substract")
	print("Enter the number 3 to Multiply")
	print("Enter the number 4 to Divide") 

#This was used to store the operation number so it can be used to call the appropriate maths function assigned to it
	choice= input("Enter the operation number: ")
	count +=1

	if choice in {'1', '2', '3', '4'}:

#This is a try except block to check for errors specifically data type errors and division by zero errors
		try:
			a =int(input("Enter the first Number:  "))
			b= int(input("Enter the second Number:  "))
			a/b

		except ValueError:
			print("Wrong Input")
		except ZeroDivisionError:
			print("Denominator is zero")
		else:

#Addition function is being called here	
			if choice == "1":

				result = f"The result of the addition operation is {addition(a,b)}"
				countadd +=1
				print(result)

#Substraction function is being called here				
			elif choice == "2":
				result = f"The result of the substraction operation is {substraction(a,b)}"
				countsub +=1
				print(result)

#Multiplication function is being called here	
			elif choice == "3":
				result = f"The result of the multiplication operation is {multiplication(a,b)}"
				countmult +=1
				print(result)

#Division function is being called here	
			elif choice == "4":
				result = f"The result of the division operation is {division(a,b)}"
				countdiv +=1
				print(result)
		finally:
				nextcalculation =input("Do you want to continue(yes/no): ")

#This is an interactive window to confirm if the user wants to continue with the calculator
				if nextcalculation == 'no':

# This is to print the usage statistics for the calculator
					final_message = f"Thank you for using our calculator. You used this calculator a total of {count} times"
					Usagestats = f"Addition Operation: {countadd} times \nSubstraction Operation: {countsub} times \nDivision Operation: {countdiv} times\nMultiplication Operation: {countmult} times"
					print(final_message)
					print(Usagestats)
					
					break

			
			
    		    
			
			
		