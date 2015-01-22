
import webapp2
from library import MovieData, FavoriteMovies
from pages import Page

class MainHandler(webapp2.RequestHandler):
    def get(self):

        #page for class
        p=Page()
        lib = FavoriteMovies()

        #movie title
        #year movie was made
        #director of the film
        md1 = MovieData()
        md1.title = "The Princess Bride"
        md1.year = 1989
        md1.director = "Rob Reiner"
        lib.add_movie(md1)

        md2 = MovieData()
        md2.title = "Dune"
        md2.year = 1986
        md2.director = "David Lynch"
        lib.add_movie(md2)

        md2 = MovieData()
        md2.title = "Star Wars"
        md2.year = 1977
        md2.director = "George Lucas"
        lib.add_movie(md2)

        lib.calc_time_span()
        p.body = lib.compileList()
        self.response.write(p.print_out())






app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
