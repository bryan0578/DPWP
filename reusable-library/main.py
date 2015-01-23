'''
Bryan Cash
1/21/2015
DPW
Reusable Library
'''
import webapp2
#from  the page file import the Page class
#this imports the page class from the page file
from page import Page
#from the library file import the library classes
#this imports the HighScores data object and the FavoriteGame library classes from the library file
from library import HighScores, FavoriteGame



class MainHandler(webapp2.RequestHandler):
    def get(self):
        #This is the page class where the main handler will show all of the html elements.
        #Here I set p as an instance of the Page class
        p = Page()
        #This is the FavoriteGame library where all the methods will be used to store, add_game and compile a list of highscores
        #Here I set lib as an instance of the FavoriteGame class
        lib = FavoriteGame()

        #Here I set md1 as an instance of the HighScores data object
        #This uses the HighScores data object as a blueprint for all of the input recieved from the request.GET method
        md1 = HighScores()
        #Here I started a conditional statement to decide which view will be printed to the screen
        #So if there is any request.GET information the information from the inputs will be stored using the HighScores blueprint
        if self.request.GET:
            md1.game = self.request.GET['game']
            md1.s = self.request.GET['score']
            md1.i = self.request.GET['initials']
            md1.players = self.request.GET['players']
            #here I call the instance of favorite games and pass in the stored information from the HighScores data object and run the add_game method
            lib.add_game(md1)

            #This sets the reults view to the compile_list method so it will show the information from the data object
            p.results = lib.compile_list()
            #This prints the results view to the web page
            self.response.write(p.print_results())

        #This is the second part of the condition that will print the form view if the request.GET information doesn't exist
        else:
            self.response.write(p.print_out())





        #This is where the main handler will write the html into the page and print it on the screen


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
