'''
Bryan Cash
1/28/15
DPW
Dynamic Site
'''


class TShirts(object):
    def __init__(self):
        self.id = 0
        self.name = ''
        self.size = ''
        self.img = ''
        self.description = ''
        self.price = 0
        self.final_price = 0



class Shirt(object):
    def __init__(self):
        woman = TShirts()
        woman.id = 'victorian_woman'
        woman.name = 'Victorian Woman'
        woman.size = 'Sm, Med, Lg, Xl, XXL'
        woman.img = '/images/bts-woman.png'
        woman.description = 'Black shirt with a victorian woman in a dress and umbrella and a skull face. This shirt is pres-hrunk and is machine washable.'
        woman.price = '$15'
        woman.final_price = '$7.50'

        skull = TShirts()
        skull.id = 'metal_skull'
        skull.name = 'Metal Skull'
        skull.size = 'Sm, Med, Lg, Xl, XXL'
        skull.img = 'images/bts-fire.png'
        skull.description = 'Black shirt with a stretched bloody skull with fangs. This shirt is for the extreme metal heads. '
        skull.price = '$15'
        skull.final_price = '$7.50'

        three_b = TShirts()
        three_b.id = "three_b"
        three_b.name = "Three B's"
        three_b.size = 'Xs, Sm, Med, Lg, Xl, XXL'
        three_b.img = 'images/bts-3b.png'
        three_b.description = 'Black shirt with orange and grey background, with Beneath the Sky logo on the back on top of a pile of skulls.'
        three_b.price = '$15'
        three_b.final_price = '$7.50'

        f_bomb = TShirts()
        f_bomb.id = "f_bomb"
        f_bomb.name = 'F-Bomb'
        f_bomb.size = 'Sm, Med, Lg, Xl, XXL'
        f_bomb.img = 'images/bts-fshirt.png'
        f_bomb.description = 'Black shirt with Blue and purple background, following the traditional "F-Bomb shirts many metal bands are using today but with a little twist.'
        f_bomb.price = '$15'
        f_bomb.final_price = '$7.50'

        hood = TShirts()
        hood.id = 'hoody'
        hood.name = 'Respect for the Dead'
        hood.size = 'Sm, Med, Lg, Xl, XXL'
        hood.img = 'images/bts-hoody.png'
        hood.description = 'One of the most popular is the Beneath the Sky hoodie featuring a line from the song Respect for the Dead on the hood.'
        hood.price = '$55'
        hood.final_price = '$35'

        self.shirts = [woman, skull, three_b, f_bomb, hood]


















