
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

	page_body = '''<form method="GET">
				<label>First Name: </label><input type="text" name="f_name" />
				<label>Last Name </label><input type="text" name="l_name" />
				<label>Email: </label><input type="text" name="email" />
				<label>Phone: </label><input type="text" name="phone" />
				<p>Preferred Contact Method: </p>
					<label>Phone</label>
						<input type="radio" name="contact" value="phone_number" checked/>
					<label>Email</label>
						<input type="radio" name="contact" value="email_address" />
			<label>Reason for Contact</label>
				<select name="reason">
					<option value="pay">Pay Status</option>
					<option value="work">Request for Work</option>
					<option value="fired">Fired</option>
				</select>
			<input type="submit" value="Submit" />'''

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

		self.response.write(page_head + page_body + page_close)
			
	else:
		self.response.write(page_head + page_body + page_close) #PRINT

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
