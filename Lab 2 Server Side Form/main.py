'''
Bryan Cash
1/15/2015
DPW
Simple Login
'''
import webapp2
from pages import Page, Delivery

class MainHandler(webapp2.RequestHandler):
    def get(self):
    	p = Page()

	if self.request.GET:
		#stores info we got from the form 
		person = Delivery()
		person.f_name = self.request.GET['f_name']
		person.l_name = self.request.GET['l_name']
		person.address = self.request.GET['address']
		person.apt = self.request.GET['apt']
		person.city = self.request.GET['city']
		person.state = self.request.GET['state']
		person.zip = self.request.GET['zip']
		person.residence = self.request.GET['residence']
		person.phone = self.request.GET['phone']
		person.order = self.request.GET['order']

#Writes the information from the form 

		p.data = person
		self.response.write(p.results())
	else:
		self.response.write(p.print_out()) #PRINT




app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
