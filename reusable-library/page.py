#This is the page class
class Page(object):
    #The constructor function that initializes the class
    def __init__(self):
        #create a private title attribute
        self.__title = "Welcome!"
        #create a public css attribute
        self.css = "css/styles.css"
        #create  a private heading attribute where the beginning of the html code will be written for all the views of the page
        self.__head = '''
<!DOCTYPE HTML>
<html>
    <head>
        <title>Enter your information</title>
        <link href="css/styles.css rel="stylesheet" type="text/css" />
    </head>
    <body>'''
        #create a body attribute where all the html body elements will be located
        #create an html form with at least five inputs
        #make sure form uses GET method
        #create html div tags for css styles
        self.body = '''
        <form method="GET">
            <label for="textinput">Text Input</label>
                <input id="textinput" name="textinput" type="text" placeholder="placeholder" /><br />
            <label for="textinput">Text Input</label>
                <input id="textinput" name="textinput" type="text" placeholder="placeholder" /><br />
            <label for="textinput">Text Input</label>
                <input id="textinput" name="textinput" type="text" placeholder="placeholder" /><br />
            <label for="textinput">Text Input</label>
                <input id="textinput" name="textinput" type="text" placeholder="placeholder" /><br />
            <label for="textinput">Text Input</label>
                <input id="textinput" name="textinput" type="text" placeholder="placeholder" /><br />
            <input class="input_size" id="button" type="submit" value="Submit" />

        </form>'''

        #create a close attribute which will contain the ending html code for all views of the page
        self.close = '''
    </body>
<html>'''

    #create a method that will print all the html elements to the page
    def print_out(self):
        #
        all = self.__head + self.body + self.close
        all = all.format(**locals())
        return all



