# reads the given file and returns the available slots and input coins as lists
def read_file(file_path):
	
	# open the file in read mode
	with open(file_path,"r") as my_file:
		
		# read the number of slots from the first line
		no_of_slots = int(my_file.readline()) 
		slots = [] # used to store the available slots
		
		for i in range(no_of_slots):
			# read the next line and split the values seperated by spaces to a list
			# containing the slot thickness/trigger mass
			slot = my_file.readline().split() 
			slots.append(slot) # add slot list to the list of all slots
		
		# read the number of coins from the next line
		no_of_coins = int(my_file.readline())
		coins = [] # used to store all input coins
		
		for i in range(no_of_coins):
			# read the next line and splot the values seperated by spaces to a list
			# containing the coin thickness/mass
			coin = my_file.readline().split()
			coins.append(coin) # add coin list to the list of all coins
			
		return slots, coins

slots = [] # used to store list of slots
coins = [] # used to store list of coins

# set file path to read input		
read_file_path = "aa_test_02.txt"

distance = 0 # total distance travelled by the coins

#read the input and return lists of slots/coins
slots, coins = read_file(read_file_path)

# loop through list of coins
for coin in coins:
	# loop through list of slots
	for slot in slots:
		# if coin thickness <= slot thickness and coin mass >= trigger mass
		if int(coin[0]) <= int(slot[0]) and int(coin[1]) >= int(slot[1]):
			distance += slots.index(slot) + 1 # add to total distance
			break # jump out of slots loop as found coin

# print total distance			
print(distance)
	
