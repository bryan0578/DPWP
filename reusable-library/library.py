'''
Bryan
1/21/2015
DPW
Reusable Library
'''


#reusable library classes
#Here I created a reusable library class called FavoriteGame
class FavoriteGame(object):
    #this is the constuctor function that make it run
    def __init__(self):
        #here I set up an empty array to store information from the data object
        self.__games_list = []
    #I set up a function to add games to the empty array
    def add_game(self, g):
        #this is the code thats appends a game to the game array
        self.__games_list.append(g)
        #tested to make sure it is working
        #print g.game

    #here I set up a method to compile the list of items in the array and output them in the html
    def compile_list(self):
        output = ''
        for game in self.__games_list:
            output += game.i + ' ' + game.s + '<br />'
        return output


#this is my data object
class HighScores(object):
    def __init__(self):
        self.game = ''
        self.__score = ''
        self.__initials = ''
        self.players = ''

    @property
    def score(self):
        pass

    @score.setter
    def score(self, s):
        self.score = s

    @property
    def initials(self):
        pass

    @initials.setter
    def initials(self, i):
        self.initials = i









#set up a data object and methods

#set up additional classes
