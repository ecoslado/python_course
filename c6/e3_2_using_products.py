__author__ = 'Enrique Coslado'
from importlib import import_module

def main():
    product_type = "EssentialProduct"

    module = import_module('c6.e3_1_products')
    class_ = getattr(module, product_type)

    my_product = class_(name="stuff", sku="ST-223291", price=32.00)
    print type(my_product)
    print my_product.vat()

    
if __name__ == "__main__":
    main()
