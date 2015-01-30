'''
Bryan Cash
1/28/15
DPW
Dynamic Site
'''

#created a pge class to hold the universal html code that will be apart of every page
#this will become a super class
class Page(object):
    #constructor function that initializes the class
    def __init__(self):
        #here I created the beginning portion of the html code with the _head attribute
        self._head = '''
<!DOCTYPE HTML>
<html>
    <head>
        <title>Welcome to the Web Store</title>
        <link href="css/style.css" rel="stylesheet" type="text/css" />
    </head>
    <body>'''
        #This holds the part of the body html code that will be apart of every page
        self._body = '''
        <div id="container">
            <h1> Beneath The Sky Web Store</h1>
            <h2>Check out our shirts</h2>
            <div id="ad">
                <p>Today through this week we are liquidating old merchandise. Check out our shirts on sale. Our t-shirts are now <strong>50% off</strong> and our hoodie has been marked down from $55 to $35. Pick up a shirt and a hoodie today while supplies last!</p>
            </div>
            <nav id="nav">
                <ul>
                    <li class="active"><a href="?id=victorian_woman"><span>Victorian Woman</span></a></li>
                    <li><a href="?id=three_b">Three B's</a></li>
                    <li><a href="?id=metal_skull">Metal Skull</a></li>
                    <li><a href="?id=f_bomb">F - Bomb</a></li>
                    <li><a href="?id=hoody">Hoodie</a></li>
                </ul>
            </nav>
        '''
        #This holds the closing html tags
        self._close = '''
        </div>
    </body>
</html>'''

    #this is the method used to print out the basic structure of the page without the content pages
    def print_out(self):
        return self._head + self._body + self._close


#here I created a class that inherits from the page class making the page class a super class
#I used the Page object to show that the ContentPage will inherit from the Page class
class ContentPage(Page):
    #This is the constructor function that will initialize the class
    def __init__(self):
        #here is the constructor for the super class
        super(ContentPage, self).__init__()
        
        self.__list_inputs = ''
        self.num = 0
        self.content_head = '''
        <div id="content">
            <h3>Shirts Info</h3>
            '''
        self.content_name = '<p><strong>Name: </strong>'
        self.content_size = '<br /><p><strong>Sizes: </strong>'
        self.content_img = '<div id="img"><img src="'
        self.content_img2 = '" height="300" width="300"></div>'
        self.content_description = '<br /><strong>Description: </strong>'
        self.content_price = '<br /><strong>Original Price: </strong>'
        self.content_sale = '<br /><strong>Sale Price: </strong>'
        self.content_close = '</p></div>'

    @property
    def inputs(self):
        return self.__list_inputs


    @inputs.setter
    def inputs(self, arr):
        self.inputs = arr
        for item in arr:
            self.__list_inputs += item[self.num]

    def print_out(self):
        return self._head + self._body + self.content_head + self.content_name + self.data.name + self.content_size + self.data.size + self.content_img + self.data.img + self.content_img2 +self.content_description + self.data.description + self.content_price + self.data.price + self.content_sale + self.data.final_price + self.content_close + self._close






