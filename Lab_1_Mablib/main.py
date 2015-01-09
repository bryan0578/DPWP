'''
Bryan Cash
Lab 1 Madlibs
DPWP
'''
#introduction to program with prompt for welcome message

print "Madlibs!!!"
name = raw_input("Enter your name: ")

#Welcome message

print "Hello " + name + ", welcome to Madlibs."
print "To play Madlibs enter your answers to the following prompts and a funny story will be created. Ready....."

#Set up variables for user input, dictionary and an array for use in the madlib

story = raw_input("Are you a jedi or are you a sith: ")
side = dict()
side = {"jedi":"Master","sith":"Darth"}
sillyWord1 = raw_input("Enter a silly word: ")
adjective1 = raw_input("Enter an adjective: ")
noun1 = raw_input("Enter a noun: ")
sillyWord2 = raw_input("Enter a second silly word: ")
numberTroops = int(raw_input("Enter a number greater than 0 but less than 100: "))
sillyWord3 = raw_input("Enter a third silly word: ")
numberNoun = int(raw_input("Enter another number greater than 0 but less than 1000: "))
noun2 = raw_input("Enter another noun: ")
adjective2 = raw_input("Enter another adjective: ")
action = raw_input("Finally enter an action: ")
people = ["Han","Chewy","Leia","C3P0"]

'''
Funtion that takes both raw_input integers and calculates the nuber of troops used in the madlib.
Used both logical operators and mathmematical operators
Used one conditional statement
'''

def calcTroops(numberTroops,numberNoun):
	if numberTroops < 50 and numberNoun < 500:
		troops = numberTroops*numberNoun
		return troops
	else:
		troops = numberNoun + numberTroops
		return troops

troop = calcTroops(numberTroops,numberNoun)


