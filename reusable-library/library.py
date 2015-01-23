#reusable library classes


class FavoriteGame(object):
    def __init__(self):
        self.__games_list = []

    def add_game(self, g):
        self.__games_list.append(g)
        print g.game

    def complile_list(self):
        output = ''
        for game in self.__games_list:
            output += game.initials + ' ' + game.s + '<br />'
        return output



class HighScores(object):
    def __init__(self):
        self.game = ''
        self.__score = ''
        self.initials = ''
        self.players = ''

    @property
    def score(self):
        pass

    @score.setter
    def score(self, s):
        self.score = s









#set up a data object and methods

#set up additional classes
