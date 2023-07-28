prompt = "Please verify your age before entering into DripCinemas so we can properly accommodate you for the right prices:"
#This prompt is for a while loop to ask the diffrent types of ages and prices 
prompt += "\n(Enter 'quit' when you have accommodated the right amount of guests):"
#This is used to break the loop when all of the ages have been picked 

active = True
#Flag is being used, and criterias are being set for the loop 
while active:
		age = input(prompt)
    #when active the prompt will be repeated multiple times 
		if age == 'quit':
			active = False
		else:
    #when the flag is false the program was stopped becuase the user inputted quit into the prompt 
			age = int(age)
        #this regualtes the infinted combinations of ages being picked and these  if,elif statements narrow down the options
			if age <= 3:
				print("\nThe price for your toddler is free!")
			elif age >= 12:
				print("\nThe price would be $15.")
			else:
				print("\nThe price would be $10. (Disregard if under 3 years old)")
