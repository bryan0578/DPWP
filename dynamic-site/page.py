'''
Bryan Cash
1/28/15
DPW
Dynamic Site
'''


class Page(object):#borrow stuff from object class
    def __init__(self):
        self.data = TShirts()
        self.content = ''
        self._head = '''
<!DOCTYPE HTML>
<html>
    <head>
        <title>Welcome to the Web Store</title>
        <link href="css/style.css" rel="stylesheet" type="text/css" />
    </head>
    <body>'''
        self._body = '''
        <h1> Beneath The Sky Web Store</h1>
        <a href="?id=victorian_woman">Victorian Woman</a><br>
        <a href="?id=three_b">Three B's</a><br>
        <a href="?id=metal_skull">Metal Skull</a><br>
        <a href="?id=f_bomb">F - Bomb</a><br>
        <a href="?id=hoody">Hoody</a><br>
        <a href="?id=wddts">What Demons Do To Saints</a><br>
        <a href="?id=tdtmd">The Day The Music Died</a><br>
        <a href="?id=iml">In Loving Memory</a><br>
        '''
        self._close = '''
    </body>
</html>'''

    def print_out(self):
        return self._head + self._body + self._close


class ContentPage(Page):
    def __init__(self):
        super(ContentPage, self).__init__()


class TShirts(object):
    def __init__(self):
        self.id = 0
        self.name = ''
        self.size = ''
        self.img = ''
        self.description = ''
        self.price = 0
        self.clearance = 0.50
        self.final_price = 0

