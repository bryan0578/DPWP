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
        self.clearance = 0.50
        self.final_price = 0


class Shirt(object):
    def __init__(self):
        woman = TShirts()
        woman.id = 'victorian_woman'
        woman.name = 'Victorian Woman'
        woman.size = 'Sm, Med, Lg, Xl, XXL'
        woman.img = 'images/bts-woman.png'
        woman.description = '''Black shirt with a victorian woman in a dress and umbrella and a skull face. This
    and is machine washable'''
        price = 15
        woman.final_price = (1 - woman.clearance) * woman.price

        skull = TShirts()
        skull.id = 'metal_skull'
        skull.name = 'Metal Skull'
        skull.size = 'Sm, Med, Lg, Xl, XXL'
        skull.img = 'images/bts-fire.png'
        skull.description = '''Black shirt with a stretched bloody skull with fangs. This shirt is for the extreme
        metal heads. '''
        skull.price = 15
        skull.final_price = (1 - skull.clearance) * skull.price

        three_b = TShirts()
        three_b.id = "three_b"
        three_b.name = "Three B's"
        three_b.size = 'Xs, Sm, Med, Lg, Xl, XXL'
        three_b.img = 'images/bts-3b.png'
        three_b.description = '''Black shirt with a victorian woman in a dress and umbrella and a skull face. This
    and is machine washable'''
        three_b.price = 15
        three_b.final_price = (1 - three_b.clearance) * three_b.price

        f_bomb = TShirts()
        f_bomb.id = "f_bomb"
        f_bomb.name = 'F-Bomb'
        f_bomb.size = 'Sm, Med, Lg, Xl, XXL'
        f_bomb.img = 'images/bts-fshirt.png'
        f_bomb.description = '''Black shirt with a victorian woman in a dress and umbrella and a skull face. This
    and is machine washable'''
        f_bomb.price = 15
        f_bomb.final_price = (1 - f_bomb.clearance) * f_bomb.price

        hood = TShirts()
        hood.id = 'hoody'
        hood.name = 'Hoody'
        hood.size = 'Sm, Med, Lg, Xl, XXL'
        hood.img = 'images/bts-hoody.png'
        hood.description = '''Black shirt with a victorian woman in a dress and umbrella and a skull face. This
    and is machine washable'''
        hood.price = 55
        hood.final_price = (1 - hood.clearance) * hood.price

        self.shirts = [woman, skull, three_b, f_bomb, hood]
















