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
Funtion that takes both raw_input integers and calculates the number of troops used in the madlib.
Used both logical operators and mathmematical operators
Used one conditional statement
The purpose of this function is to calculate the number of troops or storm troopers used in the madlib story
'''

def calcTroops(numberTroops,numberNoun):
	if numberTroops < 50 and numberNoun < 500:
		troops = numberTroops*numberNoun
		return troops
	else:
		troops = numberNoun + numberTroops
		return troops

troop = calcTroops(numberTroops,numberNoun)

'''
Function that takes both raw_input integers and calculates the number of the noun used in the madlib
Used both logical and mathmematical operators
Used one conditional statement
The purpose of this function is to calculate the number of a raw_input noun to use in the madlib
'''

def calcNoun(numberTroops,numberNoun):
	if numberTroops > 50 and numberNoun > 800:
		noun = numberNoun/numberTroops
		return noun
	else:
		noun = numberNoun * numberTroops
		return noun

noun = calcNoun(numberTroops,numberNoun)

'''
Function that chooses the appropriate story to print in the madlib
Uses a logical operator and includes a for loop to loop through the names given in the array
The purpose of this function is the appropriate story to print according to the raw_input
If the user enters jedi the story addresses a jedi master by putting master in front of a silly word, 
if the user enters sith, the story slightly alters and addresses a sith master by changing all the 
words master to Darth.
'''

def calcStory(story):
	if story == "jedi":
		print "A long time ago in a galaxy far, far away, The rebel alliance has had there first victory against the empires new villain but " + side[story] + " " + sillyWord1 + " and his " + adjective1 + " " + noun1 + " flew to the planet of " + sillyWord2 + "  " + side[story] + " " + sillyWord1 + " has begun his defense with " + str(troop) + " of his most elite troopers. Meanwhile "
		for p in people:
			print p 
		print "came out of hyperspace in the " + sillyWord3 + " system with " + str(noun) + " " + noun2 + "s to aid the alliance in the " + adjective2 + " " + action + "."
	else:
		print "A long time ago in a galaxy far, far away, The rebel alliance has had there first victory against the empires new villain " + side[story] + " " + sillyWord1 + " and his " + adjective1 + " " + noun1 + ". But the war has only just begun. On the planet of " + sillyWord2 + "  " + side[story] + " " + sillyWord1 + " has begun his attack with " + str(troop) + " of his most elite storm troopers. Meanwhile "
		for p in people:
			print p 
		print "came out of hyperspace in the " + sillyWord3 + " system with " + str(noun) + " " + noun2 + "s to aid the alliance in the " + adjective2 + " " + action + "."

finalStory = calcStory(story)






