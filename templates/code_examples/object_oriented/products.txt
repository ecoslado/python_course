__author__ = 'Enrique Coslado'

class AbstractProduct(object):
    def __init__(self, name, sku, price):
        self.name = name
        self.sku = sku
        self.price = price

    def vat(self):
        raise NotImplementedError

    def final_price(self):
        raise NotImplementedError


class EssentialProduct(AbstractProduct):
    def vat(self):
        return self.price * 0.04

    def final_price(self):
        return self.price * 1.04

class IntermediateProduct(AbstractProduct):
    def vat(self):
        return self.price * 0.10

    def final_price(self):
        return self.price * 1.10

class NormalProduct(AbstractProduct):
    def vat(self):
        return self.price * 0.21

    def final_price(self):
        return self.price * 1.21