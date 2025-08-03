## The computer or python code randomly generates a number and notifies the user to guess a number

  
##The user guesses the number and the program checks it the guessed input number is equal to the randomly generated number
from random import randint
from flask import Flask 
from requests import request
import jsonify

app=Flask(__name__)


@app.route('/play_game', methods = ['GET', 'POST'])
def play_game():
	a = randint(1,2)
	for i in range(5):
		#b =int(input())
		data = request.get_json()
		b =int(data.get('b'))
		if a == b:
		  
		  return jsonify(result = "Correct")
	   #	print("Correct")
		elif a > b:
			
			return jsonify(result = "Lower")
		#	print("lower")
		elif a < b:
			return jsonify(result = "Higher")
			#print("higher")	
		else:
			return jsonify(result = "No Number inputted")
			#print("no number inputted")
			
if __name__ == '__main__':
	 app.run(host ='0.0.0.0', port = 5000)



	
    


##If it's equal to the number, print “correct”


##If it is greater than the number print “High”  or “Too High” based on the level 
##If it is lower than the number print “low” or “lower” 


##Limit the number of tries to five - loop
##There should be a condition to check if no number was inputted and put 0 
##There should be a message that shows you cant try again 
