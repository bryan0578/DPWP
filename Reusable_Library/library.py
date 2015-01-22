class FavoriteMovies(object):
    def __init__(self):
        self.__movie_list = []
        #have an array to hold the movie information
        #some way to add to the array of movies
        #generate a list of movies
        #calculation time span between movies

    def add_movie(self, m):
        self.__movie_list.append(m)
        print m.title
        #<Movie Data Object

    def compileList(self):
        output = ''
        for movie in self.__movie_list: #for each movie in movie array
            output += 'Title: ' + movie.title + ' (' + str(movie.year) +') Directed By: ' + movie.director +'<br />'
            return output

    def calc_time_span(self):
        '''
        calculate the time in between movies
        '''
        #years
        years = []
        for movie in self.__movie_list:
            years.append(movie.year)


        #sort years from low to high
        years.sort()

        #subtract the low year from the high year
        num = len(years) - 1
        span = years[num] - years[0] #last number - first number
        #return the span of time
        return 'The span between films is ' + str(span)




class MovieData(object):
    def __init__(self):
        self.title = ''
        self.__year = 0 #check for valid year
        self.director = ''

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, y):
        if y > 2014:
            print "Error, invalid date!"
            self.__year = 2014
        else:
            self.__year = y

