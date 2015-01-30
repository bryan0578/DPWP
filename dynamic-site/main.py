'''
Bryan Cash
1/28/2015
DPW
Dynamic Site
'''


import webapp2
from page import ContentPage
from data import Shirt

class MainHandler(webapp2.RequestHandler):
    def get(self):
        s = Shirt()
        cp = ContentPage()

        if self.request.GET:
            if self.request.GET['id'] == "victorian_woman":
                cp.data = s.shirts[0]
                self.response.write(cp.print_out())
            elif self.request.GET['id'] == "metal_skull":
                cp.data = s.shirts[1]
                self.response.write(cp.print_out())
            elif self.request.GET['id'] == "three_b":
                cp.data = s.shirts[2]
                self.response.write(cp.print_out())
            elif self.request.GET['id'] == "f_bomb":
                cp.data = s.shirts[3]
                self.response.write(cp.print_out())
            elif self.request.GET['id'] == "hoody":
                cp.data = s.shirts[4]
                self.response.write(cp.print_out())

        else:
            cp.data = s.shirts[0]
            self.response.write(cp.print_out())











app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
