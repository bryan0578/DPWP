'''
Bryan Cash
1/15/2015
DPW
Simple Login
'''

import webapp2 #use the webapp2 library

class MainHandler(webapp2.RequestHandler):#declaring a class
    def get(self): #the function that starts everything.
    	page_head = '''<!DOCTYPE HTML>
<html>
	<head>
		<title></title>
	</head>
	<body>
		<h1>Employee Contact Database</h1>'''

		page_body = '''<form method="GET">
			<label>First Name: </lable<input type="text" name="f_name" />
			<label>Last Name </label><input type="text" name="l_name" />
			<label>Email: </label><input type="text" name="email" />
			<label>Phone: </label><input type="text" name="phone" />
			<label>Preferred Contact Method </lable>
				<input type="radio" name="contact" value="phone" checked/>
				<input type="radio" name="contact" value="email" />
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
      

  


#never touch this section
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
