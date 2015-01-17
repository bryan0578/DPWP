'''
Bryan Cash
1/15/2015
DPW
Simple Login
'''
import webapp2
from pages import Page 

class MainHandler(webapp2.RequestHandler):
    def get(self):
    	p = Page()

	if self.request.GET:
		#stores info we got from the formm
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

		self.response.write(p.head)
		self.response.write('<div id="box">' + person.f_name + ' ' + person.l_name)
		self.response.write('<br /> Your order will be delivered to: <br /> ' + person.address)
		self.response.write(' ' + person.apt)
		self.response.write('<br /> ' + person.city)
		self.response.write('</br /> ' + person.state)
		self.response.write(' ' + person.zip)
		self.response.write('<br /> Your residence is a(an) ' + person.residence)
		self.response.write('</br /> Your order is under phone number ' + person.phone)
		self.response.write('</br /> and You would like this order ' + person.order + '.')
		self.response.write('<br /> Your oder should be at your door in 45 minutes' +'</div>' + p.close)
			
	else:
		self.response.write(p.head + p.body + p.close) #PRINT

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
