__author__ = 'Enrique Coslado'

from abc import ABCMeta, abstractmethod

class AbstractProduct(object):

    __metaclass__ = ABCMeta

    def __init__(self, name, sku, price):
        self.name = name
        self.sku = sku
        self.price = price

    @abstractmethod
    def vat(self):
        pass

    @abstractmethod
    def final_price(self):
        pass


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