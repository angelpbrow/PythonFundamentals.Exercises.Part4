from random import randrange


def ran_num():
	rand_num = randrange(10)
	return rand_num



def high_or_low(number,rand_num):
	
	if number >  rand_num:
			print('Too high')
			#print('The random number was: ' + str( rand_num))
			#print('Your guess was: ' + str(number))
	
	elif number < rand_num:
			print('Too low')
			#print('The random number was: ' + str( rand_num))
			#print('Your guess was: ' + str(number))

	else:
			 print("Your guess is correct")
			
		
	# x = int(user_number)


def play():
	play_again = True
	while play_again == True:
	
		number = input('Give me a number between 0 and 10: ')
		high_or_low(int(number), x)
		if (int(number) == x):
			play_again = False 




x = int (ran_num())
play()


        



