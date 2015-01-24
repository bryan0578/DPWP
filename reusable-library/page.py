'''
Bryan Cash
1/21/2015
DPW
Reusable Library
'''


#Here I created my Page object
class Page(object):
    #The constructor function that initializes the class
    def __init__(self):
        #Here I created my title attribute that contains the welcome text
        self.title = "Welcome!"
        #Here I created my css attribute this points to the css file in html
        self.css = "css/styles.css"
        #Here I created my head attribute this holds all the information that will be the html for each view
        self.head = '''
<!DOCTYPE HTML>
<html>
    <head>
        <title>{self.title}</title>
        <link href="{self.css}" rel="stylesheet" type="text/css" />
    </head>
    <body>'''
        #here I created the input view, this holds all the html for the form view
        self.input = '''
        <div id="head">
            <h1>High Score Tracker</h1>
            <p>Keep track of your high scores. Just enter the name of the game your high score your initials and select multiplayer or single player, hit add game and see all of your high scores</p>
        </div>
        <div id="form">
            <h2>Keep track of your High Scores</h2>
            <form method="GET">
                <div class="i">
                    <label>Name of Game: </label><input class="input" type="text" name="game" /><br />
                </div>
                <div class="i">
                    <label>Your High Score: </label><input class="input" type="number" name="score" /><br />
                </div>
                <div class="i">
                    <label>Your Initials: </label><input class="input" type="text" name="initials" /><br />
                </div>
                <div class="i">
                    <label>Players: </label>
                        <select class="input" name="players">
                            <option>Single Player</option>
                            <option>Multiplayer</option>
                        </select><br />
                </div>
                <div id="button">
                    <input type="submit" value="Add Game" class="btn" />
                </div>
            </form>
        </div>'''
        self.container_head = '''<h2>Here is your list of High Scores</h2>
        <div id="container">

        '''

        self.results = ''

        self.container_close = '</div>'
        #create a close attribute which will contain the ending html code for all views of the page
        self.close = '''
    </body>
<html>'''


    #create a method that will print all the html elements to the page
    def print_out(self):
        input_page = self.head + self.input + self.close
        input_page = input_page.format(**locals())
        return input_page

    def print_results(self):
        self.results = self.head + self.container_head + self.results + self.container_close + self.close
        self.results = self.results.format(**locals())
        return self.results




