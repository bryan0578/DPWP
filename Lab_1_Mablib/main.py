print "Madlibs!!!"
name = raw_input("Enter your name: ")

print "Hello " + name + ", welcome to Madlibs."
print "To play Madlibs enter your answers to the following prompts and a funny story will be created. Ready....."
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



def calcTroops(numberTroops,numberNoun):
	if numberTroops < 50:
		troops = numberTroops*numberNoun
		return troops
	else:
		troops = numberNoun + numberTroops
		return troops

troop = calcTroops(numberTroops,numberNoun)
print troop