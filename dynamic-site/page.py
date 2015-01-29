'''
Bryan Cash
1/28/15
DPW
Dynamic Site
'''


class Page(object):#borrow stuff from object class
    def __init__(self):
        self._head = '''
<!DOCTYPE HTML>
<html>
    <head>
        <title></title>
    </head>
    <body>'''

        self._body = '''
        <h1> Beneath The Sky Merch Store</h1>
        '''
        self._close = '''
    </body>
</html>'''

    def print_out(self):
        return self._head + self._body + self.close
