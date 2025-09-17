#Exercise 4









# Exercises: Level 1
# Declare an empty list
empty_list = []

# Declare a list with more than 5 items
items_list = ['item1','item2','item3','item4','item5']


# Find the length of your list
print(len(items_list))


# Get the first item, the middle item and the last item of the list

first,second,third,fourth,fifth = items_list
print(first,third,fifth)


# Declare a list called mixed_data_types, put your(name, age, height, marital status, address)

# Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
IT_Companies = ['Amazon','Microsoft', 'Apple','Oracle','IBM']

IT_Companies.sort()
print(IT_Companies)




# Print the list using print()
# Print the number of companies in the list
# Print the first, middle and last company
first,second,third,fourth,fifth = items_list
print(first,third,fifth)


# Print the list after modifying one of the companies
IT_Companies[1] = ['Microsft Inc']
print(IT_Companies)


# Add an IT company to it_companies
IT_Companies.append('Nvidia')


# Insert an IT company in the middle of the companies list
IT_Companies.insert(3,'ScaleAI')
print(IT_Companies)


# Change one of the it_companies names to uppercase (IBM excluded!)

#for item in IT_Companies:
	

#IT_Companies_upper=IT_Companies.upper()
print(IT_Companies)

# Join the it_companies with a string '#;  '
# Check if a certain company exists in the it_companies list.


print('Facebook' in IT_Companies)



# Slice out the first 3 companies from the list
slice = IT_Companies[0:3]
print(slice)

# Slice out the last 3 companies from the list
slice = IT_Companies[-3:]
print(slice)


# Slice out the middle IT company or companies from the list
slice = slice = IT_Companies[3]

# Remove the first IT company from the list
IT_Companies.pop(1)
print(IT_Companies)


# Remove the middle IT company or companies from the list


# Remove the last IT company from the list
# Remove all IT companies from the list
IT_Companies.clear()
print(IT_Companies)

# Destroy the IT companies list
del IT_Companies
#print(IT_Companies)


# Join the following lists:
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

all = front_end + back_end

fullstack = all.copy()
print(fullstack)
fullstack.insert(6,['Python','SQL'])
print(fullstack)

# After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack, then insert Python and SQL after Redux.

# Exercises: Level 2
# The following is a list of 10 students ages:
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

#To sort the age column
ages.sort(reverse=True)


# Sort the list and find the min and max age

#Max age
max = ages[0]
print(ages[0])

#Min Age 
min = ages[-1]
print(ages[-1])

# Add the min age and the max age again to the list
# Find the median age (one middle item or two middle items divided by two)

# Find the average age (sum of all items divided by their number )
average = sum(ages)/len(ages)
print(average)


# Find the range of the ages (max minus min)
range = max - min
print(range)


# Compare the value of (min - average) and (max - average), use abs() method
# Find the middle country(ies) in the countries list
# Divide the countries list into two equal lists if it is even if not one more country for the first half.
# ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic countries.
# 🎉 CO