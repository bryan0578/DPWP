'''
Bryan Cash
1/15/2015
DPW
Simple Login
'''
import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
    	page_head = '''<!DOCTYPE HTML>
<html>
	<head>
		<title>Order</title>
	</head>
	<body>
		<h1>Delivery</h1>'''

	page_body = '''<h2>Enter Delivery Information</h2>
			<div id="form_box">
				<form method="GET">
					<label>First Name: </label><input type="text" name="f_name" /><br />
					<label>Last Name </label><input type="text" name="l_name" /><br />
					<label>Address: </label><input type="text" name="address" /><br />
					<select name="residence">
						<option value="House">House</option>
						<option value="Apt">Apt</option>
					</select>
					<label>Apt Number: </label><input type="text" name="apt" /><br />
					<label>City: </label><input type="text" name="city" /></br>
					<label>State: </label><input type="text" name="state" />
					<label>Zip: </label><input type="text" name="zip" /><br />
					<label>Phone: </label><input type="text" name="phone" /><br />
					<p>Would you like this order now or at a later time: 
						<label>Now</label>
							<input type="radio" name="order" value="Now" checked/>
						<label>Later</label>
							<input type="radio" name="order" value="Later" /><br />
					</p>
				<input type="submit" value="Submit" />
			</div>'''

	page_close = '''</form>
	</body>
</html>'''
	if self.request.GET:
		#stores info we got from the formm
		person = Delivery()
		person.f_name = self.request.GET['f_name']
		person.l_name = self.request.GET['l_name']
		person.address = self.request.GET['address']
		person.residence = self.request.GET['residence']
		person.apt = self.request.GET['apt']
		person.city = self.request.GET['city']
		person.state = self.request.GET['state']
		person.zip = self.request.GET['zip']
		person.phone = self.request.GET['phone']
		person.order = self.request.GET['order']

		self.response.write(page_head)
		self.response.write(person.f_name + ' ' + person.l_name)
		self.response.write('<br />' + person.address)
		self.response.write('<br /> ' + person.residence)
		self.response.write(' ' + person.apt)
		self.response.write('<br /> ' + person.city)
		self.response.write('</br /> ' + person.state)
		self.response.write(' ' + person.zip)
		self.response.write('</br /> ' + person.phone)
		self.response.write('</br /> I would like this order ' + person.order + '.')
		self.response.write(page_close)
			
	else:
		self.response.write(page_head + page_body + page_close) #PRINT

class Delivery(object):
	def __init__(self):
		self.f_name = ""
		self.l_name = ""
		self.address = ""
		self.residence = ""
		self.apt = ""
		self.city = ""
		self.state = ""
		self.zip = ""
		self.phone = ""
		self.order = ""


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
