'''
Bryan Cash
1/21/2015
DWP
Reusable Library
'''
import webapp2
#from  the page file import the Page class
from page import Page
#from the library file import the library classes


class MainHandler(webapp2.RequestHandler):
    def get(self):

        #This is the page class where the main handler will show all of the html elements.
        p = Page()

        #This is where the main handler will write the html into the page and print it on the screen
        self.response.write(p.print_out())

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
