class Cart:

    def __init__(self):
        self.products = {}

    def add_product(self, product: Product, quantity: int | float):
        if not isinstance(product, Product):
            raise TypeError('Error in Product datatype')
        elif not isinstance(quantity, int | float):
            raise TypeError('Error in quantity of Product')
        elif quantity <= 0:
            raise ValueError('Quantity must be > 0. But less or equal got.')
        elif product in self.products:
            self.products[product] += quantity
        else:
            self.products[product] = quantity

    def Total(self):
        summa = 0
        for product, quantity in self.products.items():
            summa += product.price * quantity
        return summa

    def __str__(self):

        res = ''

        for product, quantity in self.products.items():
            res += f'{product} x {quantity} = {product.price * quantity}$ \n'
        return res
