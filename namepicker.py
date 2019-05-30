import random 
#random name generator!!!!!!!!


# The requirements for this were 
# 1) Enter as many tester/participant names as you want 
# 2) Randomly select a name from that list. 
# 3) If a tester's name was picked already, remove them from the list so they don't get picked again
# 4) Print a statement congratulating winner(s)


name = ""
names_list = []

# Set conditions and variables
print("Welcome to the [Company Name] Field Trials Random Name Picker(for Bravo Points!)")
num_of_winners = input("How many winners would you like?(ex.1, 2, etc) ")
num_of_winners = int(num_of_winners)

while True:
	names = input("Please input a tester name and press enter. Enter 'q' to end. ")
	names = names.lower()
	names_list.append(names)
	if names == 'q':
		names_list.remove('q')
		for i in range(num_of_winners):	
			random.shuffle(names_list)
			winner = names_list.pop()				
			print(f"The {i +1} Bravo Winner is {winner}!")
			# print(names_list)
		stop = input("Press Enter to Exit" )
		break
