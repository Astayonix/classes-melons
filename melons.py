"""This file should have our melon-type classes in it."""


class WatermelonOrder(object):
    species = "Watermelon" 
    color = "green"
    imported = False
    shape = 'natural'
    seasons = ['Fall', 'Summer']

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""
        normal_price = 5
        if qty >= 3:
            self.qty = float(qty) * normal_price * 0.75
        else:
            self.qty = 5 * qty
        print self.qty
        # if self.species is "Casaba" or "Ogen":
        #     normal_price += 1
        #     if self.imported == True:
        #         sub_total1 = normal_price * 1.5
        #     elif self.shape == "square":
        #         sub_total1 = normal_price * 2
        #     else:
        #         pass
        # print sub_total1

class CantaloupeOrder(object):
    species = "Cantaloupe" 
    color = "tan"
    imported = False
    shape = 'natural'
    seasons = ['Spring', 'Summer']

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""
        normal_price = 5
        if qty >= 5:
            self.qty = float(qty) * normal_price * 0.5
        else:
            self.qty = 5 * qty
        print self.qty

class CasabaOrder(object):
    species = "Casaba" 
    color = "green"
    imported = True
    shape = 'natural'
    seasons = ['Spring', 'Summer', 'Fall', 'Winter']

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""
        normal_price = (5+1)*1.5 
        self.qty = float(normal_price) * qty
        print self.qty

class SharlynOrder(object):
    species = "Sharlyn" 
    color = "tan"
    imported = True
    shape = 'natural'
    seasons = ['Summer']

class SantaClausOrder(object):
    species = "Santa Claus" 
    color = "green"
    imported = True
    shape = 'natural'
    seasons = ['Winter', 'Spring']

class ChristmasOrder(object):
    species = "Christmas" 
    color = "green"
    imported = False
    shape = 'natural'
    seasons = ['Winter']

class HornedMelonOrder(object):
    species = "Horned Melon" 
    color = "yellow"
    imported = True
    shape = 'natural'
    seasons = ['Summer']

class XiguaOrder(object):
    species = "Xigua" 
    color = "black"
    imported = True
    shape = 'square'
    seasons = ['Summer']

class OgenOrder(object):
    species = "Ogen" 
    color = "tan"
    imported = False
    shape = 'natural'
    seasons = ['Spring', 'Summer']

watermelon = WatermelonOrder()
cantaloupe = CantaloupeOrder()
casaba = CasabaOrder()
sharlyn = SharlynOrder()
santa_claus = SantaClausOrder()
christmas = ChristmasOrder()
horned_melon = HornedMelonOrder()
xigua = XiguaOrder()
ogen = OgenOrder()

def get_price(self, qty):
    """Calculate price, given a number of melons ordered."""
    normal_price = 5
    self.qty = 5

    if self.species is "Casaba" or "Ogen":
        normal_price += 1
        if self.imported == True:
            sub_total1 = normal_price * 1.5
        elif self.shape == "square":
            sub_total1 = normal_price * 2
        else:
            pass
    print sub_total1


    # if self.species == "Casabas" or "Ogen":
    #     sub_total1 += 1
    # elif self.imported == True:
    #     sub_total2 = float(sub_total1 * 1.5)
    # elif self.shape == "square":
    #     sub_total3
    total = 0   # TODO, calculate the real amount!

    return total