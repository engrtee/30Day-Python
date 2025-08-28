#This is the module to import random numbers.
from random import randint

#This is the function to create a play game logic
def play_game(a,b):
	
	

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
		return b
	

count = 0
failed_count = 0
successful_count = 0
while True:

#Try catch exception to catch errors
	try:
		count +=1
		a = randint(1,12)	
		b =int(input("Enter a valid number: "))
	except ValueError:
		print("Input a valid number")
	else:
		print("Valid number inputted")
		play_game(a,b)
		if a == b:
			successful_count +=1
		elif a < b or a > b:
			failed_count += 1
	finally:
			c = input("Do you want to play again.yes/no: ")
			if c == "no":
				print("Thank you for playing this game")
				usagestats = f"You played this game a total number of {count} times, you had {failed_count} unsuccessful attempts and {successful_count} successful attempts"
				print(usagestats)
				
				break
		

