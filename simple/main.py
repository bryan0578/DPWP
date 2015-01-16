
import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
    	

    	page_head = '''<!DOCTYPE HTML>
<html>
	<head>
		<title></title>
	</head>
	<body>
		<h1>Employee Contact Database</h1>'''

	page_body = '''<h2>Add Employee Contact</h2>
			<div id="form_box">
				<form method="GET">
					<label>First Name: </label><input type="text" name="f_name" /><br />
					<label>Last Name </label><input type="text" name="l_name" /><br />
					<label>Email: </label><input type="text" name="email" /><br />
					<label>Phone: </label><input type="tel" name="phone" /><br />
					<p>Preferred Contact Method: </p>
						<label>Phone</label>
							<input type="radio" name="contact" value="phone" checked/>
						<label>Email</label>
							<input type="radio" name="contact" value="email" /><br />
					<label>Reason for Contact: </label><br />
					<select name="reason">
						<option value="Pay Status">Pay Status</option>
						<option value="Request for Work">Request for Work</option>
						<option value="Fired">Fired</option>
					</select><br />
				<input type="submit" value="Submit" />
			</div>'''

	page_close = '''</form>
	</body>
</html>'''


	if self.request.GET:
		#stores info we got from the formm
		f_name = self.request.GET['f_name']
		l_name = self.request.GET['l_name']
		email = self.request.GET['email']
		phone = self.request.GET['phone']
		contact = self.request.GET['contact']
		reason = self.request.GET['reason']

		self.response.write(page_head + str(Employee()) + page_close)
			
	else:
		self.response.write(page_head + page_body + page_close) #PRINT


class Employee(object):
	def __init__(self):
		self.f_name = ""
		self.l_name = ""
		self.email = ""
		self.phone = ""
		self.contact = ""
		self.reason = ""

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
