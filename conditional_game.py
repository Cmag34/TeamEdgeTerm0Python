import random

# -------------------------------------------- 

	# You've just learned about variables, conditionals.
	# Just from knowing those two topics, you can do so much!
	
	# Let's try to make a simple program that responds to the user.
	# We're going to recreate the Magic 8 Ball!!!
			
			# Never heard of it? That's ok!

					# You got this!

  # -------------------------------------------- 

	# How a Magic 8 Ball Works:

	# The user asks a question and vigoriously shakes the ball. 
	# Then the ball will respond with one of twenty responses, chosen at random. 

	# That's pretty simple right?

 # -------------------------------------------- 

	# Part 1: 
	# Print instructions on the screen and 
	# prompt the user to ask a question

	

  # --------------------------------------------

print("How a Magic 8 Ball works:")
print("The user asks a question and vigorously shakes the ball.")
print("Then the ball gives the user gets a fortune")













# -------------------------------------------- 

	# Part 2: Next, we need to randomly select a response from 20 options.

	# Randomly select a number from 0 - 19       
	# Use that to select from the following responses:

question = input('Ask the fortune teller a question>> ')
select= random.randint(0-19)
if  select==0:
	print(" It is certain.")
elif  select==1:
	print("It is decidedly so.")
elif  select==2:
	print("Without a doubt.")
elif  select==3:
	print("Yes - definitely.")
elif  select==4:
	print("You may rely on it.")
elif  select==5:
	print("As I see it, yes.")
elif  select==6:
	print("Most likely.")
elif  select==7:
	print("Outlook good.")
elif  select==8:
	print("Yes.")
elif  select==9:
	print("Signs point to yes.")
elif  select==10:
	print("Reply hazy, try again.")
elif  select==11:
	print("Ask again later.")
elif  select==12:
	print("Better not tell you now.")
elif  select==13:
	print("Cannot predict now.")
elif  select==14:
	print("Concentrate and ask again.")
elif  select==15:
	print("Don't count on it.")
elif  select==16:
	print("My reply is no.")
elif  select==17:
	print("My sources say no.")
elif  select==18:
	print("Outlook not so good.")
elif  select==19:
	print("Very doubtful.")
		

	# Look up random.rand_int to see how you can use it to select a random number.

  # -------------------------------------------- 






















# -------------------------------------------- 

	# Part 3: Customize it!

	# Select your own theme and use case and modify your code!
	
# -------------------------------------------- 



select1= input('For a second fortune, select a random number from 0-19>> ')
if  select1==0:
	print(" you suck.")
elif  select1==1:
	print("unlikely.")
elif  select1==2:
	print("no.")
elif  select1==3:
	print("nope.")
elif  select1==4:
	print("never.")
elif  select1==5:
	print("this leads to a fatal ending.")
elif  select1==6:
	print("hopefully.")
elif  select1==7:
	print("sadly so.")
elif  select1==8:
	print("Yes.")
elif  select1==9:
	print("maybe.")
elif  select1==10:
	print("Reply hazy, try again.")
elif  select1==11:
	print("Ask again later.")
elif  select1==12:
	print("Better not tell you now.")
elif  select1==13:
	print("the future will tell you.")
elif  select1==14:
	print("the past")
elif  select1==15:
	print("Don't count on it.")
elif  select1==16:
	print("My reply is no.")
elif  select1==17:
	print("My sources say deffinetly not.")
elif  select1==18:
	print("not likely my friend.")
else:
	print("Very doubtful.")
	













