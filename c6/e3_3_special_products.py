__author__ = 'Enrique Coslado'

from c6.e3_1_1_products import AbstractProduct

class SpecialProduct(AbstractProduct):
    def vat(self):
        return self.price * 0.60

special_product = SpecialProduct(name="A product", sku="AP-2332929", price=3000.23)