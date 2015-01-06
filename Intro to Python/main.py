#print "hello world!"

#one lined comments

'''
Doc strings
'''

#http://legacy.pythong.org/dev/peps/pep-0008/

first_name = "Kermit"
last_name = "De Frog"
#print first_name

#response = raw_input("Enter your name     ")
#print "hello there,  ", response

birth_year = 1965
current_year = 2015
age = current_year - birth_year
#print "You are " + str(age) + " years old"

#budget = 200
budget = 90

if budget > 100:
	brand = "nike"
	print "Yay we can buy cool " + brand + " shoes!"
elif budget > 50:
	#print "We can at least get some generic sneakers"
	pass
else:
	#print "No cool shoes for me."
	pass

characters = ["leia","luke","chewy","lando"]
characters.append("obi won")
#print characters[0]

movies = dict() #create dictionary object
movies = {"Star Wars":"Darth Vader", "Silence of the Lambs":"Hannibal Lecter"}
#print movies["Star Wars"]

#while loop-----
'''
i = 0
while i<9:
	print "The count is", i
	i = i+1
'''

#for loop------
'''
for i in range(0,10):
	print "The counr is ", i
	i = i+1
'''

#for each loop------
rappers = ["tupac","Nas","Biggie Smalls"]
for r in rappers:
	#print "One of the best rappers is " + r
	pass

#function---------
'''
x = 2
def calcArea(h, w):
	area = h * w 
	return area + x

a = calcArea(20, 40);
#print "My area is " + str(a) + "sqft"
print a
'''

title = "Contact Us"
body = "You can contact us at contact@us.com"
message = '''
<!DOCTYPE HTML>
<html>
	<head>
		<title>{title}</title>
	</head>
	<body>
		{body}
	</body>
</html>
'''
message = message.format(**locals())
print message


