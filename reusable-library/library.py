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
        #I set up the output to an empty string to hold the return information
        output = ''
        #Using a for loop I looped through the array of games and compiled a list of all the information
        for game in self.__games_list:
            #here I put together the information to be used in html code for the list
            output += '<div id="results1">' + game.game + ' ' + game.players + '</div><div id="results2"> ' + game.i + ' ' + str(game.s) + '</div>'
        #Finially I return the output to be printed to screen
        return output

    #I set up a calculation to keep track of the user's high score this calculation will give the average high score
    def calc_average(self):
        #I set up an empty array to hold the information for the calculation
        s = []
        #I created a for loop to cycle through the list of game to pull out all the scores
        for game in self.__games_list:
            #This will put all of the scores into the empty array
            s.append(game.s)
        #here I set up a variable num and set it the leangth of the array
        num = len(s)
        #I set up an variable to to hold the sum of all the scores in the array
        total_sum = sum(s)
        #Then I set up a varaible to hold the calculation of the sum of all the scores divided by the length of all the scores
        average = total_sum/num
        #Finally I return a string with a message and the average score converted to a string to be printed on the screen
        return  'Your average high schore is ' + str(average)


#this is my data object
class HighScores(object):
    #I set up my constuctor function so that it will run
    def __init__(self):
        #here is the blueprint for the information from both the hardcoded information and the request.GET information
        self.game = ''
        #here I made sure that the score input is treated as an integer for the average calculation
        self.__score = int()
        self.__initials = ''
        self.players = ''

    #Here I have made my getter and setter for both my scores and initials because they are private attributes
    @property
    #method for getter for score
    def score(self):
        return self.__score

    #method for setter for score
    @score.setter
    def score(self, s):
        self.score = s

    #method for getter for initials
    @property
    def initials(self):
        return self.__initials

    #method for setter for initals
    @initials.setter
    def initials(self, i):
        self.initials = i



