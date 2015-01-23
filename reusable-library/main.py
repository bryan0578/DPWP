'''
Bryan Cash
1/21/2015
DWP
Reusable Library
'''
import webapp2
#from  the page file import the Page class
from page import Page
from library import HighScores, FavoriteGame
#from the library file import the library classes


class MainHandler(webapp2.RequestHandler):
    def get(self):
        #This is the page class where the main handler will show all of the html elements.
        p = Page()

        lib = FavoriteGame()

        md1 = HighScores()
        if self.request.GET:
            md1.game = self.request.GET['game']
            md1.s = self.request.GET['score']
            md1.initials = self.request.GET['initials']
            md1.players = self.request.GET['players']
            lib.add_game(md1)

            p.results = lib.complile_list()
            self.response.write(p.print_results())

        else:
            self.response.write(p.print_out())





        #This is where the main handler will write the html into the page and print it on the screen


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
