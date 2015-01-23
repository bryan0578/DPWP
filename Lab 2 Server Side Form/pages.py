class Page(object):
	def __init__(self):
		self.data = Delivery()
		self.head = '''<!DOCTYPE HTML>
<html>
	<head>
		<title>Delivery</title>
		<link href="css/styles.css" rel="stylesheet" type="text/css" />
	</head>
	<body>
		<div id="background">
			<h1>Delivery</h1>
		</div>'''

		self.body = '''<h2>Enter Delivery Information</h2>
				<div id="form_box">
				<form id="form" method="GET">
					<div class="name">
						<label>First Name: </label><input class="input_size" type="text" name="f_name" /><br />
					</div>
					<div class="name">
						<label>Last Name: </label><input class="input_size" type="text" name="l_name" /><br />
					</div>
					<div class="name">
						<label>Address: </label><input class="input_size" type="text" name="address" /><br />
					</div>
					<div class="name">
						<select name="residence">
							<option value="House">House</option>
							<option value="Apt">Apt</option>
						</select>
						<label>Apt Number: </label><input class="input_apt" type="text" name="apt" /><br />
					</div>
					<div class="name">
						<label>City: </label><input class="input_size" type="text" name="city" /></br>
					</div>
					<div class="name">
						<label>State: </label><input class="input_size" type="text" name="state" />
					</div>
					<div class="name">
						<label>Zip: </label><input class="input_zip" type="text" name="zip" /><br />
					</div>
					<div class="name">
						<label>Phone: </label><input class="input_size" type="text" name="phone" /><br />
					</div>
					<div class="name">
					<p>Would you like this order now or at a later time: </p>
						<label>Now</label>
							<input type="radio" name="order" value="Now" checked/>
						<label>Later</label>
							<input type="radio" name="order" value="Later" /><br />
					</div>
					<div class="name">
						<input class="input_size" id="button" type="submit" value="Submit" />
					</div>
			</div>
		</form>'''

		self.results_body = ''

		self.close = '''</form>
	</body>
</html>'''

	def results(self):
		self.results_body = self.head + '<div id="box">' + self.data.f_name + ' ' + self.data.l_name + \
			'<br /> Your order will be delivered to: <br /> ' + self.data.address + \
			' ' + self.data.apt + '<br /> ' + self.data.city + '</br /> ' + self.data.state + \
			' ' + self.data.zip + '<br /> Your residence is a(an) ' + self.data.residence + \
			'</br /> Your order is under phone number ' + self.data.phone + \
			'</br /> and You would like this order ' + self.data.order + '.' + \
			'<br /> Your oder should be at your door in 45 minutes' +'</div>' + self.close
		return self.results_body
	

	def print_out(self):
		all = self.head + self.body + self.close
		all = all.format(**locals())
		return all

class Delivery(object):
	#class that instantiates the person information 
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