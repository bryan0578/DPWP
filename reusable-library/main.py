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
        '''
        This is the FavoriteGame library where all the methods will be used to store, add_game and compile a list of
        highscores. Here I set lib as an instance of the FavoriteGame class
        '''
        lib = FavoriteGame()

        '''Here I set md1 as an instance of the HighScores data object. This uses the HighScores data object as a
        blueprint for all of the input received from the request.GET method. There is one for each game information.
        '''
        new_game = HighScores()
        game_1 = HighScores()
        game_2 = HighScores()
        game_3 = HighScores()
        '''
        Here I started a conditional statement to decide which view will be printed to the screen. So if there is any
        request.GET information, the information from the inputs will be stored using the HighScores blueprint
        '''
        if self.request.GET:
            new_game.game = self.request.GET['game']
            new_game.s = int(self.request.GET['score'])
            new_game.i = self.request.GET['initials']
            new_game.players = self.request.GET['players']
            #here I call the instance of favorite games and pass in the stored information from the HighScores data object and run the add_game method
            lib.add_game(new_game)

            '''
            Here I hard coded some info as if a user had signed in and accessed information that was saved in a
            database I did it this way because I could not figure out how to get information from the form to save into
            a database to be accessed. This way there is information that shows that the library is working and it is
            recieving information from the form and adding it to the compile_list method.
            '''
            #Here I set up the attributes for the HighScores data object for the Hard coded information
            game_1.game = "Call of Duty Black Ops 2"
            game_1.s = 58765
            game_1.i = "BJC"
            game_1.players = "Multiplayer"
            #Here I called the instance of the FavoriteGame library to add the game to the list
            lib.add_game(game_1)

            #Here I set up the attributes for the HighScores data object for the Hard coded information
            game_2.game = "Gears of War 2"
            game_2.s = 289876
            game_2.i = "BJC"
            game_2.players = "Single Player"
            #Here I called the instance of the FavoriteGame library to add the game to the list
            lib.add_game(game_2)

            #Here I set up the attributes for the HighScores data object for the Hard coded information
            game_3.game = "Nuketown Zombies"
            game_3.s = 34785
            game_3.i = "BJC"
            game_3.players = "Multiplayer"
            #Here I called the instance of the FavoriteGame library to add the game to the list
            lib.add_game(game_3)

            #This sets the reults view to the compile_list method so it will show the information from the data object
            p.results = lib.compile_list() + lib.calc_average()

            #This prints the results view to the web page
            self.response.write(p.print_results())

        #This is the second part of the condition that will print the form view if the request.GET information doesn't exist
        else:
            self.response.write(p.print_out())





        #This is where the main handler will write the html into the page and print it on the screen


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
