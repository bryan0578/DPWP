'''
Name
date
class
assignment
'''

import webapp2 #use the webapp2 library

class MainHandler(webapp2.RequestHandler):#declaring a class
    def get(self): #the function that starts everything.
        self.response.write('Hello world!')
        #code goes here

    def additional_function(self):
    	pass
    	#code goes here


#never touch this section
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
