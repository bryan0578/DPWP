'''
Bryan Cash
1/28/15
DPW
Dynamic Site
'''

class TShirts(object):
    def __init__(self):
        self.shirt_id = 0
        self.size = ''
        self.img = ''
        self.description = ''
        self.price = 0
        self.clearance = 0.50
        self.final_price = 0


class Shirt(object):
    def __init__(self):
        self.woman = TShirts()
        self.woman.shirt_id = 1
        self.woman.size = 'Sm, Med, Lg, Xl, XXL'
        self.woman.img = 'images/bts-woman.jpg'
        self.woman.description = '''Black shirt with a victorian woman in a dress and umbrella and a skull face. This
    and is machine washable'''
        self.price = 15
        self.woman.final_price = (1 - self.woman.clearance) * self.woman.price

        self.fire = TShirts()
        self.fire.shirt_id = 2
        self.fire.size = 'Sm, Med, Lg, Xl, XXL'
        self.fire.img = 'images/bts-fire.jpg'
        self.fire.description = '''Black shirt with a stretched bloody skull with fangs. This shirt is for the extreme
        metal heads. '''
        self.fire.price = 15
        self.fire.final_price = (1 - self.fire.clearance) * self.fire.price

        self.three_b = TShirts()
        self.three_b.shirt_id = 3
        self.three_b.size = 'Xs, Sm, Med, Lg, Xl, XXL'
        self.three_b.img = 'images/bts-3b.jpg'
        self.three_b.description = '''Black shirt with a victorian woman in a dress and umbrella and a skull face. This
    and is machine washable'''
        self.three_b.price = 15
        self.three_b.final_price = (1 - self.three_b.clearance) * self.three_b.price

        self.f_shirt = TShirts()
        self.f_shirt.shirt_id = 4
        self.f_shirt.size = 'Sm, Med, Lg, Xl, XXL'
        self.f_shirt.img = 'images/bts-fshirt.jpg'
        self.f_shirt.description = '''Black shirt with a victorian woman in a dress and umbrella and a skull face. This
    and is machine washable'''
        self.f_shirt.price = 15
        self.f_shirt.final_price = (1 - self.f_shirt.clearance) * self.f_shirt.price

        self.hood = TShirts()
        self.hood.shirt_id = 5
        self.hood.size = 'Sm, Med, Lg, Xl, XXL'
        self.hood.img = 'images/bts-hoody.jpg'
        self.hood.description = '''Black shirt with a victorian woman in a dress and umbrella and a skull face. This
    and is machine washable'''
        self.hood.price = 55
        self.hood.final_price = (1 - self.hood.clearance) * self.hood.price


class Albums(object):
    def __init__(self):
        self.cd_id = 0
        self.album = ''
        self.year = 0
        self.img = ''
        self.description = ''
        self.price = 0
        self.sale = 0.10
        self.final_price = 0


class CD(object):
    def __init__(self):
        self.wddts = Albums()
        self.wddts.cd_id = 6
        self.wddts.album = 'What Demons Do To Saints'
        self.wddts.year = 2007
        self.wddts.img = 'images/bts-WDDTS.jpg'
        self.wddts.description = '''What Demons Do To Saints, featuring a hellacious collection of songs that elicit
fevered comparisons to bands such as Carcass, Hypocrisy, Shadows Fall and Killswitch Engage.'''
        self.wddts.price = 15
        self.wddts.final_price = (1 - self.wddts.sale) * self.wddts.price

        self.tdtmd = Albums()
        self.tdtmd.cd_id = 7
        self.tdtmd.album = 'What Demons Do To Saints'
        self.tdtmd.year = 2008
        self.tdtmd.img = 'images/bts-TDTMD.jpg'
        self.tdtmd.description = '''The Day The Music Died'''
        self.tdtmd.price = 15
        self.tdtmd.final_price = (1 - self.tdtmd.sale) * self.tdtmd.price

        self.ilm = Albums()
        self.ilm.cd_id = 8
        self.ilm.album = 'What Demons Do To Saints'
        self.ilm.year = 2010
        self.ilm.img = 'images/bts-IML.jpg'
        self.ilm.description = '''In Loving Memory the vicious new album full of monster breakdowns and unholy 808's.
For fans of Killswitch Engage, All That Remains and Suicide Silence.'''
        self.ilm.price = 15
        self.ilm.final_price = (1 - self.ilm.sale) * self.ilm.price











