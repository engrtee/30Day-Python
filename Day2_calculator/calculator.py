
#Division Operation Function	
def division(a,b):
	c = a/b
	
	
	
#Multiplication Operation Function
def multiplication(a,b,):
	c = a*b
#	print(c)

#Substraction Operation Function
def substraction(a,b):
	c = a-b
#	print(c)

# Addition Operation function
def addition(a,b):
	c = a+b
#q	print(c)
	

# Conditional statement for the calculator
#s = input("Enter the sign: ")
print("This is a simple calculator")
print("Enter the number 1 to Add")
print("Enter the number 2 to Substract")
print("Enter the number 3 to Multiply")
print("Enter the number 4 to Divide")


while True: 
	choice= input("Enter the operation number: ")

	if choice in {'1', '2', '3', '4'}:

		try:
			a =int(input("Enter the first Number:  "))
			b= int(input("Enter the second Number:  "))

		except ValueError:
			print("Wrong Input")
		else:

			if choice == "1":
				
				addition(a,b)
			elif choice == "2":
				substraction(a,b)
			elif choice == "3":
				multiplication(a,b)
			elif choice == "4":
				division(a,b)
		finally:
				nextcalculation =input("Do you want to continue(yes/no): ")
				if nextcalculation == 'no':
					break

			
			
    		    
			
			
		