#To create a todo app.
#Step 1 create a l
b = []



def addtask():
	a = input("Enter your to do: ")
	b.append(a)
	
def printtask():
	print(b)
	
def deletetask():
	b.pop()


# Task manager
print('Add Task: Press 1 for this feature')
print('Show Tasks: Press 2 for this feature')
print('Delete task: Press 3 for this feature')

while True:
	choice =input('Enter your Input number between 1-3: ')
	if choice == "1":
			addtask()
	elif choice == "2":
			printtask()
	elif choice == "3":
			deletetask()
	
	nexttask = input('Do you want to enter another task yes/no: ')
	if nexttask == 'no':
					break
				
	
	
