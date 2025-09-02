
#This is the function to add a new contact
def addcontact(name,phone):
	contactbook={name:"",phone:""}
	return contactbook
	



#This is the function to delete a contact
def deletecontact(name):
	for name in contactbook:
		print(name)
		
#removecontact("Ton")


print("Show contacts list. press 1")
print("Update contacts list. press 2")
print("Delete a contact. press 3")
print("Add a new contacts. press 4")




while True:
	choice = input("Enter your choice: ")

	if choice in ("1","2","3","4"):
		try:
			name = input("Enter your name: ")
			phone =int(input("Enter your phone number: "))
		except Valueerror:
			print("wrong data type") 
		else:
			if choice == 1:
				showcontact()
			elif choice == 2:
				updatecontact(name)
			elif choice == 3:
				deletecontact(name)
			elif choice == 4:
				addcontact(name,phone)
				print(contactbook)
		finally:
			next = input("Do you want to perform another operation(yes/no): ")
			if next == "no":
				break
		
		
		
	
		
		
		

		
