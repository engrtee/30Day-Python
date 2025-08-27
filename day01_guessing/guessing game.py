#This is the module to import random numbers.
from random import randint

#This is the function to create a play game logic
def play_game(b):
	
	a = randint(1,12)	

#If statement to check if the a is equal to b.
	if a == b:
		print("This is Correct!!!")
	elif a > b:
		txt = f"This was so close as it was {a-b} lower than the correct answer which is {a}"
		print(txt)
	elif a < b:
		txt = f"This was so close as it was {b-a} higher than the correct answer which is {a}"
		print(txt)
	else:
		print("no number inputted")


while True:
	
#Try catch exception to catch errors
	try:
		b =int(input("Enter a valid number: "))
	except ValueError:
		print("Input a valid number")
	else:
		print("Valid number inputted")
		play_game(b)
	finally:
			c = input("Do you want to play again.yes/no: ")
			if c == "no":
				print("Thank you for playing this game")
				
				break
		

