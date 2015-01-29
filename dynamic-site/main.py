'''
Bryan Cash
1/28/2015
DPW
Dynamic Site
'''


import webapp2
from page import Page, ContentPage
from data import Shirt

class MainHandler(webapp2.RequestHandler):
    def get(self):
        p = Page()
        cp = ContentPage
        s = Shirt()


        if self.request.GET:
            if self.request.GET['id'] == "victorian_woman":
                cp.data = s.shirts[0]
                self.response.write(cp.content_view())
            elif self.request.GET['id'] == "metal_skull":
                cp.data = s.shirts[1]
                self.response.write(cp.content_view())
            elif self.request.GET['id'] == "three_b":
                cp.data = s.shirts[2]
                self.response.write(cp.content_view())
            elif self.request.GET['id'] == "f_bomb":
                cp.data = s.shirts[3]
                self.response.write(cp.content_view())
            elif self.request.GET['id'] == "hoody":
                cp.data = s.shirts[4]
                self.response.write(cp.content_view())

        else:
            self.response.write(p.print_out())




app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
